0) Home
1) Variables
1) Data Types
1) Numbers
1) Strings
1) Booleans
1) Operators

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
