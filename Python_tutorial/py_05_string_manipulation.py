# string method
# s.capitalize()        Returns a string with the first letter capitalized, the rest lowercase.
# s.count(x,[y.z])      Returns the number of times string x appears in string s. Optionally you can add y as
# a starting point and z as an ending point to search only a portion of the string.
# s.find(x,[y.z])       Returns a number indicating the first position at which string x can be found in string
# s. Optional y and z parameters allow you to limit the search to a portion of the string. Returns –1 if none found.
# s.index(x,[y.z])      Similar to find but returns a “substring not found” error if string x can’t be found in string y.
# s.isalpha()           Returns True if s is at least one character long and contains only letters (A-Z or a-z).
# s.isdecimal()         Returns True if s is at least one character long and contains only numeric characters (0-9).
# s.islower()           Returns True if s contains letters and all those letters are lowercase.
# s.isnumeric()         Returns True if s is at least one character long and contains only numeric characters (0-9).
# s.isprintable()       Returns True if string s contains only printable characters.
# s.istitle()           Returns True if string s contains letters and the first letter of each word is uppercase followed by lowercase letters.
# s.isupper()           Returns True if all letters in the string are uppercase.
# s.lower()             Returns s with all letters converted to lowercase.
# s.lstrip()            Returns s with any leading spaces removed.
# s.replace(x,y)        Returns a copy of string s with all characters x replaced by character y.
# s.rfind(x,[y,z])      Similar to find but searches backwards from the start of the string. If y and z are provided, searches backwards from position z to position y. Returns –1 if string x not found.
# s.rindex()            Same as .rfind but returns an error if the substring isn’t found.
# s.rstrip()            Returns string x with any trailing spaces removed.
# s.strip()             Returns string x with leading and trailing spaces removed.
# s.swapcase()          Returns string s with uppercase letters converted to lowercase and lowercase letters converted to uppercase.
# s.title()             Returns string s with the first letter of every word capitalized and all other letters lowercase.
# s.upper()             Returns string s with all letters converted to uppercase.

s1 = "there is no such word as schmeedledorp"
s2 = "  a b c  "
s3 = "ABC"
#Captialize first letter, the rest lowercase
print(s3.capitalize())
#Count the number of space in s1
print(s1.count(" "))
#Find the dot in s3
print(s3.find("."))
#Is s2 all lowercase letters
print(s2.islower())
#Convert s3 to all lowercase
print(s3.lower())
#String leading character from s2
print(s2.lstrip)
#String leading and trailing characters frim s2
print(s2.strip())
#Swap the cse of letters in s1
print(s1.swapcase())
#Show s1 in title case (initial caps)
print(s1.title)
#Show s1 uppercase
print(s1.upper())