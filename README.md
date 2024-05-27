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

**VS Code : https://code.visualstudio.com/**

**Learn more about python : https://www.w3schools.com/python/default.asp**

**Learn more about python : https://www.geeksforgeeks.org/python-programming-language/**

**Learn more about python : https://realpython.com/**



Contents
--------
**&nbsp;&nbsp;&nbsp;** **1. Home :** **&nbsp;**  **[`Home`](#home)** 

**&nbsp;&nbsp;&nbsp;** **2. Variables :** **&nbsp;**  **[`Variables`](#variables)** 

**&nbsp;&nbsp;&nbsp;** **3. Data Types :** **&nbsp;**  **[`Data-Types`](#data-types)** 

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

**&nbsp;&nbsp;&nbsp;** **18. make my library :** **&nbsp;**  **[`make-my-library`](#make-my-library)**

**&nbsp;&nbsp;&nbsp;** **19. Datetime :** **&nbsp;**  **[`Datetime`](#datetime)**

**&nbsp;&nbsp;&nbsp;** **20. Math :** **&nbsp;**  **[`Math`](#math)**

**&nbsp;&nbsp;&nbsp;**  **21. JSON :** **&nbsp;**  **[`JSON`](#json)**

**&nbsp;&nbsp;&nbsp;**  **22. RegEx :** **&nbsp;**  **[`RegEx`](#regex)**

**&nbsp;&nbsp;&nbsp;**  **23. Try-Except :** **&nbsp;**  **[`Try-Except`](#try-except)**

**&nbsp;&nbsp;&nbsp;**  **24. Input :** **&nbsp;**  **[`Input`](#input)**

**&nbsp;&nbsp;&nbsp;**  **25. String Formatting :** **&nbsp;**  **[`String-Formatting`](#string-formatting)**

**&nbsp;&nbsp;&nbsp;**  **26. File Handling :** **&nbsp;**  **[`File-Handling`](#file-handling)**

**&nbsp;&nbsp;&nbsp;**  **27. Built In Functions :** **&nbsp;**  **[`Built-In-Functions`](#built-in-functions)**

**&nbsp;&nbsp;&nbsp;**  **28. Python Error :** **&nbsp;**  **[`Python-Error`](#python-error)**

**&nbsp;&nbsp;&nbsp;**  **29. Random :** **&nbsp;**  **[`Random`](#random)**

**&nbsp;&nbsp;&nbsp;**  **30. Enum :** **&nbsp;**  **[`Enum`](#enum)**

**&nbsp;&nbsp;&nbsp;**  **31. System :** **&nbsp;**  **[`System`](#system)**

**&nbsp;&nbsp;&nbsp;**  **32. Path :** **&nbsp;**  **[`Path`](#path)**

**&nbsp;&nbsp;&nbsp;**  **33. Pickle :** **&nbsp;**  **[`Pickle`](#pickle)**

**&nbsp;&nbsp;&nbsp;**  **34. Collections :** **&nbsp;**  **[`Collections`](#collections)**

**&nbsp;&nbsp;&nbsp;**  **35. Operator :** **&nbsp;**  **[`Operator`](#operator)**

**&nbsp;&nbsp;&nbsp;**  **36. Progress Bar :** **&nbsp;**  **[`Progress-Bar`](#progress-bar)**

**&nbsp;&nbsp;&nbsp;**  **37. Matplotlib(chart) :** **&nbsp;**  **[`Matplotlib`](#matplotlib)**

**&nbsp;&nbsp;&nbsp;**  **38. Table(tabulate) :** **&nbsp;**  **[`Table`](#table)**

**&nbsp;&nbsp;&nbsp;**  **39. OOP(Class) :** **&nbsp;**  **[`Class`](#class)**

**&nbsp;&nbsp;&nbsp;**  **40. CSV :** **&nbsp;**  **[`CSV`](#csv)**

**&nbsp;&nbsp;&nbsp;**  **41. txt :** **&nbsp;**  **[`txt`](#txt)**

**&nbsp;&nbsp;&nbsp;**  **42. OS :** **&nbsp;**  **[`OS`](#os)**

**&nbsp;&nbsp;&nbsp;**  **43. MySQL :** **&nbsp;**  **[`MySQL`](#mysql)**



Home
----
```python
print("Hello, World!")
>> "Hello, World!"

# hello world
```


Variables
----
![Monty Python](https://files.realpython.com/media/Variables-in-Python_Watermarked.3868fbf92e1d.jpg)
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


Data-Types
----------
![Monty Python](https://files.realpython.com/media/Basic-Data-Types-in-Python_Watermarked.e3dd34457952.jpg)
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
![Monty Python](https://files.realpython.com/media/Python-Basics-Chapter-Numbers-in-Python_Watermarked.70cee8925cbf.jpg)
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
![Monty Python](https://files.realpython.com/media/Strings-and-Character-Data-in-Python_Watermarked.797803948b10.jpg)
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
![Monty Python](https://files.realpython.com/media/What-is-a-Python-Boolean_Watermarked.ba6413996cb3.jpg)
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
![Monty Python](https://files.realpython.com/media/Operators-and-Expressions-in-Python_Watermarked.651045da4031.jpg)
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
![Monty Python](https://files.realpython.com/media/Lists-and-Tuples-in-Python_Watermarked.4d655c81a78b.jpg)
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
![Monty Python](https://files.realpython.com/media/Pythons-tuple-Built-in-Data-Type-A-Deep-Dive-with-Examples_Watermarked.e85efb14c955.jpg)
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
![Monty Python](https://files.realpython.com/media/Sets-in-Python_Watermarked.cd8d2e9563c3.jpg)
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
![Monty Python](https://files.realpython.com/media/Dictionaries-in-Python_Watermarked.3656a2293c00.jpg)
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
![Monty Python](https://files.realpython.com/media/Conditional-Statements-in-Python_Watermarked.b6b7d30ff62b.jpg)
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
![Monty Python](https://files.realpython.com/media/Python-while-Loops-Indefinite-Iteration_Watermarked.2dfa40d8e92c.jpg)
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
![Monty Python](https://files.realpython.com/media/Python-for-Loops-Definite-Iteration_Watermarked.9c0d36b6de30.jpg)
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
![Monty Python](https://files.realpython.com/media/Inner-Functions-What-Are-They-Good-For_Watermarked.995d44a06cdd.jpg)
```python
def my_function():
  print("Hello from a function")

my_function()
>> "Hello from a function"
```

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

```python
def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function(fname = "Tobias")
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

```python
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
```

```python
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
```

```python
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
```

### Decorator :

**decorators are used in Python to modify the behavior of functions or classes. 
They are higher-order functions that take a function or class as input and return a new function or class with modified behavior. 
Decorators are commonly used to add new functionality to existing code without changing the underlying implementation, 
making the code more usable and modular.**

```python
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
```

```python
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
```

```python
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
```

### generator :

**Generator in Python is an easy way to generate browsers and with this feature you can easily control one and exit it at any time. 
In the case of ordinary functions in Python, the issue of speed and amount of memory is raised. 
You have problems in terms of speed and memory in a Python function, 
which have been solved to a large extent by using Generator in Python.**

```python
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
```

```python
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
```

### Name & Main :

**Management and control function**

```python
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

```

```python
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
```

lambda
--------
![Monty Python](https://files.realpython.com/media/How-to-Use-Python-Lambda-Functions_Watermarked.2afa4f5ea5d4.jpg)
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
![Monty Python](https://files.realpython.com/media/Iterators-and-Iterables-in-Python-What-Are-They-and-How-to-Use-Them_Watermarked.5df74332ac58.jpg)
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
![Monty Python](https://files.realpython.com/media/Scope-in-Python---LEGB-Rule_Watermarked.e5f68e7a3642.jpg)
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
![Monty Python](https://files.realpython.com/media/How-to-Use-Python-datetime-With-Examples_Watermarked.2676ca0aacf2.jpg)
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
![Monty Python](https://files.realpython.com/media/Pythons-Math-Module-Guide_Watermarked.c882e267cbd0.jpg)
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
![Monty Python](https://files.realpython.com/media/Working-With-JSON-Data-in-Python_Watermarked.66a8fdcb8859.jpg)
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


RegEx
------
![Monty Python](https://files.realpython.com/media/Regular-Expressions-Regexes-in-Python-Part-1_Watermarked.0423050c5371.jpg)
```python
import re
txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)
>> ['ai', 'ai']
```

**`findall`	Returns a list containing all matches.**

**`search`	Returns a Match object if there is a match anywhere in the string.**

**`split`	Returns a list where the string has been split at each match.**

**`sub`	Replaces one or many matches with a string.**

**`[]`	A set of characters.**

**`\`	Signals a special sequence (can also be used to escape special characters).**

**`.`	Any character (except newline character).**

**`^`	Starts with.**

**`$`	Ends with.**

**`*`	Zero or more occurrences.**

**`+`	One or more occurrences.**

**`?`	Zero or one occurrences.**

**`{}`	Exactly the specified number of occurrences.**

**`|`	Either or.**

**`()`	Capture and group.**


Try-Except
------
![Monty Python](https://files.realpython.com/media/Python_Exceptions_Watermark.47f814fbeced.jpg)
* **`try`	block lets you test a block of code for errors.**
* **`except`	block lets you handle the error.**
* **`else`	block lets you execute code when there is no error.**
* **`finally`	block lets you execute code, regardless of the result of the try- and except blocks.**

```python
try:
  print(x)
except:
  print("An exception occurred")
>> "An exception occurred"
```

```python
try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")
>> "Variable x is not defined"
```

```python
try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")
>> "Hello"
>> "Nothing went wrong"
```

```python
try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")
>> "Something went wrong"
>> "The 'try except' is finished"
```

```python
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
```


Input
------
![Monty Python](https://files.realpython.com/media/Basic-Input-Output-and-String-Formatting-in-Python_Watermarked.65ba5b535841.jpg)
```python
username = input("Enter username:")
print("Username is: " + username)
>> "Username is: iran"
```

```python
num1 = int(input())
num2 = int(input())
print(num1 + num2)
```

```python
num1 = float(input())
num2 = float(input())
print(num1 + num2)
```

```python
# taking two inputs at a time
x, y = input("Enter two values: ").split()
print("Number of boys: ", x)
print("Number of girls: ", y)
```


String Formatting
------
```python
price = 49
txt = "The price is {} dollars"
print(txt.format(price))
>> "The price is 49 dollars"
```

```python
quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))
>> "I want 3 pieces of item number 567 for 49.00 dollars."
```


File-Handling
------
![Monty Python](https://files.realpython.com/media/Reading-and-Writing-Files-in-Python_Watermarked.0d394921fd90.jpg)
**`close()`	Closes the file.**

**`detach()`	Returns the separated raw stream from the buffer.**

**`fileno()`	Returns a number that represents the stream, from the operating system's perspective.**

**`flush()`	Flushes the internal buffer.**

**`isatty()`	Returns whether the file stream is interactive or not.**

**`read()`	Returns the file content.**

**`readable()`	Returns whether the file stream can be read or not.**

**`readline()`	Returns one line from the file.**

**`readlines()`	Returns a list of lines from the file.**

**`seek()`	Change the file position.**

**`seekable()`	Returns whether the file allows us to change the file position.**

**`tell()`	Returns the current file position.**

**`truncate()`	Resizes the file to a specified size.**

**`writable()`	Returns whether the file can be written to or not.**

**`write()`	Writes the specified string to the file.**

**`writelines()`	Writes a list of strings to the file.**

* **`"r"`	Read - Default value. Opens a file for reading, error if the file does not exist.**
* **`"a"`	Append - Opens a file for appending, creates the file if it does not exist.**
* **`"w"`	Write - Opens a file for writing, creates the file if it does not exist.**
* **`"x"`	Create - Creates the specified file, returns an error if the file exists.**
* **`"t"`	Text - Default value. Text mode.**
* **`"b"`	Binary - Binary mode (e.g. images).**
  
```python
f = open("demofile.txt")
```

```python
f = open("demofile.txt", "rt")
```

```python
f = open("demofile.txt", "r")
print(f.read())
```

```python
f = open("D:\\myfiles\welcome.txt", "r")
print(f.read())
```

```python
f = open("demofile.txt", "r")
print(f.read(5))  # Return the 5 first characters of the file
```

```python
f = open("demofile.txt", "r")
print(f.readline())
```

```python
f = open("demofile.txt", "r")
print(f.readline())
f.close()
```

### Write to an Existing File :
**`"a"`	Append - will append to the end of the file.**

**`"w"`	Write - will overwrite any existing content.**
```python
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
```

### Create a New File :
**`"x"`	Create - will create a file, returns an error if the file exist.**

**`"a"`	Append - will create a file if the specified file does not exist.**

**`"w"`	Write - will create a file if the specified file does not exist.**
```python
f = open("myfile.txt", "x")

f = open("myfile.txt", "w")
```

### Delete a File :
```python
import os
os.remove("demofile.txt")
```

### Check if File exist :
```python
import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")
```

### Delete Folder :
```python
import os
os.rmdir("myfolder")
```


Built-In-Functions
------
### abs() (Returns the absolute value of a number) :
```python
x = abs(-7.25)
print(x)
>> 7.25
```

### all() (Returns True if all items in an iterable object are true) :
```python
mylist = [True, True, True]
x = all(mylist)
print(x)
>> True
```

### any() (Returns True if any item in an iterable object is true) :
```python
mylist = [False, True, False]
x = any(mylist)
print(x)
>> True
```

### ascii() (Returns a readable version of an object. Replaces none-ascii characters with escape character) :
```python
x = ascii("My name is Ståle")
print(x)
>> 'My name is St\xe5le'
```

### bin() (Returns the binary version of a number) :
```python
x = bin(36)
print(x)
>> 0b100100
```

### bool() (Returns the boolean value of the specified object) :
```python
x = bool(1)
print(x)
>> True
```

### bytearray() (Returns an array of bytes) :
```python
x = bytearray(4)
print(x)
>> bytearray(b'\x00\x00\x00\x00')
```

### bytes() (Returns a bytes object) :
```python
x = bytes(4)
print(x)
>> b'\x00\x00\x00\x00'
```

### callable() (Returns True if the specified object is callable, otherwise False) :
```python
x = 5
print(callable(x))
>> False
```

### chr() (Returns a character from the specified Unicode code.) :
```python
x = chr(97)
print(x)
>> 'a'
```

### complex() (Returns a complex number) :
```python
x = complex(3, 5)
print(x)
>> (3+5j)
```

### dir() (Returns a list of the specified object's properties and methods) :
```python
class Person:
  name = "John"
  age = 36
  country = "Norway"

print(dir(Person))
>> ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'age', 'country', 'name']
```

### divmod() (Returns the quotient and the remainder when argument1 is divided by argument2) :
```python
x = divmod(5, 2)
print(x)
>> (2, 1)
```

### enumerate() (Takes a collection (e.g. a tuple) and returns it as an enumerate object) :
```python
x = ('apple', 'banana', 'cherry')
y = enumerate(x)
print(y)
>> <enumerate object at 0x14f74341f400>
```

### eval() (Evaluates and executes an expression) :
```python
x = 'print(55)'
eval(x)
print(x)
>> 55
```

### exec() (Executes the specified code (or object)) :
```python
x = 'name = "John"\nprint(name)'
exec(x)
>> "John"
```

### filter() (Use a filter function to exclude items in an iterable object) :
```python
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
```

### float() (Returns a floating point number) :
```python
x = float(3)
print(x)
>> 3.0
```

### format() (Formats a specified value) :
**`'<'` Left aligns the result (within the available space)**

**`'>'` Right aligns the result (within the available space)**

**`'^'` Center aligns the result (within the available space)**

**`'='` Places the sign to the left most position**

**`'+'` Use a plus sign to indicate if the result is positive or negative**

**`'-'` Use a minus sign for negative values only**

**`' '` Use a leading space for positive numbers**

**`','` Use a comma as a thousand separator**

**`'_'` Use a underscore as a thousand separator**

**`'b'` Binary format**

**`'c'` Converts the value into the corresponding unicode character**

**`'d'` Decimal format**

**`'e'` Scientific format, with a lower case e**

**`'E'` Scientific format, with an upper case E**

**`'f'` Fix point number format**

**`'F'` Fix point number format, upper case**

**`'g'` General format**

**`'G'` General format (using a upper case E for scientific notations)**

**`'o'` Octal format**

**`'x'` Hex format, lower case**

**`'X'` Hex format, upper case**

**`'n'` Number format**

**`'%'` Percentage format**
```python
x = format(0.5, '%')
print(x)
>> 50.000000%
```

### frozenset() (Returns a frozenset object) :
```python
mylist = ['apple', 'banana', 'cherry']
x = frozenset(mylist)
print(x)
>> frozenset({'banana', 'cherry', 'apple'})
```

### hex() (Converts a number into a hexadecimal value) :
```python
x = hex(255)
print(x)
>> 0xff
```

### id() (Returns the id of an object) :
```python
x = ('apple', 'banana', 'cherry')
y = id(x)
print(y)
>> 23082267064192
```

### isinstance() (Returns True if a specified object is an instance of a specified object) :
```python
x = isinstance(5, int)
print(x)
>> True
```

### iter() (Returns an iterator object) :
```python
x = iter(["apple", "banana", "cherry"])
print(next(x))
print(next(x))
print(next(x))
>> "apple"
>> "banana"
>> "cherry"
```

### map() (Returns the specified iterator with the specified function applied to each item) :
```python
def myfunc(n):
  return len(n)
x = map(myfunc, ('apple', 'banana', 'cherry'))
print(x)
>> <map object at 0x1481154c4130>
```

```python
def square(number):
    return number ** 2


numbers = [1, 2, 3, 4, 5]
squared = map(square, numbers)

list(squared)
>> [1, 4, 9, 16, 25]
```

```python
str_nums = ["4", "8", "6", "5", "3", "2", "8", "9", "2", "5"]

int_nums = map(int, str_nums)
print(int_nums)
>> <map object at 0x7fb2c7e34c70>

print(list(int_nums))
>> [4, 8, 6, 5, 3, 2, 8, 9, 2, 5]

print(str_nums)
>> ["4", "8", "6", "5", "3", "2", "8", "9", "2", "5"]
```

```python
first_it = [1, 2, 3]
second_it = [4, 5, 6, 7]

print(list(map(pow, first_it, second_it)))
>> [1, 32, 729]
```

```python
string_it = ["processing", "strings", "with", "map"]
list(map(str.capitalize, string_it))
>> ['Processing', 'Strings', 'With', 'Map']

list(map(str.upper, string_it))
>> ['PROCESSING', 'STRINGS', 'WITH', 'MAP']

list(map(str.lower, string_it))
>> ['processing', 'strings', 'with', 'map']
```

```python
import math

numbers = [1, 2, 3, 4, 5, 6, 7]

print(list(map(math.factorial, numbers)))
>> [1, 2, 6, 24, 120, 720, 5040]
```

### max() (Returns the largest item in an iterable) :
```python
x = max(5, 10)
print(x)
>> 10
```

### memoryview() (Returns a memory view object) :
```python
x = memoryview(b"Hello")

print(x)
>> <memory at 0x1495289cfa00>

#return the Unicode of the first character
print(x[0])
>> 72

#return the Unicode of the second character
print(x[1])
>> 101
```

### min() (Returns the smallest item in an iterable) :
```python
x = min(5, 10)
print(x)
>> 5
```

### next() (Returns the next item in an iterable) :
```python
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
```

### object() (Returns a new object) :
```python
x = object()
print(x)
>> <object object at 0x15447e7c4d70>
```

### oct() (Converts a number into an octal) :
```python
x = oct(12)
print(x)
>> 0o14
```

### ord() (Convert an integer representing the Unicode of the specified character) :
```python
x = ord("h")
print(x)
>> 104
```

### range() (Returns a sequence of numbers, starting from 0 and increments by 1 (by default)) :
```python
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
```

### reversed() (Returns a reversed iterator) :
```python
alph = ["a", "b", "c", "d"]
ralph = reversed(alph)
for x in ralph:
  print(x)
>> 'd'
   'c'
   'b'
   'a'
```

### round() (Rounds a numbers) :
```python
x = round(5.76543, 2)
print(x)
>> 5.77
```

### slice() (Returns a slice object) :
```python
a = ("a", "b", "c", "d", "e", "f", "g", "h")
x = slice(2)
print(a[x])
>> ('a', 'b')
```

### sorted() (Returns a sorted list) :
```python
a = ("b", "g", "a", "d", "f", "c", "h", "e")
x = sorted(a)
print(x)
>> ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
```

### str() (Returns a string object) :
```python
x = str(3.5)
print(x)
>> "3.5"
```

### sum() (Sums the items of an iterator) :
```python
a = (1, 2, 3, 4, 5)
x = sum(a)
>> 15
```

### type() (Returns the type of an object) :
```python
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
```


Python-Error
------
![Monty Python](https://files.realpython.com/media/Python-3.12-Preview-1-Error-Messages_Watermarked.ca9ce482328d.jpg)
**`ArithmeticError`               # Raised when an error occurs in numeric calculations**

**`AssertionError`                # Raised when an assert statement fails**

**`AttributeError`                # Raised when attribute reference or assignment fails**

**`Exception`                     # Base class for all exceptions**

**`EOFError`                      # Raised when the input() method hits an "end of file" condition (EOF)**

**`FloatingPointError`            # Raised when a floating point calculation fails**

**`GeneratorExit`                # Raised when a generator is closed (with the close() method)**

**`ImportError`                   # Raised when an imported module does not exist**

**`IndentationError`              # Raised when indentation is not correct**

**`IndexError`                    # Raised when an index of a sequence does not exist**

**`KeyError`                      # Raised when a key does not exist in a dictionary**

**`KeyboardInterrupt`             # Raised when the user presses Ctrl+c, Ctrl+z or Delete**

**`LookupError`                   # Raised when errors raised cant be found**

**`MemoryError`                  # Raised when a program runs out of memory**

**`NameError`                     # Raised when a variable does not exist**

**`NotImplementedError`           # Raised when an abstract method requires an inherited class to override the method**

**`OSError`                       # Raised when a system related operation causes an error**

**`OverflowError`                 # Raised when the result of a numeric calculation is too large**

**`ReferenceError`                # Raised when a weak reference object does not exist**

**`RuntimeError`                  # Raised when an error occurs that do not belong to any specific exceptions**

**`StopIteration`                 # Raised when the next() method of an iterator has no further values**

**`SyntaxError`                   # Raised when a syntax error occurs**

**`TabError`                      # Raised when indentation consists of tabs or spaces**

**`SystemError`                   # Raised when a system error occurs**

**`SystemExit`                    # Raised when the sys.exit() function is called**

**`TypeError`                     # Raised when two different types are combined**

**`UnboundLocalError`             # Raised when a local variable is referenced before assignment**

**`UnicodeError`                  # Raised when a unicode problem occurs**

**`UnicodeEncodeError`            # Raised when a unicode encoding problem occurs**

**`UnicodeDecodeError`            # Raised when a unicode decoding problem occurs**

**`UnicodeTranslateError`         # Raised when a unicode translation problem occurs**

**`ValueError`                    # Raised when there is a wrong value in a specified data type**

**`ZeroDivisionError`             # Raised when the second operator in a division is zero**


Random
------
### randrange() (Returns a random number between the given range) :
```python
import random
print(random.randrange(3, 9))
>> 4
```

### randint() (Returns a random number between the given range) :
```python
import random
print(random.randint(3, 9))
>> 9
```

### choice() (Returns a random element from the given sequence) :
```python
import random
mylist = ["apple", "banana", "cherry"]
print(random.choice(mylist))
>> "cherry"
```

### shuffle() (Takes a sequence and returns the sequence in a random order) :
```python
import random
mylist = ["apple", "banana", "cherry"]
random.shuffle(mylist)
print(mylist)
>> ['cherry', 'apple', 'banana']
```

### sample() (Returns a given sample of a sequence) :
```python
import random
mylist = ["apple", "banana", "cherry"]
print(random.sample(mylist, k=2))
>> ['cherry', 'banana']
```

### uniform() (Returns a random float number between two given parameters) :
```python
import random
print(random.uniform(20, 60))
>> 47.016106134431425
```


Enum
------
![Monty Python](https://files.realpython.com/media/Build-Enumerations-With-Pythons-enum_Watermarked.bbcd46a82f58.jpg)
**for first this is a normal calss with normal ability :**
```python
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
```

**Or**

```python
class Season(Enum):
    SPRING = 1
    SUMMER = 2
    AUTUMN = 3
    WINTER = 4
print("The enum member associated with value 2 is : ", Season(2).name)
print("The enum member associated with name AUTUMN is : ", Season['AUTUMN'].value)
>> "The enum member associated with value 2 is :  SUMMER"
>> "The enum member associated with name AUTUMN is :  3"
```

**now we use enum :**

```python
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
```

```python
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
```


System
----
```python
import sys
print(sys.version)
>> 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)]

import sys 
age = 17
if age < 18: 
    sys.exit("Age less than 18")     
else: 
    print("Age is not less than 18") 
```


System
----
**OS has many Module , and we don't need all of them , so visit this site for all OS Module**

https://www.w3schools.com/python/module_os.asp


Path
------
![Monty Python](https://files.realpython.com/media/Python-3s-pathlib-Module-Taming-the-File-System_Watermarked.524352e6d4ce.jpg)
### python path :
```python
from pathlib import Path
print(Path.cwd())
>> "C:\Users\Name\AppData\Local\Programs\Python\Python311"
```

### user path 
```python
# user path :
from pathlib import Path
print(Path.home())
>> "C:\Users\Name"
```

### special path : 
```python
from pathlib import Path
print(Path("C:\\Users\\Name\\Desktop\\Pic"))
>> WindowsPath('C:\\Users\\Name\\Desktop\\Pic')
```

### Picking Out Components of a Path : 
```python
from pathlib import Path
path = Path("C:\\Users\\Name\\realpython\\test.md")
print(path)
>> WindowsPath('C:/Users/Name/realpython/test.md')

print(path.name)
>> 'test.md'

print(path.stem)
>> 'test'

print(path.suffix)
>> '.md'

print(path.anchor)
>> 'C:\\'

print(path.parent)
>> WindowsPath('C:/Users/Name/realpython")

print(path.parent.parent)
>> WindowsPath('C:/Users/Name')
```

### Reading and Writing Files : 
```python
from pathlib import Path
path = Path("C:\\Users\\NAJAFI\\Desktop\\Pic.txt")
with path.open(mode="r", encoding="utf-8") as md_file:
    content = md_file.read()
    print(content)
>> "hello"
```
* **`.read_text()` opens the path in text mode and returns the contents as a string.**
* **`.read_bytes()` opens the path in binary mode and returns the contents as a byte string.**
* **`.write_text()` opens the path and writes string data to it.**
* **`.write_bytes()` opens the path in binary mode and writes data to it.**


### Renaming Files : 
```python
from pathlib import Path
txt_path = Path("/home/gahjelle/realpython/hello.txt")
Print(txt_path)
>> PosixPath("/home/gahjelle/realpython/hello.txt")

md_path = txt_path.with_suffix(".md")
>> PosixPath('/home/gahjelle/realpython/hello.md')
txt_path.replace(md_path)
```

### Copying Files : 
```python
from pathlib import Path
source = Path("shopping_list.md")
destination = source.with_stem("shopping_list_02")
destination.write_bytes(source.read_bytes()) # .read_bytes() to read the content of source and then write this content to destination using .write_bytes().
```

### Moving Files : 
```python
from pathlib import Path
source = Path("hello.py")
destination = Path("goodbye.py")
if not destination.exists():
    source.replace(destination)
```

### Create Files : 
```python
from pathlib import Path
filename = Path("C:\\Users\\NAJAFI\\Desktop\\h.txt")
filename.exists()
>> False
filename.touch()
filename.exists()
>> True
```

Pickle
------
![Monty Python](https://files.realpython.com/media/Object-Serialization-With-the-Python-Pickle-Module_Watermarked.8e4667c2f71f.jpg)
```python
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
```

Collections
------
![Monty Python](https://files.realpython.com/media/Pythons-Collections-Module_Watermarked.31248400c167.jpg)
```python
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
```

```python
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
```

```python
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
```

```python
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
```

```python
from collections import defaultdict  
    
# Defining a dict  
d = defaultdict(list)  
    
for i in range(5):  
    d[i].append(i)  
        
print("Dictionary with values as list:")  
print(d)
>> "Dictionary with values as list:"
>> defaultdict(<class ‘list’>, {0: [0], 1: [1], 2: [2], 3: [3], 4: [4]})
```

```python
from collections import ChainMap  

d1 = {'a': 1, 'b': 2} 
d2 = {'c': 3, 'd': 4} 
d3 = {'e': 5, 'f': 6} 
  
# Defining the chainmap  
c = ChainMap(d1, d2, d3)    
print(c)
>> ChainMap({'a': 1, 'b': 2}, {'c': 3, 'd': 4}, {'e': 5, 'f': 6})
```

```python
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
```

```python
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
```

```python
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
```

```python
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
```

```python
from collections import deque 
    
# Declaring deque 
queue = deque(['name','age','DOB'])  
    
print(queue)
>> deque(['name', 'age', 'DOB'])
```

```python
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
```

```python
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
```


Operator
------
![Monty Python](https://files.realpython.com/media/Python_s-operator-Module_Watermarked.8ca3c8521230.jpg)
**`add(a, b)` a + b : This function returns addition of the given arguments.**                                                                                  

**`sub(a, b)` a - b : This function returns difference of the given arguments.**                                                                               

**`mul(a, b)` a * b : This function returns product of the given arguments.**                                                                                         

**`truediv(a,b)` a / b : This function returns division of the given arguments.**                                                                                     

**`floordiv(a,b)` a // b : This function also returns division of the given arguments.**          

**`pow(a,b)` a ** b : This function returns exponentiation of the given arguments.**                                                                                  

**`mod(a,b)` a % b : This function returns modulus of the given arguments.**                                                                                 

**`lt(a, b)` a < b : This function is used to check if a is less than b or not.**                               

**`le(a, b)` a <= b : This function is used to check if a is less than or equal to b or not.**      

**`eq(a, b)` a == b : This function is used to check if a is equal to b or not.**                               

**`gt(a,b)` a > b : This function is used to check if a is greater than b or not.**                       

**`ge(a,b)` a >= b : This function is used to check if a is greater than or equal to b or not.** 

**`ne(a,b)` a != b : This function is used to check if a is not equal to b or is equal.**

```python
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
```

```python
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
```

```python
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
```

```python
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
```


Progress-Bar
------
```python
# $ pip3 install tqdm
from tqdm import tqdm
from time import sleep

total = 0
for num in tqdm([1, 2, 3, 4]):
    sleep(0.25)
    total = total + num
    
>> Processing: 100%|████████████████████| 4/4 [00:01<00:00,  3.95s/it]
```


Matplotlib
------
![Monty Python](https://files.realpython.com/media/Python_Plotting_With_Matplotlib_Watermark.610acdacc476.jpg)

```python
import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([0, 6])
ypoints = np.array([0, 250])

plt.plot(xpoints, ypoints)
plt.show()
```
![Figure_1](https://github.com/Hafez-CS/Python-Handbook/assets/151014739/57e266ef-a403-4b19-aaa7-8d3eb7ac4351)

**The plot() function is used to draw points (markers) in a diagram.**
**By default, the plot() function draws a line from point to point.**
**The function takes parameters for specifying points in the diagram.**
**Parameter 1 is an array containing the points on the x-axis.**
**Parameter 2 is an array containing the points on the y-axis.**
**If we need to plot a line from (1, 3) to (8, 10), we have to pass two arrays [1, 8] and [3, 10] to the plot function.**

```python
import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1, 8])
ypoints = np.array([3, 10])

plt.plot(xpoints, ypoints, 'o')
plt.show()
```
![Figure_2](https://github.com/Hafez-CS/Python-Handbook/assets/151014739/8fe4137d-168e-4ee5-8c3a-24bba808543c)


```python
import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1, 2, 6, 8])
ypoints = np.array([3, 8, 1, 10])

plt.plot(xpoints, ypoints)
plt.show()
```
![Figure_3](https://github.com/Hafez-CS/Python-Handbook/assets/151014739/c713e39e-7bac-45e0-9c49-e228ed15cbd5)


```python
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10, 5, 7])

plt.plot(ypoints)
plt.show()

# The x-points are [0, 1, 2, 3, 4, 5].
```
![Figure_4](https://github.com/Hafez-CS/Python-Handbook/assets/151014739/d08c6c0d-72a1-4af3-be87-b60a15a4ed78)


```python
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker = 'o')
plt.show()
```
![Figure_5](https://github.com/Hafez-CS/Python-Handbook/assets/151014739/af0d89dc-3488-42ab-9f95-435f435c6af1)


```python
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker = 'o')
plt.show()
```
![Figure_5](https://github.com/Hafez-CS/Python-Handbook/assets/151014739/af0d89dc-3488-42ab-9f95-435f435c6af1)

### You can choose any of these markers :
**`'o'`	Circle**

**`'*'`	Star**

**`'.'`	Point**	

**`','`	Pixel**	

**`'x'`	X**

**`'X'`	X (filled)**

**`'+'`	Plus**

**`'P'`	Plus (filled)**

**`'s'`	Square**

**`'D'`	Diamond**

**`'d'`	Diamond (thin)**

**`'p'`	Pentagon**

**`'H'`	Hexagon**

**`'h'`	Hexagon**

**`'v'`	Triangle Down**

**`'^'`	Triangle Up**

**`'<'`	Triangle Left**

**`'>'`	Triangle Right**

**`'1'`	Tri Down**

**`'2'`	Tri Up**

**`'3'`	Tri Left**

**`'4'`	Tri Right**

**`'|'`	Vline**

**`'_'`	Hline**


```python
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, 'o:r')
plt.show()
```
![Figure_6](https://github.com/Hafez-CS/Python-Handbook/assets/151014739/2c5b91a8-ff7e-41ce-974c-19e198603035)


### Line Reference :
**`'o'`	Circle**

**`'-'`	Solid line**

**`':'`	Dotted line**

**`'--'`	Dashed line**

**`'-.'`	Dashed/dotted line**


### Color Reference :
**`'o'`	Circle**

**`'r'`	Red**

**`'g'`	Green**	

**`'b'`	Blue**

**`'c'`	Cyan**

**`'m'`	Magenta**	

**`'y'`	Yellow**

**`'k'`	Black**

**`'w'`	White**


```python
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker = 'o', ms = 20) # Marker Size
plt.show()
```
![Figure_7](https://github.com/Hafez-CS/Python-Handbook/assets/151014739/7f9c8a4d-798f-49a0-b04a-2bd393bd3f17)


```python
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker = 'o', ms = 20, mec = 'r') # Marker Color
plt.show()
```
![Figure_8](https://github.com/Hafez-CS/Python-Handbook/assets/151014739/ab3f946e-362d-4654-85c4-39d66917eb70)


```python
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker = 'o', ms = 20, mfc = 'r') # Marker Color
plt.show()
```
![Figure_9](https://github.com/Hafez-CS/Python-Handbook/assets/151014739/8a7d25c2-9b4e-4a47-afc3-e5c341752a00)


```python
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker = 'o', ms = 20, mec = 'r', mfc = 'r') # Marker Color
plt.show()
```
![Figure_10](https://github.com/Hafez-CS/Python-Handbook/assets/151014739/aae66e00-c763-472f-a504-b15138f572fb)


```python
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, linestyle = 'dotted')
plt.show()
```
![Figure_11](https://github.com/Hafez-CS/Python-Handbook/assets/151014739/e75927cf-26ba-499a-ae91-2920053b9038)


### Line Styles : 

**`'solid'` (default)	'-'**

**`'dotted'` ':'**	

**`'dashed'` '--'**

**`'dashdot'` '-.'**

**`'None'` ''   or   ' '**


```python
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, color = 'r')
plt.show()
```
![Figure_12](https://github.com/Hafez-CS/Python-Handbook/assets/151014739/f59b873e-535f-43ad-8f1f-f97633c10b30)


```python
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, linewidth = '20.5')
plt.show()
```
![Figure_13](https://github.com/Hafez-CS/Python-Handbook/assets/151014739/b6a2bbe8-e453-4704-aa89-78185b82ea52)


```python
import matplotlib.pyplot as plt
import numpy as np

y1 = np.array([3, 8, 1, 10])
y2 = np.array([6, 2, 7, 11])

plt.plot(y1)
plt.plot(y2)

plt.show()
```
![Figure_14](https://github.com/Hafez-CS/Python-Handbook/assets/151014739/d56d4b97-8220-4b7a-8922-16ddc12d261a)


```python
import matplotlib.pyplot as plt
import numpy as np

x1 = np.array([0, 1, 2, 3])
y1 = np.array([3, 8, 1, 10])
x2 = np.array([0, 1, 2, 3])
y2 = np.array([6, 2, 7, 11])

plt.plot(x1, y1, x2, y2)
plt.show()
```
![Figure_15](https://github.com/Hafez-CS/Python-Handbook/assets/151014739/11c79be4-637b-45e4-9468-e12ed5b2f805)


```python
import numpy as np
import matplotlib.pyplot as plt

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.plot(x, y)

plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

plt.show()
```
![Figure_16](https://github.com/Hafez-CS/Python-Handbook/assets/151014739/df0585fe-257b-40c8-a199-ebf01697ecdc)


```python
import numpy as np
import matplotlib.pyplot as plt

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.plot(x, y)

plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

plt.show()
```
![Figure_17](https://github.com/Hafez-CS/Python-Handbook/assets/151014739/d752fd13-173b-4353-a2bb-3f859532c65b)


```python
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
```
![Figure_18](https://github.com/Hafez-CS/Python-Handbook/assets/151014739/c7f44972-aec3-4fb1-852a-2cfdd518eccb)


```python
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
```
![Figure_19](https://github.com/Hafez-CS/Python-Handbook/assets/151014739/56948e65-27f0-4ae1-af13-ea4fb0364353)


```python
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
```
![Figure_20](https://github.com/Hafez-CS/Python-Handbook/assets/151014739/7944a9e9-185c-46eb-afdb-c828c884895e)


```python
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
```
![Figure_21](https://github.com/Hafez-CS/Python-Handbook/assets/151014739/977fadd4-dcca-46ab-b614-0bedf0cd7f86)


```python
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
```
![Figure_22](https://github.com/Hafez-CS/Python-Handbook/assets/151014739/1c2cf727-9ff3-488c-a1af-f49a2be7ea9b)


```python
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
```
![Figure_23](https://github.com/Hafez-CS/Python-Handbook/assets/151014739/372df0aa-4478-41e3-8a1c-28b446691200)


```python
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
```
![Figure_24](https://github.com/Hafez-CS/Python-Handbook/assets/151014739/cbd9dca0-e58c-450d-9f3c-ef935d1d75fd)


```python
import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])

plt.scatter(x, y)
plt.show()
```
![Figure_25](https://github.com/Hafez-CS/Python-Handbook/assets/151014739/1ff56130-6906-4586-93cc-168f723fff57)


```python
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
```
![Figure_26](https://github.com/Hafez-CS/Python-Handbook/assets/151014739/1b6c636f-4d16-4239-99c6-55572115f887)


```python
import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
colors = np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100])

plt.scatter(x, y, c=colors, cmap='viridis')

plt.colorbar()

plt.show()
```
![Figure_27](https://github.com/Hafez-CS/Python-Handbook/assets/151014739/c222abd2-0fd9-4b6d-bf16-bba7da477f86)


```python
import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
sizes = np.array([20,50,100,200,500,1000,60,90,10,300,600,800,75])

plt.scatter(x, y, s=sizes)

plt.show()
```
![Figure_28](https://github.com/Hafez-CS/Python-Handbook/assets/151014739/62163c92-81c5-4d0e-bf44-335bce0038e4)


```python
import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x,y)
plt.show()
```
![Figure_29](https://github.com/Hafez-CS/Python-Handbook/assets/151014739/2cd065c0-e2e2-41c2-b069-6370943ac22e)


```python
import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.barh(x, y)
plt.show()
```
![Figure_30](https://github.com/Hafez-CS/Python-Handbook/assets/151014739/d4265bd8-9662-4aa6-924d-4d77da935715)


```python
import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x, y, color = "red")
plt.show()
```
![Figure_31](https://github.com/Hafez-CS/Python-Handbook/assets/151014739/bc74c131-c11a-4b43-9899-f37673c8545f)


```python
import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x, y, width = 0.1)
plt.show()
```
![Figure_32](https://github.com/Hafez-CS/Python-Handbook/assets/151014739/04f6784f-f769-482d-a265-7f2d11380021)


```python
import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])

plt.pie(y)
plt.show() 
```
![Figure_33](https://github.com/Hafez-CS/Python-Handbook/assets/151014739/9e13f6b2-da5f-46e4-b6e1-0aea013d813e)


```python
import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

plt.pie(y, labels = mylabels)
plt.show() 
```
![Figure_34](https://github.com/Hafez-CS/Python-Handbook/assets/151014739/a889ef59-7709-433f-8e70-9e0a261a5571)


```python
import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
myexplode = [0.2, 0, 0, 0]

plt.pie(y, labels = mylabels, explode = myexplode)
plt.show()
```
![Figure_35](https://github.com/Hafez-CS/Python-Handbook/assets/151014739/95fbcc26-1844-4c23-bdd9-72d95e02c027)


```python
import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

plt.pie(y, labels = mylabels)
plt.legend()
plt.show() 
```
![Figure_36](https://github.com/Hafez-CS/Python-Handbook/assets/151014739/0c476500-8db1-4336-a378-34696ac177cf)



Table
------
```python
# $ pip3 install tabulate

table = [["Sun",696000,1989100000],["Earth",6371,5973.6],["Moon",1737,73.5],["Mars",3390,641.85]]
print(tabulate(table))

>> -----  ------  -------------
   Sun    696000   1.9891e+09
   Earth    6371   5973.6
   Moon     1737   73.5
   Mars     3390   641.85
   -----  ------  -------------
```

```python
print(tabulate(table, headers=["Planet","R (km)", "mass (x 10^29 kg)"]))

>> Planet      R (km)    mass (x 10^29 kg)
   --------  --------  -------------------
   Sun         696000           1.9891e+09
   Earth         6371        5973.6
   Moon          1737          73.5
   Mars          3390         641.85
```

```python
print(tabulate([["Name","Age"],["Alice",24],["Bob",19]],headers="firstrow"))  # If headers="firstrow", then the first row of data is used:

>> Name      Age
   ------  -----
   Alice      24
   Bob        19
```

```python
print(tabulate({"Name": ["Alice", "Bob"],"Age": [24, 19]}, headers="keys")) # If headers="keys", then the keys of a dictionary/dataframe, or column indices are used

>>   Age  Name
   -----  ------
      24  Alice
      19  Bob
```

**By default, only pandas.DataFrame tables have an additional column called row index. 
To add a similar column to any other type of table, pass showindex="always" or showindex=True argument to tabulate(). 
To suppress row indices for all types of data, pass showindex="never" or showindex=False. 
To add a custom row index column, pass showindex=rowIDs, where rowIDs is some iterable:**
```python
print(tabulate([["F",24],["M",19]], showindex="always"))
>> -  -  --
   0  F  24
   1  M  19
   -  -  --
```

**There is more than one way to format a table in plain text. The third optional argument named tablefmt defines how the table is formatted.Supported table formats are:**

* **"plain"**
  
* **"simple"**
  
* **"github"**
  
* **"grid"**
  
* **"simple_grid"**
  
* **"rounded_grid"**
  
* **"heavy_grid"**
  
* **"mixed_grid"**
  
* **"double_grid"**

* **"fancy_grid"**
  
* **"outline"**
  
* **"simple_outline"**
  
* **"rounded_outline"**
  
* **"heavy_outline"**
  
* **"mixed_outline"**
  
* **"double_outline"**
  
* **"fancy_outline"**
  
* **"pipe"**
  
* **"orgtbl"**
  
* **"asciidoc"**
  
* **"jira"**
  
* **"presto"**
  
* **"pretty"**
  
* **"psql"**
  
* **"rst"**
  
* **"mediawiki"**
  
* **"moinmoin"**
  
* **"youtrack"**
  
* **"html"**
  
* **"unsafehtml"**
  
* **"latex"**
  
* **"latex_raw"**
  
* **"latex_booktabs"**
  
* **"latex_longtable"**
  
* **"textile"**
  
* **"tsv"**


**plain tables do not use any pseudo-graphics to draw lines:**
```python
table = [["spam",42],["eggs",451],["bacon",0]]
headers = ["item", "qty"]
print(tabulate(table, headers, tablefmt="plain"))

>> item      qty
   spam       42
   eggs      451
   bacon       0
```


**simple is the default format (the default may change in future versions). It corresponds to simple_tables in Pandoc Markdown extensions:**
```python
print(tabulate(table, headers, tablefmt="simple"))

>> item      qty
   ------  -----
   spam       42
   eggs      451
   bacon       0
```


**github follows the conventions of GitHub flavored Markdown. It corresponds to the pipe format without alignment colons:**
```python
print(tabulate(table, headers, tablefmt="github"))

>> | item   | qty   |
   |--------|-------|
   | spam   | 42    |
   | eggs   | 451   |
   | bacon  | 0     |
```


**grid is like tables formatted by Emacs' table.el package. It corresponds to grid_tables in Pandoc Markdown extensions:**
```python
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
```


**simple_grid draws a grid using single-line box-drawing characters:**
```python
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
```


**rounded_grid draws a grid using single-line box-drawing characters with rounded corners:**
```python
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
```


**heavy_grid draws a grid using bold (thick) single-line box-drawing characters:**
```python
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
```


**mixed_grid draws a grid using a mix of light (thin) and heavy (thick) lines box-drawing characters:**
```python
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
```


**double_grid draws a grid using double-line box-drawing characters:**
```python
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
```


**fancy_grid draws a grid using a mix of single and double-line box-drawing characters:**
```python
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
```


**outline is the same as the grid format but doesn't draw lines between rows:**
```python
print(tabulate(table, headers, tablefmt="outline"))

>> +--------+-------+
   | item   |   qty |
   +========+=======+
   | spam   |    42 |
   | eggs   |   451 |
   | bacon  |     0 |
   +--------+-------+
```


**simple_outline is the same as the simple_grid format but doesn't draw lines between rows:**
```python
print(tabulate(table, headers, tablefmt="simple_outline"))

>> ┌────────┬───────┐
   │ item   │   qty │
   ├────────┼───────┤
   │ spam   │    42 │
   │ eggs   │   451 │
   │ bacon  │     0 │
   └────────┴───────┘
```


**rounded_outline is the same as the rounded_grid format but doesn't draw lines between rows:**
```python
print(tabulate(table, headers, tablefmt="rounded_outline"))

>> ╭────────┬───────╮
   │ item   │   qty │
   ├────────┼───────┤
   │ spam   │    42 │
   │ eggs   │   451 │
   │ bacon  │     0 │
   ╰────────┴───────╯
```


**heavy_outline is the same as the heavy_grid format but doesn't draw lines between rows:**
```python
print(tabulate(table, headers, tablefmt="heavy_outline"))

>> ┏━━━━━━━━┳━━━━━━━┓
   ┃ item   ┃   qty ┃
   ┣━━━━━━━━╋━━━━━━━┫
   ┃ spam   ┃    42 ┃
   ┃ eggs   ┃   451 ┃
   ┃ bacon  ┃     0 ┃
   ┗━━━━━━━━┻━━━━━━━┛
```


**mixed_outline is the same as the mixed_grid format but doesn't draw lines between rows:**
```python
print(tabulate(table, headers, tablefmt="mixed_outline"))

>> ┍━━━━━━━━┯━━━━━━━┑
   │ item   │   qty │
   ┝━━━━━━━━┿━━━━━━━┥
   │ spam   │    42 │
   │ eggs   │   451 │
   │ bacon  │     0 │
   ┕━━━━━━━━┷━━━━━━━┙
```


**double_outline is the same as the double_grid format but doesn't draw lines between rows:**
```python
print(tabulate(table, headers, tablefmt="double_outline"))

>> ╔════════╦═══════╗
   ║ item   ║   qty ║
   ╠════════╬═══════╣
   ║ spam   ║    42 ║
   ║ eggs   ║   451 ║
   ║ bacon  ║     0 ║
   ╚════════╩═══════╝
```


**fancy_outline is the same as the fancy_grid format but doesn't draw lines between rows:**
```python
print(tabulate(table, headers, tablefmt="fancy_outline"))

>> ╒════════╤═══════╕
   │ item   │   qty │
   ╞════════╪═══════╡
   │ spam   │    42 │
   │ eggs   │   451 │
   │ bacon  │     0 │
   ╘════════╧═══════╛
```


**presto is like tables formatted by Presto cli:**
```python
print(tabulate(table, headers, tablefmt="presto"))

>> item   |   qty
  --------+-------
   spam   |    42
   eggs   |   451
   bacon  |     0
```


**pretty attempts to be close to the format emitted by the PrettyTables library:**
```python
print(tabulate(table, headers, tablefmt="pretty"))

>> +-------+-----+
   | item  | qty |
   +-------+-----+
   | spam  | 42  |
   | eggs  | 451 |
   | bacon |  0  |
   +-------+-----+
```


**psql is like tables formatted by Postgres' psql cli:**
```python
print(tabulate(table, headers, tablefmt="psql"))

>> +--------+-------+
   | item   |   qty |
   |--------+-------|
   | spam   |    42 |
   | eggs   |   451 |
   | bacon  |     0 |
   +--------+-------+
```


**pipe follows the conventions of PHP Markdown Extra extension. It corresponds to pipe_tables in Pandoc. This format uses colons to indicate column alignment:**
```python
print(tabulate(table, headers, tablefmt="pipe"))

>> | item   |   qty |
   |:-------|------:|
   | spam   |    42 |
   | eggs   |   451 |
   | bacon  |     0 |
```


**asciidoc formats data like a simple table of the AsciiDoctor format:**
```python
print(tabulate(table, headers, tablefmt="asciidoc"))

>> [cols="8<,7>",options="header"]
   |====
   | item   |   qty
   | spam   |    42
   | eggs   |   451
   | bacon  |     0
   |====
```


**orgtbl follows the conventions of Emacs org-mode, and is editable also in the minor orgtbl-mode. Hence its name:**
```python
print(tabulate(table, headers, tablefmt="orgtbl"))

>> | item   |   qty |
   |--------+-------|
   | spam   |    42 |
   | eggs   |   451 |
   | bacon  |     0 |
```


**jira follows the conventions of Atlassian Jira markup language:**
```python
print(tabulate(table, headers, tablefmt="rst"))

>> ======  =====
   item      qty
   ======  =====
   spam       42
   eggs      451
   bacon       0
   ======  =====
```


**mediawiki format produces a table markup used in Wikipedia and on other MediaWiki-based sites:**
```python
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
```


**moinmoin format produces a table markup used in MoinMoin wikis:**
```python
print(tabulate(table, headers, tablefmt="moinmoin"))

>> || ''' item   ''' || ''' quantity   ''' ||
   ||  spam    ||  41.999      ||
   ||  eggs    ||  451         ||
   ||  bacon   ||              ||
```


**youtrack format produces a table markup used in Youtrack tickets:**
```python
print(tabulate(table, headers, tablefmt="youtrack"))

>> ||  item    ||  quantity   ||
   |   spam    |  41.999      |
   |   eggs    |  451         |
   |   bacon   |              |
```


**textile format produces a table markup used in Textile format:**
```python
print(tabulate(table, headers, tablefmt="textile"))

>> |_.  item   |_.   qty |
   |<. spam    |>.    42 |
   |<. eggs    |>.   451 |
   |<. bacon   |>.     0 |
```


**html produces standard HTML markup as an html.escape'd str with a .repr_html method so that Jupyter Lab and Notebook display the HTML and a .str property so that the raw HTML remains accessible. unsafehtml table format can be used if an unescaped HTML is required:**
```python
print(tabulate(table, headers, tablefmt="html"))

>> <table>
   <tbody>
   <tr><th>item  </th><th style="text-align: right;">  qty</th></tr>
   <tr><td>spam  </td><td style="text-align: right;">   42</td></tr>
   <tr><td>eggs  </td><td style="text-align: right;">  451</td></tr>
   <tr><td>bacon </td><td style="text-align: right;">    0</td></tr>
   </tbody>
   </table>
```


**latex format creates a tabular environment for LaTeX markup, replacing special characters like _ or \ to their LaTeX correspondents:**
```python
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
```



Class
------
![Monty Python](https://realpython.com/cdn-cgi/image/width=960,format=auto/https://files.realpython.com/media/Class-Concepts-Object-Oriented-Programming-in-Python_Watermarked.6cf327c51434.jpg)
**Object-oriented programming (OOP) is a method of structuring a program by bundling related properties and behaviors into individual objects. 
In this tutorial, you'll learn the basics of object-oriented programming in Pytho**

### How Define a Class in Python ?
```python
class Dog:
    pass
```
```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

""" You define the properties that all Dog objects must have in a method called .__init__(). 
Every time you create a new Dog object, .__init__() sets the initial state of the object by assigning the values of the object's properties. 
That is, .__init__() initializes each new instance of the class.
You can give .__init__() any number of parameters, but the first parameter will always be a variable called self. 
When you create a new class instance, then Python automatically passes the instance to the self parameter in .__init__() so that Python can define the new attributes on the object."""
```

### How Instantiate a Class in Python ?
```python
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
```
```python
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
```
```python
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
```
```python
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
```

### How Instantiate a Class in Python ?
```python
""" Inheritance is the process by which one class takes on the attributes and methods of another. 
Newly formed classes are called child classes, and the classes that you derive child classes from are called parent classes."""

class Parent:
    hair_color = "brown"

class Child(Parent):
    pass
```
```python
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
```
### Class Attributes :
```python
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
```
### Instance Attributes :
```python
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
```
### The .__dict__ Attribute :
```python
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
```
### Dynamic Class and Instance Attributes :
```python
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
```
```python
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
```
### Instance Methods With self :
```python
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
```

### Special Methods and Protocols :
```python
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
```



CSV
----
![Monty Python](https://realpython.com/cdn-cgi/image/width=960,format=auto/https://files.realpython.com/media/Python-Text-Parsing_Watermarked.5ac48b25acf2.jpg)
### reading :
```python
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

```

```python
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

```

```python
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

```

```python
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
```

```python
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
```

### Writing :
```python
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
```

```python
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
```

```python
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
```


txt
----

* **`"r"` Read Only.**
* **`"r+"` Read and Write.**
* **`"w"` Write Only.**
* **`"w+"` Write and Read.**
* **`"a"` Append Only.**
* **`"a+"` Append and Read.**

### reading :
```python
"""
txt file :

in the name of god
hellllllloooo
"""

file1 = open("a.txt","r")
print(file1.read())

>> "in the name of god"
   "hellllllloooo"
```

```python
"""
txt file :

in the name of god
hellllllloooo
"""

file1 = open("a.txt","r")
print(file1.readline())

>> "in the name of god"
```

### Writing :
```python
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
```


OS
----
**os has many built-in , and we don't need all of them , so visit this site for all built-in OS : https://www.w3schools.com/python/module_os.asp**


MySQL
----
![Monty Python](https://realpython.com/cdn-cgi/image/width=960,format=auto/https://files.realpython.com/media/MySQL-and-Python_Watermarked.4353d1d57493.jpg)
* **for the first download MySQL and run it.**
* **or use phpmyadmin and run it - you open phpmyadmin in the web and write code or use options in the web.**
* **pip install mysql-connector-python**
```python
import mysql.connector


mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername", # user="root",
  password="yourpassword" # password=""
)

print(mydb)

>> <mysql.connector.connection_cext.CMySQLConnection object at 0x000001CEE2E55D00>
```

**Creat database :**
```python
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
)

mycursor = mydb.cursor() # need for start

mycursor.execute("CREATE DATABASE mydatabase")
```

**all database :**
```python
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
)

mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)
```

**Creat table :**
```python
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
```

**show all tables :**
```python
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("SHOW TABLES")

for x in mycursor:
  print(x)
```

**Primary key :**
```python
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE family (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")

# When creating a table, you should also create a column with a unique key for each record.
# This can be done by defining a PRIMARY KEY.
# We use the statement "INT AUTO_INCREMENT PRIMARY KEY" which will insert a unique number for each record. Starting at 1, and increased by one for each record.
```

**ALTER TABLE :**
```python
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")
# If the table already exists, use the ALTER TABLE keyword:
```

**insert data :**
```python
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
mycursor.execute(sql, val)

mydb.commit() # It is required to make the changes, otherwise no changes are made to the table.


####################################################


import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = [
  ('Peter', 'Lowstreet 4'),
  ('Amy', 'Apple st 652'),
  ('Hannah', 'Mountain 21'),
  ('Michael', 'Valley 345'),
  ('Sandy', 'Ocean blvd 2'),
  ('Betty', 'Green Grass 1'),
  ('Richard', 'Sky st 331'),
  ('Susan', 'One way 98'),
  ('Vicky', 'Yellow Garden 2'),
  ('Ben', 'Park Lane 38'),
  ('William', 'Central st 954'),
  ('Chuck', 'Main Road 989'),
  ('Viola', 'Sideway 1633')
]

mycursor.executemany(sql, val)

mydb.commit()
```

**select all data in table :**
```python
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers")

# myresult = mycursor.fetchall() -> method, which fetches all rows from the last executed statement.

for x in mycursor:
  print(x)
```

**fetchone method in selecting :**
```python
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchone() #  fetchone method will return the first row of the result

print(myresult)
```

**Where :**
```python
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "SELECT * FROM customers WHERE address ='Park Lane 38'"

mycursor.execute(sql)

# myresult = mycursor.fetchall()

for x in mycursor:
  print(x)
```

**Like :**
```python
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "SELECT * FROM customers WHERE address LIKE '%way%'" # %  to represent wildcard characters

mycursor.execute(sql)

# myresult = mycursor.fetchall()

for x in mycursor:
  print(x)

####################################################

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "SELECT * FROM customers WHERE address = %s"
adr = ("Yellow Garden 2", )

mycursor.execute(sql, adr)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
```

**order by :**
```python
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "SELECT * FROM customers ORDER BY name" # Use the ORDER BY statement to sort the result in ascending or descending order.

mycursor.execute(sql)

for x in mycursor:
  print(x)

####################################################

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "SELECT * FROM customers ORDER BY name DESC" # Use the DESC keyword to sort the result in a descending order.

mycursor.execute(sql)

for x in mycursor:
  print(x)
```

**update :**
```python
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "UPDATE customers SET address = 'Canyon 123' WHERE address = 'Valley 345'"

mycursor.execute(sql)

mydb.commit() # It is required to make the changes, otherwise no changes are made to the table.
```

**limit :**
```python
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers LIMIT 5") # You can limit the number of records returned from the query, by using the "LIMIT" statement:

for x in mycursor:
  print(x)

####################################################

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers LIMIT 5 OFFSET 2") # If you want to return five records, starting from the third record, you can use the "OFFSET" keyword:

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
```
