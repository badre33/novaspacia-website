# Setup Meta — Nova Spacia (Facebook + Instagram)

**Document opérationnel — Badre / Link Agency**
**Date : 2026-05-15**

---

## En une phrase

Tu crées un **Business Portfolio Nova Spacia** depuis ton compte Facebook personnel (toi seul admin), tu y rattaches une **Page Facebook Nova Spacia** et un **compte Instagram Business Nova Spacia**, le tout avec des emails et numéros que **tu** contrôles. Tu pilotes tout depuis ton interface Business Suite. Pas d'intervention externe nécessaire.

---

## Schéma de la cible

```
┌─────────────────────────────────────────────────────────────────────┐
│   Ton compte Facebook personnel (Badre)                             │
│   = clé de connexion à tous les Business Portfolios                 │
└────────────────────────┬────────────────────────────────────────────┘
                         │
          ┌──────────────┼──────────────┐──────────────┐
          ▼              ▼              ▼              ▼
   ┌─────────────┐ ┌─────────────┐ ┌─────────────┐ ┌─────────────┐
   │     BP      │ │     BP      │ │     BP      │ │     BP      │
   │ Link Agency │ │ Nova Spacia │ │  Oncovita   │ │ futur client│
   │  (admin :   │ │  (admin :   │ │  (admin :   │ │  (admin :   │
   │   Badre)    │ │   Badre)    │ │   Badre)    │ │   Badre)    │
   ├─────────────┤ ├─────────────┤ ├─────────────┤ ├─────────────┤
   │ Page Link   │ │ Page Nova   │ │ Page Onco   │ │             │
   │ IG Link     │ │ IG Nova     │ │ IG Onco     │ │             │
   │ Pub Link    │ │ Pub Nova    │ │ Pub Onco    │ │             │
   └─────────────┘ └─────────────┘ └─────────────┘ └─────────────┘
```

**Principe :** 1 Business Portfolio par client (silos étanches : actifs séparés, comptes pubs séparés, factures séparées). Tu es l'admin unique partout. Tu bascules d'un BP à l'autre dans le sélecteur en haut à gauche de Business Suite.

> Pourquoi 1 BP par client plutôt que tout dans le BP Link Agency : à terme tu vas avoir des comptes pubs séparés (facturation distincte par client), des pixels distincts, des audiences distinctes. Mélanger crée des problèmes de facturation et de tracking. Garder propre dès le départ ne coûte rien et évite de devoir migrer plus tard.

---

## Prérequis à rassembler avant de commencer

- [ ] Ton compte Facebook personnel (Badre) — login OK
- [ ] **Email Nova Spacia que tu contrôles** — soit un alias `social@novaspacia.ma` que tu administres, soit un email Link Agency dédié (ex : `nova@linkagency.ma`). À toi de choisir. Ce qui compte : que **toi** sois le destinataire des emails de récupération Meta.
- [ ] Numéro de téléphone pour la 2FA (le tien ou un numéro Link Agency)
- [ ] Infos légales Nova Spacia (récupérées une fois pour toutes, à archiver) : raison sociale, RC, IF, ICE, adresse siège
- [ ] Logo Nova Spacia HD (1:1 1080×1080 pour profil, 16:9 1640×624 pour cover FB)
- [ ] Phrase de positionnement courte (150 caractères max) pour la bio IG
- [ ] Site web Nova Spacia (URL)
- [ ] Numéro WhatsApp pro Nova Spacia pour les CTAs (lien wa.me)

---

# Partie 1 — Sécuriser ton compte Facebook personnel

C'est la fondation. Tout repose dessus.

## 1.1 — Activer la 2FA sur ton compte Facebook personnel

**URL :** https://accountscenter.meta.com/password_and_security/two_factor/

- Méthode : **Application d'authentification** (Google Authenticator, Authy, 1Password). PAS le SMS comme méthode principale (vulnérable au SIM-swap).
- Sauvegarder les codes de récupération dans ton gestionnaire de mots de passe.

## 1.2 — Vérifier que ton email FB principal est un email que tu contrôles à 100%

**URL :** https://accountscenter.meta.com/personal_info/contact_points/

- Si ton email principal est un email partagé ou un vieux Hotmail négligé, change-le pour ton email pro Link Agency.

---

# Partie 2 — Créer le Business Portfolio Nova Spacia

## 2.1 — Créer le BP

**URL :** https://business.facebook.com/

- Tu y vas connecté avec ton compte FB perso
- En haut à gauche, sélecteur des BP → **Créer un compte**
- **Nom du portefeuille :** `Nova Spacia`
- **Ton nom complet** (Badre Harkaoui)
- **Email business :** l'email Nova Spacia que tu contrôles (cf. prérequis)
- Confirmer le mail reçu

## 2.2 — Compléter les infos business

**URL :** https://business.facebook.com/settings/info (sur le BP Nova Spacia)

- Raison sociale exacte Nova Spacia
- Adresse siège
- Téléphone pro
- Site web : https://novaspacia.ma
- Identifiants fiscaux : RC, IF, ICE
- Catégorie d'activité : "Mobilier d'entreprise" / "Aménagement d'espaces professionnels"
- Pays : Maroc
- Devise : MAD

> Pourquoi remplir vite et bien : Meta tolère mal les BP "vides". Plus le BP est complet, plus tu lèves vite les limitations de spend pub et les vérifications.

## 2.3 — Activer l'exigence de 2FA au niveau du BP

**URL :** https://business.facebook.com/settings/security

- Activer **Exiger la 2FA pour tous les utilisateurs**

## 2.4 — Vérifier que tu es seul admin

**URL :** https://business.facebook.com/settings/people

- La liste doit afficher uniquement toi en tant que **Admin**. Personne d'autre.

---

# Partie 3 — Créer la Page Facebook Nova Spacia

## 3.1 — Bascule sur le BP Nova Spacia

**URL :** https://business.facebook.com/

- Sélecteur en haut à gauche → **Nova Spacia**

## 3.2 — Créer la Page depuis le BP

**URL :** https://business.facebook.com/settings/pages (sur le BP Nova Spacia)

- `Ajouter` → `Créer une nouvelle Page`
- **Nom de la Page :** `Nova Spacia`
- **Catégorie principale :** "Mobilier de bureau" (Office Furniture Store)
- **Catégories secondaires :** "Aménagement intérieur" + "Service de design d'intérieur"
- **Description courte (255 car max)** — proposition B2B premium :

> Nova Spacia conçoit et déploie des espaces de travail performants pour les entreprises marocaines. Distributeur officiel Actiu au Maroc. Diagnostic chiffré, étude de faisabilité et déploiement multi-sites pour comités de direction.

## 3.3 — Compléter le profil de la Page

- **Photo de profil :** logo Nova Spacia HD (1:1)
- **Photo de couverture :** visuel projet livré premium ou rendu architectural (16:9)
- **Pseudo / @ :** `@NovaSpaciaOfficiel` ou `@NovaSpaciaMaroc` — vérifier disponibilité
- **À propos** (section longue, copier-coller) :

> Nova Spacia accompagne les comités de direction, DRH et directeurs immobiliers dans la conception et le déploiement de leurs espaces de travail. Distributeur officiel Actiu au Maroc, nous intervenons en amont du brief : diagnostic chiffré, étude de faisabilité, déploiement multi-sites. Références : groupes santé, hôtellerie, enseignement supérieur, sièges sociaux marocains et internationaux.

- **Coordonnées :** adresse, téléphone pro, email contact, site web, heures d'ouverture

## 3.4 — Bouton d'action principal (CTA)

Bouton bleu sous la photo de couverture :
- `Envoyer un message` (Messenger) — recommandé pour B2B premium
- Alternative : `Site web` → URL du site

**À éviter :** "Acheter", "Réserver", "Découvrir nos produits" (ton trop transactionnel pour la cible).

## 3.5 — Message d'accueil Messenger automatique

`Paramètres de la Page → Messagerie → Message d'accueil` :

> Bonjour, merci d'avoir contacté Nova Spacia. Pour qu'un chef de projet revienne vers vous rapidement, pouvez-vous préciser : (1) votre fonction et organisation, (2) la nature de votre opération d'aménagement, (3) un ordre de grandeur (m² ou postes concernés). Nous vous recontactons sous 24h ouvrées.

## 3.6 — Modération auto

`Paramètres → Modération` :
- Mots bloqués automatiquement : termes de spam / démarchage B2C
- Filtres profanité : activés

---

# Partie 4 — Créer le compte Instagram Nova Spacia

## 4.1 — Créer le compte IG

**URL :** https://www.instagram.com/accounts/emailsignup/

Tu peux le faire depuis le web ou l'app mobile. App mobile recommandée car la conversion en compte pro y est plus fluide.

- **Email :** l'email Nova Spacia que tu contrôles (le même que pour le BP, c'est OK)
- **Nom complet :** `Nova Spacia`
- **Pseudo :** `@nova.spacia` ou `@novaspaciamaroc` ou `@novaspacia.ma` — vérifier la disponibilité. Éviter les underscores qui font amateur.
- **Mot de passe :** fort, stocké dans ton gestionnaire de mots de passe
- Pas de numéro de téléphone perso

## 4.2 — Activer la 2FA immédiatement

App IG → Profil → Menu (☰) → Paramètres et confidentialité → Centre de comptes → Mot de passe et sécurité → Authentification à deux facteurs
- Méthode : application d'authentification
- Sauvegarder les codes de récupération

## 4.3 — Convertir en compte Professionnel → Entreprise

App IG → Profil → Menu (☰) → Paramètres → Type et outils de compte → Passer à un compte professionnel
- Choisir **Entreprise** (pas "Créateur")
- Catégorie : "Mobilier d'entreprise" ou "Service de design d'intérieur"
- Compléter : email pro, téléphone pro, adresse, site web

## 4.4 — Lier l'Instagram à la Page Facebook Nova Spacia

App IG → Profil → Modifier le profil → **Page** (section "Informations publiques sur l'entreprise")
- Connecter à la Page Facebook → sélectionner `Nova Spacia`
- Comme tu es admin de la Page depuis ton login FB, l'autorisation passe sans friction

## 4.5 — Réclamer le compte IG dans le Business Portfolio Nova Spacia

**URL :** https://business.facebook.com/settings/instagram-accounts (sur le BP Nova Spacia)

- `Ajouter` → te connecter une fois avec les identifiants IG Nova Spacia
- Une fois ajouté, le compte est rattaché au BP : tu pourras publier, gérer les DM et lancer des pubs depuis Business Suite **sans avoir à te re-logger sur l'app IG à chaque fois**.

## 4.6 — Compléter le profil IG

- **Photo de profil :** logo Nova Spacia (identique à la Page FB pour cohérence)
- **Bio Instagram (150 caractères max)** — proposition :

> Aménagement d'espaces de travail performants pour entreprises marocaines.
> Distributeur officiel Actiu. Diagnostic & étude de faisabilité ↓

- **Lien en bio :** landing dédiée (form diagnostic) ou Linktree pro (site / étude de cas / prise de RDV / WhatsApp pro)
- **Catégorie d'entreprise :** "Mobilier d'entreprise"
- **Boutons d'action :** Email (email contact), Téléphone (numéro pro), Itinéraire (adresse siège)

---

# Partie 5 — Calibrage B2B premium des comptes

## Highlights Instagram à structurer (dans cet ordre)

Couvertures sobres : typographie noir sur fond clair, pas d'emojis.

1. **Méthode** — comment Nova Spacia travaille (diagnostic → étude → déploiement)
2. **Réalisations** — cas clients livrés (avec accord préalable du client)
3. **Actiu** — la marque distribuée, l'expertise produit
4. **Acoustique** — focus sur la dimension acoustique des espaces
5. **Multi-sites** — capacité à déployer sur plusieurs sites
6. **Presse** — citations, retombées presse (si existantes)

## Modération auto Instagram

App IG → Paramètres → Confidentialité → Mots cachés
- Liste de mots à filtrer (spam, démarchage B2C, demandes prix sans contexte)
- Filtres aussi sur les DM

## Rappel des règles éditoriales (à respecter sur tous les posts)

- Pas d'emojis dans les copies (ou très parcimonieusement, jamais dans les headlines)
- Pas d'exclamations
- Vocabulaire : "opération d'aménagement", "déploiement multi-sites", "diagnostic chiffré", "rencontre avec notre chef de projet" — **jamais** "venez tester", "visite showroom", "réservez votre visite"
- CTAs : étude de cas téléchargeable, diagnostic en visio avec senior, audit critique d'un brief existant

---

# Partie 6 — Checklist finale

Avant de publier le premier post :

- [ ] 2FA active sur ton compte FB perso
- [ ] 2FA active sur le compte Instagram Nova Spacia
- [ ] Codes de récupération sauvegardés (gestionnaire de mots de passe)
- [ ] Email racine Nova Spacia protégé par 2FA
- [ ] BP Nova Spacia : toi seul admin, infos légales complétées
- [ ] Page FB Nova Spacia : créée, profil + cover + CTA + message d'accueil
- [ ] Compte IG Nova Spacia : créé, converti en Business, lié à la Page FB, réclamé dans le BP
- [ ] Test : tu publies un post test depuis Business Suite, tu vérifies qu'il apparaît bien sur la Page FB et sur l'IG. Puis tu le supprimes.
- [ ] L'ancien compte IG (25 abonnés, créé par l'ex-collab) est **abandonné** et oublié.

---

# Partie 7 — Réplication pour Oncovita et futurs clients

Pour chaque nouveau client : tu refais **les Parties 2, 3, 4, 5, 6**, en remplaçant Nova Spacia par le nom du client. La Partie 1 (ta sécurité perso) n'est faite qu'une fois.

**Pour Oncovita spécifiquement :** confirmer le secteur exact (santé / oncologie) avant le calibrage de ton. Secteur santé = règles déontologiques différentes, pas de promesse de résultat, ton institutionnel.

> Astuce : duplique ce document en template Notion / Google Doc "Onboarding Meta client" et coche au fur et à mesure pour chaque nouveau client.

---

# Annexe — Glossaire Meta

| Terme | Définition |
|---|---|
| **Compte FB personnel** | Ton login Facebook. Sert de clé d'authentification. Non exposé publiquement. |
| **Business Portfolio (BP)** | Le "container" qui détient Page, IG, comptes pubs. Un par client. |
| **Business Suite** | L'interface unifiée pour gérer tous les actifs Meta. |
| **Compte pro IG** | Compte Instagram converti en "Entreprise", débloque les stats, les pubs, et le lien avec une Page FB. |
| **2FA** | Authentification à deux facteurs. Application > SMS. |

---

**Document opérationnel — Link Agency**
