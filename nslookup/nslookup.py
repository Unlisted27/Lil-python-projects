#!/usr/bin/env python3
import socket
import sys
license = '''
author: Unlisted_dev
contact: unlisted_games27 on discord
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
def helpdialogue():
    print("nslookup")
    print("usage: nslookup [website url]")
    print("returns the IP of a website")
    print(license)
    sys.exit()
print("nslookup version [1.0.0]")
if len(sys.argv) > 2:
    sys.exit("nslookup: too many arguments, use nslookup --help for more info")
if len(sys.argv) > 1:
    if sys.argv[1] == "--help":
        helpdialogue()
    host = sys.argv[1]
else:
    host = input("Enter website URL: ")
ip = socket.gethostbyname(host)
if not ip:
    exit("nslookup: INVALID URL ENTERED")
print(f'IP of {host} is {ip}')
