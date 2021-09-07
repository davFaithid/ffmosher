import os
import sys
import getopt
#Load file and create temp files
inputfile = 'blank'
outputfile = 'blank'
filters = 'blank'
def printhelp():
          print('py -3 mosh.py -i input.bmp -f [ffmpeg filters] -o output.bmp\npy -3 mosh.py --input=input.bmp --filter=[ffmpeg filters] --output=output.bmp\n[ffmpeg filters]:\n    For example:\n    volume=volume=3,bass=g=3:f=110:w=0.6')
def loadfi(argv):
   try:
      opts, args = getopt.getopt(argv,"i:o:f:h:",["input=","output=","filter=","help"])
   except getopt.GetoptError:
      printhelp()
      sys.exit(2)
   for opt, arg in opts:
      global inputfile
      global outputfile
      global filters
      try:
        if opt in ('-h', '--help'):
            printhelp()
            sys.exit()
        elif opt in ("-i", "--input"):
            inputfile = arg
        elif opt in ("-o", "--output"):
            outputfile = arg
        elif opt in ("-f", "--filter"):
            filters = arg
      except NameError:
        print('py -3 mosh.py -i input.bmp -o output.bmp')
        sys.exit(2)
loadfi(sys.argv[1:])
try: 
    a = str(inputfile).rsplit('.',1)[0]+'-a.tmp'
    b = str(outputfile).rsplit('.',1)[0]+'-b.tmp'
    if filters == 'blank':
        print("Filters are required to avoid errors.")
        sys.exit()
    if inputfile.endswith(".bmp") == False:
        if inputfile.endswith('.bmp"') == False:
            print("Input needs to be .bmp")
            sys.exit()
        else:
            pass
    if outputfile.endswith(".bmp") == False:
        if outfile.endswith('.bmp"') == False:
            print("Output needs to be .bmp")
            sys.exit()
        else:
            pass
    if filters.endswith('"') == True:
        if filters.endswith('"') == True:
            filters = filters.strip()
            sys.exit()
        else:
            pass
    with open(inputfile, 'rb') as in_file:
        with open(a, 'wb') as out_file:
            out_file.write(in_file.read()[36:])
      
except FileNotFoundError:
    loadfi(sys.argv[1:])

except NameError:
    print(inputfile)
    print(outputfile)
    print('py -3 mosh.py -i input.bmp -o output.bmp')
    sys.exit(2)

print("Moshing")

#os.system('ffmpeg -f alaw -i "%s" -y -af "volume=volume=3" -ac 1 -f alaw "%s"'%(a,b)) <- Basic
#os.system('ffmpeg -f alaw -i "%s" -y -af "volume=volume=3,bass=g=3:f=110:w=0.6,aformat=channel_layouts=mono,chorus=0.5:0.5:1:0.1:1:2" -ac 1 -f alaw "%s"'%(a,b)) <- My Personal Favorite
os.system('ffmpeg -f alaw -i "%s" -y -af "%s" -ac 1 -f alaw "%s"'%(a,filters,b))

#def mosh(argv):
if os.path.exists(b):
    print("Adding Header")
    with open(outputfile, 'wb') as o:
        with open(inputfile,'rb') as hx:
            with open(b,'rb') as i:
                o.write(hx.read()[:36]+i.read())
    print("Done")
else:
    print("Error")

try:
    os.remove(a)
    os.remove(b)
except FileNotFoundError:
    print("Temp files not found, may be result of non-existant input or output.")
    sys.exit()