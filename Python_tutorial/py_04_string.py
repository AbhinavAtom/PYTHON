# string concatenation
first_name = "Raja "
middle_name = "Ram "
last_name = "Mohan Roy"
full_name = first_name + middle_name + last_name
print(full_name)

#string length
print(len(""))
print(len(" "))
print(len("ramesh"))

#Python Sequence operators
# x in s                 Returns True if x exists somewhere in string s.
# x not in s             Returns True if x is not contained within string s.
# s * n or n * s         Repeats string s n times.
# s[i]                   The ith item of string s where the first character is 0.
# s[i:j]                 A slice from string x beginning with the character at position i through to the character at position j.
# s[i:j:k]               A slice of s from i to j with step k.
# min(s)                 The smallest (lowest) item of string s.
# max(s)                 The largest (highest) item of string s.
# s.index(x[, i[, j]])   The numeric position of the first occurrence of x in string s. The optional i and  j let you limit the search to the characters from i to j.
# s.count(x)             The total number of times string x appears in larger string s.

#-------------USES
s = "Abracadabra Hocus Pocus you're a turtle dove"
#Is there a lowercase t is contains in S?
print("t" in s)
#IS there an uppercase letter t is contains in S?
print("T" in s)
# Is there no uppercase T in s?
print("T" not in s)
# Print 15 hyphens in a row
print("-" * 15)
# Print first character in string X
print(s[0])
# Print characters 33 - 39 from string x
print(s[33:39])
# Print every third character in s starting at zero
print(s[0:44:3])
# Print lowest character is s (a sapce is lower than the letter a)
print(min(s))
# Print the highest character is s
print(max(s))
# # Where is the first uppercase p
# print(s.index("P")
# # Where is the first lowercase 0 in the letter half of string s
# #Note that the returned value still starts counting from zero
# # print(s.index("o",22,44))
# # How many lowercase letters a are in string s?
# # print(s.count("a"))

