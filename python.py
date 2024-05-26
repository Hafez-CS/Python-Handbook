
1) Home
2) Variables
3) Data Types
4) Numbers
5) Strings
6) Booleans
7) Operators
8) Lists
9) Tuples
10) Sets
11) Dictionaries
12) if ... else
13) while Loops
14) for Loops
15) Functions
16) lambda
17) iterators(iter)
18) make my library
19) Datetime(import datetime)
20) Math
21) JSON
22) RegEx(import re)
23) Try...Except
24) Input
25) String Formatting
26) File Handling
27) Built In Functions
28) Python Error
29) Random(import random)
30) Enum
31) System(import sys)
32) OS(import OS)
33) Path(import path)
34) Pickle(import pickle)
35) Collections(import collections)
36) Operator(import operator)
37) Progress Bar
38) Matplotlib(chart)
39) Table(import tabulate)
40) OOP(Class)
41) CSV
42) txt


***************************************************************************************************************************************************************************

# https://www.w3schools.com/python/default.asp                     for read more

# https://www.geeksforgeeks.org/python-programming-language/       for read more

***************************************************************************************************************************************************************************

0) Home

print("Hello, World!")
>> "Hello, World!"


# hello world



# python y.py                    for run code in VScode terminal

# pip install x                  for install a library

# pip install --upgrade x        for upgrade a library

***************************************************************************************************************************************************************************

1) Variables


x = 5
y = "John"
print(x)
print(y)
>> 5
>> "John"

###################################################################

x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)
>> "Sally"

###################################################################

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

###################################################################

x = 5
y = "John"
print(type(x))
print(type(y))
>> <class 'int'>
>> <class 'str'>

###################################################################

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
>> "Orange"
>> "Banana"
>> "Cherry"

###################################################################

x = y = z = "Orange"
print(x)
print(y)
print(z)
>> "Orange"
>> "Orange"
>> "Orange"

###################################################################

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)
>> ["apple", "banana", "cherry"]
>> ["apple", "banana", "cherry"]
>> ["apple", "banana", "cherry"]

###################################################################

x = "Python is awesome"
print(x)
>> "Python is awesome"

###################################################################

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)
>> "Python" , "is" , "awesome"

###################################################################

x = "Python "
y = "is "
z = "awesome"
print(x + y + z)
>> "Python is awesome"

###################################################################

x = 5
y = 10
print(x + y)
>> 15

***************************************************************************************************************************************************************************

1) Data Types


"""
Text Type :	str

Numeric Types :	int, float, complex

Sequence Types :	list, tuple, range

Mapping Type :	dict

Set Types :	set, frozenset

Boolean Type :	bool

Binary Types :	bytes, bytearray, memoryview

None Type :	NoneType

"""


x = "Hello World"	                              # str	
x = 20	                                        # int	
x = 20.5	                                      # float	
x = 1j	                                        # complex	
x = ["apple", "banana", "cherry"]	              # list	
x = ("apple", "banana", "cherry")	              # tuple	
x = range(6)	                                  # range	
x = {"name" : "John", "age" : 36}  	            # dict	
x = {"apple", "banana", "cherry"}	              # set	
x = frozenset({"apple", "banana", "cherry"})	  # frozenset	
x = True	                                      # bool	
x = b"Hello"	                                  # bytes	
x = bytearray(5)	                              # bytearray	
x = memoryview(bytes(5))	                      # memoryview	
x = None	                                      # NoneType


x = str("Hello World")	                        # str	
x = int(20)	                                    # int	
x = float(20.5)	                                # float	
x = complex(1j)	                                # complex	
x = list(("apple", "banana", "cherry"))	        # list	
x = tuple(("apple", "banana", "cherry"))	      # tuple	
x = range(6)	                                  # range	
x = dict(name="John", age=36)	                  # dict	
x = set(("apple", "banana", "cherry"))	        # set	
x = frozenset(("apple", "banana", "cherry"))	  # frozenset	
x = bool(5)	                                    # bool	
x = bytes(5)	                                  # bytes	
x = bytearray(5)	                              # bytearray	
x = memoryview(bytes(5))	                      # memoryview

***************************************************************************************************************************************************************************

1) Numbers


x = 1    # int
y = 2.8  # float
z = 1j   # complex

x = 1
y = 35656222554887711
z = -3255522

x = 1.10
y = 1.0
z = -35.59

x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3

x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2

x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'

***************************************************************************************************************************************************************************

1) Strings


a = "Hello"
print(a)
>> "Hello"

###################################################################

a = "Hello, World!"
print(a[1])
>> "e"

###################################################################

b = "Hello, World!"
print(b[2:5])
>> "llo"

###################################################################

a = "Hello, World!"
print(len(a))
>> 13

###################################################################

txt = "The best things in life are free!"
print("free" in txt)
>> True

###################################################################

a = "Hello, World!"
print(a.upper())
>> "HELLO, WORLD!"

###################################################################

a = "Hello, World!"
print(a.lower())
>> "hello, world!"

###################################################################

a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"
>> "Hello, World!"

###################################################################

a = "Hello, World!"
print(a.replace("H", "J"))
>> "Jello, World!"

###################################################################

a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']
>> "['Hello', ' World!']"

###################################################################

a = "Hello"
b = "World"
c = a + b
print(c)
>> "HelloWorld"

###################################################################

a = "Hello"
b = "World"
c = a + " " + b
print(c)
>> "Hello World"

###################################################################

age = 36
txt = "My name is John, I am " + age
print(txt)
>> "My name is John, I am 36"

###################################################################

age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))
>> "My name is John, I am 36"

###################################################################

print('G','F', sep='', end='')
print('G')
>> "GFG"

###################################################################

print('09','12','2016', sep='-', end='\n')
>> "09-12-2016"

###################################################################

print('Red','Green','Blue', sep=',', end='@')
print('geeksforgeeks')
>> "Red,Green,Blue@geeksforgeeks"

###################################################################

print("Geeks : %2d, Portal : %5.2f" % (1, 05.333)) 
>> "Geeks :  1, Portal : 5.33"
 
###################################################################

print("Total students : %3d, Boys : %2d" % (240, 120))   # print integer value
>> "Total students : 240, Boys : 120"
 
###################################################################

print("%7.3o" % (25))   # print octal value
>> "    031"
 
###################################################################

print("%10.3E" % (356.08977))   # print exponential value
>> "3.561E+02"

###################################################################

tab = {'geeks': 4127, 'for': 4098, 'geek': 8637678}
print('Geeks: {0[geeks]:d}; For: {0[for]:d}; '
    'Geeks: {0[geek]:d}'.format(tab))
>> "Geeks: 4127; For: 4098; Geeks: 8637678"

###################################################################

"    \'    "	  # Single Quote
"    \\    "	  # Backslash	
"    \n    "	  # New Line	
"    \r    "	  # Carriage Return	
"    \t    " 	  # Tab	
"    \b    "	  # Backspace	
"    \f    "	  # Form Feed	
"    \ooo    "	# Octal value	
"    \xhh    " 	# Hex value

########################################

# All string methods


#####################################################################################################
# .capitalize()             # Converts the first character to upper case
txt = "hello, and welcome to my world."
x = txt.capitalize()
print (x)
>> "Hello, and welcome to my world."

#####################################################################################################
# .casefold()               # Converts string into lower case
txt = "Hello, And Welcome To My World!"
x = txt.casefold()
print(x)
>> "hello, and welcome to my world!"

#####################################################################################################
# .center()                 # Returns a centered string
txt = "banana"
x = txt.center(20)
print(x)
>> "       banana       "

#####################################################################################################
# .count()                  # Returns the number of times a specified value occurs in a string
txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple")
print(x)
>> 2

#####################################################################################################
# .encode()                 # Returns an encoded version of the string
txt = "My name is Ståle"
x = txt.encode()
print(x)
>> b'My name is St\xc3\xa5le'

#####################################################################################################
# .endswith()               # Returns true if the string ends with the specified value
txt = "Hello, welcome to my world."
x = txt.endswith(".")
print(x)
>> True

#####################################################################################################
# .expandtabs()             # Sets the tab size of the string
txt = "H\te\tl\tl\to"
x =  txt.expandtabs(2)
print(x)
>> "H e l l o"

#####################################################################################################
# .find()                   # Searches the string for a specified value and returns the position of where it was found
txt = "Hello, welcome to my world."
x = txt.find("welcome")
print(x)
>> 7

#####################################################################################################
# .format()                 # Formats specified values in a string
txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))
>> "For only 49.00 dollars!"

#####################################################################################################
# .index()                  # Searches the string for a specified value and returns the position of where it was found
txt = "Hello, welcome to my world."
x = txt.index("welcome")
print(x)
>> 7

#####################################################################################################
# .isalnum()                # Returns True if all characters in the string are alphanumeric
txt = "Company12"
x = txt.isalnum()
print(x)
>> True

#####################################################################################################
# .isalpha()                # Returns True if all characters in the string are in the alphabet
txt = "CompanyX"
x = txt.isalpha()
print(x)
>> True

#####################################################################################################
# .isascii()                # Returns True if all characters in the string are ascii characters
txt = "Company123"
x = txt.isascii()
print(x)
>> True

#####################################################################################################
# .isdecimal()	            # Returns True if all characters in the string are decimals
txt = "1234"
x = txt.isdecimal()
print(x)
>> True

#####################################################################################################
# .isdigit()                # Returns True if all characters in the string are digits
txt = "50800"
x = txt.isdigit()
print(x)
>> True

#####################################################################################################
# .isidentifier()           # Returns True if the string is an identifier
txt = "Demo"
x = txt.isidentifier()
print(x)
>> True

#####################################################################################################
# .islower()                # Returns True if all characters in the string are lower case
txt = "hello world!"
x = txt.islower()
print(x)
>> True

#####################################################################################################
# .isnumeric()              # Returns True if all characters in the string are numeric
txt = "565543"
x = txt.isnumeric()
print(x)
>> True

#####################################################################################################
# .isprintable()            # Returns True if all characters in the string are printable
txt = "Hello! Are you #1?"
x = txt.isprintable()
print(x)
>> True

#####################################################################################################
# .isspace()                # Returns True if all characters in the string are whitespaces
txt = "   "
x = txt.isspace()
print(x)
>> True

#####################################################################################################
# .istitle()                # Returns True if the string follows the rules of a title
txt = "Hello, And Welcome To My World!"
x = txt.istitle()
print(x)
>> True

#####################################################################################################
# .isupper()                # Returns True if all characters in the string are upper case
txt = "THIS IS NOW!"
x = txt.isupper()
print(x)
>> True

#####################################################################################################
# .join()                   # Joins the elements of an iterable to the end of the string
myTuple = ("John", "Peter", "Vicky")
x = "#".join(myTuple)
print(x)
>> "John#Peter#Vicky"

#####################################################################################################
# .ljust()                  # Returns a left justified version of the string
txt = "banana"
x = txt.ljust(20)
print(x, "is my favorite fruit.")
>> "banana               is my favorite fruit."

#####################################################################################################
# .lower()                  # Converts a string into lower case
txt = "Hello my FRIENDS"
x = txt.lower()
print(x)
>> "hello my friends"

#####################################################################################################
# .lstrip()                 # Returns a left trim version of the string
txt = "     banana     "
x = txt.lstrip()
print("of all fruits", x, "is my favorite")
>> "of all fruits banana      is my favorite"

#####################################################################################################
# .maketrans()              # Returns a translation table to be used in translations
txt = "Hello Sam!"
mytable = str.maketrans("S", "P")
print(txt.translate(mytable))
>> "Hello Pam!"

#####################################################################################################
# .partition()              # Returns a tuple where the string is parted into three parts
txt = "I could eat bananas all day"
x = txt.partition("bananas")
print(x)
>> ('I could eat ', 'bananas', ' all day')

#####################################################################################################
# .replace()                # Returns a string where a specified value is replaced with a specified value
txt = "I like bananas"
x = txt.replace("bananas", "apples")
print(x)
>> "I like apples"

#####################################################################################################
# .rfind()                  # Searches the string for a specified value and returns the last position of where it was found
txt = "Mi casa, su casa."
x = txt.rfind("casa")
print(x)
>> 12

#####################################################################################################
# .rindex()                 # Searches the string for a specified value and returns the last position of where it was found
txt = "Mi casa, su casa."
x = txt.rindex("casa")
print(x)
>> 12

#####################################################################################################
# .rjust()                  # Returns a right justified version of the string
txt = "banana"
x = txt.rjust(20)
print(x, "is my favorite fruit.")
>> "              banana is my favorite fruit."

#####################################################################################################
# .rpartition()             # Returns a tuple where the string is parted into three parts
txt = "I could eat bananas all day, bananas are my favorite fruit"
x = txt.rpartition("bananas")
print(x)
>> ('I could eat bananas all day, ', 'bananas', ' are my favorite fruit')

#####################################################################################################
# .rsplit()                 # Splits the string at the specified separator, and returns a list
txt = "apple, banana, cherry"
x = txt.rsplit(", ")
print(x)
>> ['apple', 'banana', 'cherry']

#####################################################################################################
# .rstrip()                 # Returns a right trim version of the string
txt = "     banana     "
x = txt.rstrip()
print("of all fruits", x, "is my favorite")
>> "of all fruits      banana is my favorite"

#####################################################################################################
# .split()                  # Splits the string at the specified separator, and returns a list
txt = "welcome to the jungle"
x = txt.split()
print(x)
>> ['welcome', 'to', 'the', 'jungle']

#####################################################################################################
# .splitlines()             # Splits the string at line breaks and returns a list
txt = "Thank you for the music\nWelcome to the jungle"
x = txt.splitlines()
print(x)
>> ['Thank you for the music', 'Welcome to the jungle']

#####################################################################################################
# .startswith()             # Returns true if the string starts with the specified value
txt = "Hello, welcome to my world."
x = txt.startswith("Hello")
print(x)
>> True

#####################################################################################################
# .strip()                  # Returns a trimmed version of the string
txt = "     banana     "
x = txt.strip()
print("of all fruits", x, "is my favorite")
>> "of all fruits banana is my favorite"

#####################################################################################################
# .swapcase()	            # Swaps cases, lower case becomes upper case and vice versa
txt = "Hello My Name Is PETER"
x = txt.swapcase()
print(x)
>> "hELLO mY nAME iS peter"

#####################################################################################################
# .title()                  # Converts the first character of each word to upper case
txt = "Welcome to my world"
x = txt.title()
print(x)
>> "Welcome To My World"

#####################################################################################################
# .translate()              # Returns a translated string
mydict = {83:  80}
txt = "Hello Sam!"
print(txt.translate(mydict))
>> "Hello Pam!"

#####################################################################################################
# .upper()                  # Converts a string into upper case
txt = "Hello my friends"
x = txt.upper()
print(x)
>> "HELLO MY FRIENDS"

#####################################################################################################
# .zfill()                  # Fills the string with a specified number of 0 values at the beginning
txt = "50"
x = txt.zfill(10)
print(x)
>> 0000000050

***************************************************************************************************************************************************************************

1) Booleans

print(10 > 9)
print(10 == 9)
print(10 < 9)
>> True
>> False
>> False


print(bool("Hello"))
print(bool(15))
>> True
>> True

***************************************************************************************************************************************************************************

1) Operators



# +		    x + y	       2 + 2 = 4
# -		    x - y	       2 - 2 = 0
# *		    x * y	       2 * 3 = 6
# /		    x / y	       4 / 2 = 2
# %		    x % y	       4 % 2 = 0
# **		  x ** y	     2 ** 3 = 8
# //		  x // y       8 // 4 = 2


# ==		x == y	       2 == 2
# !=		x != y	       2 != 3
# >		  x > y	         4 > 2
# <		  x < y	         2 < 4
# >=		x >= y	       4 >= 4
# <=		x <= y         4 <= 4


# and 	    Returns True if both statements are true	                                x < 5 and x < 10
# or	      Returns True if one of the statements is true	                            x < 5 or x < 4	
# not	      Reverse the result, returns False if the result is true	                  not(x < 5 and x < 10)


# in 	      Returns True if a sequence with the specified value is present in the object	        x in y	
# not in	  Returns True if a sequence with the specified value is not present in the object	    x not in y


# & 	      AND	Sets each bit to 1 if both bits are 1	                                                                                      x & y	
# |	        OR	Sets each bit to 1 if one of two bits is 1	                                                                                x | y	
# ^	        XOR	Sets each bit to 1 if only one of two bits is 1	                                                                            x ^ y	
# ~	        NOT	Inverts all the bits	                                                                                                      ~x	
# <<	      Zero fill left shift Shift left by pushing zeros in from the right and let the leftmost bits fall off	                          x << 2	
# >>	      Signed right shift Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off	    x >> 2


# =	  x = 5	             x = 5	
# +=	x += 3	           x = x + 3	
# -=	x -= 3	           x = x - 3	
# *=	x *= 3	           x = x * 3	
# /=	x /= 3	           x = x / 3	
# %=	x %= 3	           x = x % 3	
# //=	x //= 3	           x = x // 3	
# **=	x **= 3	           x = x ** 3	
# &=	x &= 3	           x = x & 3	
# |=	x |= 3	           x = x | 3	
# ^=	x ^= 3	           x = x ^ 3	
# >>=	x >>= 3	           x = x >> 3	
# <<=	x <<= 3	           x = x << 3

***************************************************************************************************************************************************************************

1) Lists


mylist = ["apple", "banana", "cherry"]


thislist = ["apple", "banana", "cherry"]
print(thislist)
>> ['apple', 'banana', 'cherry']


thislist = ["apple", "banana", "cherry"]
print(len(thislist))
>> 3


thislist = ["apple", "banana", "cherry"]
print(thislist[1])
>> "banana"


thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
>> ['cherry', 'orange', 'kiwi']


thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)
>> ['apple', 'blackcurrant', 'cherry']


thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)
>> ['apple', 'blackcurrant', 'watermelon', 'cherry']


thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)
>> ['apple', 'banana', 'watermelon', 'cherry']


thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)
>> ['apple', 'banana', 'cherry', 'orange']


thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
>> ['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']


thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)
>> ['apple', 'cherry']


thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)
>> ['apple', 'cherry']


thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)
>> ['apple', 'banana']


thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)
>> ['banana', 'cherry']


thislist = ["apple", "banana", "cherry"]
del thislist


thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)
>> []


thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)
>> ['banana', 'kiwi', 'mango', 'orange', 'pineapple']


thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)
>> ['pineapple', 'orange', 'mango', 'kiwi', 'banana']


thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)
>> ['banana', 'cherry', 'Kiwi', 'Orange']


thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)
>> ['apple', 'banana', 'cherry']


thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)
>> ['apple', 'banana', 'cherry']


list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)
>> ['a', 'b', 'c', 1, 2, 3]

########################################

# All List methods


#####################################################################################################
# .append()	    Adds an element at the end of the list
fruits = ['apple', 'banana', 'cherry']
fruits.append("orange")
print(fruits)
>> ['apple', 'banana', 'cherry', 'orange']

#####################################################################################################
# .clear()	    Removes all the elements from the list
fruits = ['apple', 'banana', 'cherry', 'orange']
fruits.clear()
print(fruits)
>> []

#####################################################################################################
# .copy()	    Returns a copy of the list
fruits = ['apple', 'banana', 'cherry', 'orange']
x = fruits.copy()
print(x)
>> ['apple', 'banana', 'cherry', 'orange']

#####################################################################################################
# .count()	    Returns the number of elements with the specified value
fruits = ['apple', 'banana', 'cherry']
x = fruits.count("cherry")
print(x)
>> 1

#####################################################################################################
# .extend()	    Add the elements of a list (or any iterable), to the end of the current list
fruits = ['apple', 'banana', 'cherry']
cars = ['Ford', 'BMW', 'Volvo']
fruits.extend(cars)
print(fruits)
>> ['apple', 'banana', 'cherry', 'Ford', 'BMW', 'Volvo']

#####################################################################################################
# index()	    Returns the index of the first element with the specified value
fruits = ['apple', 'banana', 'cherry']
x = fruits.index("cherry")
print(x)
>> 2

#####################################################################################################
# insert()	    Adds an element at the specified position
fruits = ['apple', 'banana', 'cherry']
fruits.insert(1, "orange")
print(fruits)
>> ['apple', 'orange', 'banana', 'cherry']

#####################################################################################################
# pop()	        Removes the element at the specified position
fruits = ['apple', 'banana', 'cherry']
fruits.pop(1)
print(fruits)
>> ['apple', 'cherry']

#####################################################################################################
# remove()	    Removes the item with the specified value
fruits = ['apple', 'banana', 'cherry']
fruits.remove("banana")
print(fruits)
>> ['apple', 'cherry']

#####################################################################################################
# reverse()	    Reverses the order of the list
fruits = ['apple', 'banana', 'cherry']
fruits.reverse()
print(fruits)
>> ['cherry', 'banana', 'apple']

#####################################################################################################
# sort()	    Sorts the list
cars = ['Ford', 'BMW', 'Volvo']
cars.sort()
print(cars)
>> ['BMW', 'Ford', 'Volvo']

***************************************************************************************************************************************************************************

1) Tuples


# count()	Returns the number of times a specified value occurs in a tuple
# index()	Searches the tuple for a specified value and returns the position of where it was found

mytuple = ("apple", "banana", "cherry")


thistuple = ("apple", "banana", "cherry")
print(thistuple)
>> ('apple', 'banana', 'cherry')


thistuple = ("apple", "banana", "cherry")
print(len(thistuple))
>> 3


thistuple = ("apple", "banana", "cherry")
print(thistuple[1])
>> "banana"


thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print(thistuple)
>> ('banana', 'cherry')


thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple)
>> Error


tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)
>> ('a', 'b', 'c', 1, 2, 3)

***************************************************************************************************************************************************************************

1) Sets


myset = {"apple", "banana", "cherry"}


thisset = {"apple", "banana", "cherry"}
print(thisset)
>> {'cherry', 'banana', 'apple'}


thisset = {"apple", "banana", "cherry"}
print(len(thisset))
>> 3


thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)
>> {'cherry', 'apple', 'banana', 'orange'}


thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)
>> {'papaya', 'mango', 'pineapple', 'apple', 'banana', 'cherry'}


thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)
>> {'cherry', 'apple'}


thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)
>> {'cherry', 'apple'}


thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
>> "cherry"
print(thisset)
>> {'apple', 'banana'}


thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)
>> ()


thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset)
>> Error


set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)
>> {1, 'c', 2, 3, 'a', 'b'}


set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)
>> {1, 'c', 2, 3, 'a', 'b'}


x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x)
>> {'apple'}


x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print(z)
>> {'apple'}

########################################

# All Sets methods


#####################################################################################################
# add()	                            Adds an element to the set
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)
>> {'cherry', 'orange', 'apple', 'banana'}

#####################################################################################################
# clear()	                        Removes all the elements from the set
fruits = {"apple", "banana", "cherry"}
fruits.clear()
print(fruits)
>> set()

#####################################################################################################
# copy()	                        Returns a copy of the set
fruits = {"apple", "banana", "cherry"}
x = fruits.copy()
print(x)
>> {'apple', 'cherry', 'banana'}

#####################################################################################################
# difference()	                    Returns a set containing the difference between two or more sets
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.difference(y)
print(z)
>> {'cherry', 'banana'}

#####################################################################################################
# difference_update()               Removes the items in this set that are also included in another, specified set
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.difference_update(y)
print(x)
>> {'cherry', 'banana'}

#####################################################################################################
# discard()	                        Remove the specified item
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)
>> {'apple', 'cherry'}

#####################################################################################################
# intersection()	                Returns a set, that is the intersection of two other sets
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print(z)
>> {'apple'}

#####################################################################################################
# intersection_update()	            Removes the items in this set that are not present in other, specified set(s)
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y) 
print(x)
>> {'apple'}

#####################################################################################################
# isdisjoint()	                    Returns whether two sets have a intersection or not
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "facebook"}
z = x.isdisjoint(y) 
print(z)
>> True

#####################################################################################################
# issubset()	                    Returns whether another set contains this set or not
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}
z = x.issubset(y)
print(z)
>> True

#####################################################################################################
# issuperset()	                    Returns whether this set contains another set or not
x = {"f", "e", "d", "c", "b", "a"}
y = {"a", "b", "c"}
z = x.issuperset(y) 
print(z)
>> True

#####################################################################################################
# pop()	                            Removes an element from the set
fruits = {"apple", "banana", "cherry"}
fruits.pop() 
print(fruits)
>> {'banana', 'cherry'}

#####################################################################################################
# remove()	                        Removes the specified element
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana") 
print(fruits)
>> {'cherry', 'apple'}

#####################################################################################################
# symmetric_difference()	        Returns a set with the symmetric differences of two sets
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)
print(z)
>> {'cherry', 'microsoft', 'banana', 'google'}

#####################################################################################################
# symmetric_difference_update()	    inserts the symmetric differences from this set and another
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print(x)
>> {'google', 'microsoft', 'banana', 'cherry'}

#####################################################################################################
# union()	                        Return a set containing the union of sets
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.union(y)
print(z)
>> {'apple', 'microsoft', 'cherry', 'banana', 'google'}

#####################################################################################################
# update()	                        Update the set with the union of this set and others
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.update(y) 
print(x)
>> {'cherry', 'microsoft', 'banana', 'apple', 'google'}

***************************************************************************************************************************************************************************

1) Dictionaries



thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}



thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
>> {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}



thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])
>> "Ford"



thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(len(thisdict))
>> 3



thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}



thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)
>> {'name': 'John', 'age': 36, 'country': 'Norway'}



thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict.get("model")
>> "Mustang"
x = thisdict["model"]
>> "Mustang"



thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict.keys())
>> dict_keys(['brand', 'model', 'year'])



car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}



thisdict = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
print(thisdict.values())
>> dict_values(['Ford', 'Mustang', 1964])



thisdict = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
print(thisdict.items())
>> dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])



thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018

# or

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})



thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)
>> {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'red'}

# or

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color": "red"})



thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)
>> {'brand': 'Ford', 'year': 1964}

# or

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)
>> {'brand': 'Ford', 'model': 'Mustang'}

# or

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)
>> {'brand': 'Ford', 'year': 1964}



thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)
>> {}



thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict.values():
  print(x)
>> "Ford"
   "Mustang"
   1964



thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict.keys():
  print(x)
>> "brand"
   "model"
   "year"



thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)
>> {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}



myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

########################################

# All Dictionaries methods


#####################################################################################################
# .clear()	         Removes all the elements from the dictionary
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.clear()
print(car)
>> {}

#####################################################################################################
# copy()	         Returns a copy of the dictionary
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.copy()
print(x)
>> {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

#####################################################################################################
# fromkeys()	     Returns a dictionary with the specified keys and value
x = ('key1', 'key2', 'key3')
y = 0
thisdict = dict.fromkeys(x, y)
print(thisdict)
>> {'key1': 0, 'key2': 0, 'key3': 0}

#####################################################################################################
# get()	             Returns the value of the specified key
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.get("model")
print(x)
>> "Mustang"

#####################################################################################################
# items()	         Returns a list containing a tuple for each key value pair
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.items()
print(x)
>> dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])

#####################################################################################################
# keys()	         Returns a list containing the dictionary's keys
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.keys()
print(x)
>> dict_keys(['brand', 'model', 'year'])

#####################################################################################################
# pop()	             Removes the element with the specified key
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.pop("model")
print(car)
>> {'brand': 'Ford', 'year': 1964}

#####################################################################################################
# popitem()	         Removes the last inserted key-value pair
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.popitem()
print(car)
>> {'brand': 'Ford', 'model': 'Mustang'}

#####################################################################################################
# setdefault()	     Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.setdefault("model", "Bronco")
print(x)
>> "Mustang"

#####################################################################################################
# update()	         Updates the dictionary with the specified key-value pairs
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.update({"color": "White"})
print(car)
>> {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'White'}

#####################################################################################################
# values()	         Returns a list of all the values in the dictionary
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.values()
print(x)
>> dict_values(['Ford', 'Mustang', 1964])

***************************************************************************************************************************************************************************

1) if ... else


# Equals :                      a == b
# Not Equals :                  a != b
# Less than :                   a < b
# Less than or equal to :       a <= b
# Greater than :                a > b
# Greater than or equal to :    a >= b


a = 33
b = 200
if b > a:
  print("b is greater than a")
>> "b is greater than a"



a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
>> "a and b are equal"



a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
>> "a is greater than b"



a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")
>> "b is not greater than a"



a = 200
b = 100
if a > b: print("a is greater than b")
>> "a is greater than b"



a = 2
b = 330
print("A") if a > b else print("B")
>> "B"



a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")
>> "="



a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")
>> "Both conditions are True"



a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")
>> "At least one of the conditions is True"



a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")
>> "a is NOT greater than b"



x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")
>> "Above ten,"
   "and also above 20!"

***************************************************************************************************************************************************************************

1) while Loops


i = 1
while i < 6:
  print(i)
  i += 1
>> 1
   2
   3
   4
   5



i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1
>> 1
   2
   3



i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
>> 1
   2
   4
   5
   6



i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")
>> 1
   2
   3
   4
   5
   "i is no longer less than 6"

***************************************************************************************************************************************************************************

1) for Loops


fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
>> "apple"
   "banana"
   "cherry"



for x in "banana":
  print(x)
>> 'b'
   'a'
   'n'
   'a'
   'n'
   'a'



fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)
>> "apple"



fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)
>> "apple"
   "cherry"



for x in range(6):
  print(x)
>> 0
   1
   2
   3
   4
   5



for x in range(2, 6):
  print(x)
>> 2
   3
   4
   5



for x in range(2, 30, 3):
  print(x)
>> 2
   5
   8
   11
   14
   17
   20
   23
   26
   29



for x in range(6):
  print(x)
else:
  print("Finally finished!")
>> 0
   1
   2
   3
   4
   5
   "Finally finished!"



for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")
>> 0
   1
   2



adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)
>> "red apple"
   "red banana"
   "red cherry"
   "big apple"
   "big banana"
   "big cherry"
   "tasty apple"
   "tasty banana"
   "tasty cherry"

***************************************************************************************************************************************************************************

1) Functions


def my_function():
  print("Hello from a function")

my_function()
>> "Hello from a function"

###################################################################

def myfunc():
  x = 300
  print(x)
myfunc()
>> 300

###################################################################

def myfunc():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfunc()
>> 300

###################################################################

x = 300
def myfunc():
  print(x)

myfunc()
print(x)
>> 300
>> 300

###################################################################

x = 300
def myfunc():
  x = 200
  print(x)

myfunc()
print(x)
>> 200
>> 300

###################################################################

def myfunc():
  global x
  x = 300

myfunc()
print(x)
>> 300

###################################################################

x = 300
def myfunc():
  global x
  x = 200

myfunc()
print(x)
>> 200

###################################################################

def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function(fname = "Tobias")
my_function("Linus")

>> "Emil Refsnes"
>> "Tobias Refsnes"
>> "Linus Refsnes"

###################################################################

def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")
>> "Emil Refsnes"

###################################################################

def my_function(*kids):  #  *  it's for more than one value
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")
>> "The youngest child is Linus"

###################################################################

def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")
>> "The youngest child is Linus"

###################################################################

def my_function(**kid):  # **  it's mean we don't need call number , just call that word
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")
>> "His last name is Refsnes"

###################################################################

def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")
>> "I am from Sweden"
>> "I am from India"
>> "I am from Norway"
>> "I am from Brazil"

###################################################################

def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]
my_function(fruits)
>> "apple"
   "banana"
   "cherry"

###################################################################

def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))
>> 15
>> 25
>> 45

###################################################################

def my_function(x, /):
  print(x)

my_function(3)
>> 3

###################################################################

def my_function(*, x):
  print(x)

my_function(x = 3)
>> 3

###################################################################

def my_function(a, b, /, *, c, d):
  print(a + b + c + d)

my_function(5, 6, c = 7, d = 8)
>> 26

###################################################################

def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)

>> "Recursion Example Results"
   1
   3
   6
   10
   15
   21

###################################################################


def shout(text): 
    return text.upper() 
 
def whisper(text): 
    return text.lower() 
 
def greet(func): 
    # storing the function in a variable 
    greeting = func("""Hi, I am created by a function passed as an argument.""") 
    print (greeting) 
 
greet(shout) 
greet(whisper) 

>> "HI, I AM CREATED BY A FUNCTION PASSED AS AN ARGUMENT."
   "hi, i am created by a function passed as an argument."

###################################################################

def say_hello(name):
    return f"Hello {name}"

def be_awesome(name):
    return f"Yo {name}, together we're the awesomest!"

def greet_bob(greeter_func):
    return greeter_func("Bob")

greet_bob(say_hello)
>> 'Hello Bob'

greet_bob(be_awesome)
>> 'Yo Bob, together were the awesomest!'

###################################################################

def parent():
    print("Printing from parent()")

    def first_child():
        print("Printing from first_child()")

    def second_child():
        print("Printing from second_child()")

    second_child()
    first_child()

parent()
>> "Printing from parent()"
   "Printing from second_child()"
   "Printing from first_child()

###################################################################

ِDecorator :



"""
decorators are used in Python to modify the behavior of functions or classes. 
They are higher-order functions that take a function or class as input and return a new function or class with modified behavior. 
Decorators are commonly used to add new functionality to existing code without changing the underlying implementation, 
making the code more usable and modular.

"""


# for first , look at this and undrestand it :

def decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

def say_whee():
    print("Whee!")

say_whee = decorator(say_whee)


>> "Something is happening before the function is called."
   "Whee!"
   "Something is happening after the function is called."


# now we can do this with Decorator :


def decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@decorator
def say_whee():
    print("Whee!")

>> "Something is happening before the function is called."
   "Whee!"
   "Something is happening after the function is called."

#################################

def make_pretty(func):

    def inner():
        print("I got decorated")
        func()
    return inner

@make_pretty
def ordinary():
    print("I am ordinary")

ordinary()  

>> "I got decorated"
   "I am ordinary"

#################################

def star(func):
    def inner(*args, **kwargs):
        print("*" * 30)
        func(*args, **kwargs)
        print("*" * 30)
    return inner

def percent(func):
    def inner(*args, **kwargs):
        print("%" * 30)
        func(*args, **kwargs)
        print("%" * 30)
    return inner

@star
@percent
def printer(msg):
    print(msg)
printer("Hello")

>> '******************************"
   "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"
   "Hello"
   "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"
   "******************************"

###################################################################

generator :



"""
Generator in Python is an easy way to generate browsers and with this feature you can easily control one and exit it at any time. 
In the case of ordinary functions in Python, the issue of speed and amount of memory is raised. 
You have problems in terms of speed and memory in a Python function, 
which have been solved to a large extent by using Generator in Python.

"""


def simpleGeneratorFun(): 
    yield 1            
    yield 2            
    yield 3            
   
for value in simpleGeneratorFun():  
    print(value)

>> 1
   2
   3


# Or we can do this :


def simpleGeneratorFun(): 
    yield 1
    yield 2
    yield 3
   
x = simpleGeneratorFun() 
print(next(x)) 
print(next(x)) 
print(next(x))

>> 1
   2
   3

#################################

def fib(limit): 
      
    a, b = 0, 1
    while a < limit: 
        yield a 
        a, b = b, a + b 
  
x = fib(5) 

print(next(x))  
print(next(x)) 
print(next(x)) 
print(next(x)) 
print(next(x)) 

print("\nUsing for in loop") 
for i in fib(5):  
    print(i)


>> 0
   1
   1
   2
   3
   "Using for in loop"
   0
   1
   1
   2
   3

###################################################################

Name & Main :



"""    Management and control function    """

from time import sleep

print("This is my file to demonstrate best practices.")

def process_data(data):
    print("Beginning data processing...")
    modified_data = data + " that has been modified"
    sleep(3)
    print("Data processing finished.")
    return modified_data

def main():
    data = "My data read from the Web"
    print(data)
    modified_data = process_data(data)
    print(modified_data)

if __name__ == "__main__":
    main()


>> "This is my file to demonstrate best practices."
   "My data read from the Web"
   "Beginning data processing..."
   "Data processing finished."
   "My data read from the Web that has been modified"

"""  With this method, it is possible to manage which function is executed and in what model the scripts are executed  """


#################################

def echo(text: str, repetitions: int = 3) -> str:
    """Imitate a real-world echo."""
    echoed_text = ""
    for i in range(repetitions, 0, -1):
        echoed_text += f"{text[-i:]}\n"
    return f"{echoed_text.lower()}."

if __name__ == "__main__":
    text = input("Yell something at a mountain: ")
    print(echo(text))


>> Yell something at a mountain: hh
   hh
   hh
   h 
   . 

***************************************************************************************************************************************************************************

1) lambda


x = lambda a : a + 10
print(x(5))
>> 15



x = lambda a, b : a * b
print(x(5, 6))
>> 30



x = lambda a, b, c : a + b + c
print(x(5, 6, 2))
>> 13



def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
print(mydoubler(11))
>> 22



def myfunc(n):
  return lambda a : a * n

mytripler = myfunc(3)
print(mytripler(11))
>> 22



def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)
print(mydoubler(11))
print(mytripler(11))
>> 22
>> 33

***************************************************************************************************************************************************************************

1) iterators (iter)


mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))
>> "apple"
>> "banana"
>> "cherry"



mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
>> 'b'
>> 'a'
>> 'n'
>> 'a'
>> 'n'
>> 'a'



mytuple = ("apple", "banana", "cherry")
for x in mytuple:
  print(x)
>> "apple"
   "banana"
   "cherry"

***************************************************************************************************************************************************************************

1) make my library


# for first make a python file as app.py
# and write some func or class :

def greeting(name):
  print("Hello, " + name)

# and open a nother python file as try.py and wrire this :
  
import app

app.greeting("Jonathan")
>> "Hello, Jonathan"

# now you have your own library 


#-----------------------------------------------------

# example:

# app.py :

person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}

# try.py :

import app
a = app.person1["age"]
print(a)
>> 36

# or

import app as mx
a = mx.person1["age"]
print(a)

***************************************************************************************************************************************************************************

1) Datetime(import datetime)


import datetime
x = datetime.datetime.now()
print(x)
>> 2024-02-21 05:37:25.261486


import datetime
x = datetime.datetime.now()
print(x.year)
print(x.strftime("%A"))
>> 2024
>> Wednesday


import datetime
x = datetime.datetime(2020, 5, 17)
print(x)
>> 2020-05-17 00:00:00


import datetime
x = datetime.datetime(2018, 6, 1)
print(x.strftime("%B"))
>> June



# %a	Weekday, short version	Wed	
# %A	Weekday, full version	Wednesday	
# %w	Weekday as a number 0-6, 0 is Sunday	3	
# %d	Day of month 01-31	31	
# %b	Month name, short version	Dec	
# %B	Month name, full version	December	
# %m	Month as a number 01-12	12	
# %y	Year, short version, without century	18	
# %Y	Year, full version	2018	
# %H	Hour 00-23	17	
# %I	Hour 00-12	05	
# %p	AM/PM	PM	
# %M	Minute 00-59	41	
# %S	Second 00-59	08	
# %f	Microsecond 000000-999999	548513	
# %z	UTC offset	+0100	
# %Z	Timezone	CST	
# %j	Day number of year 001-366	365	
# %U	Week number of year, Sunday as the first day of week, 00-53	52	
# %W	Week number of year, Monday as the first day of week, 00-53	52	
# %c	Local version of date and time	Mon Dec 31 17:41:00 2018	
# %C	Century	20	
# %x	Local version of date	12/31/18	
# %X	Local version of time	17:41:00	
# %%	A % character	%	
# %G	ISO 8601 year	2018	
# %u	ISO 8601 weekday (1-7)	1	
# %V	ISO 8601 weeknumber (01-53)	01

***************************************************************************************************************************************************************************

1) Math


x = min(5, 10, 25)
y = max(5, 10, 25)
print(x)
print(y)
>> 5
>> 25


x = abs(-7.25)
print(x)
>> 7.25


x = pow(4, 3)
print(x)
>> 64


import math
x = math.sqrt(64)
print(x)
>> 8.0


import math
x = math.ceil(1.4)
y = math.floor(1.4)
print(x) # returns 2
print(y) # returns 1
>> 2
>> 1


import math
x = math.pi
print(x)
>> 3.141592653589793

########################################

# All math methods


#####################################################################################################
# math.ceil()                    Rounds a number up to the nearest integer
import math
print(math.ceil(1.4))
print(math.ceil(5.3))
print(math.ceil(-5.3))
print(math.ceil(22.6))
print(math.ceil(10.0))
>> 2
>> 6
>> -5
>> 23
>> 10

#####################################################################################################
# math.comb()                    Returns the number of ways to choose k items from n items without repetition and order
# Import math Library
import math
n = 7
k = 5
print (math.comb(n, k))
>> 21

#####################################################################################################
# math.copysign()                Returns a float consisting of the value of the first parameter and the sign of the second parameter
import math  
print(math.copysign(4, -1))
print(math.copysign(-8, 97.21))
print(math.copysign(-43, -76))
>> -4.0
>> 8.0
>> -43.0

#####################################################################################################
# math.cos()                     Returns the cosine of a number
import math
print (math.cos(0.00))
print (math.cos(-1.23))
print (math.cos(10))
print (math.cos(3.14159265359))
>> 1.0
>> 0.3342377271245026
>> -0.8390715290764524
>> -1.0

#####################################################################################################
# math.degrees()                 Converts an angle from radians to degrees
import math
print (math.degrees(8.90))
print (math.degrees(-20))
print (math.degrees(1))
print (math.degrees(90))
>> 509.9324376664327
>> -1145.9155902616465
>> 57.29577951308232
>> 5156.620156177409

#####################################################################################################
# math.dist()                    Returns the Euclidean distance between two points (p and q), where p and q are the coordinates of that point
import math

p = [3]
q = [1]
print (math.dist(p, q))
>> 2.0

p = [3, 3]
q = [6, 12]
print (math.dist(p, q))
>> 9.486832980505138

#####################################################################################################
# math.fabs()                    Returns the absolute value of a number
import math
print(math.fabs(-66.43))
print(math.fabs(-7))
>> 66.43
>> 7.0

#####################################################################################################
# math.floor()                   Rounds a number down to the nearest integer
import math
print(math.floor(0.6))
print(math.floor(1.4))
print(math.floor(5.3))
print(math.floor(-5.3))
print(math.floor(22.6))
print(math.floor(10.0))
>> 0
>> 1
>> 5
>> -6
>> 22
>> 10

#####################################################################################################
# math.fmod()                    Returns the remainder of x/y
import math
print(math.fmod(20, 4))
print(math.fmod(20, 3))
print(math.fmod(15, 6))
print(math.fmod(-10, 3))
print(math.fmod(0, 0))
>> 0.0
>> 2.0
>> 3.0
>> -1.0

#####################################################################################################
# math.fsum()                    Returns the sum of all items in any iterable (tuples, arrays, lists, etc.)
import math
print(math.fsum([1, 2, 3, 4, 5]))
print(math.fsum([100, 400, 340, 500]))
print(math.fsum([1.7, 0.3, 1.5, 4.5]))
>> 15.0
>> 1340.0
>> 8.0

#####################################################################################################
# math.gcd()                     Returns the greatest common divisor of two integers
import math
print (math.gcd(3, 6))
print (math.gcd(6, 12))
print (math.gcd(12, 36))
print (math.gcd(-12, -36))
print (math.gcd(5, 12))
print (math.gcd(10, 0))
print (math.gcd(0, 34))
print (math.gcd(0, 0))
>> 3
>> 6
>> 12
>> 12
>> 1
>> 10
>> 34
>> 0

#####################################################################################################
# math.isclose()                 Checks whether two values are close to each other, or not
import math
print(math.isclose(1.233, 1.4566))
print(math.isclose(1.233, 1.233))
print(math.isclose(1.233, 1.24))
print(math.isclose(1.233, 1.233000001))
>> False
>> True
>> False
>> True

***************************************************************************************************************************************************************************

1) JSON



import json
# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'
# parse x:
y = json.loads(x)
# the result is a Python dictionary:
print(y["age"])
>> 30



import json
# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}
# convert into JSON:
y = json.dumps(x)
# the result is a JSON string:
print(y)
>> {"name": "John", "age": 30, "city": "New York"}



import json
print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))
>> {"name": "John", "age": 30}
>> ["apple", "bananas"]
>> ["apple", "bananas"]
>> "hello"
>> 42
>> 31.76
>> true
>> false
>> null



import json
x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}
print(json.dumps(x))
>> {"name": "John", "age": 30, "married": true, "divorced": false, "children": ["Ann", "Billy"], "pets": null, "cars": [{"model": "BMW 230", "mpg": 27.5}, {"model": "Ford Edge", "mpg": 24.1}]}

***************************************************************************************************************************************************************************

1) RegEx (import re)


import re
txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)
>> ['ai', 'ai']


# findall	  Returns a list containing all matches
# search	  Returns a Match object if there is a match anywhere in the string
# split	    Returns a list where the string has been split at each match
# sub	      Replaces one or many matches with a string

# []	       A set of characters	                                                                 "[a-m]"	
# \	         Signals a special sequence (can also be used to escape special characters)	           "\d"	
# .	         Any character (except newline character)	                                             "he..o"	
# ^	         Starts with	                                                                         "^hello"	
# $	         Ends with	                                                                           "planet$"	
# *	         Zero or more occurrences	                                                             "he.*o"	
# +	         One or more occurrences	                                                             "he.+o"	
# ?	         Zero or one occurrences	                                                             "he.?o"	
# {}	       Exactly the specified number of occurrences	                                         "he.{2}o"	
# |	         Either or	                                                                           "falls|stays"	
# ()	       Capture and group


# regex has many things , for easyer way use : 
# Regex online like : https://regex101.com/

***************************************************************************************************************************************************************************

1) Try...Except


# The     try          block lets you test a block of code for errors.
# The     except       block lets you handle the error.
# The     else         block lets you execute code when there is no error.
# The     finally      block lets you execute code, regardless of the result of the try- and except blocks.


try:
  print(x)
except:
  print("An exception occurred")
>> "An exception occurred"



try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")
>> "Variable x is not defined"



try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")
>> "Hello"
>> "Nothing went wrong"



try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")
>> "Something went wrong"
>> "The 'try except' is finished"



try:
  f = open("demofile.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")
>> "Something went wrong when opening the file"

***************************************************************************************************************************************************************************

1) Input


username = input("Enter username:")
print("Username is: " + username)
>> "Username is: iran"


num1 = int(input())
num2 = int(input())
print(num1 + num2)


num1 = float(input())
num2 = float(input())
print(num1 + num2)


# taking two inputs at a time
x, y = input("Enter two values: ").split()
print("Number of boys: ", x)
print("Number of girls: ", y)

***************************************************************************************************************************************************************************

1) String Formatting


price = 49
txt = "The price is {} dollars"
print(txt.format(price))
>> "The price is 49 dollars"



quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))
>> "I want 3 pieces of item number 567 for 49.00 dollars."

***************************************************************************************************************************************************************************

1) File Handling


# close()	        Closes the file
# detach()	        Returns the separated raw stream from the buffer
# fileno()	        Returns a number that represents the stream, from the operating system's perspective
# flush()	        Flushes the internal buffer
# isatty()	        Returns whether the file stream is interactive or not
# read()	        Returns the file content
# readable()	    Returns whether the file stream can be read or not
# readline()	    Returns one line from the file
# readlines()	    Returns a list of lines from the file
# seek()	        Change the file position
# seekable()	    Returns whether the file allows us to change the file position
# tell()	        Returns the current file position
# truncate()	    Resizes the file to a specified size
# writable()	    Returns whether the file can be written to or not
# write()	        Writes the specified string to the file
# writelines()	    Writes a list of strings to the file

#####################################################################################################

## File Handling :

# "r" - Read - Default value. Opens a file for reading, error if the file does not exist

# "a" - Append - Opens a file for appending, creates the file if it does not exist

# "w" - Write - Opens a file for writing, creates the file if it does not exist

# "x" - Create - Creates the specified file, returns an error if the file exists

# "t" - Text - Default value. Text mode

# "b" - Binary - Binary mode (e.g. images)


f = open("demofile.txt")


f = open("demofile.txt", "rt")


f = open("demofile.txt", "r")
print(f.read())


f = open("D:\\myfiles\welcome.txt", "r")
print(f.read())


f = open("demofile.txt", "r")
print(f.read(5))  # Return the 5 first characters of the file


f = open("demofile.txt", "r")
print(f.readline())


f = open("demofile.txt", "r")
print(f.readline())
f.close()

#####################################################################################################

## Write to an Existing File : 

# "a" - Append - will append to the end of the file

# "w" - Write - will overwrite any existing content


f = open("demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()
#open and read the file after the appending:
f = open("demofile2.txt", "r")
print(f.read())
>> "Now the file has more content!"


f = open("demofile3.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()
#open and read the file after the overwriting:
f = open("demofile3.txt", "r")
print(f.read())
>> "Woops! I have deleted the content!"


#####################################################################################################

## Create a New File :

# "x" - Create - will create a file, returns an error if the file exist

# "a" - Append - will create a file if the specified file does not exist

# "w" - Write - will create a file if the specified file does not exist


f = open("myfile.txt", "x")


f = open("myfile.txt", "w")

#####################################################################################################

## Delete a File :

import os
os.remove("demofile.txt")

#####################################################################################################

## Check if File exist :

import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")

#####################################################################################################

## Delete Folder :

import os
os.rmdir("myfolder")

***************************************************************************************************************************************************************************

1) Built In Functions


# abs()                    Returns the absolute value of a number
x = abs(-7.25)
print(x)
>> 7.25

###################################################################

# all()                    Returns True if all items in an iterable object are true
mylist = [True, True, True]
x = all(mylist)
print(x)
>> True

###################################################################

# any()                    Returns True if any item in an iterable object is true
mylist = [False, True, False]
x = any(mylist)
print(x)
>> True

###################################################################

# ascii()                  Returns a readable version of an object. Replaces none-ascii characters with escape character
x = ascii("My name is Ståle")
print(x)
>> 'My name is St\xe5le'

###################################################################

# bin()                    Returns the binary version of a number
x = bin(36)
print(x)
>> 0b100100

###################################################################

# bool()                   Returns the boolean value of the specified object
x = bool(1)
print(x)
>> True

###################################################################

# bytearray()              Returns an array of bytes
x = bytearray(4)
print(x)
>> bytearray(b'\x00\x00\x00\x00')

###################################################################

# bytes()                  Returns a bytes object
x = bytes(4)
print(x)
>> b'\x00\x00\x00\x00'

###################################################################

# callable()               Returns True if the specified object is callable, otherwise False
x = 5
print(callable(x))
>> False

###################################################################

# chr()                    Returns a character from the specified Unicode code.
x = chr(97)
print(x)
>> 'a'

###################################################################

# complex()                Returns a complex number
x = complex(3, 5)
print(x)
>> (3+5j)

###################################################################

# dir()                    Returns a list of the specified object's properties and methods
class Person:
  name = "John"
  age = 36
  country = "Norway"

print(dir(Person))
>> ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'age', 'country', 'name']

###################################################################

# divmod()                 Returns the quotient and the remainder when argument1 is divided by argument2
x = divmod(5, 2)
print(x)
>> (2, 1)

###################################################################

# enumerate()              Takes a collection (e.g. a tuple) and returns it as an enumerate object
x = ('apple', 'banana', 'cherry')
y = enumerate(x)
print(y)
>> <enumerate object at 0x14f74341f400>

###################################################################

# eval()                   Evaluates and executes an expression
x = 'print(55)'
eval(x)
print(x)
>> 55

###################################################################

# exec()                   Executes the specified code (or object)
x = 'name = "John"\nprint(name)'
exec(x)
>> "John"

###################################################################

# filter()                 Use a filter function to exclude items in an iterable object
ages = [5, 12, 17, 18, 24, 32]

def myFunc(x):
  if x < 18:
    return False
  else:
    return True

adults = filter(myFunc, ages)

for x in adults:
  print(x)
>> 18
   24
   32

###################################################################

# float()                  Returns a floating point number
x = float(3)
print(x)
>> 3.0

###################################################################

# format()                 Formats a specified value

'<' - Left aligns the result (within the available space)
'>' - Right aligns the result (within the available space)
'^' - Center aligns the result (within the available space)
'=' - Places the sign to the left most position
'+' - Use a plus sign to indicate if the result is positive or negative
'-' - Use a minus sign for negative values only
' ' - Use a leading space for positive numbers
',' - Use a comma as a thousand separator
'_' - Use a underscore as a thousand separator
'b' - Binary format
'c' - Converts the value into the corresponding unicode character
'd' - Decimal format
'e' - Scientific format, with a lower case e
'E' - Scientific format, with an upper case E
'f' - Fix point number format
'F' - Fix point number format, upper case
'g' - General format
'G' - General format (using a upper case E for scientific notations)
'o' - Octal format
'x' - Hex format, lower case
'X' - Hex format, upper case
'n' - Number format
'%' - Percentage format

x = format(0.5, '%')
print(x)
>> 50.000000%

###################################################################

# frozenset()              Returns a frozenset object
mylist = ['apple', 'banana', 'cherry']
x = frozenset(mylist)
print(x)
>> frozenset({'banana', 'cherry', 'apple'})

###################################################################

# hex()                    Converts a number into a hexadecimal value
x = hex(255)
print(x)
>> 0xff

###################################################################

# id()                     Returns the id of an object
x = ('apple', 'banana', 'cherry')
y = id(x)
print(y)
>> 23082267064192

###################################################################

# isinstance()             Returns True if a specified object is an instance of a specified object
x = isinstance(5, int)
print(x)
>> True

###################################################################

# iter()                   Returns an iterator object
x = iter(["apple", "banana", "cherry"])
print(next(x))
print(next(x))
print(next(x))
>> "apple"
>> "banana"
>> "cherry"

###################################################################

# map()                    Returns the specified iterator with the specified function applied to each item
def myfunc(n):
  return len(n)
x = map(myfunc, ('apple', 'banana', 'cherry'))
print(x)
>> <map object at 0x1481154c4130>

#################################

def square(number):
    return number ** 2


numbers = [1, 2, 3, 4, 5]
squared = map(square, numbers)

list(squared)
>> [1, 4, 9, 16, 25]

#################################

str_nums = ["4", "8", "6", "5", "3", "2", "8", "9", "2", "5"]

int_nums = map(int, str_nums)
print(int_nums)
>> <map object at 0x7fb2c7e34c70>

print(list(int_nums))
>> [4, 8, 6, 5, 3, 2, 8, 9, 2, 5]

print(str_nums)
>> ["4", "8", "6", "5", "3", "2", "8", "9", "2", "5"]

#################################

first_it = [1, 2, 3]
second_it = [4, 5, 6, 7]

print(list(map(pow, first_it, second_it)))
>> [1, 32, 729]

#################################

string_it = ["processing", "strings", "with", "map"]
list(map(str.capitalize, string_it))
>> ['Processing', 'Strings', 'With', 'Map']

list(map(str.upper, string_it))
>> ['PROCESSING', 'STRINGS', 'WITH', 'MAP']

list(map(str.lower, string_it))
>> ['processing', 'strings', 'with', 'map']

#################################

import math

numbers = [1, 2, 3, 4, 5, 6, 7]

print(list(map(math.factorial, numbers)))
>> [1, 2, 6, 24, 120, 720, 5040]

###################################################################

# max()                    Returns the largest item in an iterable
x = max(5, 10)
print(x)
>> 10

###################################################################

# memoryview()             Returns a memory view object
x = memoryview(b"Hello")

print(x)
>> <memory at 0x1495289cfa00>

#return the Unicode of the first character
print(x[0])
>> 72

#return the Unicode of the second character
print(x[1])
>> 101

###################################################################

# min()                    Returns the smallest item in an iterable
x = min(5, 10)
print(x)
>> 5

###################################################################

# next()                   Returns the next item in an iterable
mylist = iter(["apple", "banana", "cherry"])
x = next(mylist)
print(x)
>> "apple"
x = next(mylist)
print(x)
>> "banana"
x = next(mylist)
print(x)
>> "cherry"

###################################################################

# object()                 Returns a new object
x = object()
print(x)
>> <object object at 0x15447e7c4d70>

###################################################################

# oct()                    Converts a number into an octal
x = oct(12)
print(x)
>> 0o14

###################################################################

# ord()                    Convert an integer representing the Unicode of the specified character
x = ord("h")
print(x)
>> 104

###################################################################

# range()                  Returns a sequence of numbers, starting from 0 and increments by 1 (by default)
x = range(6)
for n in x:
  print(n)
>> 0
   1
   2
   3
   4
   5


x = range(3, 20, 2)
for n in x:
  print(n)
>> 3
   5
   7
   9
   11
   13
   15
   17
   19

###################################################################

# reversed()               Returns a reversed iterator
alph = ["a", "b", "c", "d"]
ralph = reversed(alph)
for x in ralph:
  print(x)
>> 'd'
   'c'
   'b'
   'a'

###################################################################

# round()                  Rounds a numbers
x = round(5.76543, 2)
print(x)
>> 5.77

###################################################################

# slice()                  Returns a slice object
a = ("a", "b", "c", "d", "e", "f", "g", "h")
x = slice(2)
print(a[x])
>> ('a', 'b')

###################################################################

# sorted()                 Returns a sorted list
a = ("b", "g", "a", "d", "f", "c", "h", "e")
x = sorted(a)
print(x)
>> ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

###################################################################

# str()                    Returns a string object
x = str(3.5)
print(x)
>> "3.5"

###################################################################

# sum()                    Sums the items of an iterator
a = (1, 2, 3, 4, 5)
x = sum(a)
>> 15

###################################################################

# type()                   Returns the type of an object
a = ('apple', 'banana', 'cherry')
b = "Hello World"
c = 33

x = type(a)
y = type(b)
z = type(c)

print(x,y,z)
>> <class 'tuple'> 
>> <class 'str'> 
>> <class 'int'>

***************************************************************************************************************************************************************************

1) Python Error

ArithmeticError               # Raised when an error occurs in numeric calculations
AssertionError                # Raised when an assert statement fails
AttributeError                # Raised when attribute reference or assignment fails
Exception                     # Base class for all exceptions
EOFError                      # Raised when the input() method hits an "end of file" condition (EOF)
FloatingPointError            # Raised when a floating point calculation fails
GeneratorExit                 # Raised when a generator is closed (with the close() method)
ImportError                   # Raised when an imported module does not exist
IndentationError              # Raised when indentation is not correct
IndexError                    # Raised when an index of a sequence does not exist
KeyError                      # Raised when a key does not exist in a dictionary
KeyboardInterrupt             # Raised when the user presses Ctrl+c, Ctrl+z or Delete
LookupError                   # Raised when errors raised cant be found
MemoryError                   # Raised when a program runs out of memory
NameError                     # Raised when a variable does not exist
NotImplementedError           # Raised when an abstract method requires an inherited class to override the method
OSError                       # Raised when a system related operation causes an error
OverflowError                 # Raised when the result of a numeric calculation is too large
ReferenceError                # Raised when a weak reference object does not exist
RuntimeError                  # Raised when an error occurs that do not belong to any specific exceptions
StopIteration                 # Raised when the next() method of an iterator has no further values
SyntaxError                   # Raised when a syntax error occurs
TabError                      # Raised when indentation consists of tabs or spaces
SystemError                   # Raised when a system error occurs
SystemExit                    # Raised when the sys.exit() function is called
TypeError                     # Raised when two different types are combined
UnboundLocalError             # Raised when a local variable is referenced before assignment
UnicodeError                  # Raised when a unicode problem occurs
UnicodeEncodeError            # Raised when a unicode encoding problem occurs
UnicodeDecodeError            # Raised when a unicode decoding problem occurs
UnicodeTranslateError         # Raised when a unicode translation problem occurs
ValueError                    # Raised when there is a wrong value in a specified data type
ZeroDivisionError             # Raised when the second operator in a division is zero

***************************************************************************************************************************************************************************

1) Random(import random)


# randrange()       Returns a random number between the given range
import random
print(random.randrange(3, 9))
>> 4


# randint()         Returns a random number between the given range
import random
print(random.randint(3, 9))
>> 9


# choice()          Returns a random element from the given sequence
import random
mylist = ["apple", "banana", "cherry"]
print(random.choice(mylist))
>> "cherry"


# shuffle()         Takes a sequence and returns the sequence in a random order
import random
mylist = ["apple", "banana", "cherry"]
random.shuffle(mylist)
print(mylist)
>> ['cherry', 'apple', 'banana']


# sample()          Returns a given sample of a sequence
import random
mylist = ["apple", "banana", "cherry"]
print(random.sample(mylist, k=2))
>> ['cherry', 'banana']


# uniform()         Returns a random float number between two given parameters
import random
print(random.uniform(20, 60))
>> 47.016106134431425

***************************************************************************************************************************************************************************

1) Enum


# for first this is a normal calss with normal ability :

class Season(Enum):
    SPRING = 1
    SUMMER = 2
    AUTUMN = 3
    WINTER = 4
print(Season.SPRING)
print(Season.SPRING.name)
print(Season.SPRING.value)
print(type(Season.SPRING))
print(repr(Season.SPRING))
print(list(Season))
>> Season.SPRING
>> SPRING
>> 1
>> <enum 'Season'>
>> <Season.SPRING: 1>
>> [<Season.SPRING: 1>, <Season.SUMMER: 2>, <Season.AUTUMN: 3>, <Season.WINTER: 4>]

# or :

class Season(Enum):
    SPRING = 1
    SUMMER = 2
    AUTUMN = 3
    WINTER = 4
print("The enum member associated with value 2 is : ", Season(2).name)
print("The enum member associated with name AUTUMN is : ", Season['AUTUMN'].value)
>> "The enum member associated with value 2 is :  SUMMER"
>> "The enum member associated with name AUTUMN is :  3"

# now we use enum :

import enum
class Animal(enum.Enum):
    dog = 1
    cat = 2
    lion = 3
di = {}
di[Animal.dog] = 'bark'
di[Animal.lion] = 'roar'
if di == {Animal.dog: 'bark', Animal.lion: 'roar'}:
    print("Enum is hashed")
else:
    print("Enum is not hashed")
>> "Enum is hashed"

###########################################
 
import enum
class Animal(enum.Enum):
    dog = 1
    cat = 2
    lion = 3
if Animal.dog is Animal.cat:
    print("Dog and cat are same animals")
else:
    print("Dog and cat are different animals")
if Animal.lion != Animal.cat:
    print("Lions and cat are different")
else:
    print("Lions and cat are same")
>> "Dog and cat are different animals"
>> "Lions and cat are different"

**************************************************************************************************************************************************************************

1) System(import sys)


import sys
print(sys.version)
>> 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)]

import sys 
age = 17
if age < 18: 
    sys.exit("Age less than 18")     
else: 
    print("Age is not less than 18") 

***************************************************************************************************************************************************************************

1) OS(import os)

# os has many built-in , and we don't need all of them , so visit this site for all built-in OS :
# https://www.w3schools.com/python/module_os.asp

***************************************************************************************************************************************************************************

1) Path(import path)


# python path :
from pathlib import Path
print(Path.cwd())
>> "C:\Users\NAJAFI\AppData\Local\Programs\Python\Python311"



# user path :
from pathlib import Path
print(Path.home())
>> "C:\Users\NAJAFI"



# special path :
from pathlib import Path
print(Path("C:\\Users\\NAJAFI\\Desktop\\Pic"))
>> WindowsPath('C:\\Users\\NAJAFI\\Desktop\\Pic')



# Picking Out Components of a Path
from pathlib import Path
path = Path("C:\\Users\\gahjelle\\realpython\\test.md")
print(path)
>> WindowsPath('C:/Users/gahjelle/realpython/test.md')

print(path.name)
>> 'test.md'

print(path.stem)
>> 'test'

print(path.suffix)
>> '.md'

print(path.anchor)
>> 'C:\\'

print(path.parent)
>> WindowsPath('C:/Users/gahjelle/realpython")

print(path.parent.parent)
>> WindowsPath('C:/Users/gahjelle')



# Reading and Writing Files
from pathlib import Path
path = Path("C:\\Users\\NAJAFI\\Desktop\\Pic.txt")
with path.open(mode="r", encoding="utf-8") as md_file:
    content = md_file.read()
    print(content)
>> "hello"

#  .read_text()       opens the path in text mode and returns the contents as a string.
#  .read_bytes()      opens the path in binary mode and returns the contents as a byte string.
#  .write_text()      opens the path and writes string data to it.
#  .write_bytes()     opens the path in binary mode and writes data to it.



# Renaming Files
from pathlib import Path
txt_path = Path("/home/gahjelle/realpython/hello.txt")
Print(txt_path)
>> PosixPath("/home/gahjelle/realpython/hello.txt")

md_path = txt_path.with_suffix(".md")
>> PosixPath('/home/gahjelle/realpython/hello.md')
txt_path.replace(md_path)



# Copying Files
from pathlib import Path
source = Path("shopping_list.md")
destination = source.with_stem("shopping_list_02")
destination.write_bytes(source.read_bytes()) # .read_bytes() to read the content of source and then write this content to destination using .write_bytes().



# Moving Files
from pathlib import Path
source = Path("hello.py")
destination = Path("goodbye.py")
if not destination.exists():
    source.replace(destination)



# Create Files
from pathlib import Path
filename = Path("C:\\Users\\NAJAFI\\Desktop\\h.txt")
filename.exists()
>> False
filename.touch()
filename.exists()
>> True

***************************************************************************************************************************************************************************

1) Pickle(import pickle)

import pickle
Omkar = {'key' : 'Omkar', 'name' : 'Omkar Pathak', 
'age' : 21, 'pay' : 40000}

Jagdish = {'key' : 'Jagdish', 'name' : 'Jagdish Pathak',
'age' : 50, 'pay' : 50000}
 
db = {}
db['Omkar'] = Omkar
db['Jagdish'] = Jagdish

b = pickle.dumps(db)   

myEntry = pickle.loads(b)
print(myEntry)
>> {'Omkar': {'key': 'Omkar', 'name': 'Omkar Pathak', 'age': 21, 'pay': 40000}, 'Jagdish': {'key': 'Jagdish', 'name': 'Jagdish Pathak', 'age': 50, 'pay': 50000}}

***************************************************************************************************************************************************************************

1) Collections(import collections)


from collections import Counter  
# With sequence of items   
print(Counter(['B','B','A','B','C','A','B', 
               'B','A','C'])) 
>> Counter({'B': 5, 'A': 3, 'C': 2})

# with dictionary  
print(Counter({'A':3, 'B':5, 'C':2})) 
>> Counter({'B': 5, 'A': 3, 'C': 2})

# with keyword arguments  
print(Counter(A=3, B=5, C=2))
>> Counter({'B': 5, 'A': 3, 'C': 2})

####################################################

from collections import OrderedDict  
    
print("This is a Dict:\n")  
d = {}  
d['a'] = 1
d['b'] = 2
d['c'] = 3
d['d'] = 4

>> "This is a Dict:"
    
for key, value in d.items():  
    print(key, value)  

>> a 1
   b 2
   c 3
   d 4
    
print("\nThis is an Ordered Dict:\n")  
>> "This is an Ordered Dict:"
od = OrderedDict()  
od['a'] = 1
od['b'] = 2
od['c'] = 3
od['d'] = 4
    
for key, value in od.items():  
    print(key, value)

>> a 1
   b 2
   c 3
   d 4

##################

from collections import OrderedDict  

od = OrderedDict()  
od['a'] = 1
od['b'] = 2
od['c'] = 3
od['d'] = 4
    
print('Before Deleting') 
for key, value in od.items():  
    print(key, value)  

>> "Before Deleting"
>> a 1
   b 2
   c 3
   d 4
      
# deleting element 
od.pop('a') 
  
# Re-inserting the same 
od['a'] = 1
  
print('\nAfter re-inserting') 
for key, value in od.items():  
    print(key, value)

>> "After re-inserting"
>>  b 2
    c 3
    d 4
    a 1

####################################################

from collections import defaultdict  
     
# Defining the dict  
d = defaultdict(int)  
     
L = [1, 2, 3, 4, 2, 4, 1, 2]  
     
# Iterate through the list  
# for keeping the count  
for i in L:  
    # The default value is 0  
    # so there is no need to   
    # enter the key first  
    d[i] += 1
         
print(d)
>> defaultdict(<class 'int'>, {1: 2, 2: 3, 3: 1, 4: 2})

##################

from collections import defaultdict  
    
# Defining a dict  
d = defaultdict(list)  
    
for i in range(5):  
    d[i].append(i)  
        
print("Dictionary with values as list:")  
print(d)
>> "Dictionary with values as list:"
>> defaultdict(<class ‘list’>, {0: [0], 1: [1], 2: [2], 3: [3], 4: [4]})

####################################################

from collections import ChainMap  

d1 = {'a': 1, 'b': 2} 
d2 = {'c': 3, 'd': 4} 
d3 = {'e': 5, 'f': 6} 
  
# Defining the chainmap  
c = ChainMap(d1, d2, d3)    
print(c)
>> ChainMap({'a': 1, 'b': 2}, {'c': 3, 'd': 4}, {'e': 5, 'f': 6})

##################

from collections import ChainMap  

d1 = {'a': 1, 'b': 2} 
d2 = {'c': 3, 'd': 4} 
d3 = {'e': 5, 'f': 6} 
  
# Defining the chainmap  
c = ChainMap(d1, d2, d3)  
     
# Accessing Values using key name 
print(c['a']) 
>> 1

# Accessing values using values() 
# method 
print(c.values()) 
>> ValuesView(ChainMap({'a': 1, 'b': 2}, {'c': 3, 'd': 4}, {'e': 5, 'f': 6})) 

# Accessing keys using keys() 
# method 
print(c.keys())
>> KeysView(ChainMap({'a': 1, 'b': 2}, {'c': 3, 'd': 4}, {'e': 5, 'f': 6}))

####################################################
    
import collections  
    
# initializing dictionaries  
dic1 = { 'a' : 1, 'b' : 2 }  
dic2 = { 'b' : 3, 'c' : 4 }  
dic3 = { 'f' : 5 }  
    
# initializing ChainMap  
chain = collections.ChainMap(dic1, dic2)  
    
# printing chainMap  
print ("All the ChainMap contents are : ")  
print (chain)  
>> "All the ChainMap contents are : "
>> ChainMap({'a': 1, 'b': 2}, {'b': 3, 'c': 4})
    
# using new_child() to add new dictionary  
chain1 = chain.new_child(dic3)  
    
# printing chainMap 
print ("Displaying new ChainMap : ")  
print (chain1)
>> "Displaying new ChainMap :" 
   ChainMap({'f': 5}, {'a': 1, 'b': 2}, {'b': 3, 'c': 4})

####################################################

from collections import namedtuple 
    
# Declaring namedtuple()  
Student = namedtuple('Student',['name','age','DOB'])  
    
# Adding values  
S = Student('Nandini','19','2541997')
    
# Access using index  
print ("The Student age using index is : ",end ="")  
print (S[1])  
>> "The Student age using index is :" 19
    
# Access using name   
print ("The Student name using keyname is : ",end ="")  
print (S.name)
>> "The Student name using keyname is :" "Nandini"

##################

from collections import namedtuple 
    
# Declaring namedtuple()  
Student = namedtuple('Student',['name','age','DOB'])  
    
# Adding values  
S = Student('Nandini','19','2541997')  
    
# initializing iterable   
li = ['Manjeet', '19', '411997' ]  
    
# initializing dict  
di = { 'name' : "Nikhil", 'age' : 19 , 'DOB' : '1391997' }  
    
# using _make() to return namedtuple()  
print ("The namedtuple instance using iterable is  : ")  
print (Student._make(li))  
>> "The namedtuple instance using iterable is  : "
   Student(name='Manjeet', age='19', DOB='411997')
    
# using _asdict() to return an OrderedDict()  
print ("The OrderedDict instance using namedtuple is  : ")  
print (S._asdict())
>> "The OrderedDict instance using namedtuple is  : "
   OrderedDict([('name', 'Nandini'), ('age', '19'), ('DOB', '2541997')])

####################################################

from collections import deque 
    
# Declaring deque 
queue = deque(['name','age','DOB'])  
    
print(queue)
>> deque(['name', 'age', 'DOB'])

##################

from collections import deque  
    
# initializing deque  
de = deque([1,2,3])  
    
# using append() to insert element at right end   
# inserts 4 at the end of deque  
de.append(4)  
    
# printing modified deque  
print ("The deque after appending at right is : ")  
print (de)  
>> "The deque after appending at right is :" 
   deque([1, 2, 3, 4])
    
# using appendleft() to insert element at left end   
# inserts 6 at the beginning of deque  
de.appendleft(6)  
    
# printing modified deque  
print ("The deque after appending at left is : ")  
print (de)
>> "The deque after appending at left is :" 
   deque([6, 1, 2, 3, 4])

##################

from collections import deque 
  
# initializing deque  
de = deque([6, 1, 2, 3, 4]) 
  
# using pop() to delete element from right end   
# deletes 4 from the right end of deque  
de.pop()  
    
# printing modified deque  
print ("The deque after deleting from right is : ")  
print (de)  
>> "The deque after deleting from right is : "
   deque([6, 1, 2, 3])
    
# using popleft() to delete element from left end   
# deletes 6 from the left end of deque  
de.popleft()  
    
# printing modified deque  
print ("The deque after deleting from left is : ")  
print (de)
>> "The deque after deleting from left is : "
   deque([1, 2, 3])

***************************************************************************************************************************************************************************

1) Operator(import operator)


# add(a, b) : This function returns addition of the given arguments.                                                                                        a + b

# sub(a, b) : This function returns difference of the given arguments.                                                                                      a - b

# mul(a, b) : This function returns product of the given arguments.                                                                                         a * b

# truediv(a,b) : This function returns division of the given arguments.                                                                                     a / b

# floordiv(a,b) : This function also returns division of the given arguments. But the value is floored value i.e. returns greatest small integer.           a // b

# pow(a,b) : This function returns exponentiation of the given arguments.                                                                                   a ** b

# mod(a,b) : This function returns modulus of the given arguments.                                                                                          a % b

# lt(a, b) : This function is used to check if a is less than b or not. Returns true if a is less than b, else returns false.                               a < b

# le(a, b) : This function is used to check if a is less than or equal to b or not. Returns true if a is less than or equal to b, else returns false.       a <= b

# eq(a, b) : This function is used to check if a is equal to b or not. Returns true if a is equal to b, else returns false.                                 a == b

# gt(a,b) : This function is used to check if a is greater than b or not. Returns true if a is greater than b, else returns false.                          a > b

# ge(a,b) : This function is used to check if a is greater than or equal to b or not. Returns true if a is greater than or equal to b, else returns false.  a >= b

# ne(a,b) : This function is used to check if a is not equal to b or is equal. Returns true if a is not equal to b, else returns false.                     a != b

####################################################

import operator 
# Initializing variables 
a = 4
b = 3
  
# using add() to add two numbers 
print ("The addition of numbers is :",end=""); 
print (operator.add(a, b)) 
>> "The addition of numbers is:" 7
  
# using sub() to subtract two numbers 
print ("The difference of numbers is :",end=""); 
print (operator.sub(a, b)) 
>> "The difference of numbers is :" 1
  
# using mul() to multiply two numbers 
print ("The product of numbers is :",end=""); 
print (operator.mul(a, b)) 
>> "The product of numbers is:" 12

####################################################

import operator 
# Initializing variables 
a = 5
b = 2
  
# using truediv() to divide two numbers 
print ("The true division of numbers is : ",end=""); 
print (operator.truediv(a,b)) 
>> "The true division of numbers is:" 2.5
  
# using floordiv() to divide two numbers 
print ("The floor division of numbers is : ",end=""); 
print (operator.floordiv(a,b)) 
>> "The floor division of numbers is:" 2
  
# using pow() to exponentiate two numbers 
print ("The exponentiation of numbers is : ",end=""); 
print (operator.pow(a,b)) 
>> "The exponentiation of numbers is:" 25
  
# using mod() to take modulus of two numbers 
print ("The modulus of numbers is : ",end=""); 
print (operator.mod(a,b)) 
>> "The modulus of numbers is:" 1

####################################################

import operator 
  
# Initializing variables 
a = 3
b = 3
  
# using lt() to check if a is less than b 
if(operator.lt(a,b)): 
       print ("3 is less than 3") 
else : print ("3 is not less than 3") 
>> "3 is not less than 3"
  
# using le() to check if a is less than or equal to b 
if(operator.le(a,b)): 
       print ("3 is less than or equal to 3") 
else : print ("3 is not less than or equal to 3") 
>> "3 is less than or equal to 3"
  
# using eq() to check if a is equal to b 
if (operator.eq(a,b)): 
       print ("3 is equal to 3") 
else : print ("3 is not equal to 3") 
>> "3 is equal to 3"

####################################################

import operator 
  
# Initializing variables 
a = 4
b = 3
  
# using gt() to check if a is greater than b 
if (operator.gt(a,b)): 
       print ("4 is greater than 3") 
else : print ("4 is not greater than 3")
>> "4 is greater than 3"
  
# using ge() to check if a is greater than or equal to b 
if (operator.ge(a,b)): 
       print ("4 is greater than or equal to 3") 
else : print ("4 is not greater than or equal to 3") 
>> "4 is greater than or equal to 3"
  
# using ne() to check if a is not equal to b 
if (operator.ne(a,b)): 
       print ("4 is not equal to 3") 
else : print ("4 is equal to 3") 
>> "4 is not equal to 3"

***************************************************************************************************************************************************************************

1) Progress Bar


# $ pip3 install tqdm
from tqdm import tqdm
from time import sleep

total = 0
for num in tqdm([1, 2, 3, 4]):
    sleep(0.25)
    total = total + num
    
>> Processing: 100%|████████████████████| 4/4 [00:01<00:00,  3.95s/it]

***************************************************************************************************************************************************************************

1) Matplotlib(chart)

"""
import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([0, 6])
ypoints = np.array([0, 250])

plt.plot(xpoints, ypoints)
plt.show()
"""

# The plot() function is used to draw points (markers) in a diagram.
# By default, the plot() function draws a line from point to point.
# The function takes parameters for specifying points in the diagram.
# Parameter 1 is an array containing the points on the x-axis.
# Parameter 2 is an array containing the points on the y-axis.
# If we need to plot a line from (1, 3) to (8, 10), we have to pass two arrays [1, 8] and [3, 10] to the plot function.

"""
import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1, 8])
ypoints = np.array([3, 10])

plt.plot(xpoints, ypoints, 'o')
plt.show()
"""

####################################################
"""
import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1, 2, 6, 8])
ypoints = np.array([3, 8, 1, 10])

plt.plot(xpoints, ypoints)
plt.show()
"""
####################################################
"""
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10, 5, 7])

plt.plot(ypoints)
plt.show()

# The x-points are [0, 1, 2, 3, 4, 5].
"""
####################################################
"""
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker = 'o')
plt.show()
"""
####################################################

# You can choose any of these markers:

# 'o'	Circle	
# '*'	Star	
# '.'	Point	
# ','	Pixel	
# 'x'	X	
# 'X'	X (filled)	
# '+'	Plus	
# 'P'	Plus (filled)	
# 's'	Square	
# 'D'	Diamond	
# 'd'	Diamond (thin)	
# 'p'	Pentagon	
# 'H'	Hexagon	
# 'h'	Hexagon	
# 'v'	Triangle Down	
# '^'	Triangle Up	
# '<'	Triangle Left	
# '>'	Triangle Right	
# '1'	Tri Down	
# '2'	Tri Up	
# '3'	Tri Left	
# '4'	Tri Right	
# '|'	Vline	
# '_'	Hline

####################################################
"""
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, 'o:r')
plt.show()
"""
####################################################

# Line Reference :

# '-'	Solid line	
# ':'	Dotted line	
# '--'	Dashed line	
# '-.'	Dashed/dotted line


# Color Reference :

# 'r'	Red	
# 'g'	Green	
# 'b'	Blue	
# 'c'	Cyan	
# 'm'	Magenta	
# 'y'	Yellow	
# 'k'	Black	
# 'w'	White

####################################################
"""
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker = 'o', ms = 20) # Marker Size
plt.show()
"""
####################################################
"""
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker = 'o', ms = 20, mec = 'r') # Marker Color
plt.show()
"""
####################################################
"""
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker = 'o', ms = 20, mfc = 'r') # Marker Color
plt.show()
"""
####################################################
"""
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker = 'o', ms = 20, mec = 'r', mfc = 'r') # Marker Color
plt.show()
"""
####################################################
"""
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, linestyle = 'dotted')
plt.show()
"""
####################################################

# Line Styles : 

# 'solid'      (default)	'-'	
# 'dotted'	                ':'	
# 'dashed'	                '--'	
# 'dashdot'	                '-.'	
# 'None'	                ''   or   ' '

####################################################
"""
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, color = 'r')
plt.show()
"""
####################################################
"""
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, linewidth = '20.5')
plt.show()
"""
####################################################
"""
import matplotlib.pyplot as plt
import numpy as np

y1 = np.array([3, 8, 1, 10])
y2 = np.array([6, 2, 7, 11])

plt.plot(y1)
plt.plot(y2)

plt.show()
"""
####################################################
"""
import matplotlib.pyplot as plt
import numpy as np

x1 = np.array([0, 1, 2, 3])
y1 = np.array([3, 8, 1, 10])
x2 = np.array([0, 1, 2, 3])
y2 = np.array([6, 2, 7, 11])

plt.plot(x1, y1, x2, y2)
plt.show()
"""
####################################################
"""
import numpy as np
import matplotlib.pyplot as plt

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.plot(x, y)

plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

plt.show()
"""
####################################################
"""
import numpy as np
import matplotlib.pyplot as plt

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.plot(x, y)

plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

plt.show()
"""
####################################################
"""
import numpy as np
import matplotlib.pyplot as plt

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

plt.plot(x, y)

plt.grid()

plt.show()
"""
####################################################
"""
import numpy as np
import matplotlib.pyplot as plt

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

plt.plot(x, y)

plt.grid(axis = 'x')

plt.show()
"""
####################################################
"""
import numpy as np
import matplotlib.pyplot as plt

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

plt.plot(x, y)

plt.grid(axis = 'y')

plt.show()
"""
####################################################
"""
import numpy as np
import matplotlib.pyplot as plt

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

plt.plot(x, y)

plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)

plt.show()
"""
####################################################
"""
import matplotlib.pyplot as plt
import numpy as np

#plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(1, 2, 1)
plt.plot(x,y)

#plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(1, 2, 2)
plt.plot(x,y)

plt.show()
"""
####################################################
"""
import matplotlib.pyplot as plt
import numpy as np

#plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 1, 1)
plt.plot(x,y)

#plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 1, 2)
plt.plot(x,y)

plt.show()
"""
####################################################
"""
import matplotlib.pyplot as plt
import numpy as np

x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 3, 1)
plt.plot(x,y)

x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 3, 2)
plt.plot(x,y)

x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 3, 3)
plt.plot(x,y)

x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 3, 4)
plt.plot(x,y)

x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 3, 5)
plt.plot(x,y)

x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 3, 6)
plt.plot(x,y)

plt.show()
"""
####################################################
"""
import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])

plt.scatter(x, y)
plt.show()
"""
####################################################
"""
import matplotlib.pyplot as plt
import numpy as np

#day one, the age and speed of 13 cars:
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
plt.scatter(x, y)

#day two, the age and speed of 15 cars:
x = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
y = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])
plt.scatter(x, y)

plt.show()
"""
####################################################
"""
import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
colors = np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100])

plt.scatter(x, y, c=colors, cmap='viridis')

plt.colorbar()

plt.show()
"""
####################################################
"""
import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
sizes = np.array([20,50,100,200,500,1000,60,90,10,300,600,800,75])

plt.scatter(x, y, s=sizes)

plt.show()
"""
####################################################
"""
import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x,y)
plt.show()
"""
####################################################
"""
import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.barh(x, y)
plt.show()
"""
####################################################
"""
import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x, y, color = "red")
plt.show()
"""
####################################################
"""
import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x, y, width = 0.1)
plt.show()
"""
####################################################
"""
import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])

plt.pie(y)
plt.show() 
"""
####################################################
"""
import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

plt.pie(y, labels = mylabels)
plt.show() 
"""
####################################################
"""
import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
myexplode = [0.2, 0, 0, 0]

plt.pie(y, labels = mylabels, explode = myexplode)
plt.show()
"""
####################################################
"""
import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

plt.pie(y, labels = mylabels)
plt.legend()
plt.show() 
"""

***************************************************************************************************************************************************************************

1) Table (import tabulate)


# $ pip3 install tabulate

import tabulate

table = [["Sun",696000,1989100000],["Earth",6371,5973.6],["Moon",1737,73.5],["Mars",3390,641.85]]
print(tabulate(table))

>> -----  ------  -------------
   Sun    696000   1.9891e+09
   Earth    6371   5973.6
   Moon     1737   73.5
   Mars     3390   641.85
   -----  ------  -------------

####################################################

print(tabulate(table, headers=["Planet","R (km)", "mass (x 10^29 kg)"]))

>> Planet      R (km)    mass (x 10^29 kg)
   --------  --------  -------------------
   Sun         696000           1.9891e+09
   Earth         6371        5973.6
   Moon          1737          73.5
   Mars          3390         641.85

####################################################

print(tabulate([["Name","Age"],["Alice",24],["Bob",19]],headers="firstrow"))  # If headers="firstrow", then the first row of data is used:

>> Name      Age
   ------  -----
   Alice      24
   Bob        19

####################################################

print(tabulate({"Name": ["Alice", "Bob"],"Age": [24, 19]}, headers="keys")) # If headers="keys", then the keys of a dictionary/dataframe, or column indices are used

>>   Age  Name
   -----  ------
      24  Alice
      19  Bob

####################################################

"""
By default, only pandas.DataFrame tables have an additional column called row index. 
To add a similar column to any other type of table, pass showindex="always" or showindex=True argument to tabulate(). 
To suppress row indices for all types of data, pass showindex="never" or showindex=False. 
To add a custom row index column, pass showindex=rowIDs, where rowIDs is some iterable:
"""
print(tabulate([["F",24],["M",19]], showindex="always"))
>> -  -  --
   0  F  24
   1  M  19
   -  -  --

####################################################

# There is more than one way to format a table in plain text. The third optional argument named tablefmt defines how the table is formatted.Supported table formats are:

"plain"
"simple"
"github"
"grid"
"simple_grid"
"rounded_grid"
"heavy_grid"
"mixed_grid"
"double_grid"
"fancy_grid"
"outline"
"simple_outline"
"rounded_outline"
"heavy_outline"
"mixed_outline"
"double_outline"
"fancy_outline"
"pipe"
"orgtbl"
"asciidoc"
"jira"
"presto"
"pretty"
"psql"
"rst"
"mediawiki"
"moinmoin"
"youtrack"
"html"
"unsafehtml"
"latex"
"latex_raw"
"latex_booktabs"
"latex_longtable"
"textile"
"tsv"

####################################################

# plain tables do not use any pseudo-graphics to draw lines:

table = [["spam",42],["eggs",451],["bacon",0]]
headers = ["item", "qty"]
print(tabulate(table, headers, tablefmt="plain"))

>> item      qty
   spam       42
   eggs      451
   bacon       0

####################################################

# simple is the default format (the default may change in future versions). It corresponds to simple_tables in Pandoc Markdown extensions:

print(tabulate(table, headers, tablefmt="simple"))

>> item      qty
   ------  -----
   spam       42
   eggs      451
   bacon       0

####################################################

# github follows the conventions of GitHub flavored Markdown. It corresponds to the pipe format without alignment colons:

print(tabulate(table, headers, tablefmt="github"))

>> | item   | qty   |
   |--------|-------|
   | spam   | 42    |
   | eggs   | 451   |
   | bacon  | 0     |

####################################################

# grid is like tables formatted by Emacs' table.el package. It corresponds to grid_tables in Pandoc Markdown extensions:

print(tabulate(table, headers, tablefmt="grid"))

>> +--------+-------+
   | item   |   qty |
   +========+=======+
   | spam   |    42 |
   +--------+-------+
   | eggs   |   451 |
   +--------+-------+
   | bacon  |     0 |
   +--------+-------+

####################################################

# simple_grid draws a grid using single-line box-drawing characters:

print(tabulate(table, headers, tablefmt="simple_grid"))

>> ┌────────┬───────┐
   │ item   │   qty │
   ├────────┼───────┤
   │ spam   │    42 │
   ├────────┼───────┤
   │ eggs   │   451 │
   ├────────┼───────┤
   │ bacon  │     0 │
   └────────┴───────┘

####################################################

# rounded_grid draws a grid using single-line box-drawing characters with rounded corners:

print(tabulate(table, headers, tablefmt="rounded_grid"))

>> ╭────────┬───────╮
   │ item   │   qty │
   ├────────┼───────┤
   │ spam   │    42 │
   ├────────┼───────┤
   │ eggs   │   451 │
   ├────────┼───────┤
   │ bacon  │     0 │
   ╰────────┴───────╯

####################################################

# heavy_grid draws a grid using bold (thick) single-line box-drawing characters:

print(tabulate(table, headers, tablefmt="heavy_grid"))

>> ┏━━━━━━━━┳━━━━━━━┓
   ┃ item   ┃   qty ┃
   ┣━━━━━━━━╋━━━━━━━┫
   ┃ spam   ┃    42 ┃
   ┣━━━━━━━━╋━━━━━━━┫
   ┃ eggs   ┃   451 ┃
   ┣━━━━━━━━╋━━━━━━━┫
   ┃ bacon  ┃     0 ┃
   ┗━━━━━━━━┻━━━━━━━┛

####################################################

# mixed_grid draws a grid using a mix of light (thin) and heavy (thick) lines box-drawing characters:

print(tabulate(table, headers, tablefmt="mixed_grid"))

>> ┍━━━━━━━━┯━━━━━━━┑
   │ item   │   qty │
   ┝━━━━━━━━┿━━━━━━━┥
   │ spam   │    42 │
   ├────────┼───────┤
   │ eggs   │   451 │
   ├────────┼───────┤
   │ bacon  │     0 │
   ┕━━━━━━━━┷━━━━━━━┙

####################################################

# double_grid draws a grid using double-line box-drawing characters:

print(tabulate(table, headers, tablefmt="double_grid"))

>> ╔════════╦═══════╗
   ║ item   ║   qty ║
   ╠════════╬═══════╣
   ║ spam   ║    42 ║
   ╠════════╬═══════╣
   ║ eggs   ║   451 ║
   ╠════════╬═══════╣
   ║ bacon  ║     0 ║
   ╚════════╩═══════╝

####################################################

# fancy_grid draws a grid using a mix of single and double-line box-drawing characters:

print(tabulate(table, headers, tablefmt="fancy_grid"))

>> ╒════════╤═══════╕
   │ item   │   qty │
   ╞════════╪═══════╡
   │ spam   │    42 │
   ├────────┼───────┤
   │ eggs   │   451 │
   ├────────┼───────┤
   │ bacon  │     0 │
   ╘════════╧═══════╛

####################################################

# outline is the same as the grid format but doesn't draw lines between rows:

print(tabulate(table, headers, tablefmt="outline"))

>> +--------+-------+
   | item   |   qty |
   +========+=======+
   | spam   |    42 |
   | eggs   |   451 |
   | bacon  |     0 |
   +--------+-------+

####################################################

# simple_outline is the same as the simple_grid format but doesn't draw lines between rows:

print(tabulate(table, headers, tablefmt="simple_outline"))

>> ┌────────┬───────┐
   │ item   │   qty │
   ├────────┼───────┤
   │ spam   │    42 │
   │ eggs   │   451 │
   │ bacon  │     0 │
   └────────┴───────┘

####################################################

# rounded_outline is the same as the rounded_grid format but doesn't draw lines between rows:

print(tabulate(table, headers, tablefmt="rounded_outline"))

>> ╭────────┬───────╮
   │ item   │   qty │
   ├────────┼───────┤
   │ spam   │    42 │
   │ eggs   │   451 │
   │ bacon  │     0 │
   ╰────────┴───────╯

####################################################

# heavy_outline is the same as the heavy_grid format but doesn't draw lines between rows:

print(tabulate(table, headers, tablefmt="heavy_outline"))

>> ┏━━━━━━━━┳━━━━━━━┓
   ┃ item   ┃   qty ┃
   ┣━━━━━━━━╋━━━━━━━┫
   ┃ spam   ┃    42 ┃
   ┃ eggs   ┃   451 ┃
   ┃ bacon  ┃     0 ┃
   ┗━━━━━━━━┻━━━━━━━┛

####################################################

# mixed_outline is the same as the mixed_grid format but doesn't draw lines between rows:

print(tabulate(table, headers, tablefmt="mixed_outline"))

>> ┍━━━━━━━━┯━━━━━━━┑
   │ item   │   qty │
   ┝━━━━━━━━┿━━━━━━━┥
   │ spam   │    42 │
   │ eggs   │   451 │
   │ bacon  │     0 │
   ┕━━━━━━━━┷━━━━━━━┙

####################################################

# double_outline is the same as the double_grid format but doesn't draw lines between rows:

print(tabulate(table, headers, tablefmt="double_outline"))

>> ╔════════╦═══════╗
   ║ item   ║   qty ║
   ╠════════╬═══════╣
   ║ spam   ║    42 ║
   ║ eggs   ║   451 ║
   ║ bacon  ║     0 ║
   ╚════════╩═══════╝

####################################################

# fancy_outline is the same as the fancy_grid format but doesn't draw lines between rows:

print(tabulate(table, headers, tablefmt="fancy_outline"))

>> ╒════════╤═══════╕
   │ item   │   qty │
   ╞════════╪═══════╡
   │ spam   │    42 │
   │ eggs   │   451 │
   │ bacon  │     0 │
   ╘════════╧═══════╛

####################################################

# presto is like tables formatted by Presto cli:

print(tabulate(table, headers, tablefmt="presto"))

>> item   |   qty
  --------+-------
   spam   |    42
   eggs   |   451
   bacon  |     0

####################################################

# pretty attempts to be close to the format emitted by the PrettyTables library:

print(tabulate(table, headers, tablefmt="pretty"))

>> +-------+-----+
   | item  | qty |
   +-------+-----+
   | spam  | 42  |
   | eggs  | 451 |
   | bacon |  0  |
   +-------+-----+

####################################################

# psql is like tables formatted by Postgres' psql cli:

print(tabulate(table, headers, tablefmt="psql"))

>> +--------+-------+
   | item   |   qty |
   |--------+-------|
   | spam   |    42 |
   | eggs   |   451 |
   | bacon  |     0 |
   +--------+-------+

####################################################

# pipe follows the conventions of PHP Markdown Extra extension. It corresponds to pipe_tables in Pandoc. This format uses colons to indicate column alignment:

print(tabulate(table, headers, tablefmt="pipe"))

>> | item   |   qty |
   |:-------|------:|
   | spam   |    42 |
   | eggs   |   451 |
   | bacon  |     0 |

####################################################

# asciidoc formats data like a simple table of the AsciiDoctor format:

print(tabulate(table, headers, tablefmt="asciidoc"))

>> [cols="8<,7>",options="header"]
   |====
   | item   |   qty
   | spam   |    42
   | eggs   |   451
   | bacon  |     0
   |====

####################################################

# orgtbl follows the conventions of Emacs org-mode, and is editable also in the minor orgtbl-mode. Hence its name:

print(tabulate(table, headers, tablefmt="orgtbl"))

>> | item   |   qty |
   |--------+-------|
   | spam   |    42 |
   | eggs   |   451 |
   | bacon  |     0 |

####################################################

# jira follows the conventions of Atlassian Jira markup language:

print(tabulate(table, headers, tablefmt="jira"))

>> || item   ||   qty ||
   | spam   |    42 |
   | eggs   |   451 |
   | bacon  |     0 |

####################################################

# rst formats data like a simple table of the reStructuredText format:

print(tabulate(table, headers, tablefmt="rst"))

>> ======  =====
   item      qty
   ======  =====
   spam       42
   eggs      451
   bacon       0
   ======  =====

####################################################

# mediawiki format produces a table markup used in Wikipedia and on other MediaWiki-based sites:

print(tabulate(table, headers, tablefmt="mediawiki"))

>> {| class="wikitable" style="text-align: left;"
   |+ <!-- caption -->
   |-
   ! item   !! align="right"|   qty
   |-
   | spam   || align="right"|    42
   |-
   | eggs   || align="right"|   451
   |-
   | bacon  || align="right"|     0
   |}

####################################################

# moinmoin format produces a table markup used in MoinMoin wikis:

print(tabulate(table, headers, tablefmt="moinmoin"))

>> || ''' item   ''' || ''' quantity   ''' ||
   ||  spam    ||  41.999      ||
   ||  eggs    ||  451         ||
   ||  bacon   ||              ||

####################################################

# youtrack format produces a table markup used in Youtrack tickets:

print(tabulate(table, headers, tablefmt="youtrack"))

>> ||  item    ||  quantity   ||
   |   spam    |  41.999      |
   |   eggs    |  451         |
   |   bacon   |              |

####################################################

# textile format produces a table markup used in Textile format:

print(tabulate(table, headers, tablefmt="textile"))

>> |_.  item   |_.   qty |
   |<. spam    |>.    42 |
   |<. eggs    |>.   451 |
   |<. bacon   |>.     0 |

####################################################

# html produces standard HTML markup as an html.escape'd str with a .repr_html method so that Jupyter Lab and Notebook display the HTML and a .str property so that the raw HTML remains accessible. unsafehtml table format can be used if an unescaped HTML is required:

print(tabulate(table, headers, tablefmt="html"))

>> <table>
   <tbody>
   <tr><th>item  </th><th style="text-align: right;">  qty</th></tr>
   <tr><td>spam  </td><td style="text-align: right;">   42</td></tr>
   <tr><td>eggs  </td><td style="text-align: right;">  451</td></tr>
   <tr><td>bacon </td><td style="text-align: right;">    0</td></tr>
   </tbody>
   </table>

####################################################

# latex format creates a tabular environment for LaTeX markup, replacing special characters like _ or \ to their LaTeX correspondents:

print(tabulate(table, headers, tablefmt="latex"))

>> \begin{tabular}{lr}
   \hline
    item   &   qty \\
   \hline
    spam   &    42 \\
    eggs   &   451 \\
    bacon  &     0 \\
   \hline
   \end{tabular}

**************************************************************************************************************************************************************************

40) OOP(Class)


""" Object-oriented programming (OOP) is a method of structuring a program by bundling related properties and behaviors into individual objects. 
In this tutorial, you'll learn the basics of object-oriented programming in Pytho"""

####################################################

## How Define a Class in Python ?


class Dog:
    pass

##########################

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

""" You define the properties that all Dog objects must have in a method called .__init__(). 
Every time you create a new Dog object, .__init__() sets the initial state of the object by assigning the values of the object's properties. 
That is, .__init__() initializes each new instance of the class.
You can give .__init__() any number of parameters, but the first parameter will always be a variable called self. 
When you create a new class instance, then Python automatically passes the instance to the self parameter in .__init__() so that Python can define the new attributes on the object."""

####################################################

## How Instantiate a Class in Python ?


class Dog:
     pass

Dog()
>> <__main__.Dog object at 0x106702d30>
Dog()
>> <__main__.Dog object at 0x0004ccc90>

a = Dog()
b = Dog()
a == b
>> False



""" The new Dog instance is located at a different memory address. 
That's because it's an entirely new instance and is completely unique from the first Dog object that you created."""

##########################

class Dog:
     species = "Canis familiaris"
     def __init__(self, name, age):
         self.name = name
         self.age = age

miles = Dog("Miles", 4)
buddy = Dog("Buddy", 9)


miles.name
>> 'Miles'
miles.age
>> 4

buddy.name
>> 'Buddy'
buddy.age
>> 9

buddy.age = 10
buddy.age
>> 10

miles.species = "Felis silvestris"
miles.species
>> 'Felis silvestris'

##########################

class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old"

    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"
    

miles = Dog("Miles", 4)
miles.description()
>> 'Miles is 4 years old'

miles.speak("Woof Woof")
>> 'Miles says Woof Woof'

miles.speak("Bow Wow")
>> 'Miles says Bow Wow'

##########################

class Dog:
    # ...

    def __str__(self):  # In the editor window, change the name of the Dog class’s .description() method to .__str__()
        return f"{self.name} is {self.age} years old"   
    
miles = Dog("Miles", 4)
print(miles)
>> 'Miles is 4 years old'

##########################

class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"
    

buddy.speak("Yap")
>> 'Buddy says Yap'

jim.speak("Woof")
>> 'Jim says Woof'

jack.speak("Woof")
>> 'Jack says Woof'

####################################################

## How Inherit From Another Class in Python ?


""" Inheritance is the process by which one class takes on the attributes and methods of another. 
Newly formed classes are called child classes, and the classes that you derive child classes from are called parent classes."""

class Parent:
    hair_color = "brown"

class Child(Parent):
    pass

##########################

class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"
    
class JackRussellTerrier(Dog):
    pass

class Dachshund(Dog):
    pass

class Bulldog(Dog):
    pass

miles = JackRussellTerrier("Miles", 4)
buddy = Dachshund("Buddy", 9)
jack = Bulldog("Jack", 3)
jim = Bulldog("Jim", 5)


miles.species
>> 'Canis familiaris'

buddy.name
>> 'Buddy'

print(jack)
>> "Jack is 3 years old"

jim.speak("Woof")
>> 'Jim says Woof'

####################################################

## Class Attributes


 class ObjectCounter:
     num_instances = 0
     def __init__(self):
         ObjectCounter.num_instances += 1


ObjectCounter()
>> <__main__.ObjectCounter object at 0x10392d810>
ObjectCounter()
>> <__main__.ObjectCounter object at 0x1039810d0>
ObjectCounter()
>> <__main__.ObjectCounter object at 0x10395b750>
ObjectCounter()
>> <__main__.ObjectCounter object at 0x103959810>

ObjectCounter.num_instances
>> 4

counter = ObjectCounter()
counter.num_instances
>> 5



"""It's important to note that you can access class attributes using either the class or one of its instances. 
That's why you can use the counter object to retrieve the value of .num_instances. 
However, if you need to modify a class attribute, then you must use the class itself rather than one of its instances.
For example, if you use self to modify .num_instances, then you'll be overriding the original class attribute by creating a new instance attribute:"""



 class ObjectCounter:
     num_instances = 0
     def __init__(self):
         self.num_instances += 1


ObjectCounter()
>> <__main__.ObjectCounter object at 0x103987550>
ObjectCounter()
>> <__main__.ObjectCounter object at 0x1039c5890>
ObjectCounter()
>> <__main__.ObjectCounter object at 0x10396a890>
ObjectCounter()
>> <__main__.ObjectCounter object at 0x1036fa110>

ObjectCounter.num_instances
>> 0

####################################################

## Instance Attributes :


class Car:
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.started = False
        self.speed = 0
        self.max_speed = 200


toyota_camry = Car("Toyota", "Camry", 2022, "Red")
toyota_camry.make
>> 'Toyota'
toyota_camry.model
>> 'Camry'
toyota_camry.color
>> 'Red'
toyota_camry.speed
>> 0

ford_mustang = Car("Ford", "Mustang", 2022, "Black")
ford_mustang.make
>> 'Ford'
ford_mustang.model
>> 'Mustang'
ford_mustang.year
>> 2022
ford_mustang.max_speed
>> 200

####################################################

## The .__dict__ Attribute


class SampleClass:
    class_attr = 100

    def __init__(self, instance_attr):
        self.instance_attr = instance_attr

    def method(self):
        print(f"Class attribute: {self.class_attr}")
        print(f"Instance attribute: {self.instance_attr}")



SampleClass.class_attr
>> 100

SampleClass.__dict__
>> mappingproxy({
     '__module__': '__main__',
     'class_attr': 100,
     '__init__': <function SampleClass.__init__ at 0x1036c62a0>,
     'method': <function SampleClass.method at 0x1036c56c0>,
     '__dict__': <attribute '__dict__' of 'SampleClass' objects>,
     '__weakref__': <attribute '__weakref__' of 'SampleClass' objects>,
     '__doc__': None
})

SampleClass.__dict__["class_attr"]
>> 100

instance = SampleClass("Hello!")
instance.instance_attr
>> 'Hello!'

instance.method()
>> Class attribute: 100
>> Instance attribute: Hello!

instance.__dict__
>> {'instance_attr': 'Hello!'}

instance.__dict__["instance_attr"]
>> 'Hello!'

instance.__dict__["instance_attr"] = "Hello, Pythonista!"
instance.instance_attr
>> 'Hello, Pythonista!'

####################################################

## Dynamic Class and Instance Attributes


class Record:
    """Hold a record of data."""

john = {
     "name": "John Doe",
     "position": "Python Developer",
     "department": "Engineering",
     "salary": 80000,
     "hire_date": "2020-01-01",
     "is_manager": False,
}

john_record = Record()
for field, value in john.items():
     setattr(john_record, field, value)


john_record.name
>> 'John Doe'

john_record.department
>> 'Engineering'

john_record.__dict__
>> {
     'name': 'John Doe',
     'position': 'Python Developer',
     'department': 'Engineering',
     'salary': 80000,
     'hire_date': '2020-01-01',
     'is_manager': False
   }

##########################

class User:
     pass


# Add instance attributes dynamically
jane = User()
jane.name = "Jane Doe"
jane.job = "Data Engineer"
jane.__dict__
>> {'name': 'Jane Doe', 'job': 'Data Engineer'}


# Add methods dynamically
def __init__(self, name, job):
     self.name = name
     self.job = job


User.__init__ = __init__
User.__dict__
>> mappingproxy({
     ...
     '__init__': <function __init__ at 0x1036ccae0>
   })


linda = User("Linda Smith", "Team Lead")
linda.__dict__
>> {'name': 'Linda Smith', 'job': 'Team Lead'}

####################################################

## Instance Methods With self


class Car:
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.started = False
        self.speed = 0
        self.max_speed = 200

    def start(self):
        print("Starting the car...")
        self.started = True

    def stop(self):
        print("Stopping the car...")
        self.started = False

    def accelerate(self, value):
        if not self.started:
            print("Car is not started!")
            return
        if self.speed + value <= self.max_speed:
            self.speed += value
        else:
            self.speed = self.max_speed
        print(f"Accelerating to {self.speed} km/h...")

    def brake(self, value):
        if self.speed - value >= 0:
            self.speed -= value
        else:
            self.speed = 0
        print(f"Braking to {self.speed} km/h...")   


ford_mustang = Car("Ford", "Mustang", 2022, "Black")
ford_mustang.start()
>> "Starting the car..."
ford_mustang.accelerate(100)
>> "Accelerating to 100 km/h..."
ford_mustang.brake(50)
>> "assertBraking to 50 km/h...""
ford_mustang.brake(80)
>> "Braking to 0 km/h...""
ford_mustang.stop()
>> "Stopping the car...""
ford_mustang.accelerate(100)
>> "Car is not started!"

####################################################

## Special Methods and Protocols :


class Car:
    def __str__(self):
        return f"{self.make}, {self.model}, {self.color}: ({self.year})"

    def __repr__(self):
        return (
            f"{type(self).__name__}"
            f'(make="{self.make}", '
            f'model="{self.model}", '
            f"year={self.year}, "
            f'color="{self.color}")'
        )


toyota_camry = Car("Toyota", "Camry", 2022, "Red")

str(toyota_camry)
>> 'Toyota, Camry, Red: (2022)'
print(toyota_camry)
>> Toyota, Camry, Red: (2022)

toyota_camry
>> Car(make="Toyota", model="Camry", year=2022, color="Red")
repr(toyota_camry)
>> 'Car(make="Toyota", model="Camry", year=2022, color="Red")'

***************************************************************************************************************************************************************************

41) CSV :


########################################################################################################

reading :



"""
CSV file :

Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age,Outcome
1,89,66,23,94,28.1,0.167,21,0
0,137,40,35,168,43.1,2.288,33,1
3,78,50,32,88,31,0.248,26,1
2,197,70,45,543,30.5,0.158,53,1
"""

import csv
with open("diabetes.csv", "r") as file:
 reader = csv.reader(file)
 for hh in reader :
  print(hh)

>> ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age', 'Outcome']
   ['1', '89', '66', '23', '94', '28.1', '0.167', '21', '0']  
   ['0', '137', '40', '35', '168', '43.1', '2.288', '33', '1']
   ['3', '78', '50', '32', '88', '31', '0.248', '26', '1']    
   ['2', '197', '70', '45', '543', '30.5', '0.158', '53', '1']

####################################################

"""
CSV file :

Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age,Outcome
1,89,66,23,94,28.1,0.167,21,0
0,137,40,35,168,43.1,2.288,33,1
3,78,50,32,88,31,0.248,26,1
2,197,70,45,543,30.5,0.158,53,1
"""

import csv
with open("diabetes.csv", "r") as file:
 reader = csv.reader(file)
 for row in reader:
  print(row[0])

>> ['Pregnancies']
   ['1']
   ['0']
   ['3']    
   ['2']

####################################################

"""
CSV file :

Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age,Outcome
1,89,66,23,94,28.1,0.167,21,0
0,137,40,35,168,43.1,2.288,33,1
3,78,50,32,88,31,0.248,26,1
2,197,70,45,543,30.5,0.158,53,1
"""

import csv
with open("diabetes.csv", "r") as file:
 reader = csv.reader(file)
 next(reader) # next column
 for row in reader:
  print(row[0])

>>  ['1']
    ['0']
    ['3']    
    ['2']

####################################################

"""
CSV file :

Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age,Outcome
1,89,66,23,94,28.1,0.167,21,0
0,137,40,35,168,43.1,2.288,33,1
3,78,50,32,88,31,0.248,26,1
2,197,70,45,543,30.5,0.158,53,1
"""

import csv
titles = []
with open("diabetes.csv", "r") as file:
 reader = csv.DictReader(file)
 for row in reader:
       titles.append(row)
 print(titles)

>> [{'Pregnancies': '1', 'Glucose': '89', 'BloodPressure': '66', 'SkinThickness': '23', 'Insulin': '94', 'BMI': '28.1', 'DiabetesPedigreeFunction': '0.167', 'Age': '21', 'Outcome': '0'}, 
    {'Pregnancies': '0', 'Glucose': '137', 'BloodPressure': '40', 'SkinThickness': '35', 'Insulin': '168', 'BMI': '43.1', 'DiabetesPedigreeFunction': '2.288', 'Age': '33', 'Outcome': '1'}, 
    {'Pregnancies': '3', 'Glucose': '78', 'BloodPressure': '50', 'SkinThickness': '32', 'Insulin': '88', 'BMI': '31', 'DiabetesPedigreeFunction': '0.248', 'Age': '26', 'Outcome': '1'}, 
    {'Pregnancies': '2', 'Glucose': '197', 'BloodPressure': '70', 'SkinThickness': '45', 'Insulin': '543', 'BMI': '30.5', 'DiabetesPedigreeFunction': '0.158', 'Age': '53', 'Outcome': '1'}]

####################################################

"""
CSV file :

Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age,Outcome
1,89,66,23,94,28.1,0.167,21,0
0,137,40,35,168,43.1,2.288,33,1
3,78,50,32,88,31,0.248,26,1
2,197,70,45,543,30.5,0.158,53,1
"""

import csv
# Open the CSV file for reading
with open('diabetes.csv', mode='r') as file:
    # Create a CSV reader with DictReader
    csv_reader = csv.DictReader(file)
 
    # Initialize an empty list to store the dictionaries
    data_list = []
 
    # Iterate through each row in the CSV file
    for row in csv_reader:
        # Append each row (as a dictionary) to the list
        data_list.append(row)
 
# Print the list of dictionaries
for data in data_list:
    print(data)

>> {'Pregnancies': '1', 'Glucose': '89', 'BloodPressure': '66', 'SkinThickness': '23', 'Insulin': '94', 'BMI': '28.1', 'DiabetesPedigreeFunction': '0.167', 'Age': '21', 'Outcome': '0'}
   {'Pregnancies': '0', 'Glucose': '137', 'BloodPressure': '40', 'SkinThickness': '35', 'Insulin': '168', 'BMI': '43.1', 'DiabetesPedigreeFunction': '2.288', 'Age': '33', 'Outcome': '1'}
   {'Pregnancies': '3', 'Glucose': '78', 'BloodPressure': '50', 'SkinThickness': '32', 'Insulin': '88', 'BMI': '31', 'DiabetesPedigreeFunction': '0.248', 'Age': '26', 'Outcome': '1'}
   {'Pregnancies': '2', 'Glucose': '197', 'BloodPressure': '70', 'SkinThickness': '45', 'Insulin': '543', 'BMI': '30.5', 'DiabetesPedigreeFunction': '0.158', 'Age': '53', 'Outcome': '1'}

########################################################################################################

Writing :



import csv
with open('gg.csv', mode='w') as gg:
    gg = csv.writer(gg)
    gg.writerow(['John Smith', 'Accounting', 'November'])
    gg.writerow(['Erica Meyers', 'IT', 'March'])


"""
CSV file :

John Smith,Accounting,November
Erica Meyers,IT,March
"""
####################################################

import csv
# field names
fields = ['Name', 'Branch', 'Year', 'CGPA']
# data rows of csv file
rows = [['Nikhil', 'COE', '2', '9.0'],
        ['Sanchit', 'COE', '2', '9.1'],
        ['Aditya', 'IT', '2', '9.3'],
        ['Sagar', 'SE', '1', '9.5'],
        ['Prateek', 'MCE', '3', '7.8'],
        ['Sahil', 'EP', '2', '9.1']]
# name of csv file
filename = "university_records.csv"
# writing to csv file
with open(filename, 'w') as ff:
    # creating a csv writer object
    ff = csv.writer(ff)
    # writing the fields
    ff.writerow(fields)
    # writing the data rows
    ff.writerows(rows)


"""
CSV file :

Name,Branch,Year,CGPA
Nikhil,COE,2,9.0
Sanchit,COE,2,9.1
Aditya,IT,2,9.3
Sagar,SE,1,9.5
Prateek,MCE,3,7.8
Sahil,EP,2,9.1
"""
####################################################

import csv
 
# my data rows as dictionary objects
mydict = [{'branch': 'COE', 'cgpa': '9.0',
           'name': 'Nikhil', 'year': '2'},
          {'branch': 'COE', 'cgpa': '9.1',
           'name': 'Sanchit', 'year': '2'},
          {'branch': 'IT', 'cgpa': '9.3',
           'name': 'Aditya', 'year': '2'},
          {'branch': 'SE', 'cgpa': '9.5',
           'name': 'Sagar', 'year': '1'},
          {'branch': 'MCE', 'cgpa': '7.8',
           'name': 'Prateek', 'year': '3'},
          {'branch': 'EP', 'cgpa': '9.1',
           'name': 'Sahil', 'year': '2'}]
 
# field names
fields = ['name', 'branch', 'year', 'cgpa']
 
# name of csv file
filename = "university_records.csv"
 
# writing to csv file
with open(filename, 'w') as csvfile:
    # creating a csv dict writer object
    writer = csv.DictWriter(csvfile, fieldnames=fields)
 
    # writing headers (field names)
    writer.writeheader()
 
    # writing data rows
    writer.writerows(mydict)


"""
CSV file :

name,branch,year,cgpa
Nikhil,COE,2,9.0
Sanchit,COE,2,9.1
Aditya,IT,2,9.3
Sagar,SE,1,9.5
Prateek,MCE,3,7.8
Sahil,EP,2,9.1
"""
***************************************************************************************************************************************************************************

42) txt :

"""
Read Only ("r")
Read and Write ("r+")
Write Only ("w")
Write and Read ("w+")
Append Only ("a")
Append and Read ("a+")

"""

########################################################################################################

reading :



"""
txt file :

in the name of god
hellllllloooo
"""

file1 = open("a.txt","r")
print(file1.read())

>> "in the name of god"
   "hellllllloooo"

####################################################

"""
txt file :

in the name of god
hellllllloooo
"""

file1 = open("a.txt","r")
print(file1.readline())

>> "in the name of god"

########################################################################################################

Writing :



file1 = open("a.txt", "w")
L = ["This is Delhi \n", "This is Paris \n", "This is London \n"]
 
file1.write("Hello \n")
file1.writelines(L)
file1.close()  # to change file access modes


"""
txt file :

Hello 
This is Delhi 
This is Paris 
This is London 
"""
***************************************************************************************************************************************************************************
