
"""
print("Choosing characted from string")
print("-------------------------------")
string = "Hello"

res=string[0]
l=len(string)
mi=int(l/2)
res=res+string[mi]
res=res+string[l-1]
print(res)

string2 = "Hi"
res=string2[0]
print(res)

string3="Heeololeo"
value=""
for i in range(0,len(string3),2):
   value=value+string3[i]
print(value)

print("\n")

print("---------------------------------")"""
  
print("Double the Character")
print("---------------------")
string4="The"
value=""
for i in string4:
    value = value+i*2
print(value)

string5="AAbb"
value=""
for i in string5:
    value=value+i*2
print(value)

stri = "Hi-There"
value=""
for i in stri:
    value=value+i*2
print(value)

print("---------------------------")

print("Count the even Integer in the list [2,1,2,3,4]")

myList=[2,1,2,3,4]
count=0
for i in range(0,len(myList)+1):
    if i%2==0:
      count = count+1
print(count)

print("count of the Even integer in the list [2,2,0]")
myList1=[2,2,0]
count=0
for i in range(0,len(myList1)+1):
    if i%2==0:
      count = count+1
print(count)
print("count of the Even integer in the list [1,3,5]")

li=[1,3,5]
count=0
for i in li:
    if i%2==0:
      count=count+1
print(count)


        


