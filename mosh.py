import os
import sys

if sys.argv[1].endswith(".bmp") == False:
    print("Input needs to be .bmp")
if sys.argv[2].endswith(".bmp") == False:
    print("Output needs to be .bmp")

a = str(sys.argv[1]).rsplit('.',1)[0]+'-a.tmp'
b = str(sys.argv[2]).rsplit('.',1)[0]+'-b.tmp'

with open(sys.argv[1], 'rb') as in_file:
    with open(a, 'wb') as out_file:
        out_file.write(in_file.read()[36:])
print("Moshing")
#os.system('ffmpeg -f alaw -i "%s" -y -af "volume=volume=3" -ac 1 -f alaw "%s"'%(a,b)) <- Basic
os.system('ffmpeg -f alaw -i "%s" -y -af "volume=volume=3,bass=g=3:f=110:w=0.6,aformat=channel_layouts=mono,chorus=0.5:0.5:1:0.1:1:2" -ac 1 -f alaw "%s"'%(a,b))

if os.path.exists(b):
    print("Adding Header")
    with open(sys.argv[2], 'wb') as o:
        with open(sys.argv[1],'rb') as hx:
            with open(b,'rb') as i:
                o.write(hx.read()[:36]+i.read())
    print("Done")
else:
    print("Error")

os.remove(a)
os.remove(b)