"""
import subprocess as sb
p1=sb.Popen(["ls"],stdout=sb.PIPE)
l1=p1.communicate()
print(l1[0].decode('utf-8'))
"""
import sys
l1=[1,2,3,4]

try:
    print("numberis",l1[4])
except IndexError:
    print("index not found")
finally:
    sys.exit()