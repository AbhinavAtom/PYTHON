#Define a new class Member


# Creating an instance from a class
class Member:
    """ Create a new member. """
    def __init__(self, uname, fname):
        #Define attributes and give them avalues
        self.username = uname
        self.fullname = fname

#The class end at the first un-indented line.

#Create an instance of the Member class named new_guy
new_guy = Member('Rombo', 'Rocco Moe')

#See what's  in the instance, as well as its individual properties.
print(new_guy)
print(new_guy.username)
print(new_guy.fullname)
print(type(new_guy))


# Changing the value of an attribute
# Change new_guy's user name then print both attributes again.
new_guy.username = "Pricess"
print(new_guy.username)
print(new_guy.fullname)


# If you forget to import datetime at the top of the code, you’ll get an error message
# when you run the code telling you it doesn’t know what dt.date.today() means.
# Just add the import line to the top of the code and try again.

