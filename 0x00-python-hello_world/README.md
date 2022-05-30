0x00. Python - Hello, World
0. Run Python file mandatory
Write a Shell script that runs a Python script.

The Python file name will be saved in the environment variable $PYFILE

1. Run inline mandatory
Write a Shell script that runs Python code.

The Python code will be saved in the environment variable $PYCODE

2. Hello, print mandatory
Write a Python script that prints exactly "Programming is like building a multilingual puzzle, followed by a new line.

3. Print integer mandatory
Complete this source code in order to print the integer stored in the variable number, followed by Battery street, followed by a new line.

You can find the source code here
#!/usr/bin/python3
number = 98
# YOUR CODE GOES HERE. PLEASE REMOVE THIS LINE
The output of the script should be: the number, followed by Battery street, followed by a new line
You are not allowed to cast the variable number into a string
Your code must be 3 lines long
You have to use the new print numbers tips (with .format(...))

    C is strongly typed… not in Python! The variable number can be assigned to a string, a float, a bool etc… Forcing the type during a string format ("...".format(...)) is a way to control the type of a variable
4. Print float mandatory
Complete the source code in order to print the float stored in the variable number with a precision of 2 digits.

You can find the source code here
#!/usr/bin/python3
number = 3.14159
# YOUR CODE GOES HERE. PLEASE REMOVE THIS LINE
The output of the program should be: Float:, followed by the float with only 2 digits followed by a new line
You are not allowed to cast number to string
You have to use the new print formatting tips (with .format(...))

5. Print string mandatory
Complete this source code in order to print 3 times a string stored in the variable str, followed by its first 9 characters.

6. Play with strings mandatory
Complete this source code to print Welcome to Holberton School!


#!/usr/bin/python3
str1 = "Holberton"
str2 = "School"
# YOUR CODE GOES HERE. PLEASE REMOVE THIS LINE
print("Welcome to {}!".format(str1))

7. Copy - Cut - Paste mandatory
Complete this source code

#!/usr/bin/python3
word = "Holberton"
# YOUR CODE GOES HERE. PLEASE REMOVE THIS LINE
print("First 3 letters: {}".format(word_first_3))
print("Last 2 letters: {}".format(word_last_2))
print("Middle word: {}".format(middle_word))
You can find the source code here
You are not allowed to use any loops or conditional statements
Your program should be exactly 8 lines long
word_first_3 should contain the first 3 letters of the variable word
word_last_2 should contain the last 2 letters of the variable word
middle_word should contain the value of the variable word without the first and last letters

8. Create a new sentence mandatory
Complete this source code to print object-oriented programming with Python, followed by a new line.

#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
# YOUR CODE GOES HERE. PLEASE REMOVE THIS LINE
print(str)
You can find the source code here
You are not allowed to use any loops or conditional statements
Your program should be exactly 5 lines long
You are not allowed to create new variables
You are not allowed to use string literals

9. Easter Egg mandatory
Write a Python script that prints “The Zen of Python”, by TimPeters, followed by a new line.

Your script should be maximum 98 characters long (please check with wc -m 9-easter_egg.py)
guillaume@ubuntu:~/py/0x00$ ./9-easter_egg.py
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
guillaume@ubuntu:~/py/0x00$
10. Linked list cycle mandatory
Technical interview preparation:

You are not allowed to google anything
Whiteboard first
This task and all future technical interview prep tasks will include checks for the efficiency of your solution, i.e. is your solution’s runtime fast enough, does your solution require extra memory usage / mallocs, etc.
Write a function in C that checks if a singly linked list has a cycle in it.

Prototype: int check_cycle(listint_t *list);
Return: 0 if there is no cycle, 1 if there is a cycle
Requirements:

Only these functions are allowed: write, printf, putchar, puts, malloc, free
carrie@ubuntu:~/0x00$ cat lists.h

    Solving a problem is already a big win! but finding the best and optimal way to solve it, it’s way better! Think about the most optimal / fastest way to do it.
11. Hello, write #advanced
Write a Python script that prints exactly and that piece of art is useful - Dora Korpar, 2015-10-19, followed by a new line.

12. Compile #advanced
Write a script that compiles a Python script file.

The Python file name will be stored in the environment variable $PYFILE

The output filename has to be $PYFILEc (ex: export PYFILE=my_main.py => output filename: my_main.pyc)

13. ByteCode -> Python #1 #advanced
Write the Python function def magic_calculation(a, b): that does exactly the same as the following Python bytecode:


  3           0 LOAD_CONST               1 (98)
              3 LOAD_FAST                0 (a)
              6 LOAD_FAST                1 (b)
              9 BINARY_POWER
             10 BINARY_ADD
             11 RETURN_VALUE
Tip Python bytecode
