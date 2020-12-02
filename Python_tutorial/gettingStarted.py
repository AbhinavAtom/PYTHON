#Comment "you know !"
print ("hello")
print ("Abhinav's phone is cool.")
print ('Abhinav have a "cat" ')
print ('Mary\'s dog said "Woof".')
print ("Mary's dog said \"Woof\".")
print ("The old pond\nA frog jumped in,\nKerplunk!")

#data_type
print(1000)     #int
print(1.99999)  #float
print("anika")  #string
print(True)     #bool

#Arithmetic_operators
print(100+300)  #addition
print(300-100)  #subtraction
print(20*30)    #multiplication
print(10/5)     #division
print(7%2)      #modulus
print(3**2)     #exponent
print(11//5)    #floor division

#comparison_operator
print(3<8)      #less than 
print(3<=8)     #less than or equal to
print(3>8)      #greater than
print(3>=8)     #greater than or equal to
print(3==8)     #equal to
print(3!=8)     #not equal to
#----(is)
#----(is not)

#boolean_operator
num1 = 4
num2 = 0
if (2 > 3 and (num1 == num2)) :
    print("inside and")
elif (2>3 or (num1 > num2)):
    print("inside or")
elif (not (num1>num2)):
    print("inside not")

#variable_name
#1. start with number or underscore
_var = 89
print(_var )
#2.after the first letter you can use numbers, letters or underscore
v_ = 77
v2 = 90
vv = 45
print(v_ + v2 + vv)
#3. variables names are case sensitive
var = "john"
VAR = "sena"
print(var + VAR)
#4. variables names cannot be enclosed in single, double quotes
# "var" can't do this

#Using Semicolon for line break
var=1
var2 = 3
print(var + var2)

var = 1; var2 = 3
print(var + var2)

var1 = 1; var2 = 3; print(var + var2)