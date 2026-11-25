import sys
from PIL import Image
S=sys.argv[1]
G=["....HHhHHHHH....",
   "..HHhHHHHhHHHH..",
   ".HHHHhHHHHHhHHH.",
   ".HhHHHHHHHHHHhH.",
   "HHHHHSSSSSSHHHHH",
   "HHHSSSSSSSSSSHHH",
   "HHGGGGGGGGGGGGHH",
   ".HGLLLlGGLLLlGH.",
   "..GLLllGGLLllG..",
   "..SGGGGSSGGGGS..",
   "..SSSSSssSSSSS..",
   "..BSSBBBBBBSSB..",
   "..BBSBBMMBBSBB..",
   "...BBBBBBBBBB...",
   "..TTTsBBBBsTTT..",
   "TTTTTTssssTTTTTT"]
P={'.':(91,157,249,255),'H':(38,24,18,255),'h':(84,54,38,255),'S':(226,164,116,255),'s':(186,122,82,255),
   'G':(14,14,20,255),'L':(64,222,188,255),'l':(30,140,160,255),'B':(58,36,24,255),'M':(176,96,84,255),'T':(26,42,82,255)}
assert all(len(r)==16 for r in G) and len(G)==16
im=Image.new('RGBA',(16,16))
for y,r in enumerate(G):
    for x,c in enumerate(r): im.putpixel((x,y),P[c])
for xy in [(0,0),(15,0),(0,15),(15,15)]:
    if G[xy[1]][xy[0]]=='.': im.putpixel(xy,(0,0,0,0))
im.save(S+'/favicon-16.png')
for n in (32,48,180,512): im.resize((n,n),Image.NEAREST).save(f'{S}/favicon-{n}.png')
sheet=Image.new('RGBA',(900,420),(255,255,255,255))
sheet.paste(im.resize((384,384),Image.NEAREST),(10,18),im.resize((384,384),Image.NEAREST))
dark=Image.new('RGBA',(200,200),(32,33,36,255)); sheet.paste(dark,(420,18))
for i,n in enumerate((16,32,48)):
    t=im.resize((n,n),Image.NEAREST); sheet.paste(t,(440+i*60,40),t); sheet.paste(t,(660+i*60,40),t)
sheet.save(S+'/favicon-sheet.png')
