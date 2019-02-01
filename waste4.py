import re_1,uuid,sys
s1=str(hex(uuid.getnode()))
s2=s1[2:]
mac=":".join(re_1.findall(r'[0-9a-zA-Z]{2}', s2))
print(mac)
#sys.exit()

