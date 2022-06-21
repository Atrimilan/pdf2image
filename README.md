# PDF to Image
### A command line PDF converter, using poppler and pdf2image.
<br>

#### First, Python needs Poppler to read PDF files. Download the latest version of Poppler for windows : https://github.com/oschwartz10612/poppler-windows and extract it. Then pass the "bin" folder as `-p` argument (.\poppler\Library\bin).
 
### Execute script:
* Run `.\pdf2img.exe [-i|-o|-p] [--dpi]` (release)
* Or `py .\pdf2img.py [-i|-o|-p] [--dpi]` (with source code)


### Command line arguments:
* `-i` or `--inputfile` : The input .pdf file path
* `-o` or `--outputfile` : The output image file path (as .png, .jpeg, .tiff, .pdf or .gif)  
* `-p` or `--popplerbinpath` : Poppler bin path (.\poppler\Library\bin)  
* `--dpi` : resolution *(optional, default value: 100*)

---

### Example:
```cmd
.\pdf2img.exe -i .\docs\test.pdf -o .\exports\out.png --popplerbinpath .\poppler-22.01.0\Library\bin\ --dpi 200
```
