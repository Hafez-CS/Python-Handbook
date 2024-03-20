Python Handbook
===============================
![Monty Python](https://cdn.dribbble.com/users/330915/screenshots/3587000/10_coding_dribbble.gif)

Introduction
--------
**Welcome to python handbook!
This handbook is a complete collection of Python tips and topics in a "learning by example" approach and I hope it is useful.**

### What is Python?
**Python is a popular programming language. It was created by Guido van Rossum, and released in 1991.**
**It is used for:
web development (server-side),
software development,
mathematics,
system scripting.**

### What can Python do?
**Python can be used on a server to create web applications.
Python can be used alongside software to create workflows.
Python can connect to database systems. It can also read and modify files.
Python can be used to handle big data and perform complex mathematics.
Python can be used for rapid prototyping, or for production-ready software development.**

### Why Python?
**Python works on different platforms (Windows, Mac, Linux, Raspberry Pi, etc).
Python has a simple syntax similar to the English language.
Python has syntax that allows developers to write programs with fewer lines than some other programming languages.
Python runs on an interpreter system, meaning that code can be executed as soon as it is written. This means that prototyping can be very quick.
Python can be treated in a procedural way, an object-oriented way or a functional way.**

### good to know!
**Python : https://www.python.org/**

**The Python Standard Library : https://docs.python.org/3/library/index.html**

**Learn more about python : https://www.w3schools.com/python/default.asp**

**Learn more about python : https://www.geeksforgeeks.org/python-programming-language/**

**VS Code : https://code.visualstudio.com/**



Contents
--------
**&nbsp;&nbsp;&nbsp;** **1. Home :** **&nbsp;**  **[`Home`](#home)** **&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**  **21. JSON :** **&nbsp;**  **[`JSON`](#json)**

**&nbsp;&nbsp;&nbsp;** **2. Variables :** **&nbsp;**  **[`Variables`](#variables)**

**&nbsp;&nbsp;&nbsp;** **3. Data Types :** **&nbsp;**  **[`DataTypes`](#datatypes)**

**&nbsp;&nbsp;&nbsp;** **4. Numbers :** **&nbsp;**  **[`Numbers`](#numbers)**

**&nbsp;&nbsp;&nbsp;** **5. Strings :** **&nbsp;**  **[`Strings`](#strings)**

**&nbsp;&nbsp;&nbsp;** **6. Booleans :** **&nbsp;**  **[`Booleans`](#booleans)**

**&nbsp;&nbsp;&nbsp;** **7. Operators :** **&nbsp;**  **[`Operators`](#operators)**

**&nbsp;&nbsp;&nbsp;** **8. Lists :** **&nbsp;**  **[`Lists`](#lists)**

**&nbsp;&nbsp;&nbsp;** **9. Tuples :** **&nbsp;**  **[`Tuples`](#tuples)**

**&nbsp;&nbsp;&nbsp;** **10. Sets :** **&nbsp;**  **[`Sets`](#sets)**

**&nbsp;&nbsp;&nbsp;** **11. Dictionaries :** **&nbsp;**  **[`Dictionaries`](#dictionaries)**

**&nbsp;&nbsp;&nbsp;** **12. if-else :** **&nbsp;**  **[`if-else`](#if-else)**

**&nbsp;&nbsp;&nbsp;** **13. While Loops :** **&nbsp;**  **[`While-Loops`](#while-loops)**

**&nbsp;&nbsp;&nbsp;** **14. for Loops :** **&nbsp;**  **[`for-Loops`](#for-loops)**

**&nbsp;&nbsp;&nbsp;** **15. Functions :** **&nbsp;**  **[`Functions`](#functions)**

**&nbsp;&nbsp;&nbsp;** **16. lambda :** **&nbsp;**  **[`lambda`](#lambda)**

**&nbsp;&nbsp;&nbsp;** **17. iterators :** **&nbsp;**  **[`iterators`](#iterators)**

**&nbsp;&nbsp;&nbsp;** **18. make-my-library :** **&nbsp;**  **[`make-my-library`](#make-my-library)**

**&nbsp;&nbsp;&nbsp;** **19. Datetime :** **&nbsp;**  **[`Datetime`](#datetime)**

**&nbsp;&nbsp;&nbsp;** **20. Math :** **&nbsp;**  **[`Math`](#math)**




Home
----
```python
print("Hello, World!")
>> "Hello, World!"

# hello world
```


Variables
----
```python
x = 5
y = "John"
print(x)
print(y)
>> 5
>> "John"
```

```python
x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)
>> "Sally"

```

```python
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
```

```python
x = 5
y = "John"
print(type(x))
print(type(y))
>> <class 'int'>
>> <class 'str'>
```

```python
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
>> "Orange"
>> "Banana"
>> "Cherry"
```

```python
x = y = z = "Orange"
print(x)
print(y)
print(z)
>> "Orange"
>> "Orange"
>> "Orange"
```

```python
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)
>> ["apple", "banana", "cherry"]
>> ["apple", "banana", "cherry"]
>> ["apple", "banana", "cherry"]
```

```python
x = "Python is awesome"
print(x)
>> "Python is awesome"
```

```python
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)
>> "Python" , "is" , "awesome"
```

```python
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)
>> "Python is awesome"
```

```python
x = 5
y = 10
print(x + y)
>> 15
```


DataTypes
----------
* **Text Type :	str**
* **Numeric Types :	int, float, complex**
* **Sequence Types :	list, tuple, range**
* **Mapping Type :	dict**
* **Set Types :	set, frozenset**
* **Boolean Type :	bool**
* **Binary Types :	bytes, bytearray, memoryview**
* **None Type :	NoneType**

```python
x = "Hello World"	                              # str	
x = 20	                                          # int	
x = 20.5	                                      # float	
x = 1j	                                          # complex	
x = ["apple", "banana", "cherry"]	              # list	
x = ("apple", "banana", "cherry")	              # tuple	
x = range(6)	                                  # range	
x = {"name" : "John", "age" : 36}  	              # dict	
x = {"apple", "banana", "cherry"}	              # set	
x = frozenset({"apple", "banana", "cherry"})	  # frozenset	
x = True	                                      # bool	
x = b"Hello"	                                  # bytes	
x = bytearray(5)	                              # bytearray	
x = memoryview(bytes(5))	                      # memoryview	
x = None	                                      # NoneType
```

```python
x = str("Hello World")	                        # str	
x = int(20)	                                    # int	
x = float(20.5)	                                # float	
x = complex(1j)	                                # complex	
x = list(("apple", "banana", "cherry"))	        # list	
x = tuple(("apple", "banana", "cherry"))	    # tuple	
x = range(6)	                                # range	
x = dict(name="John", age=36)	                # dict	
x = set(("apple", "banana", "cherry"))	        # set	
x = frozenset(("apple", "banana", "cherry"))	# frozenset	
x = bool(5)	                                    # bool	
x = bytes(5)	                                # bytes	
x = bytearray(5)	                            # bytearray	
x = memoryview(bytes(5))	                    # memoryview
```


Numbers
---
```python
x = 1    # int
y = 2.8  # float
z = 1j   # complex
```

```python
x = 1
y = 35656222554887711
z = -3255522
```

```python
x = 1.10
y = 1.0
z = -35.59
```

```python
x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3
```

```python
x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2
```

```python
x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'
```


Strings
-----
```python
a = "Hello"
print(a)
>> "Hello"
```

```python
a = "Hello, World!"
print(a[1])
>> "e"
```

```python
b = "Hello, World!"
print(b[2:5])
>> "llo"
```

```python
a = "Hello, World!"
print(len(a))
>> 13
```

```python
txt = "The best things in life are free!"
print("free" in txt)
>> True
```

```python
a = "Hello, World!"
print(a.upper())
>> "HELLO, WORLD!"
```

```python
a = "Hello, World!"
print(a.lower())
>> "hello, world!"
```

```python
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"
>> "Hello, World!"
```

```python
a = "Hello, World!"
print(a.replace("H", "J"))
>> "Jello, World!"
```

```python
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']
>> "['Hello', ' World!']"
```

```python
a = "Hello"
b = "World"
c = a + b
print(c)
>> "HelloWorld"
```

```python
a = "Hello"
b = "World"
c = a + " " + b
print(c)
>> "Hello World"
```

```python
age = 36
txt = "My name is John, I am " + age
print(txt)
>> "My name is John, I am 36"
```

```python
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))
>> "My name is John, I am 36"
```

```python
print('G','F', sep='', end='')
print('G')
>> "GFG"
```

```python
print('09','12','2016', sep='-', end='\n')
>> "09-12-2016"
```

```python
print('Red','Green','Blue', sep=',', end='@')
print('geeksforgeeks')
>> "Red,Green,Blue@geeksforgeeks"
```

```python
print("Geeks : %2d, Portal : %5.2f" % (1, 05.333)) 
>> "Geeks :  1, Portal : 5.33"
 ```

```python
print("Total students : %3d, Boys : %2d" % (240, 120))   # print integer value
>> "Total students : 240, Boys : 120"
 ```

```python
print("%7.3o" % (25))   # print octal value
>> "    031"
 ```

```python
print("%10.3E" % (356.08977))   # print exponential value
>> "3.561E+02"
```

```python
tab = {'geeks': 4127, 'for': 4098, 'geek': 8637678}
print('Geeks: {0[geeks]:d}; For: {0[for]:d}; '
    'Geeks: {0[geek]:d}'.format(tab))
>> "Geeks: 4127; For: 4098; Geeks: 8637678"
```

**`"    \'    "` Single Quote**

**`"    \\    "` Backslash**

**`"    \n    "` New Line**

**`"    \r    "` Carriage Return**

**`"    \t    "` Tab**

**`"    \b    "` Backspace**

**`"    \f    "` Form Feed**

**`"    \ooo    "` Octal value**

**`"    \xhh    "` Hex value**

### All string methods :
**.capitalize() (Converts the first character to upper case)**
```python
txt = "hello, and welcome to my world."
x = txt.capitalize()
print (x)
>> "Hello, and welcome to my world."
```

**.casefold() (Converts string into lower case)**
```python
txt = "Hello, And Welcome To My World!"
x = txt.casefold()
print(x)
>> "hello, and welcome to my world!"
```

**.center() (Returns a centered string)**
```python
txt = "banana"
x = txt.center(20)
print(x)
>> "       banana       "
```

**.count() (Returns the number of times a specified value occurs in a string)**
```python
txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple")
print(x)
>> 2
```

**.encode() (Returns an encoded version of the string)**
```python
txt = "My name is Ståle"
x = txt.encode()
print(x)
>> b'My name is St\xc3\xa5le'
```

**.endswith() (Returns true if the string ends with the specified value)**
```python
txt = "Hello, welcome to my world."
x = txt.endswith(".")
print(x)
>> True
```

**.expandtabs() (Sets the tab size of the string)**
```python
txt = "H\te\tl\tl\to"
x =  txt.expandtabs(2)
print(x)
>> "H e l l o"
```

**.find() (Searches the string for a specified value and returns the position of where it was found)**
```python
txt = "Hello, welcome to my world."
x = txt.find("welcome")
print(x)
>> 7
```

**.format() (Formats specified values in a string)**
```python
txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))
>> "For only 49.00 dollars!"
```

**.index() (Searches the string for a specified value and returns the position of where it was found)**
```python
txt = "Hello, welcome to my world."
x = txt.index("welcome")
print(x)
>> 7
```

**.isalnum() (Returns True if all characters in the string are alphanumeric)**
```python
txt = "Company12"
x = txt.isalnum()
print(x)
>> True
```

**.isalpha() (Returns True if all characters in the string are in the alphabet)**
```python
txt = "CompanyX"
x = txt.isalpha()
print(x)
>> True
```

**.isascii() (Returns True if all characters in the string are ascii characters)**
```python
txt = "Company123"
x = txt.isascii()
print(x)
>> True
```

**.isdecimal() (Returns True if all characters in the string are decimals)**
```python
txt = "1234"
x = txt.isdecimal()
print(x)
>> True
```

**.isdigit() (Returns True if all characters in the string are digits)**
```python
txt = "50800"
x = txt.isdigit()
print(x)
>> True
```

**.isidentifier() (Returns True if the string is an identifier)**
```python
txt = "Demo"
x = txt.isidentifier()
print(x)
>> True
```

**.islower() (Returns True if all characters in the string are lower case)**
```python
txt = "hello world!"
x = txt.islower()
print(x)
>> True
```

**.isnumeric() (Returns True if all characters in the string are numeric)**
```python
txt = "565543"
x = txt.isnumeric()
print(x)
>> True
```

**.isprintable() (Returns True if all characters in the string are printable)**
```python
txt = "Hello! Are you #1?"
x = txt.isprintable()
print(x)
>> True
```

**.isspace() (Returns True if all characters in the string are whitespaces)**
```python
txt = "   "
x = txt.isspace()
print(x)
>> True
```

**.istitle() (Returns True if the string follows the rules of a title)**
```python
txt = "Hello, And Welcome To My World!"
x = txt.istitle()
print(x)
>> True
```

**.isupper() (Returns True if all characters in the string are upper case)**
```python
txt = "THIS IS NOW!"
x = txt.isupper()
print(x)
>> True
```

**.join() (Joins the elements of an iterable to the end of the string)**
```python
myTuple = ("John", "Peter", "Vicky")
x = "#".join(myTuple)
print(x)
>> "John#Peter#Vicky"
```

**.ljust() (Returns a left justified version of the string)**
```python
txt = "banana"
x = txt.ljust(20)
print(x, "is my favorite fruit.")
>> "banana               is my favorite fruit."
```

**.lower() (Converts a string into lower case)**
```python
txt = "Hello my FRIENDS"
x = txt.lower()
print(x)
>> "hello my friends"
```

**.lstrip() (Returns a left trim version of the string)**
```python
txt = "     banana     "
x = txt.lstrip()
print("of all fruits", x, "is my favorite")
>> "of all fruits banana      is my favorite"
```

**.maketrans() (Returns a translation table to be used in translations)**
```python
txt = "Hello Sam!"
mytable = str.maketrans("S", "P")
print(txt.translate(mytable))
>> "Hello Pam!"
```

**.partition() (Returns a tuple where the string is parted into three parts)**
```python
txt = "I could eat bananas all day"
x = txt.partition("bananas")
print(x)
>> ('I could eat ', 'bananas', ' all day')
```

**.replace() (Returns a string where a specified value is replaced with a specified value)**
```python
txt = "I like bananas"
x = txt.replace("bananas", "apples")
print(x)
>> "I like apples"
```

**.rfind() (Searches the string for a specified value and returns the last position of where it was found)**
```python
txt = "Mi casa, su casa."
x = txt.rfind("casa")
print(x)
>> 12
```

**.rindex() (Searches the string for a specified value and returns the last position of where it was found)**
```python
txt = "Mi casa, su casa."
x = txt.rindex("casa")
print(x)
>> 12
```

**.rjust() (Returns a right justified version of the string)**
```python
txt = "banana"
x = txt.rjust(20)
print(x, "is my favorite fruit.")
>> "              banana is my favorite fruit."
```

**.rpartition() (Returns a tuple where the string is parted into three parts)**
```python
txt = "I could eat bananas all day, bananas are my favorite fruit"
x = txt.rpartition("bananas")
print(x)
>> ('I could eat bananas all day, ', 'bananas', ' are my favorite fruit')
```

**.rsplit() (Splits the string at the specified separator, and returns a list)**
```python
txt = "apple, banana, cherry"
x = txt.rsplit(", ")
print(x)
>> ['apple', 'banana', 'cherry']
```

**.rstrip() (Returns a right trim version of the string)**
```python
txt = "     banana     "
x = txt.rstrip()
print("of all fruits", x, "is my favorite")
>> "of all fruits      banana is my favorite"
```

**.split() (Splits the string at the specified separator, and returns a list)**
```python
txt = "welcome to the jungle"
x = txt.split()
print(x)
>> ['welcome', 'to', 'the', 'jungle']
```

**.splitlines() (Splits the string at line breaks and returns a list)**
```python
txt = "Thank you for the music\nWelcome to the jungle"
x = txt.splitlines()
print(x)
>> ['Thank you for the music', 'Welcome to the jungle']
```

**.startswith()             (Returns true if the string starts with the specified value)**
```python
txt = "Hello, welcome to my world."
x = txt.startswith("Hello")
print(x)
>> True
```

**.strip() (Returns a trimmed version of the string)**
```python
txt = "     banana     "
x = txt.strip()
print("of all fruits", x, "is my favorite")
>> "of all fruits banana is my favorite"
```

**.swapcase() (Swaps cases, lower case becomes upper case and vice versa)**
```python
txt = "Hello My Name Is PETER"
x = txt.swapcase()
print(x)
>> "hELLO mY nAME iS peter"
```

**.title() (Converts the first character of each word to upper case)**
```python
txt = "Welcome to my world"
x = txt.title()
print(x)
>> "Welcome To My World"
```

**.translate() (Returns a translated string)**
```python
mydict = {83:  80}
txt = "Hello Sam!"
print(txt.translate(mydict))
>> "Hello Pam!"
```

**.upper() (Converts a string into upper case)**
```python
txt = "Hello my friends"
x = txt.upper()
print(x)
>> "HELLO MY FRIENDS"
```

**.zfill() (Fills the string with a specified number of 0 values at the beginning0**
```python
txt = "50"
x = txt.zfill(10)
print(x)
>> 0000000050
```


Booleans
-----
```python
print(10 > 9)
print(10 == 9)
print(10 < 9)
>> True
>> False
>> False
```

```python
print(bool("Hello"))
print(bool(15))
>> True
>> True
```


Operators
---------

**`2 + 2 = 4`**

**`2 - 2 = 0`**

**`2 * 3 = 6`**

**`4 / 2 = 2`**

**`4 % 2 = 0`**

**`2 ** 3 = 8`**

**`8 // 4 = 2`**

**`2 == 2` 2 is equal to 2**

**`2 != 3` 2 is not equal to 3**

**`4 > 2` 4 is greater than 2**

**`2 < 4` 2 smaller than 4**

**`4 >= 4` 4 bigger equals 4**

**`4 <= 4` 4 bigger equals 4**

**`and` Returns True if both statements are true `x < 5 and x < 10`**

**`or` Returns True if one of the statements is true `x < 5 or x < 4`**

**`not` Reverse the result, returns False if the result is true `not(x < 5 and x < 10)`**

**`in` Returns True if a sequence with the specified value is present in the object `x in y`**

**`not in` Returns True if a sequence with the specified value is not present in the object `x not in y`**

**`&` AND	Sets each bit to 1 if both bits are 1 `x & y`**

**`|` OR	Sets each bit to 1 if one of two bits is 1 `x | y`**

**`^` XOR	Sets each bit to 1 if only one of two bits is 1 `x ^ y`**

**`~` NOT	Inverts all the bits `~x`**

**`<<` Zero fill left shift Shift left by pushing zeros in from the right and let the leftmost bits fall off `x << 2`**

**`>>` Signed right shift Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off `x >> 2`**



**`x = 5` Or `x = 5`**

**`x += 3` Or `x = x + 3`**

**`x -= 3` Or `x = x - 3`**

**`x *= 3` Or `x = x * 3`**

**`x /= 3` Or `x = x / 3`**

**`x %= 3` Or `x = x % 3`**

**`x //= 3` Or `x = x // 3`**

**`x **= 3` Or `x = x ** 3`**

**`x &= 3` Or `x = x & 3`**

**`x |= 3` Or `x = x | 3`**

**`x ^= 3` Or `x = x ^ 3`**

**`x >>= 3` Or `x = x >> 3`**

**`x <<= 3` Or `x = x << 3`**


Lists
--------
```python
mylist = ["apple", "banana", "cherry"]
```

```python
thislist = ["apple", "banana", "cherry"]
print(thislist)
>> ['apple', 'banana', 'cherry']
```

```python
thislist = ["apple", "banana", "cherry"]
print(len(thislist))
>> 3
```

```python
thislist = ["apple", "banana", "cherry"]
print(thislist[1])
>> "banana"
```

```python
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
>> ['cherry', 'orange', 'kiwi']
```

```python
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)
>> ['apple', 'blackcurrant', 'watermelon', 'cherry']
```

```python
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)
>> ['apple', 'banana', 'watermelon', 'cherry']
```

```python
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)
>> ['apple', 'banana', 'cherry', 'orange']
```

```python
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
>> ['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']
```

```python
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)
>> ['apple', 'cherry']
```

```python
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)
>> ['apple', 'cherry']
```

```python
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)
>> ['apple', 'banana']
```

```python
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)
>> ['banana', 'cherry']
```

```python
thislist = ["apple", "banana", "cherry"]
del thislist
```

```python
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)
>> []
```

```python
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)
>> ['banana', 'kiwi', 'mango', 'orange', 'pineapple']
```

```python
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)
>> ['pineapple', 'orange', 'mango', 'kiwi', 'banana']
```

```python
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)
>> ['banana', 'cherry', 'Kiwi', 'Orange']
```

```python
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)
>> ['apple', 'banana', 'cherry']
```

```python
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)
>> ['apple', 'banana', 'cherry']
```

```python
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)
>> ['a', 'b', 'c', 1, 2, 3]
```

### All List methods :
**.append() (Adds an element at the end of the list)**
```python
fruits = ['apple', 'banana', 'cherry']
fruits.append("orange")
print(fruits)
>> ['apple', 'banana', 'cherry', 'orange']
```

**.clear() (Removes all the elements from the list)**
```python
fruits = ['apple', 'banana', 'cherry', 'orange']
fruits.clear()
print(fruits)
>> []
```

**.copy() (Returns a copy of the list)**
```python
fruits = ['apple', 'banana', 'cherry', 'orange']
x = fruits.copy()
print(x)
>> ['apple', 'banana', 'cherry', 'orange']
```

**.count() (Returns the number of elements with the specified value)**
```python
fruits = ['apple', 'banana', 'cherry']
x = fruits.count("cherry")
print(x)
>> 1
```

**.extend() (Add the elements of a list (or any iterable), to the end of the current list)**
```python
fruits = ['apple', 'banana', 'cherry']
cars = ['Ford', 'BMW', 'Volvo']
fruits.extend(cars)
print(fruits)
>> ['apple', 'banana', 'cherry', 'Ford', 'BMW', 'Volvo']
```

**.index() (Returns the index of the first element with the specified value)**
```python
fruits = ['apple', 'banana', 'cherry']
x = fruits.index("cherry")
print(x)
>> 2
```

**.insert() (Adds an element at the specified position)**
```python
fruits = ['apple', 'banana', 'cherry']
fruits.insert(1, "orange")
print(fruits)
>> ['apple', 'orange', 'banana', 'cherry']
```

**.pop() (Removes the element at the specified position)**
```python
fruits = ['apple', 'banana', 'cherry']
fruits.pop(1)
print(fruits)
>> ['apple', 'cherry']
```

**.remove() (Removes the item with the specified value)**
```python
fruits = ['apple', 'banana', 'cherry']
fruits.remove("banana")
print(fruits)
>> ['apple', 'cherry']
```

**.reverse() (Reverses the order of the list)**
```python
fruits = ['apple', 'banana', 'cherry']
fruits.reverse()
print(fruits)
>> ['cherry', 'banana', 'apple']
```

**.sort() (Sorts the list)**
```python
cars = ['Ford', 'BMW', 'Volvo']
cars.sort()
print(cars)
>> ['BMW', 'Ford', 'Volvo']
```



Tuples
---------
* **`count()`	Returns the number of times a specified value occurs in a tuple.**
* **`index()`	Searches the tuple for a specified value and returns the position of where it was found.**

```python
mytuple = ("apple", "banana", "cherry")
```

```python
thistuple = ("apple", "banana", "cherry")
print(thistuple)
>> ('apple', 'banana', 'cherry')
```

```python
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))
>> 3
```

```python
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])
>> "banana"
```

```python
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print(thistuple)
>> ('banana', 'cherry')
```

```python
thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple)
>> Error
```

```python
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)
>> ('a', 'b', 'c', 1, 2, 3)
```


Sets
----
```python
myset = {"apple", "banana", "cherry"}
```

```python
thisset = {"apple", "banana", "cherry"}
print(thisset)
>> {'cherry', 'banana', 'apple'}
```

```python
thisset = {"apple", "banana", "cherry"}
print(len(thisset))
>> 3
```

```python
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)
>> {'cherry', 'apple', 'banana', 'orange'}
```

```python
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)
>> {'papaya', 'mango', 'pineapple', 'apple', 'banana', 'cherry'}
```

```python
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)
>> {'cherry', 'apple'}
```

```python
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)
>> {'cherry', 'apple'}
```

```python
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
>> "cherry"
print(thisset)
>> {'apple', 'banana'}
```

```python
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
>> "cherry"
print(thisset)
>> {'apple', 'banana'}
```

```python
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)
>> ()
```

```python
thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset)
>> Error
```

```python
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)
>> {1, 'c', 2, 3, 'a', 'b'}
```

```python
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)
>> {1, 'c', 2, 3, 'a', 'b'}
```

```python
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x)
>> {'apple'}
```

```python
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print(z)
>> {'apple'}
```

### All Sets methods :
**.add() (Adds an element to the set)**
```python
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)
>> {'cherry', 'orange', 'apple', 'banana'}
```

**.clear() (Removes all the elements from the set)**
```python
fruits = {"apple", "banana", "cherry"}
fruits.clear()
print(fruits)
>> set()
```

**.copy() (Returns a copy of the set)**
```python
fruits = {"apple", "banana", "cherry"}
x = fruits.copy()
print(x)
>> {'apple', 'cherry', 'banana'}
```

**.difference() (Returns a set containing the difference between two or more sets)**
```python
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.difference(y)
print(z)
>> {'cherry', 'banana'}
```

**.difference_update() (Removes the items in this set that are also included in another, specified set)**
```python
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.difference_update(y)
print(x)
>> {'cherry', 'banana'}
```

**.discard()(Remove the specified item)**
```python
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)
>> {'apple', 'cherry'}
```

**.intersection() (Returns a set, that is the intersection of two other sets)**
```python
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print(z)
>> {'apple'}
```

**.intersection_update() (Removes the items in this set that are not present in other, specified set(s))**
```python
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y) 
print(x)
>> {'apple'}
```

**.isdisjoint() (Returns whether two sets have a intersection or not)**
```python
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "facebook"}
z = x.isdisjoint(y) 
print(z)
>> True
```

**.issubset() (Returns whether another set contains this set or not)**
```python
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}
z = x.issubset(y)
print(z)
>> True
```

**.issuperset() (Returns whether this set contains another set or not)**
```python
x = {"f", "e", "d", "c", "b", "a"}
y = {"a", "b", "c"}
z = x.issuperset(y) 
print(z)
>> True
```

**.pop() (Removes an element from the set)**
```python
fruits = {"apple", "banana", "cherry"}
fruits.pop() 
print(fruits)
>> {'banana', 'cherry'}
```

**.remove() (Removes the specified element)**
```python
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana") 
print(fruits)
>> {'cherry', 'apple'}
```

**.symmetric_difference() (Returns a set with the symmetric differences of two sets)**
```python
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)
print(z)
>> {'cherry', 'microsoft', 'banana', 'google'}
```

**.symmetric_difference_update() (inserts the symmetric differences from this set and another)**
```python
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print(x)
>> {'google', 'microsoft', 'banana', 'cherry'}
```

**.union() (Return a set containing the union of sets)**
```python
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.union(y)
print(z)
>> {'apple', 'microsoft', 'cherry', 'banana', 'google'}
```

**.update() (Update the set with the union of this set and others)**
```python
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.update(y) 
print(x)
>> {'cherry', 'microsoft', 'banana', 'apple', 'google'}
```

Dictionaries
------
```python
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
```

```python
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
>> {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
```

```python
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])
>> "Ford"
```

```python
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(len(thisdict))
>> 3
```

```python
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
```

```python
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)
>> {'name': 'John', 'age': 36, 'country': 'Norway'}
```

```python
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict.get("model")
>> "Mustang"
x = thisdict["model"]
>> "Mustang"
```

```python
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict.keys())
>> dict_keys(['brand', 'model', 'year'])
```

```python
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
```

```python
thisdict = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
print(thisdict.values())
>> dict_values(['Ford', 'Mustang', 1964])
```

```python
thisdict = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
print(thisdict.items())
>> dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])
```

```python
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018

# Or

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})
```

```python
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
```

```python
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
```

```python
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)
>> {}
```

```python
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
```

```python
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
```

```python
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)
>> {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
```

```python
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
```

### All Dictionaries methods :
**.clear() (Removes all the elements from the dictionary)**
```python
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.clear()
print(car)
>> {}
```

**.copy() (Returns a copy of the dictionary)**
```python
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.copy()
print(x)
>> {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
```

**.fromkeys() (Returns a dictionary with the specified keys and value)**
```python
x = ('key1', 'key2', 'key3')
y = 0
thisdict = dict.fromkeys(x, y)
print(thisdict)
>> {'key1': 0, 'key2': 0, 'key3': 0}
```

**.get() (Returns the value of the specified key)**
```python
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.get("model")
print(x)
>> "Mustang"
```

**.items() (Returns a list containing a tuple for each key value pair)**
```python
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.items()
print(x)
>> dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])
```

**.keys() (Returns a list containing the dictionary's keys)**
```python
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.keys()
print(x)
>> dict_keys(['brand', 'model', 'year'])
```

**.pop() (Removes the element with the specified key)**
```python
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.pop("model")
print(car)
>> {'brand': 'Ford', 'year': 1964}
```

**.popitem() (Removes the last inserted key-value pair)**
```python
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.popitem()
print(car)
>> {'brand': 'Ford', 'model': 'Mustang'}
```

**.setdefault() (Returns the value of the specified key. If the key does not exist: insert the key, with the specified value)**
```python
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.setdefault("model", "Bronco")
print(x)
>> "Mustang"
```

**.update() (Updates the dictionary with the specified key-value pairs)**
```python
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.update({"color": "White"})
print(car)
>> {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'White'}
```

**.values() (Returns a list of all the values in the dictionary)**
```python
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.values()
print(x)
>> dict_values(['Ford', 'Mustang', 1964])
```


if-else
-----
* **Equals : `a == b`**
* **Not Equals : `a != b`**
* **Less than : `a < b`**
* **Less than or equal to : `a <= b`**
* **Greater than : `a > b`**
* **Greater than or equal to : `a >= b`**

```python
a = 33
b = 200
if b > a:
  print("b is greater than a")
>> "b is greater than a"
```

```python
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
>> "a and b are equal"
```

```python
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
>> "a is greater than b"
```

```python
a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")
>> "b is not greater than a"
```

```python
a = 200
b = 100
if a > b: print("a is greater than b")
>> "a is greater than b"
```

```python
a = 2
b = 330
print("A") if a > b else print("B")
>> "B"
```

```python
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")
>> "="
```

```python
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")
>> "Both conditions are True"
```

```python
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")
>> "At least one of the conditions is True"
```

```python
a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")
>> "a is NOT greater than b"
```

```python
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")
>> "Above ten,"
   "and also above 20!"
```


While-Loops
------
```python
i = 1
while i < 6:
  print(i)
  i += 1
>> 1
   2
   3
   4
   5
```

```python
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1
>> 1
   2
   3
```

```python
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
```

```python
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
```


for-Loops
-------
```python
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
>> "apple"
   "banana"
   "cherry"
```

```python
for x in "banana":
  print(x)
>> 'b'
   'a'
   'n'
   'a'
   'n'
   'a'
```

```python
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)
>> "apple"
```

```python
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)
>> "apple"
   "cherry"
```

```python
for x in range(6):
  print(x)
>> 0
   1
   2
   3
   4
   5
```

```python
for x in range(2, 6):
  print(x)
>> 2
   3
   4
   5
```

```python
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
```

```python
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
```

```python
for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")
>> 0
   1
   2
```

```python
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
```

Functions
-------------
```python
def my_function():
  print("Hello from a function")

my_function()
>> "Hello from a function"
```

```python
def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")
>> "Emil Refsnes"
>> "Tobias Refsnes"
>> "Linus Refsnes"
```

```python
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")
>> "Emil Refsnes"
```

```python
def my_function(*kids):  #  *  it's for more than one value
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")
>> "The youngest child is Linus"
```

```python
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")
>> "The youngest child is Linus"
```

```python
def my_function(**kid):  # **  it's mean we don't need call number , just call that word
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")
>> "His last name is Refsnes"
```

```python
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
```

```python
def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]
my_function(fruits)
>> "apple"
   "banana"
   "cherry"
```

```python
def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))
>> 15
>> 25
>> 45
```

```python
def my_function(x, /):
  print(x)

my_function(3)
>> 3
```

```python
def my_function(*, x):
  print(x)

my_function(x = 3)
>> 3
```

```python
def my_function(a, b, /, *, c, d):
  print(a + b + c + d)

my_function(5, 6, c = 7, d = 8)
>> 26
```

```python
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
```


lambda
--------
```python
x = lambda a : a + 10
print(x(5))
>> 15
```

```python
x = lambda a, b : a * b
print(x(5, 6))
>> 30
```

```python
x = lambda a, b, c : a + b + c
print(x(5, 6, 2))
>> 13
```

```python
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
print(mydoubler(11))
>> 22
```

```python
def myfunc(n):
  return lambda a : a * n

mytripler = myfunc(3)
print(mytripler(11))
>> 22
```

```python
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)
print(mydoubler(11))
print(mytripler(11))
>> 22
>> 33
```


iterators
---------
```python
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))
>> "apple"
>> "banana"
>> "cherry"
```

```python
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
```

```python
mytuple = ("apple", "banana", "cherry")
for x in mytuple:
  print(x)
>> "apple"
   "banana"
   "cherry"
```



Scope
--------------
```python
def myfunc():
  x = 300
  print(x)
myfunc()
>> 300
```

```python
def myfunc():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfunc()
>> 300
```

```python
x = 300
def myfunc():
  print(x)

myfunc()
print(x)
>> 300
>> 300
```

```python
x = 300
def myfunc():
  x = 200
  print(x)

myfunc()
print(x)
>> 200
>> 300
```

```python
def myfunc():
  global x
  x = 300

myfunc()
print(x)
>> 300
```

```python
x = 300
def myfunc():
  global x
  x = 200

myfunc()
print(x)
>> 200
```


make-my-library
------
**for first make a python file as app.py**
**and write some func or class :**
```python
def greeting(name):
  print("Hello, " + name)
```
**and open a nother python file as try.py and wrire this :**
```python
import app

app.greeting("Jonathan")
>> "Hello, Jonathan"
```
**now you have your own library**

### example :
**app.py :**
```python
person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}
```
**try.py :**
```python
import app
a = app.person1["age"]
print(a)
>> 36

# or

import app as mx
a = mx.person1["age"]
print(a)
```

Datetime
------
```python
import datetime
x = datetime.datetime.now()
print(x)
>> 2024-02-21 05:37:25.261486
```

```python
import datetime
x = datetime.datetime.now()
print(x.year)
print(x.strftime("%A"))
>> 2024
>> Wednesday
```

```python
import datetime
x = datetime.datetime(2020, 5, 17)
print(x)
>> 2020-05-17 00:00:00
```

```python
import datetime
x = datetime.datetime(2018, 6, 1)
print(x.strftime("%B"))
>> June
```

**`%a`	Weekday, short version	Wed.**

**`%A`	Weekday, full version	Wednesday.**

**`%w`	Weekday as a number 0-6, 0 is Sunday	3.**

**`%d`	Day of month 01-31	31.**

**`%b`	Month name, short version	Dec.**

**`%B`	Month name, full version	December.**

**`%m`	Month as a number 01-12	12.**

**`%y`	Year, short version, without century	18.**

**`%Y`	Year, full version	2018.**

**`%H`	Hour 00-23	17.**

**`%I`	Hour 00-12	05.**

**`%p`	AM/PM	PM.**

**`%M`	Minute 00-59	41.**

**`%S`	Second 00-59	08.**

**`%f`	Microsecond 000000-999999	548513.**

**`%z`	UTC offset	+0100.**

**`%Z`	Timezone	CST.**

**`%j`	Day number of year 001-366	365.**

**`%U`	Week number of year, Sunday as the first day of week, 00-53	52.**

**`%W`	Week number of year, Monday as the first day of week, 00-53	52.**

**`%c`	Local version of date and time	Mon Dec 31 17:41:00 2018.**

**`%C`	Century	20.**

**`%x`	Local version of date	12/31/18.**

**`%X`	Local version of time	17:41:00.**

**`%%`	A % character	%.**

**`%G`	ISO 8601 year	2018.**

**`%u`	ISO 8601 weekday (1-7)	1.**

**`%V`	ISO 8601 weeknumber (01-53)	01.**


Math
------
```python
x = min(5, 10, 25)
y = max(5, 10, 25)
print(x)
print(y)
>> 5
>> 25
```

```python
x = abs(-7.25)
print(x)
>> 7.25
```

```python
x = pow(4, 3)
print(x)
>> 64
```

```python
import math
x = math.sqrt(64)
print(x)
>> 8.0
```

```python
import math
x = math.ceil(1.4)
y = math.floor(1.4)
print(x) # returns 2
print(y) # returns 1
>> 2
>> 1
```

```python
import math
x = math.pi
print(x)
>> 3.141592653589793
```

### All math methods :
**.math.ceil() (Rounds a number up to the nearest integer)**
```python
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
```

**.math.comb() (Returns the number of ways to choose k items from n items without repetition and order)**
```python
import math
n = 7
k = 5
print (math.comb(n, k))
>> 21
```

**.math.copysign() (Returns a float consisting of the value of the first parameter and the sign of the second parameter)**
```python
import math  
print(math.copysign(4, -1))
print(math.copysign(-8, 97.21))
print(math.copysign(-43, -76))
>> -4.0
>> 8.0
>> -43.0
```

**.math.cos() (Returns the cosine of a number)**
```python
import math
print (math.cos(0.00))
print (math.cos(-1.23))
print (math.cos(10))
print (math.cos(3.14159265359))
>> 1.0
>> 0.3342377271245026
>> -0.8390715290764524
>> -1.0
```

**.math.degrees() (Converts an angle from radians to degrees)**
```python
import math
print (math.degrees(8.90))
print (math.degrees(-20))
print (math.degrees(1))
print (math.degrees(90))
>> 509.9324376664327
>> -1145.9155902616465
>> 57.29577951308232
>> 5156.620156177409
```

**.math.dist() (Returns the Euclidean distance between two points (p and q), where p and q are the coordinates of that point)**
```python
import math

p = [3]
q = [1]
print (math.dist(p, q))
>> 2.0

p = [3, 3]
q = [6, 12]
print (math.dist(p, q))
>> 9.486832980505138
```

**.math.fabs() (Returns the absolute value of a number)**
```python
import math
print(math.fabs(-66.43))
print(math.fabs(-7))
>> 66.43
>> 7.0
```

**.math.floor() (Rounds a number down to the nearest integer)**
```python
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
```

**.math.fmod() (Returns the remainder of x/y)**
```python
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
```

**.math.fsum() (Returns the sum of all items in any iterable (tuples, arrays, lists, etc.))**
```python
import math
print(math.fsum([1, 2, 3, 4, 5]))
print(math.fsum([100, 400, 340, 500]))
print(math.fsum([1.7, 0.3, 1.5, 4.5]))
>> 15.0
>> 1340.0
>> 8.0
```

**.math.gcd() (Returns the greatest common divisor of two integers)**
```python
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
```

**.math.isclose() (Checks whether two values are close to each other, or not)**
```python
import math
print(math.isclose(1.233, 1.4566))
print(math.isclose(1.233, 1.233))
print(math.isclose(1.233, 1.24))
print(math.isclose(1.233, 1.233000001))
>> False
>> True
>> False
>> True
```


JSON
------
```python
import json
# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'
# parse x:
y = json.loads(x)
# the result is a Python dictionary:
print(y["age"])
>> 30
```

```python
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
```

```python
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
>> True
>> False
>> Null
```

```python
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
```
