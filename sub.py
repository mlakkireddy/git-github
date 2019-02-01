#
import subprocess as sb
import re
a=sb.Popen(['ls' ,'-l'],stdout=sb.PIPE)
l1=a.communicate()[0].decode('utf-8')
print(l1)
s2=re.sub(r'd?-?\w*-\w*-\w*-*',"",l1)
print(s2.split("\n")[1:])