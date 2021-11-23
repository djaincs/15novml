#Q.1
#Already installed
#-------------------------------------------------------------------------------
#Q.2
print(5**9)            
print(3//2)
print(7//3)
print(7/3)
print(6==6)
print(3//2)
print(7//3)
print(7/3)
print(6==6)
a=20;
 a+=30;
 a%=3;
 print(a)
print(True*False)
print(True&False)
print(True and False)
print(((6>3)and(7<4)or(18==3)and(9>3)))
print(True is False)
print(False in 'False')
print(((True==False)or(False>True))and(False<=True))

#-------------------------------------------------------------------------------
#Q.3
s2="here"
s=s1+" "+s2
print(s)

#-------------------------------------------------------------------------------
#Q.4


a=[1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
print(a[3][1][2])

#-------------------------------------------------------------------------------
#Q.5

s1="Nice to have it"
s2="here"
a=[1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
a.insert(0,s1)
a.append(s2)
print(a)

#-------------------------------------------------------------------------------
#Q.6

numbers=[386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615,
953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949,
687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445,
742, 717, 958,743, 527]
for i in numbers:
    if(i==237):
     print(i)
     break
    elif(i%2==0):
     print(i)

#-------------------------------------------------------------------------------
#Q.7

color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
print(color_list_1-color_list_2)

#-------------------------------------------------------------------------------
#Q.8

s=input("Enter a string")
alphabet=('abcdefghijklmnopqrstuvwxyz')
s=s.lower()
for i in alphabet:
    f=0
    if i not in s:
     f=1
     break
if(f==0):
    print("pangram")
else:
    print("Not a pangram")

#-------------------------------------------------------------------------------
#Q.9

n=eval(input("Enter the value of n"))
a=int("%d"%n)
b=int("%d%d"%(n,n))
c=int("%d%d%d"%(n,n,n))
print(a+b+c)

#-------------------------------------------------------------------------------
#Q.10

s=input("Enter a string")
s = s.replace(" ","")
print(s)
arr = s.split("#")
print(arr)
x = []
y = []

for i in range(len(arr[0])):
    x.append(int(arr[0][i]))
    y.append(int(arr[1][i]))

print(x,y)
print("x = " + str(x))
print("y = " + str(y))

x = list(map(int,list(arr[0])))
y = list(map(int,list(arr[1])))
print(x,y)

#-------------------------------------------------------------------------------

#Q.11

s=input("Enter a string")
m=s.split(',')
print(m)
m.sort()
print(m)

#--------------------------------------------------------------------------------
#Q.12

d = {'Student': ['Rahul', 'Kishore', 'Vidhya', 'Raakhi'], 'Marks': [57,87,67,79]}
d1=d['Marks']
l=max(d['Marks'])
j=0
for i in range(len(d1)):
    if(d1[i]==l):
        j=i

d2=d['Student']
print(d2[j])

#-------------------------------------------------------------------------------
#Q.13

s=input("Enter a string")
l=0
d=0
for i in s:
    if(i.isalpha()):
        l=l+1
    if(i.isnumeric()):
        d=d+1
print("Letters ",l)
print("Digits ",d)

#--------------------------------------------------------------------------
#Q.14
d = {'Name': ['Akash', 'Soniya', 'Vishakha' , 'Akshay', 'Rahul', 'Vikas'],
'Subject': ['Python', 'Java', 'Python', 'C', 'Python', 'Java'],
'Ratings': [8.4, 7.8, 8, 9, 8.2, 5.6]}
s=input('Enter a Subject: ')
l2=[]
l3=[]
l5 =[]
for i in range(len(d["Subject"])):
    if d["Subject"][i]==s:
        l2.append(d["Subject"][i])
        l3.append(d["Name"][i])
        l5.append(d["Ratings"][i])
d1={}
d1['Name']=l3
d1['Subject']=l2
d1['Ratings']=l5
print(d1)

#-------------------------------------------------------------------------------
#Q.15
import math
direction = [input().split(" ") for i in range(4)]
pos = [0,0]

for i in direction:
    if i[0] == "UP":
        pos[1] += int(i[1])
    elif i[0] == 'DOWN':
        pos[1] -= int(i[1])
    elif i[0] == "LEFT":
        pos[0] -= int(i[1])
    else:
        pos[0] += int(i[1])
print(pos)

dis = int(math.sqrt(pos[0] ** 2 + pos[1] ** 2))
print(dis)
#------------------------------------------------------------------------------       
                                      
