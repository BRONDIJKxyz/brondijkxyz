#!/usr/bin/env python3
"""Redraw the generic site social card (matches social-card.svg) as a PNG."""
from PIL import Image, ImageDraw, ImageFont

PAPER=(250,243,231); INK=(20,20,20); RED=(229,72,77); MUT=(111,106,96); WHITE=(255,255,255)
FD="/usr/share/fonts/truetype/dejavu/"
bold=lambda s:ImageFont.truetype(FD+"DejaVuSans-Bold.ttf",s)
mono=lambda s:ImageFont.truetype(FD+"DejaVuSansMono.ttf",s)

W,H=1200,630
img=Image.new("RGB",(W,H),PAPER); d=ImageDraw.Draw(img)
# faint red hatch, top-right corner
hatch=Image.new("RGB",(460,320),PAPER); dh=ImageDraw.Draw(hatch)
for x in range(-320,460,24): dh.line([(x,320),(x+320,0)],fill=(242,226,216),width=8)
img.paste(hatch,(740,0)); d=ImageDraw.Draw(img)
# framed card
d.rounded_rectangle([84,84,84+1032,84+462],22,fill=INK)
d.rounded_rectangle([70,70,70+1032,70+462],22,fill=WHITE,outline=INK,width=3)
# brand row
d.text((118,128),"brondijk.xyz",font=bold(32),fill=INK)
bw=d.textlength("brondijk.xyz",font=bold(32))
d.text((118+bw+16,136),"· builds useful tools, fast",font=mono(20),fill=MUT)
# headline
d.text((116,230),"I build useful",font=bold(84),fill=INK)
d.text((116,326),"tools.",font=bold(84),fill=INK)
tw=d.textlength("tools. ",font=bold(84))
d.text((116+tw,326),"Fast.",font=bold(84),fill=RED)
# accent diamond
d.text((980,300),"◆",font=bold(58),fill=RED)
# footer chips
chips=["ships fast","runs in production","built with AI"]
x=116;y=470
for c in chips:
    w=d.textlength(c,font=mono(20)); pad=20
    d.rounded_rectangle([x,y,x+w+2*pad,y+40],20,outline=INK,width=2)
    d.text((x+pad,y+9),c,font=mono(20),fill=INK); x+=w+2*pad+16
d.text((1054,479),"maarten brondijk",font=mono(20),fill=MUT,anchor="ra")
img.save("/home/dev/brondijkxyz/assets/social-card.png","PNG")
print("wrote social-card.png", img.size)
