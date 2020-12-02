people = {
 'htanaka': 'Haru Tanaka',
 'ppatel': 'Priya Patel',
 'bagarcia': 'Benjamin Alberto Garcia',
 'zmin': 'Zhang Min',
 'afarooqi': 'Ayesha Farooqi',
 'hajackson': 'Hanna Jackson',
 'papatel': 'Pratyush Aarav Patel',
 'hrjackson': 'Henry Jackson'
 }
print(people)

#--------------------------------------------------
#length 
print(len(people))

#--------------------------------------------------
#access
print(people['zmin'])

#--------------------------------------------------
#check whether it is or not?
print('ppatel' in people)   #True
print('huzack' in people)   #False

#--------------------------------------------------
#getting with get()
print(people.get('papatel'))    #value
print(people.get('huzack'))     #None
print(people.get('huzack', 'Unbeknownst to this dictionary'))  # Unbeknownst to this dictionary

#--------------------------------------------------
#changing the value of key
people['hajackson'] = 'Hanna Jackson-Smith'     #got married
print(people['hajackson'])

#--------------------------------------------------
#updating
# Make a data dictionary named people.
people = {
 'papatel': 'Pratyush Aarav Patel',
 'hrjackson': 'Henry Jackson'
 }
# Change the value of the hrjackson key.
people.update({'hrjackson':'Henrietta Jackson'})
print(people)
# Update the dictionary with a new property:value pair.
people.update({'wwiggins':'Wanda Wiggins'})
print(people)

#--------------------------------------------------
# Looping through a Dictionary
for person in people:
    print(person)
print("---")
for person in people:
    print(people[person])
print("---")
for person in people.values():
    print(person)
print("---")
for key, value in people.items():
    print(key, "=", value)


                                        #Data Dictionary Methods
# clear()            Empties the dictionary by remove all keys and values.
# copy()             Returns a copy of the dictionary.
# fromkeys()         Returns a new copy of the dictionary but with only specified keys and values.
# get()              Returns the value of the specified key, or None if it doesn’t exist.
# items()            Returns a list of items as a tuple for each key-value pair.
# keys()             Returns a list of all the keys in a dictionary.
# pop()              Removes the item specified by the key from the dictionary, and stores it in a variable.
# popitem()          Removes the last key-value pair.
# setdefault()       Returns the value of the specified key. If the key does not exist: insert  the key, with the specified value.
# update()           Updates the value of an existing key, or adds a new key-value pair if the specified key isn’t already in the dictionary.
# values()           Returns a list of all the values in the dictionary


#------------------------------------------
#copy a dictionary :: newDictionaryName = dictionary.copy()
people = {
        'mkumar' : 'Manoj Kumar',
        'arajat' : 'Abhinav Rajat',
        'pranavat' : 'Pari Ranavat',
        'psingh' : 'Priya Singh'
}

people2 = people.copy()
print(people)
print(people2)

#------------------------------------------
# Deleting Dictionary Item

# Define a dictionary named people.
people = {
 'htanaka': 'Haru Tanaka',
 'zmin': 'Zhang Min',
 'afarooqi': 'Ayesha Farooqi',
 }
# Show original people dictionary.
print(people)
# Remove zmin from the dictionary.
del people["zmin"]      #if key not used then complete dictionary will be deleted
#Show what's in people now.
print(people)

# To remove all key-value pairs from a dictionary without deleting the entire
# dictionary, use the clear method with this syntax:
# dictionaryname.clear()

# Define a dictionary named people.
people = {
 'htanaka': 'Haru Tanaka',
 'zmin': 'Zhang Min',
 'afarooqi': 'Ayesha Farooqi',
 }
# Show original people dictionary.
print(people)
# Remove all data from the dictionary.
people.clear()
#Show what's in people now.
print(people)


#You can use pop() method
people = {
 'htanaka': 'Haru Tanaka',
 'zmin': 'Zhang Min',
 'afarooqi': 'Ayesha Farooqi',
 }
variable = people.pop("zmin")
print(variable)
print(people)

variable = people.pop("htanaka")
variable = people.popitem()

print(variable)
print(people)
#-----------------------------------------------------
#multiKey dictionary
product = {
 'name' : 'Ray-Ban Wayfarer Sunglasses',
 'unit_price' : 112.99,
 'taxable' : True,
 'in_stock' : 10,
 'models' : ['Black', 'Tortoise']
}
print('Name: ', product['name'])
print('Price: ',f"${product['unit_price']:.2f}")
print('Taxable: ',product['taxable'])
print('In Stock:',product['in_stock'])
print('Models:')
for model in product['models']:
 print(" " * 10 + model)           #The " " * 10 on the last line of code says to print a space (“ ”) ten times



#-----------------------------------------------------
#fromkey()
# Create a generic dictionary for products name product.
product = {
 'name': '',
 'unit_price': 0,
 'taxable': True,
 'in_stock': 0,
 'models': []
}
# Create a dictionary names DWC001 that has the same keys as product.
DWC001 = dict.fromkeys(product.keys())
#Show what's in the new dictionary.
print(DWC001)

#-----------------------------------------------------
#setdefault()
#Create a generic dictionary fro prodecut name product.
product = {
    'name' : '',
    'unit_price' : 0,
    'taxable' : True,
    'in_stock' : 0,
    'models' : []
}
# Create a dictionary for product SKU $DWC001
DCWC001 = dict.fromkeys(product.keys())
DWC001.setdefault('taxable', True)
DWC001.setdefault('model', [])
DWC001.setdefault('reorder_point', 100)

#Show whta's in the new dictionary.
print("Dictionary after fromkeys() and setdefalut()")
print(DWC001)

#Change the taxable fiels from None to True
print("|Dictionary after formkeys() and setdefault()")
DWC001['taxable'] = True

#Print the dictionary after changing taxable to True
print(DCWC001)

#---------------------------------------------
#Nesting Dictionary
#Create  generic dictionary to cinatin multiple product dictionaries
products = {
    'RB00111':{'name' : 'Rayban Sunglasses', 'price':11.98, 'models':['black', 'tortoise']},
    'DWC0317':{'name':'Drown with Camera', 'price':72.95, 'models' : ['white', 'black']},
    'MTS0540':{'name': 'T-shirt', 'price':2.96, 'models':['small', 'medium', 'long']} ,
    'ECD2989':{'name':'Echo Dot', 'price':29.99, 'models': []}
}
print(f"{'ID':<6} {' Name':<17} {'Price':>8} {' Models '}")
print('-' * 60)
#Loop throught each dicitonary in the products isctionary
for oneproduct in products.keys():
    #Get the id of one product.
    id = oneproduct
    #get the name of one product
    name = products[oneproduct]['name']
    #get the unit proce of one product and format with $
    unit_price ='$' + f"{products[oneproduct]['price']:,.2f}"
    #Crete and empty string variable name models
    models = ''
    #Loop through the models list and tack onto models
    #one item from the list followed by a comma and a space.
    for m in products[oneproduct]['models']:
        models += m + ', '
    #If the models variable is more than two characters in length,
    #Peel off the last two characters (last comma and space)
    if len(models) > 2:
        models = models[:-2]
    else:
        models = "<none>"
    #Print all the variables with a neat f-string
    print(f"{id:<6} {name:<17} {unit_price :>8} {models}")
