print("Hello Vasu")
name = input("Write your name : ")
print("Hello", name, "Welcome here")

a = 123
b = "Vasu"
c= 'a'
print(a, b, c)

ln = input("Enter word : ")
length = len(ln)
print("Length is : ", length)

a = True
b = False
print(not a)
print(not b)

Keyword List in Python
import keyword
print(keyword.kwlist)

age = 20
if age > 18:
    print("Eligible to Vote")

def fun():
    print("Welcome here")
fun()

def evenodd(x):
if(x % 2 == 0):
        return "Even"
    else:
        return "Odd"
print(evenodd(4))
