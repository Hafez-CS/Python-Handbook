0) Home
1) Variables
1) Data Types
1) Numbers
1) Strings
1) Booleans
1) Operators
1) Lists
1) Tuples
1) Sets
1) Dictionaries
1) if ... else
1) while Loops
1) for Loops
1) Functions
1) lambda
1) class And Objects
1) iterators(iter)
1) Scope
1) make my library
1) Datetime(import datetime)
1) Math
1) JSON
1) RegEx(import re)
1) Try...Except
1) Input
1) String Formatting
1) File Handling
1) Built In Functions
1) Python Error
1) Random(import random)
1) Enum
1) System(import sys)
1) OS(import OS)
1) Path(import path)
1) Pickle(import pickle)
1) Collections(import collections)
1) Operator(import operator)
1) Progress Bar


***************************************************************************************************************************************************************************

# https://www.w3schools.com/python/default.asp                     for read more

# https://www.geeksforgeeks.org/python-programming-language/       for read more

***************************************************************************************************************************************************************************

0) Home

print("Hello, World!")
>> "Hello, World!"


# hello world

***************************************************************************************************************************************************************************

1) Variables


x = 5
y = "John"
print(x)
print(y)
>> 5
>> "John"


x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)
>> "Sally"


x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0


x = 5
y = "John"
print(type(x))
print(type(y))
>> <class 'int'>
>> <class 'str'>


x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
>> "Orange"
>> "Banana"
>> "Cherry"


x = y = z = "Orange"
print(x)
print(y)
print(z)
>> "Orange"
>> "Orange"
>> "Orange"


fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)
>> ["apple", "banana", "cherry"]
>> ["apple", "banana", "cherry"]
>> ["apple", "banana", "cherry"]


x = "Python is awesome"
print(x)
>> "Python is awesome"


x = "Python"
y = "is"
z = "awesome"
print(x, y, z)
>> "Python" , "is" , "awesome"


x = "Python "
y = "is "
z = "awesome"
print(x + y + z)
>> "Python is awesome"


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



a = "Hello, World!"
print(a[1])
>> "e"



b = "Hello, World!"
print(b[2:5])
>> "llo"



a = "Hello, World!"
print(len(a))
>> 13



txt = "The best things in life are free!"
print("free" in txt)
>> True



a = "Hello, World!"
print(a.upper())
>> "HELLO, WORLD!"



a = "Hello, World!"
print(a.lower())
>> "hello, world!"



a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"
>> "Hello, World!"



a = "Hello, World!"
print(a.replace("H", "J"))
>> "Jello, World!"



a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']
>> "['Hello', ' World!']"



a = "Hello"
b = "World"
c = a + b
print(c)
>> "HelloWorld"



a = "Hello"
b = "World"
c = a + " " + b
print(c)
>> "Hello World"



age = 36
txt = "My name is John, I am " + age
print(txt)
>> "My name is John, I am 36"



age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))
>> "My name is John, I am 36"



print('G','F', sep='', end='')
print('G')
>> "GFG"



print('09','12','2016', sep='-', end='\n')
>> "09-12-2016"



print('Red','Green','Blue', sep=',', end='@')
print('geeksforgeeks')
>> "Red,Green,Blue@geeksforgeeks"



print("Geeks : %2d, Portal : %5.2f" % (1, 05.333)) 
>> "Geeks :  1, Portal : 5.33"
 


print("Total students : %3d, Boys : %2d" % (240, 120))   # print integer value
>> "Total students : 240, Boys : 120"
 


print("%7.3o" % (25))   # print octal value
>> "    031"
 


print("%10.3E" % (356.08977))   # print exponential value
>> "3.561E+02"



tab = {'geeks': 4127, 'for': 4098, 'geek': 8637678}
print('Geeks: {0[geeks]:d}; For: {0[for]:d}; '
    'Geeks: {0[geek]:d}'.format(tab))
>> "Geeks: 4127; For: 4098; Geeks: 8637678"

########################################

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




def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")
>> "Emil Refsnes"
>> "Tobias Refsnes"
>> "Linus Refsnes"




def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")
>> "Emil Refsnes"




def my_function(*kids):  #  *  it's for more than one value
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")
>> "The youngest child is Linus"




def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")
>> "The youngest child is Linus"




def my_function(**kid):  # **  it's mean we don't need call number , just call that word
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")
>> "His last name is Refsnes"




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




def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]
my_function(fruits)
>> "apple"
   "banana"
   "cherry"




def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))
>> 15
>> 25
>> 45




def my_function(x, /):
  print(x)

my_function(3)
>> 3




def my_function(*, x):
  print(x)

my_function(x = 3)
>> 3




def my_function(a, b, /, *, c, d):
  print(a + b + c + d)

my_function(5, 6, c = 7, d = 8)
>> 26




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

1) class And Objects


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

1) Scope



def myfunc():
  x = 300
  print(x)
myfunc()
>> 300



def myfunc():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfunc()
>> 300



x = 300
def myfunc():
  print(x)

myfunc()
print(x)
>> 300
>> 300



x = 300
def myfunc():
  x = 200
  print(x)

myfunc()
print(x)
>> 200
>> 300



def myfunc():
  global x
  x = 300

myfunc()
print(x)
>> 300



x = 300
def myfunc():
  global x
  x = 200

myfunc()
print(x)
>> 200

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
