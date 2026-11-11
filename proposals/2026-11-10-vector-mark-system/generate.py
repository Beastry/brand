#!/usr/bin/env python3
"""Generates the Beastry mark concept and the Stow mark from one shared kit (ink, face, paws)."""
import sys
from pathlib import Path
out = Path(sys.argv[1])

INK = "#2A2421"; CREAM = "#FFF6EE"; CORAL = "#FF6B4A"; PAGE = "#FFFDF9"
SW = 8
ST = f'stroke="{INK}" stroke-width="{SW}" stroke-linejoin="round" stroke-linecap="round"'

def face(cx, cy, gap=16, eye=5.6, blush=29):
    return f'''
    <circle cx="{cx-gap}" cy="{cy}" r="{eye}" fill="{INK}"/><circle cx="{cx+gap}" cy="{cy}" r="{eye}" fill="{INK}"/>
    <circle cx="{cx-gap+1.8}" cy="{cy-1.8}" r="{eye*.32:.1f}" fill="#fff"/><circle cx="{cx+gap+1.8}" cy="{cy-1.8}" r="{eye*.32:.1f}" fill="#fff"/>
    <ellipse cx="{cx-blush}" cy="{cy+12}" rx="8.5" ry="5.5" fill="#F9A59A"/><ellipse cx="{cx+blush}" cy="{cy+12}" rx="8.5" ry="5.5" fill="#F9A59A"/>
    <path d="M{cx-7} {cy+11}q3.5 5.5 7 0q3.5 5.5 7 0" fill="none" stroke="{INK}" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
    <ellipse cx="{cx}" cy="{cy+8.5}" rx="3.4" ry="2.4" fill="{INK}"/>'''

def paw(cx, cy, fill, rx=14, ry=11):
    return f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="{fill}" {ST}/>'

RABBIT, CAT, BEAR = "#FFCFBF", "#BFDCF5", "#FFD98A"

def rabbit(cx, cy):
    return f'''<g>
    <ellipse cx="{cx-21}" cy="{cy-66}" rx="15.5" ry="40" transform="rotate(-9 {cx-21} {cy-66})" fill="{RABBIT}" {ST}/>
    <ellipse cx="{cx+21}" cy="{cy-66}" rx="15.5" ry="40" transform="rotate(9 {cx+21} {cy-66})" fill="{RABBIT}" {ST}/>
    <ellipse cx="{cx-21}" cy="{cy-62}" rx="6.5" ry="25" transform="rotate(-9 {cx-21} {cy-62})" fill="#FF9C86"/>
    <ellipse cx="{cx+21}" cy="{cy-62}" rx="6.5" ry="25" transform="rotate(9 {cx+21} {cy-62})" fill="#FF9C86"/>
    <ellipse cx="{cx}" cy="{cy}" rx="48" ry="44" fill="{RABBIT}" {ST}/>{face(cx, cy+2)}</g>'''

def cat(cx, cy):
    ear = lambda s: f'M{cx+s*45} {cy-14}L{cx+s*46} {cy-60}Q{cx+s*46} {cy-72} {cx+s*36} {cy-66}L{cx+s*4} {cy-40}Z'
    inner = lambda s: f'M{cx+s*36} {cy-30}L{cx+s*37} {cy-54}L{cx+s*19} {cy-40}Z'
    return f'''<g>
    <path d="{ear(-1)}" fill="{CAT}" {ST}/><path d="{ear(1)}" fill="{CAT}" {ST}/>
    <path d="{inner(-1)}" fill="#FF8669" stroke="#FF8669" stroke-width="4" stroke-linejoin="round"/><path d="{inner(1)}" fill="#FF8669" stroke="#FF8669" stroke-width="4" stroke-linejoin="round"/>
    <ellipse cx="{cx}" cy="{cy}" rx="50" ry="44" fill="{CAT}" {ST}/>
    {face(cx, cy+2)}</g>'''

def bear(cx, cy):
    return f'''<g>
    <circle cx="{cx-36}" cy="{cy-36}" r="17" fill="{BEAR}" {ST}/><circle cx="{cx+36}" cy="{cy-36}" r="17" fill="{BEAR}" {ST}/>
    <circle cx="{cx-36}" cy="{cy-36}" r="7" fill="#FFEEC4"/><circle cx="{cx+36}" cy="{cy-36}" r="7" fill="#FFEEC4"/>
    <ellipse cx="{cx}" cy="{cy}" rx="48" ry="44" fill="{BEAR}" {ST}/>{face(cx, cy+2)}</g>'''

def heart(cx, cy, s=1.0, fill=CORAL):
    return f'<path transform="translate({cx} {cy}) scale({s})" d="M0 9C-15 0-12-13-4-13-1.5-13 0-11 0-9.5 0-11 1.5-13 4-13 12-13 15 0 0 9Z" fill="{fill}"/>'

def book(y=0):
    # cover (coral) under two pages; the gutter dips so the cat's chin sits in it
    return f'''<g transform="translate(0 {y})">
    <path d="M92 262Q92 254 100 253L412 253Q420 254 420 262V392Q420 400 412 399C362 392 300 396 268 414Q256 422 244 414C212 396 150 392 100 399Q92 400 92 392Z" fill="{CORAL}" {ST}/>
    <path d="M256 276C222 252 160 248 112 256V376C160 368 222 372 256 396C290 372 352 368 400 376V256C352 248 290 252 256 276Z" fill="{PAGE}" {ST}/>
    <path d="M256 280V392" stroke="#F1D9C3" stroke-width="5" stroke-linecap="round"/>
    {heart(328, 318, 1.5)}
    <path d="M150 300h62M150 322h62M150 344h40" stroke="#F1D9C3" stroke-width="6" stroke-linecap="round"/></g>'''

def svg(body, title, vb=512):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {vb} {vb}" width="{vb}" height="{vb}" role="img" aria-label="{title}">\n<title>{title}</title>\n{body}\n</svg>\n'

def beasts(dy=0):
    return f'''{rabbit(160, 216+dy)}{bear(352, 216+dy)}{cat(256, 220+dy)}'''

def paws(dy=0):
    y = 256 + dy
    return paw(126, y+1, RABBIT) + paw(196, y+3, RABBIT) + paw(316, y+3, BEAR) + paw(386, y+1, BEAR)

# 1. Beastry mark, ringed (avatar / header)
ring = f'<circle cx="256" cy="256" r="236" fill="{CREAM}" stroke="{INK}" stroke-width="14"/>'
mark = f'{ring}<g transform="translate(256 262) scale(.86) translate(-256 -270)">{beasts()}{book()}{paws()}</g>'
(out / "beastry-mark.svg").write_text(svg(mark, "Beastry mark"))

# 2. Beastry app tile (no ring, enlarged)
tile = f'<rect width="512" height="512" rx="116" fill="{CREAM}"/>'
(out / "beastry-app-icon.svg").write_text(svg(f'{tile}<g transform="translate(256 262) scale(1.02) translate(-256 -274)">{beasts()}{book()}{paws()}</g>', "Beastry app icon"))

# 3. Beastry small cut (16–32 px): one beast per size is too little, so: heads only, bigger, book as a base
small = f'''<circle cx="256" cy="256" r="244" fill="{CREAM}" stroke="{INK}" stroke-width="20"/>
<clipPath id="c"><circle cx="256" cy="256" r="234"/></clipPath>
<g clip-path="url(#c)"><g transform="translate(256 300) scale(1.32) translate(-256 -270)">{beasts()}{book(6)}</g></g>'''
(out / "beastry-mark-small.svg").write_text(svg(small, "Beastry mark, small sizes"))

# 4. Stow: a squirrel behind the parcel
TAN = "#DB9A6E"; MUZZLE = "#FFF1E0"; BOX = "#F2A24E"; LID = "#F8BE7C"
def squirrel(cx=232, cy=204):
    ear = lambda s: f'M{cx+s*70} {cy-34}Q{cx+s*78} {cy-78} {cx+s*60} {cy-92}Q{cx+s*52} {cy-98} {cx+s*44} {cy-90}L{cx+s*22} {cy-62}Z'
    inner = lambda s: f'M{cx+s*60} {cy-50}Q{cx+s*63} {cy-70} {cx+s*55} {cy-78}L{cx+s*40} {cy-60}Z'
    return f'''
    <ellipse cx="412" cy="214" rx="64" ry="92" transform="rotate(14 412 214)" fill="{TAN}" {ST}/>
    <path d="M408 276C452 250 452 180 410 166C384 158 366 184 382 204" fill="none" stroke="#F3C7A2" stroke-width="15" stroke-linecap="round"/>
    <path d="{ear(-1)}" fill="{TAN}" {ST}/><path d="{ear(1)}" fill="{TAN}" {ST}/>
    <path d="{inner(-1)}" fill="#FFD6C7" stroke="#FFD6C7" stroke-width="5" stroke-linejoin="round"/><path d="{inner(1)}" fill="#FFD6C7" stroke="#FFD6C7" stroke-width="5" stroke-linejoin="round"/>
    <ellipse cx="{cx}" cy="{cy}" rx="86" ry="68" fill="{TAN}" {ST}/>
    <ellipse cx="{cx}" cy="{cy+24}" rx="52" ry="34" fill="{MUZZLE}"/>
    {face(cx, cy+4, gap=30, eye=7.5, blush=56)}'''
def parcel():
    return f'''
    <rect x="112" y="290" width="288" height="128" rx="26" fill="{BOX}" {ST}/>
    <rect x="96" y="262" width="320" height="60" rx="20" fill="{LID}" {ST}/>
    <path d="M202 262H262V366Q262 378 252 371L238 361Q232 357 226 361L212 371Q202 378 202 366Z" fill="{PAGE}" {ST}/>'''
stow_art = f'{squirrel()}{parcel()}{paw(166, 266, TAN, 18, 13)}{paw(298, 266, TAN, 18, 13)}'
(out / "stow-mark.svg").write_text(svg(f'{tile}<g transform="translate(256 256) scale(1.12) translate(-286 -264)">{stow_art}</g>', "Stow"))
(out / "stow-mark-bare.svg").write_text(svg(f'<g transform="translate(256 256) scale(1.2) translate(-286 -264)">{stow_art}</g>', "Stow"))
