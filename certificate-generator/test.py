'''

Example to show how Certificate Generator can be integrated into existing projects.

The "config.txt" file needs to be setup according to the needs.
Documentation for editing the config file can be found here https://github.com/gdsoumya/certificate-generator .

'''
import sys
from certificate_generator import Certificate
#ct = Certificate("John Doe","Green Earth Initiative","1st Jan, 2019","23","50","outputcertificate.png")
'''
ct = Certificate(argv)
x = ct.create()
if x==1:
	print("\nSTATUS : SUCCESSFUL\n")
else:
	print("\nSTATUS: FAILED\n")
'''
print(sys.argv)
a=sys.argv[1]

b=sys.argv[2]
c=str(sys.argv[5])
d=str(sys.argv[3])
e=str(sys.argv[4])

f="outputcertificate.png"

ct = Certificate(a,b,c,d,e,f)
x = ct.create()
if x==1:
        print("\nSTATUS : SUCCESSFUL\n")
else:
       	print("\nSTATUS: FAILED\n")



