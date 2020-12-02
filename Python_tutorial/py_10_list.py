#integer list
marks = [20, 50, 44, 78, 84, 56, 88]
print(marks)
print(marks[0])

#string list
students = ["ramesh", "john", "himanshi", "lucy", "amit", "sbnm"]
print(students)
print(students[3]) #Stduents sub three

#  An easy way to make the code readable is to always use a plural for the list
# name (such as students, scores). Then you can use the singular name (student,
# score) for the variable name. 

#-------------------------------------------------------
#List in loop
members = ["anika", "anamika", "alaknanda", "aishwarya", "arohi", "ananya"]
for member in members:
    print(member)
print("Done!")

#--------------------------------------------------------
#Seeing whether a list contains an item
laptops = ["HP", "apple", "dell", "samsung", "zeus"]
    #is samsung is in the list
has_samsung = "samsung" in laptops
print(has_samsung)                 # print("samsung" in laptops)
    #is LG is in list
has_LG = "LG" in laptops
print(has_LG)

#--------------------------------------------------------
#Getting the length of a string
alphabets = ['a', 'b', 'c', 'd', 'e', 'y']
print(len(alphabets))



#--------------------------------------------------------
# Adding an item to the end of a list
hardwares = ["monitor", "mouse", "keyboard", "USB", "chip", "cable"]
hardwares.append("speakers")

new_hardware = hardwares.append("joystick")
print(hardwares)

#add when not already present
student_name = "Amanda"
#Add student_name but only if not already in the list.
if student_name in students:
 print (student_name + " already in the list")
else:
 students.append(student_name)
 print (student_name + " added to the list")

 #Add at any position on the list
 #use insert() method :: listname.insert(position, item)

 todo = ["walking", "driving", "planting", "gotoDelhi", "checkEmail"]
 newItem = todo.insert(2, "jumping")
 print(todo)
 print("done")

#--------------------------------------------------------
#Changing an item in a list

penColor = ["orange", "blue", "black", "red", "green"]
penColor[1] = "yellow"
print(penColor)
print("changed")

#--------------------------------------------------------
#Combining or merging lists

myColor = ["pink", "red", "yellow"]
yourColor = ["green", "orange", "blue"]
#add mycolor with yourcolor
yourColor.extend(myColor)
print(yourColor)
print("entended")

#--------------------------------------------------------
#removing or deleting an item from list

phones = ["oppo", "apple", "googlePlex", "vivo", "samsung", "motorola", "nokia"]
phones.remove("vivo")
print(phones)
print("removed!")

#remove from last
phones.pop()
print(phones)
print("Removed last item")

#remove from indivisual index
phones.pop(3)
print(phones)
print("removed index", 3)

#save your remove element before deletion
removingThis = phones.pop(2)
print(phones)
print("removed", removingThis)

#remove using del() method
del phones[1]
print(phones)
print("removed index", 1)

#clear entire list (list exist but empty list)
phones.clear()
print(phones)
print("cleared!")

#delete entire list
del phones
print("completely deleted phones list")

#-----------------------------------------------
# Finding an list item’s index
languages = ["hindi", "english", "tamil", "urdu", "panjabi", "hindi", "english"]
find_for = languages.index("hindi")
print("The first hindi is index " + str(find_for))
print("got it")

# Create a list of strings.
grades = ["C", "B", "A", "D", "C", "B", "C"]
# Decide what to look for
look_for = "F"
# See if the item is in the list.
if look_for in grades:
 # If it's in the list, get and show the index.
 print(str(look_for) + " is at index " + str(grades.index(look_for)))
else:
 # If not in the list, don't even try for index number.
 print(str(look_for) + " isn't in the list.")


#-----------------------------------------------
#sorting :: listname.sort()
students = ["prateek", "pooja", "poonam", "puskar", "pranjul"]
rollNumber = [11, 89, 23, 55, 67, 9, 1]
students.sort()
rollNumber.sort()
print(students)
print(rollNumber)

    # If your list contains strings with a mixture of uppercase and lowercase letters, 
    # and if the results of the sort don’t look right, try replacing .sort() with
    # .sort(key=lambda s:s.lower()) and then running the code again. 

villages = ["Shankhari", "harbuspur", "koriyan", "Bihupur", "Sajeti"]
# villages.sort()
villages.sort(key=lambda s:s.lower())
print(villages)

#sorting date
import datetime as dt
datelist = []
datelist.append(dt.date(2020, 3, 21))
datelist.append(dt.date(2018, 4, 1))
datelist.append(dt.date(2019, 10, 11))
datelist.append(dt.date(2001, 12, 25))
datelist.sort()
for date in datelist:
    print(f"{date:%m/%d/%Y}")

#sorting reverse order
vehicles = ["motoCycle", "truck", "bus", "van", "train", "e-riksha"]
vehicleNumber = [129, 878, 456, 354, 862, 465]
vehicles.sort(reverse = True)           #Z-A mode
vehicleNumber.sort(reverse = True)      
print(vehicles); print()
print(vehicleNumber)

#-----------------------------------------------
#reverse the string
objects = ["fan", "toy", "cooler", "ac"]
objects.reverse()          #just reverse
print(objects)


#-----------------------------------------------
#copy the list
# Create a list of strings.
names = ["Zara", "Lupe", "Hong", "Alberto", "Jake"]
# Make a copy of the list
backward_names = names.copy()
# Reverse the copy
backward_names.reverse()
# Print the list
print(names)
print(backward_names)


# append()       Adds an item to the end of the list.
# clear()        Removes all items from the list, leaving it empty.
# copy()         Makes a copy of a list.
# count()        Counts how many times an element appears in a list.
# extend()       Appends the items from one list to the end of another list.
# index()        Returns the index number (position) of an element within a list.
# insert()       Inserts an item into the list at a specific position.
# pop()          Removes an element from the list, and provides a copy of that item that  you can store in a variable.
# remove()       Removes one item from the list.
# reverse()      Reverses the order of items in the list.
# sort()         Sorts the  list in ascending order. Put reverse=True inside the parentheses to sort in descending order.