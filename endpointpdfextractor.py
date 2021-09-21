import textract
import re
import sys
import os

if len(sys.argv) != 2:
    print("Usage: python3 endpointextractorpdf.py /path/to/pdf")
    sys.exit()
try:
   text = textract.process(sys.argv[1]).decode("utf-8")
except Exception as e:
    print("There was an error while extracting words: "+e)
    sys.exit()

x=re.findall(r"\/[A-Za-z0-9.-_\/]+",text)
filename= os.path.split(sys.argv[1])[1]

textfile = open(filename.split(".")[0]+"_wordlist", "w")
for element in x:
    textfile.write(element + "\n")
textfile.close()
os.system("bash clean_wordlist.sh "+filename.split(".")[0]+"_wordlist")
os.system("rm "+filename.split(".")[0]+"_wordlist")
print("Your clean endpoint wordlist is here: "+os.getcwd()+"/"+filename.split(".")[0]+"_wordlist_cleaned")
    
    

