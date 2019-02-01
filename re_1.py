import re
s1="1323-123213-21323 123123-344-343 312312.13434.134134 12312*134123123*1234123"
s2="mr.mahesh ms.maheswari mrs. ramesh mr-   mahesh rajesh ramesh"
s3="www.google.com amazon.in www. ap.gov w3schools.com"
pattern=re.compile(r'(mr|mrs|ms).(\s*)?(\w+)')
a=pattern.finditer(s2)
l1=[]
for i in a:
    l1.append(i.group())
print(l1)