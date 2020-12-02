#the chr() function inside the loop just displays the ASCII character for whatever 
#the number in counter.
counter = 65
while counter < 91:
    print (str(counter) + "=" + chr(counter))
    counter += 1
print("all done")

#-----------------------------------------------
#while loop using continue
import random
print ("Odd Numbers")
counter = 0
while counter < 10:
    #Get a random number
    number = random.randint(1, 999)
    if int (number / 2) == number / 2:
        #If it's an even number, don't print it 
        continue
    #Otherwise, if it's odd, print it and increment the counter.
    print(number)
    #Increment the loop counter.
    counter += 1
print("Loop is done")


#----------------------------------------------
#while looping with break
import random
print("Numbers that aren't evenly divisible by 5")
counter = 0
while counter < 10:
        # Get a random number
        number = random.randint(1,999)
        if int(number / 5) == number / 5:
            # If it's evenly divisible by 5, bail out.
            break
        # Otherwise, print it and keep going for a while.
        print(number)
        # Increment the loop counter.
        counter += 1
print("Loop is done")
