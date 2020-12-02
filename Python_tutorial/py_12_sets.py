# The difference between a set and a list is that the items in set have no specific order. 
# Even though you may define the set with the items in a certain order, none of the items get index numbers to identify their positions.

sample_set = {1.4, 6.55, 34.55, 67.12, 6.90}
sample_set.add(33.22)
print(sample_set)

# You can also add multiple items to a set using .update()
sample_set.update([88, 123.45, 2.98])
print(sample_set)

# You can copy a set.
# Define a set named sample_set.
sample_set = {1.98, 98.9, 74.95, 2.5, 1, 16.3}
# Show the whole set
print(sample_set)
# Make a copy and shoe the copy.
ss2 = sample_set.copy()
print(ss2)