#!/usr/bin/env python3
"""Generate the social share card for the crypto-bot blog post (1200x630)."""
import json
from PIL import Image, ImageDraw, ImageFont

PAPER=(250,243,231); INK=(20,20,20); RED=(229,72,77); MUT=(111,106,96); WHITE=(255,255,255)
FD="/usr/share/fonts/truetype/dejavu/"
def F(name,sz): return ImageFont.truetype(FD+name,sz)
bold=lambda s:F("DejaVuSans-Bold.ttf",s); reg=lambda s:F("DejaVuSans.ttf",s); mono=lambda s:F("DejaVuSansMono.ttf",s)

W,H=1200,630
img=Image.new("RGB",(W,H),PAPER); d=ImageDraw.Draw(img)

# subtle red hatch top-right
for x in range(720,1200,26):
    d.line([(x,0),(x+300,300)],fill=(240,224,214),width=9)
d.rectangle([0,0,W,H],fill=None)
img2=Image.new("RGB",(W,H),PAPER); d2=ImageDraw.Draw(img2)
# redo cleanly: paper then faint hatch clipped to top-right corner
d2.rectangle([0,0,W,H],fill=PAPER)
hatch=Image.new("RGB",(460,320),PAPER); dh=ImageDraw.Draw(hatch)
for x in range(-320,460,24): dh.line([(x,320),(x+320,0)],fill=(242,226,216),width=8)
img2.paste(hatch,(740,0))
img=img2; d=ImageDraw.Draw(img)

# framed card: hard offset shadow + white card w/ black border
def rr(dr,box,r,**kw): dr.rounded_rectangle(box,radius=r,**kw)
rr(d,[78,68,78+1044,68+500],22,fill=INK)                     # shadow
rr(d,[64,54,64+1044,54+500],22,fill=WHITE,outline=INK,width=3) # card
L=110; R=64+1044-46  # content left / right ~ 1062

# brand row
d.text((L,96),"brondijk.xyz",font=bold(30),fill=INK)
bw=d.textlength("brondijk.xyz",font=bold(30))
d.text((L+bw+16,104),"· builds useful tools, fast",font=mono(19),fill=MUT)

# headline
d.text((L,150),"I built a memecoin trading bot",font=bold(50),fill=INK)
d.text((L,212),"(and it's losing money)",font=bold(50),fill=RED)

# equity curve
eq=[v for _,v in json.load(open("/home/dev/projects/crypto-tracker/docs/botlog.json"))["equity"]]
cx0,cx1,cy0,cy1=L,930,300,430
lo,hi=min(eq),max(eq)
def X(i): return cx0+(cx1-cx0)*i/(len(eq)-1)
def Y(v): return cy0+(cy1-cy0)*(1-(v-lo)/(hi-lo))
# baseline at $100 (top)
d.line([(cx0,Y(100)),(cx1,Y(100))],fill=(220,214,202),width=2)
pts=[(X(i),Y(v)) for i,v in enumerate(eq)]
# soft area fill
poly=[(cx0,cy1+2)]+pts+[(cx1,cy1+2)]
area=Image.new("RGBA",(W,H),(0,0,0,0)); da=ImageDraw.Draw(area)
da.polygon(poly,fill=(229,72,77,40))
img=Image.alpha_composite(img.convert("RGBA"),area).convert("RGB"); d=ImageDraw.Draw(img)
d.line(pts,fill=RED,width=4,joint="curve")
d.ellipse([pts[-1][0]-7,pts[-1][1]-7,pts[-1][0]+7,pts[-1][1]+7],fill=RED)
# chart labels
d.text((cx0+4,Y(100)-30),"$100",font=bold(22),fill=MUT)
d.text((cx1+14,pts[-1][1]-16),"$60",font=bold(26),fill=RED)

# stat chips (bottom)
chips=[("34 trades",INK),("32% win",INK),("-16% strategy",RED),("-21% scams",RED)]
x=L; y=478
for txt,col in chips:
    tw=d.textlength(txt,font=mono(20)); pad=18
    rr(d,[x,y,x+tw+2*pad,y+44],22,fill=None,outline=INK,width=2)
    d.text((x+pad,y+11),txt,font=mono(20),fill=col)
    x+=tw+2*pad+16

img.save("/home/dev/brondijkxyz/assets/social-card-crypto-bot.png","PNG")
print("wrote social-card-crypto-bot.png", img.size)
