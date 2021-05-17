#looping through number
for x in range(7):
 print(x)
print("All done")

#from where to where
for x in range(1, 10):
 print(x)
print("All done")


#-------------------------------------------------
#looping through string
#method-01
for x in "snorkel":
 print(x)
print("Done")


#method-02
for i in 'python':
    print(i)
print("python printed")


#method-03
myName = "abhinav"
for i in myName:
    print(i)
print("All Done")

#-----------------------------------------------
#Looping through list
#method-01
for x in ["The", "rain", "in", "Spain"]:
 print(x)
print("Done")

#method-02
Visited = ["Kanpur", "Delhi", "Haryana", "Chandigarh", "Sri Nagar", "Ludiana", "Amritsar", "Agra"]
for x in Visited:
    print(x)
print("Done")


#--------------------------------------------------
#Bailing out of a loop
#try-01
answers = ["A", "C", "B", "D"]
for answer in answers:
    if answer == "":
        print("Incomplete")
        break
    print(answer)
print("Loop is done")

#try-02
answers = ["A", "C", "", "D"]
for answer in answers:
    if answer == "":
        print("Incomplete")
        break
    print(answer)
print("Loop is ok")

#--------------------------------------------------
#Looping with continue
answers = ["A", "C", "", "D"]
for answer in answers:
    if answer == "":
        print("Incomplete")
        continue
    print(answer)
print("Loop is done")

#--------------------------------------------------
#Nesting Loop

#outer loop
for outer in ["first", "Second", "third"]:
    print(outer)
    #inner loop
    for inner in range(3):
        print(inner+1)
print("both loops are done")
