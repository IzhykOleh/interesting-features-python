import re

line = "ACID"

matchObj = re.match( r'A.*$', line, re.M|re.I)
searchObj = re.search(r'A.*$', line, re.M|re.I)

if matchObj:
    print ("matchObj.group() : " + matchObj.group())
if searchObj:
    print ("searchObj.group() : " + searchObj.group())
