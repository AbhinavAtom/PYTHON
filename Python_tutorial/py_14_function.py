# def function_name():

def hello():
    print("hello function")

hello()

#-----------------Commenting a function
def hello(): # Practice function
 """ A docstring describing the function """
 print('Hello')

 hello()

#----------------Passing Information to a Function
    #  Generic names (x, y, a, b, etc) don’t exactly help make your code easy to understand. So you’d
    # probably be better off using a more descriptive name, such as name or even user_name
def hello(user_name):
    print("hello " + user_name)

hello("Jarvis")
this_girl = 'Meghana'
hello(this_girl)

#-----------------Defining optional parameters with defaults
def hello(user = 'nobody'):
    print("Hello " + user)

hello("Alka")
hello()

#-----------------Passing multiple values to a function
def hello(fname, lname, datestring):
    print("Hello " + fname + " " + lname)
    print('The last meet was ' + datestring)

hello("Sabnam", "Anuragi", "23/06/2020")


#-----------------Passing multiple values to a function and using conditions
def hello(fname, lname, datestring=''):
    msg = 'hello' + fname + ' ' + lname
    if len(datestring) > 0:
        msg += ' you mentioned ' + datestring
    print(msg)

hello('Alan', 'Simpson', '12/31/2019')
print('Sammy', 'Schmeedledorp')


#-----------------Using keyword arguments (kwargs)
def hello (fname, lname, datestring):   
    msg = "Hello"  + fname + " " + lname 
    msg += " you mentioned " + datestring
    print(msg)

# Pass in in literal kwargs (identify each by parameter name)
hello(datestring='12/31/2019', lname="Simpson", fname="Alan")

# Pass in in kwargs from variables (identify each by parameter name)
appt_date = '12/30/2019'
last_name = 'Janda'
first_name = 'Kylie'
hello(datestring=appt_date, lname=last_name, fname=first_name)

#--------------------Passing multiple values in a list
# ..
# ..
# ..

#--------------------Passing in an arbitrary number of arguments
#  To pass in any number of arguments, use *args as the parameter name
# Whatever you pass in becomes a tuple named args inside the function. A tuple is
# an immutable list (a list you can’t change). So again, if you want to change things,
# you need to copy the tuple to a list and then work on that copy.

def sorter(*args):
    """ Pass in any number of arguments separated by commas
    Inside the function, they treated as a tuple named args """
    # The passed-in
    # Create a list from the passed-in tuple
    newlist = list(args)
    # Sort and show the list.
    newlist.sort()
    print(newlist)

sorter(1,2,3,88,0)

#------------------------Returning Values from Functions
def alphabetize(original_list=[]):
        """ Pass any list in square brackets, displays a string with items
        sorted """
        # Inside the function make a working copy of the list passed in.
        sorted_list = original_list.copy()
        # Sort the working copy.
        sorted_list.sort()
        # Make a new empty string for output
        final_list = ''
        # Loop through sorted list and append name and comma and space.
        for name in sorted_list:
            final_list += name + ', '
        # Knock of last comma space if final list is long enough
        final_list = final_list[:-2]
        # Return the alphabetized list.
        return final_list
        # The most common way to use 

random_list = ['McMullen', 'Keaser', 'Maier', 'Wilson', 'Yudt', 'Gallagher',
'Jacobs']
alpha_list = alphabetize(random_list)
print(alpha_list)


# ********************
def odd_even(num):
    return num%2

result = odd_even(8)
print(result)


#---------------------------Unmasking Anonymous Functions

def lower(anystring):
    """ Converts string to all lowercase """
    return anystring.lower()
print(lower('Abhinav'))


def lowercaseof(anystring):
            """ Converts string to all lowercase """
            return anystring.lower()

names = ['Adams', 'Ma', 'diMeola', 'Zandusky']
names.sort(key=lowercaseof)


names = ['Adams', 'Ma', 'diMeola', 'Zandusky']
names.sort(key=lambda anystring: anystring.lower())
print(names)

#you can use lambda function for currency notation
currency = lambda n : f"${n:,.2f}"

#Same as currency you can also use it for percentage
percent = lambda n : f"{n:.2%}"

#Creating a lambda function*******************
#Show number in currency format
currency = lambda n : f"${n:,.2f}"
#Show number in percent fomate
percent = lambda n : f"{n:.2%}"

#Test currency function
print(currency(99))
print(currency(123456789.09876543))

#Test percent function
print(percent(0.065))
print(percent(.5))

