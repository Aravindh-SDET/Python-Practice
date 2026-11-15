a=8
b=5.5
Name="Aravindh"
Hometown='karamadai'
College='"BIT", Sathy'
print(a,b)
print('Hello',Name+'....!')
print("I am from "+Hometown)
print("I studied at",College)
print(Hometown[:-1])
print(Hometown[1:])
print(Hometown[-1:])
if(a%2==0):
    print("The number",a,"is Even")
    print('Even................!')
else:
    print("The number",a,"is Odd")
    print('Odd................!')
count=0
for x in range(a):
    if(a%(x+1)==0):
        count+=1
if(count==2):
    print(a,"Its a Prime Number",count)
else:
    print(a,"Its not a Prime Number",count)
