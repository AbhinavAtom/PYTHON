#  a tuple is a list, but after it’s defined you can’t change it. 

prices = (29.95, 9.98, 4.95, 79.98, 2.95)
print(len(prices))
print(prices.count(4.95))
print(4.95 in prices)

#Look whether it is there or not
look_for = 12345
if look_for in prices:
 position = prices.index(look_for)
else:
 position=-1
print(position)
#Loop through and display each item in the tuple.
for price in prices:
 print(f"${price:.2f}")




#   Any of the methods that alter data, or even just copy data, from a list cause an
#   error when you try them with a tuple. This incudes .append(), .clear(), .copy(),
#   .extend(), .insert(), .pop(), .remove(), .reverse(), and .sort(). In short,
#   a tuple makes sense if you want to show data to users without giving them any
#   means to change any of the information.