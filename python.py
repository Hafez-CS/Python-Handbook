                                                                       100 part of teach
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
