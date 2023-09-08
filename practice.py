"""
# print("Hello, World!")



a = 51
b = 10;
#c = 10
if a > b: 
 print("Five is greater than two!") 
else:
    print("okay")



#THIS IS CASTING
x = str("hafsa")    # x will be '3'
y = int(3)    # y will be 3
z = float(5)  # z will be 5.0
print(x,y,z)



#THIS IS TYPE CHECKING
x = 5
y = "John"
print(type(x))
print(type(y))



#Assign Multiple Values
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

x = y = z = "Orange"
print(x)
print(y)
print(z)



#---If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)



#GLOBAL SCOPE
x = "awesome"
def myfunc():
  x = "cheeku"
  print("Python is " + x)
myfunc()



#NUMBER TYPES : int, float , complex
x = 33 
y = 5e3
z = -5j
print(x)
print(y)
print(type(z))



#GENERATE RANDOM NUMBERS
import random
print(random.randrange(1, 100))



#Loops
for x in "banana":
  print(x)



#LENGTH
para = "This is a paragraph"
print(len(para))



#CHECK IF THE VALUE IN STRING EXISTS
txt = "The best things in life are free!"
print("free" in txt) 
#in p if / else condition
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

#CHECK IF VALUE NOT EXISTS
txt = "The best things in life are free!"
print("expensive" not in txt)



#SLICING
b = "Hello, World!"
print(b[2:5])
c = "Hello, World!"
print(c[:5])            #slice from start
d = "Hello, World!"
print(d[2:])            #slice from end
e = "Hello, World!"
print(e[-5:-2])         #negative slicing



#STRING MODIFICATIONS/METHODS
#upper()
#lower()
#strip()
#replace()
#split()



#STRING FORMAT
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

#use index numbers {0} to be sure the arguments are placed in the correct placeholders
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))



def tri_recursion(k):
  print("haha", k)
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(8)
"""


areeb = ["rotu", "kaddu", "ullu", "kaddu" ,"dhkkan", "kaddu", "kaddu" ,"meesna"]
areeb.sort()
print(areeb)
