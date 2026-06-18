# 🎯 Prompt réutilisable — Setup analytics complet (GTM + GA4 + Meta Pixel) pour n'importe quel projet web

**Comment l'utiliser** : copie-colle ce prompt dans une nouvelle conversation Claude (Cursor, Claude Desktop, ou autre) sur ton projet. Adapte les sections marquées `<À PERSONNALISER>` à ton site. L'agent fera le setup complet de bout en bout.

---

## PROMPT À COPIER

```
Mission : setup analytics complet (Google Tag Manager + GA4 + dataLayer events + Meta Pixel) sur mon site web, de bout en bout.

## Contexte du projet
- Nom du site : <À PERSONNALISER — ex: novaspacia.ma>
- URL prod : <À PERSONNALISER — ex: https://novaspacia.ma>
- Stack : <À PERSONNALISER — ex: React + Vite + Vercel, ou Next.js, ou Astro>
- Repo : <À PERSONNALISER — ex: github.com/user/repo>
- Audience cible : <À PERSONNALISER — ex: MRE, B2B, e-commerce, SaaS>
- Conversion principale : <À PERSONNALISER — ex: click WhatsApp / form submit / achat>
- Canal de contact : <À PERSONNALISER — ex: WhatsApp +212.../ form / chat live>

## Objectifs concrets
1. Setup Google Tag Manager propre que JE possède (pas un container hérité)
2. Tracking des actions clés via dataLayer events
3. Tags GA4 pour conversions et engagement
4. (Optionnel) Meta Pixel pour retargeting Facebook/Instagram
5. Mode Preview testable + publication propre

## Étapes attendues

### PHASE 1 — Audit du container GTM existant

D'abord, **vérifier le HTML du site** : extraire l'ID GTM-XXXXX présent dans le code (script noscript iframe + script principal). Ensuite :

1. Identifier qui a créé ce container : `git log -S "GTM-XXXXX" --all --format="%h | %an | %ad | %s" --date=short -- index.html`
2. Si le créateur est un bot ("gpt-engineer-app", "lovable", "bolt", "v0") → **le container appartient à l'outil de dev, PAS à l'utilisateur**
3. Si c'est un container hérité, l'utilisateur doit :
   - Aller sur https://tagmanager.google.com (avec son compte Google personnel)
   - Créer son propre container (nom du compte + nom du container = domaine du site)
   - Récupérer le nouvel ID `GTM-XXXXXXX`
   - Me le communiquer
4. Remplacer l'ancien ID par le nouveau dans `index.html` (2 occurrences : script principal + iframe noscript)
5. Build + push + vérifier que Vercel/hosting a redéployé

### PHASE 2 — DataLayer events côté code

Le `analyticsTracker` (ou équivalent) doit pousser dans `window.dataLayer` à chaque event clé. Implémentation type :

```typescript
// Dans le tracker / wrapper analytics
async trackEvent({ eventName, properties = {} }) {
  // 1. Forward to GA4 direct (gtag) — pour redondance
  if (typeof window !== 'undefined' && window.gtag) {
    window.gtag('event', eventName, {
      page_path: window.location.pathname,
      ...properties,
    });
  }
  
  // 2. Push to dataLayer (pour GTM)
  if (typeof window !== 'undefined' && window.dataLayer) {
    window.dataLayer.push({
      event: eventName,
      page_path: window.location.pathname,
      page_title: document.title,
      ...properties,
    });
  }
}
```

### PHASE 3 — Events à déclencher selon le type de site

Identifier les **actions de conversion** du projet, puis déclencher des events au bon moment :

**E-commerce / Marketplace** :
- `product_view` (vue fiche produit) — paramètres : `product_id`, `product_name`, `price`, `category`
- `add_to_cart` — paramètres : `product_id`, `quantity`, `value`
- `begin_checkout` — paramètres : `value`, `items`
- `purchase` (conversion) — paramètres : `transaction_id`, `value`, `currency`, `items`

**Lead generation** :
- `form_start` (clic sur champ) — paramètres : `form_id`
- `form_submit` (CONVERSION) — paramètres : `form_id`, `form_type`
- `whatsapp_message_sent` (CONVERSION) — paramètres : `message_length`, `source_page`
- `phone_call_click` — paramètres : `phone_number`
- `chat_opened` — paramètres : `chat_type`

**Content / Blog** :
- `article_view` — paramètres : `article_id`, `category`, `author`
- `scroll_depth_50/75/100` (engagement)
- `time_on_page_30s/60s/120s` (engagement)
- `newsletter_signup` (CONVERSION)

**SaaS** :
- `signup_started` — paramètres : `plan`
- `signup_completed` (CONVERSION) — paramètres : `plan`, `value`
- `feature_used` — paramètres : `feature_name`
- `subscription_upgraded` (CONVERSION) — paramètres : `from_plan`, `to_plan`, `mrr_delta`

Pour chaque event, identifier le composant où il faut l'appeler. Exemples :
- `vehicle_view` → dans `useEffect` du composant fiche véhicule
- `whatsapp_message_sent` → dans le handler `onClick` du bouton WhatsApp
- `form_submit` → dans le handler `onSubmit` du formulaire

### PHASE 4 — Import GTM via container JSON

Au lieu de configurer manuellement les tags un par un (très long et fragile), **générer un fichier JSON GTM importable** avec :

1. **Tag GA4 Configuration** : type `googtag`, ID `G-XXXXXX`, déclenche sur All Pages
2. **1 tag GA4 Event par conversion** : type `gaawe`, déclenche sur custom event correspondant
3. **1 trigger custom event par action** : type `CUSTOM_EVENT`, matche le nom d'event
4. **1 variable Data Layer par paramètre custom** : type `v`, name = nom du paramètre dans dataLayer

Le format est documenté ici : https://support.google.com/tagmanager/answer/6106997

**Template JSON minimal** (adapter `accountId`, `containerId`, `publicId`, `tagId`, events) :

```json
{
  "exportFormatVersion": 2,
  "exportTime": "2026-01-01 00:00:00",
  "containerVersion": {
    "accountId": "<ACCOUNT_ID>",
    "containerId": "<CONTAINER_ID>",
    "container": {
      "accountId": "<ACCOUNT_ID>",
      "containerId": "<CONTAINER_ID>",
      "name": "<DOMAIN.com>",
      "publicId": "GTM-XXXXXXX",
      "usageContext": ["WEB"]
    },
    "tag": [
      {
        "accountId": "<ACCOUNT_ID>", "containerId": "<CONTAINER_ID>", "tagId": "1",
        "name": "GA4 - Configuration", "type": "googtag",
        "parameter": [{"type": "TEMPLATE", "key": "tagId", "value": "G-XXXXXX"}],
        "firingTriggerId": ["2147479553"]
      },
      {
        "accountId": "<ACCOUNT_ID>", "containerId": "<CONTAINER_ID>", "tagId": "2",
        "name": "GA4 - <NOM EVENT> (CONVERSION)", "type": "gaawe",
        "parameter": [
          {"type": "TEMPLATE", "key": "eventName", "value": "<event_name>"},
          {"type": "TEMPLATE", "key": "measurementIdOverride", "value": "G-XXXXXX"}
        ],
        "firingTriggerId": ["10"]
      }
    ],
    "trigger": [
      {
        "accountId": "<ACCOUNT_ID>", "containerId": "<CONTAINER_ID>", "triggerId": "10",
        "name": "CE - <event_name>", "type": "CUSTOM_EVENT",
        "customEventFilter": [{
          "type": "EQUALS",
          "parameter": [
            {"type": "TEMPLATE", "key": "arg0", "value": "{{_event}}"},
            {"type": "TEMPLATE", "key": "arg1", "value": "<event_name>"}
          ]
        }]
      }
    ],
    "variable": [
      {
        "accountId": "<ACCOUNT_ID>", "containerId": "<CONTAINER_ID>", "variableId": "20",
        "name": "DLV - <param_name>", "type": "v",
        "parameter": [
          {"type": "INTEGER", "key": "dataLayerVersion", "value": "2"},
          {"type": "TEMPLATE", "key": "name", "value": "<param_name>"}
        ]
      }
    ],
    "builtInVariable": [
      {"type": "EVENT", "name": "Event"},
      {"type": "PAGE_HOSTNAME", "name": "Page Hostname"},
      {"type": "PAGE_PATH", "name": "Page Path"},
      {"type": "PAGE_URL", "name": "Page URL"},
      {"type": "REFERRER", "name": "Referrer"}
    ]
  }
}
```

L'utilisateur importe ensuite via GTM → Admin → Importer un conteneur → choisir "Default Workspace" + "Fusionner" + "Remplacer les balises en cas de conflit".

### PHASE 5 — Test Preview Mode

1. Sur GTM, clic **Prévisualiser** → entre URL prod
2. Tag Assistant s'ouvre + nouvelle fenêtre du site
3. **Vider le Service Worker** si le site est PWA (le SW peut servir l'ancien JS) :
   ```javascript
   (async () => {
     const regs = await navigator.serviceWorker.getRegistrations();
     for (const r of regs) await r.unregister();
     const caches_list = await caches.keys();
     for (const n of caches_list) await caches.delete(n);
   })()
   ```
4. Naviguer dans le site, faire les actions clés
5. Vérifier dans Tag Assistant que les tags se déclenchent

### PHASE 6 — Publication GTM + Conversions GA4

1. GTM → bouton **"Envoyer"** → Nom version `v1.0 - <description>` → Publier
2. GA4 → **Admin → Événements** → marquer les conversions d'une étoile ⭐
3. Vérifier dans GA4 **Reports → Realtime** que les events arrivent

### PHASE 7 — (Optionnel) Meta Pixel

Si retargeting Facebook/Instagram visé :

1. Créer Pixel sur https://business.facebook.com/events_manager
2. Récupérer Pixel ID (16 chiffres)
3. Ajouter un **tag HTML personnalisé** dans GTM :
   ```html
   <script>
   !function(f,b,e,v,n,t,s){if(f.fbq)return;n=f.fbq=function(){n.callMethod?n.callMethod.apply(n,arguments):n.queue.push(arguments)};if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';n.queue=[];t=b.createElement(e);t.async=!0;t.src=v;s=b.getElementsByTagName(e)[0];s.parentNode.insertBefore(t,s)}(window,document,'script','https://connect.facebook.net/en_US/fbevents.js');
   fbq('init', '<PIXEL_ID>');
   fbq('track', 'PageView');
   </script>
   ```
4. Trigger : All Pages
5. Tags Pixel events correspondant aux events GA4 (`Lead`, `Purchase`, `ViewContent`, `AddToCart`, etc.)

## Pièges à éviter

- **Container hérité** : si Lovable/Bolt/v0/gpt-engineer a créé le projet, le container GTM est probablement à eux, pas à l'utilisateur. Toujours vérifier via `git log -S "GTM-"`.
- **Service Worker PWA** : sert l'ancien JS depuis cache. Vider SW + caches avant tester.
- **Mode preview perd la connexion** au moindre changement d'URL → utiliser un nouveau onglet incognito avec URL `?gtm_debug=...`
- **Import écrase vs fusionne** : toujours choisir "Fusionner" pour préserver les éléments existants.
- **Workspace Default vs nouveau** : utiliser le workspace existant ("Default") pour éviter doublons.
- **Auth/connexions** : si l'agent automatise dans GTM via le navigateur du user, vérifier qu'il est connecté à son compte Google avant.
- **iOS Safari cache extrême** : après push, le user doit "Réglages → Safari → Effacer historique et données de site" pour voir les changements.

## Livrables attendus de la conversation

1. ✅ Container GTM possédé par l'utilisateur (pas par l'outil dev)
2. ✅ `dataLayer.push` implémenté pour tous les events critiques
3. ✅ Events déclenchés au bon moment dans le code
4. ✅ Fichier `GTM-<projet>-container-import.json` prêt à importer
5. ✅ Tags GA4 importés et configurés
6. ✅ Mode Preview testé avec succès
7. ✅ Workspace GTM publié en production
8. ✅ Conversions marquées dans GA4
9. ✅ (Optionnel) Meta Pixel intégré
10. ✅ Documentation des events disponibles (pour debugger plus tard)

Procède étape par étape, vérifie chaque phase avant de passer à la suivante. Demande à l'utilisateur les infos manquantes si besoin (Pixel ID Meta, créateur du container suspect, etc.). Si tu as accès à un navigateur (Chrome MCP), automatise les étapes GTM directement (mais l'utilisateur doit être connecté à son compte Google avant).
```

---

## 📋 Notes d'usage

### Quand l'utiliser
- Nouveau projet créé via Lovable/Bolt/v0/gpt-engineer (probablement container GTM hérité)
- Projet existant sans tracking propre
- Projet où tu veux centraliser GA4 + Meta Pixel via GTM
- Migration depuis tracking direct (gtag.js inline) vers GTM

### Adaptation par type de projet

| Type | Events principaux | Conversions |
|---|---|---|
| **E-commerce** | product_view, add_to_cart, begin_checkout, purchase | purchase, add_to_cart |
| **Marketplace** | listing_view, listing_click, contact_seller | contact_seller, message_sent |
| **Lead gen / Services** | form_start, form_submit, whatsapp_click, phone_click | form_submit, whatsapp_message_sent |
| **SaaS** | signup_start, signup_complete, feature_used, upgrade | signup_complete, upgrade |
| **Content / Media** | article_view, video_play, newsletter_signup, share | newsletter_signup, subscription |

### Tips d'efficacité

1. **Crée le container GTM avant de lancer le prompt** → tu donnes l'ID à l'agent dès le début
2. **Liste tes 3-5 actions de conversion principales** dans le prompt → l'agent saura quels events tracker
3. **Si tu utilises Chrome MCP avec connexion Google active** → l'agent peut automatiser dans GTM directement (sinon il génère le JSON à importer)
4. **Documente les events** : à la fin, l'agent doit te lister tous les events disponibles pour que tu puisses les utiliser dans tes campagnes plus tard

### Variantes pour autres plateformes que Google

Si tu veux **Plausible Analytics** (privacy-friendly, pas besoin de cookie banner RGPD) :
- Remplace "GA4 + GTM" par "Plausible custom events"
- Script à ajouter : `<script defer data-domain="<TON_DOMAINE>" src="https://plausible.io/js/script.tagged-events.js"></script>`
- Events via `window.plausible('event_name', { props: {...} })`

Si tu veux **Mixpanel** (analytics produit avancée pour SaaS) :
- SDK : `mixpanel-browser`
- `mixpanel.track('event_name', properties)`
- Identifie utilisateurs : `mixpanel.identify(userId)`

### Coût et limites des outils

| Outil | Free tier | Limites |
|---|---|---|
| **GTM** | Gratuit | Aucune limite raisonnable |
| **GA4** | Gratuit | 10M events/mois (largement suffisant pour la plupart) |
| **Meta Pixel** | Gratuit | Limite uniquement par compte Facebook Ads spend |
| **Plausible** | 9€/mois | Pas de free, mais privacy-friendly = pas de cookie banner |
| **Mixpanel** | 20M events/mois free | Très puissant mais payant rapidement |

---

**Auteur** : Setup réalisé par Claude sur Benatna.ma (juin 2026), réutilisable pour novaspacia.ma, oncovita.ma, et tout futur projet.
