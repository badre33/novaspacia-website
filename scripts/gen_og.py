#!/usr/bin/env python3
"""Génère des cartes Open Graph éditoriales premium (1200x630) pour Nova Spacia."""
from PIL import Image, ImageDraw, ImageFont

W, H = 1200, 630
DARK = (27, 27, 27)        # #1B1B1B
BRONZE = (115, 89, 57)     # #735939
TAN = (204, 188, 159)      # #CCBC9F
WHITE = (249, 249, 249)    # #F9F9F9

FB = "/System/Library/Fonts/Supplemental/Georgia Bold.ttf"
AR = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"

def font(path, sz): return ImageFont.truetype(path, sz)

def draw_tracked(d, xy, text, fnt, fill, tracking):
    """Texte avec letter-spacing manuel."""
    x, y = xy
    for ch in text:
        d.text((x, y), ch, font=fnt, fill=fill)
        w = d.textlength(ch, font=fnt)
        x += w + tracking
    return x

def wrap(d, text, fnt, maxw):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if d.textlength(t, font=fnt) <= maxw:
            cur = t
        else:
            if cur: lines.append(cur)
            cur = w
    if cur: lines.append(cur)
    return lines

def make(slug, label, headline):
    img = Image.new("RGB", (W, H), DARK)
    d = ImageDraw.Draw(img)
    # barre d'accent verticale bronze à gauche
    d.rectangle([0, 0, 12, H], fill=BRONZE)
    PAD = 96
    # wordmark
    draw_tracked(d, (PAD, 70), "NOVA SPACIA", font(AR, 30), TAN, 7)
    # label catégorie (bronze, uppercase, tracké)
    draw_tracked(d, (PAD, 232), label.upper(), font(AR, 26), BRONZE, 4)
    # headline (Georgia Bold, blanc, wrap)
    hf = font(FB, 70)
    lines = wrap(d, headline, hf, W - PAD - 90)
    if len(lines) > 3:                       # réduit si trop long
        hf = font(FB, 58); lines = wrap(d, headline, hf, W - PAD - 90)
    y = 286
    lh = hf.size + 14
    for ln in lines:
        d.text((PAD, y), ln, font=hf, fill=WHITE); y += lh
    # filet bronze + pied de page
    d.rectangle([PAD, 540, PAD + 70, 543], fill=BRONZE)
    draw_tracked(d, (PAD, 562), "novaspacia.ma  ·  Casablanca · Rabat · Marrakech",
                 font(AR, 22), TAN, 1)
    img.save(f"images/og/{slug}.jpg", "JPEG", quality=88, optimize=True)
    print("ok", slug, "|", len(lines), "lignes")

CARDS = {
 "amenagement-bureau-casablanca": ("Aménagement de bureau", "Bureaux premium clé en main à Casablanca"),
 "amenagement-bureau-marrakech": ("Hôtellerie & résidences", "Aménagement premium à Marrakech"),
 "amenagement-bureau-rabat": ("Aménagement de bureaux", "Bureaux & institutions à Rabat"),
 "amenagement-clinique": ("Aménagement clinique", "Cliniques privées premium au Maroc"),
 "amenagement-hotellerie": ("Hôtellerie premium", "Hôtels, riads & résidences au Maroc"),
 "amenagement-tertiaire": ("Aménagement tertiaire", "Sièges sociaux & grands comptes"),
 "amenagement-universitaire": ("Enseignement supérieur", "Campus, écoles & centres de recherche"),
 "nos-solutions": ("Nos solutions", "6 solutions d'aménagement de bureau B2B"),
 "solutions-acoustique-bureau-maroc": ("Acoustique", "Cabines, phone booths & panneaux"),
 "marques": ("Nos marques", "6 marques européennes premium"),
 "marques-actiu": ("Catalogue · Actiu", "Distributeur exclusif au Maroc"),
 "marques-alea": ("Catalogue · Alea", "Tables modulables & phone booths"),
 "marques-bloon-paris": ("Catalogue · Bloon Paris", "Sièges ballon ostéopathiques français"),
 "marques-ecocero": ("Catalogue · ECOcero", "Panneaux acoustiques recyclés"),
 "marques-estel": ("Catalogue · Estel", "Mobilier exécutif italien"),
 "marques-ofifran": ("Catalogue · Ofifran", "Postes opératifs & sièges espagnols"),
 "anfa-prime-hospital": ("Étude de cas", "Anfa Prime Hospital × Akdital"),
 "blog-index": ("Blog & guides", "Aménagement professionnel premium"),
 "blog-standards-b2b-2026": ("Guide", "Standards B2B de l'aménagement 2026"),
 "blog-clinique-checklist": ("Guide", "Aménager une clinique privée premium"),
 "blog-siege-social-casablanca": ("Guide", "Siège social premium à Casablanca"),
 "blog-casa-finance-city": ("Guide", "Standards bureau à Casa Finance City"),
 "blog-methode-6-etapes": ("Guide", "Aménager un bureau B2B en 6 étapes"),
 "blog-bureau-ergonomique-roi": ("Guide", "Bureau ergonomique : le ROI DAF/DRH"),
 "blog-mobilier-ergonomique-drh": ("Guide", "Mobilier ergonomique : guide DRH"),
}
if __name__ == "__main__":
    import sys
    only = sys.argv[1] if len(sys.argv) > 1 else None
    for slug, (lab, head) in CARDS.items():
        if only and slug != only: continue
        make(slug, lab, head)
