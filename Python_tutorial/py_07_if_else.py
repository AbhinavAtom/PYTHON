total = 100
sales_tax_rate = 0.065
taxable = True
if taxable:
 print(f"Subtotal : ${total:.2f}")
 sales_tax = total * sales_tax_rate
 print(f"Sales Tax: ${sales_tax:.2f}")
 total = total + sales_tax
print(f"Total : ${total:.2f}")


#else

import datetime as dt
#get the current date and time
now = dt.datetime.now()
#make a decision based on hour
if now.hour < 12:
    print("Good Morning")
else:
    print("Good afternoon")
print("I hope you are doing well!")


#elif

light_color = "green"
if light_color == "green":
 print("Go")
elif light_color == "red":
 print("Stop")
print("This code executes no matter what")

#elif and else

light_color = "yellow"
if light_color == "green":
 print("Go")
elif light_color == "red":
 print("Stop")
else:
 print("Proceed with caution")
print("This code executes no matter what")
