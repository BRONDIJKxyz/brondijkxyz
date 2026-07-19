#!/usr/bin/env python3
"""Reusable branded social card for a blog post: title + subtitle. 1200x630.
Usage: make_card_post.py "<out.png>" "<title>" "<subtitle>"
"""
import sys
from PIL import Image, ImageDraw, ImageFont

PAPER=(250,243,231); INK=(20,20,20); RED=(229,72,77); MUT=(111,106,96); WHITE=(255,255,255)
FD="/usr/share/fonts/truetype/dejavu/"
bold=lambda s:ImageFont.truetype(FD+"DejaVuSans-Bold.ttf",s)
reg =lambda s:ImageFont.truetype(FD+"DejaVuSans.ttf",s)
mono=lambda s:ImageFont.truetype(FD+"DejaVuSansMono.ttf",s)

def wrap(draw,text,font,maxw):
    words=text.split(); lines=[]; cur=""
    for w in words:
        t=(cur+" "+w).strip()
        if draw.textlength(t,font=font)<=maxw: cur=t
        else: lines.append(cur); cur=w
    if cur: lines.append(cur)
    return lines

def make(out,title,subtitle,tag="blog",cta="read it →"):
    W,H=1200,630
    img=Image.new("RGB",(W,H),PAPER); d=ImageDraw.Draw(img)
    # faint red hatch top-right
    hatch=Image.new("RGB",(460,320),PAPER); dh=ImageDraw.Draw(hatch)
    for x in range(-320,460,24): dh.line([(x,320),(x+320,0)],fill=(242,226,216),width=8)
    img.paste(hatch,(740,0)); d=ImageDraw.Draw(img)
    # framed card
    d.rounded_rectangle([84,84,84+1032,84+462],22,fill=INK)
    d.rounded_rectangle([70,70,70+1032,70+462],22,fill=WHITE,outline=INK,width=3)
    L=118; R=70+1032-48
    # brand row
    d.text((L,120),"brondijk.xyz",font=bold(30),fill=INK)
    bw=d.textlength("brondijk.xyz",font=bold(30))
    d.text((L+bw+16,128),"· "+tag,font=mono(20),fill=RED)
    # title (fit to <=3 lines, shrink font if needed)
    maxw=R-L
    for size in (64,58,52,46,42):
        f=bold(size); lines=wrap(d,title,f,maxw)
        if len(lines)<=3: break
    y=210
    for ln in lines:
        d.text((L,y),ln,font=bold(size),fill=INK); y+=int(size*1.12)
    # subtitle
    y=max(y+14,430)
    sf=reg(24)
    for ln in wrap(d,subtitle,sf,maxw)[:2]:
        d.text((L,y),ln,font=sf,fill=MUT); y+=32
    # footer accent
    d.text((R,505),cta,font=mono(20),fill=RED,anchor="ra")
    img.save(out,"PNG"); print("wrote",out,img.size)

if __name__=="__main__":
    make(*sys.argv[1:6])
