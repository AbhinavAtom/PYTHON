#synatx of function 
# variablename = functioname(param,[param])
# abs(x)         Returns the absolute value of number x (converts negative numbers to positive)
# bin(x)         Returns a string representing the value of x converted to binary.
# float(x)       Converts a string or number x to a the float data type
# format(x,y)    Returns x formatted as directed by format string y. In modern Python you’re morelikely to use f-strings, as described later in this chapter
# hex(x)         Returns a string containing x converted to hexadecimal, prefixed with 0x.
# int(x)         Converts x to the integer data type by truncating (not rounding) the decimal point and any digits after it.
# max(x,y,z ...) Takes any number of numeric arguments and returns whichever one is the largest.
# min(x,y,z ...) Takes any number of numeric arguments and returns whichever one is the smallest.
# oct(x)         Converts x to an octal number, prefixed with 0o to indicate octal.
# round(x,y)     Rounds the number x to y number of decimal places.
# str(x)         Converts number x to the string data type.
# type(x)        Returns a string indicating the data type of x.


#these are built-in function (not need of import any module)
pi = 3.14159265357989
x = 488
y = -345.78833883
z = -999.99999
print(abs(z))
print(int(z))
print(int(abs(z)))
print(round(pi, 4))
print(bin(x))
print(hex(x))
print(oct(x))
print(max(pi, x, y, z))
print(min(pi, x, y, z))
print(type(pi))
print(type(x))
print(type(str(y)))
print(str(z))

#math module functions (you should import math module before use them)
import math
z = 81
print(math.sqrt(z))

# math.acos(x)      Returns the arc cosine of x in radians.
# math.atan(x)      Returns the arc tangent of x, in radians.
# math.atan2(y, x)  Returns atan(y / x), in radians.
# math.ceil(x)      Returns the ceiling of x, the smallest integer greater than or equal to x.
# math.cos(x)       Returns the cosine of x radians.
# math.degrees(x)   Converts angle x from radians to degrees.
# math.e            Returns the mathematical constant e  (2.718281 . . .)
# math.exp(x)       Returns e raised to the power x, where e is the base of natural logarithms.
# math.factorial(x) Returns the factorial of x.
# math.floor()      Returns the floor of x, the largest integer less than or equal to x.
# math.isnan(x)     Returns True if x is not a number, otherwise returns False.
# math.log(x,y)     Returns the natural logarithm of x to base y.
# math.log2(x)      Returns the base-2 logarithm of x.
# math.pi           Returns the mathematical constant pi (3.141592 . . .)
# math.pow(x, y)    Returns x raised to the power y.
# math.radians(x)   Converts angle x from degrees to radians.
# math.sin(x)       Returns the arc sine of x, in radians.
# math.sqrt(x)      Takes any number of numeric arguments and returns whichever one is the smallest.
# math.tan(x)       Returns the tangent of x radians.
# math.tau()        Returns the mathematical constant tau (6.283185 . . .).

pi = math.pi
e = math.e
tau = math.tau
x = 81
y = 7
z = -23234.5454
print(pi)
print(e)
print(tau)
print(math.sqrt(x))
print(math.factorial(y))
print(math.floor(z))
print(math.degrees(y))
print(math.radians(45))