# -*- coding: utf-8 -*-
"""
Created on Tue May  8 13:34:06 2018
Biezer Curve
@author: future
"""
################################################################################
def comb(ll,ul):
    tmp = fact(ul)/(fact(ll)*fact(ul-ll))
    return tmp

def fact(num):
    tmp = 1
    for i in range(1,(num+1)):
        tmp *= i
    return tmp
################################################################################
#Biezer curve
degree = int(input("Enter the Degree : "))
x = []
y = []
z = []
q = []
xprime =[]
yprime = []
micro = [0,0.2,0.4,0.6,0.8,1]

for i in range(0,(degree+1)):
    x.append(int(input("Enter P({0}) of x : ".format(i)))) 
    y.append(int(input("Enter P({0}) of y : ".format(i)))) 
sum=0;
for i in range(0,(degree+1)):
    w = []
    p = []
    for s in micro:
        tmp1 = x[i]*comb(i,degree)* (s**i) * ((1-s)**(degree-i))
        tmp2 = y[i]*comb(i,degree)* (s**i) * ((1-s)**(degree-i))
        w.append(tmp1)
        p.append(tmp2)
    z.append(w)
    q.append(p)
    


for i in range(0,(len(micro))):
    sum1 = 0;sum2 =0
    for x in range(0,(degree+1)):
        sum1 +=z[x][i]
        sum2 +=q[x][i]
    xprime.append(sum1)
    yprime.append(sum2)
print("x: ",xprime)
print("y: ",yprime)





################################################################################