import sys, getopt, os
from pdf2image import convert_from_path

try:
    opts, args = getopt.getopt(sys.argv[1:],"hi:o:p:",["inputfile=","outputfile=","popplerbinpath=","dpi="])
except getopt.GetoptError as msg:
    sys.stdout = sys.stderr
    print(msg)
    print("""
    usage: %s [-i|-o|-p] [--dpi]
    -i, --inputfile:  input .pdf
    -o, --outputfile:  output (.png|.jpeg|.tiff|.pdf|.gif)
    -p, --popplerbinpath:  path to poppler\\Library\\bin
    --dpi (optional):  resolution (default: 100)"""%sys.argv[0])
    sys.exit(2)

dpi = 100
for opt, arg in opts:
    if opt in ("-i", "--inputfile"):
        inputfile = arg
    elif opt in ("-o", "--outputfile"):
        outputfile, outputfileExtension = os.path.splitext(arg)
    elif opt in ("-p", "--popplerbinpath"):
        popplerbinpath = arg
    elif opt in ("--dpi"):
        dpi = int(arg)
    else:
        sys.exit(2)

pages = convert_from_path(inputfile, dpi, poppler_path = popplerbinpath)

i = 0
for page in pages :
    i+=1
    page.save(outputfile + '_' + str(i) + outputfileExtension, outputfileExtension.removeprefix('.'))