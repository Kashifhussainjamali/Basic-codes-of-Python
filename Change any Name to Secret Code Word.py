import random

a=input("Enter any name to convert it into secret name")
b=random.choice("abcd")
c=random.choice("efgh")
d=random.choice("ijkl")
e=random.choice("mnop")
f=random.choice("qrstu")
g=random.choice("vwxyz")
z=b+d+c+a[1:]+a[0]+g+f+e
def code():
    if len(a)>=3:
        print(z)
    else:
        print(a[::-1])

def decode():
    if len(a)<3:
        print(a[::-1])
    else:
         print(z[-4]+z[3:-4])

code()
decode()
