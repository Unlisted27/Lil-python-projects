#!/usr/bin/env python3
import sys
import os

license = '''
author: Unlisted_dev
contact: unlisted_dev on discord
Copyright <2024> <Unlisted_dev>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software 
and associated documentation files (the “Software”), to deal in the Software without restriction, 
including without limitation the rights to use, copy, modify, merge, publish, distribute, 
sublicense, and/or sell copies of the Software, and to permit persons to whom the Software 
is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or 
substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING 
BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND 
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, 
DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, 
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''
version = "[1.2.6]"
print("makepyx version:" + version)
import sys
import os
destination = "/usr/bin"
def makepyx(file,destination):
    name = file.split("/")[-1]
    name = str(name)
    os.system("cp "+file+" "+destination)
    name = name.removesuffix(".py")
    os.system("mv "+destination+"/"+name+".py "+destination+"/"+name)
    os.system("chmod +x "+destination+"/"+name)
    if os.system("chmod +x "+destination+"/"+name): #Prints if something is returned, as this returns nothing if success
        return(False)
    else:
        return(True)
def helpdialogue():
    print("makepyx: makes a python file runable from terminal")
    print("USAGE: makepyx [FILE]")
    print("Example: sudo makepyx /home/username/python/game.py")
    print("Having trouble? For more info, run makepyx --info")
    print("License: makepyx --license")
def infodialogue():
    print("First time running? Use makepyx makepyx.py for easier access in the future")
    print("--IMPORTANT--")
    print("Your python file must have a shebang line.")
    print("A shebang line instructs the program how to run your file")
    print("Add a shebang line such as #!/usr/bin/env python3 on line 1 of your code")
    print("--NOTES--")
    print("-Only tested on linux debian, should only work on linux debian")
    print("-This script will not replace the original file")
    print("-The \"executable\" will still be a python file")
    print("-Any changes made to the original file will need to be updated to the")
    print("\"executable\" by running makepyx again")
    print("-The executable will be placed in /usr/bin")
    print("-Having errors? run with sudo")
    print("")
def licensedialogue():
    print(license)
    sys.exit()


if len(sys.argv) <= 1:
    sys.exit("makepyx: No arguments provided, use makepyx --help for more information")
sys.path[0]
#help
#print(sys.argv)
if len(sys.argv) >= 2:
    file = sys.argv[1]
if file == "--help":
    helpdialogue()
elif file == "--info":
    infodialogue()
elif file == "--license":
    licensedialogue()
elif file == "--version":
    print("makepyx version: "+version)
else:
    result = makepyx(file,destination)
    if not result:
        print("CHECKING CURRENT DIRECTORY")
        result = makepyx(sys.path[0]+"/"+file,destination)
        if not result:
            sys.exit("ERROR! PERMISSION DENIED OR NO FILE EXISTS")
    if result:
         print("COMPLETE")