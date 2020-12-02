username = "Alan"
print(f"Hello {username}")

unit_price = 49.99
quantity = 30
print(f"Subtotal: ${quantity * unit_price}")

#To show commas in thousands places, use a comma in your format string right after the colon
unit_price = 49.99
quantity = 30
print(f"Subtotal: ${quantity * unit_price:,}")

#To get the pennies to show as two digits, follow the comma with .2f
unit_price = 49.99
quantity = 30
print(f"Subtotal: ${quantity * unit_price:,.2f}")


#--------------------------------------------
sales_tax_rate = 0.065
print(f"Sales Tax Rate {sales_tax_rate}")

sales_tax_rate = 0.065
print(f"Sales Tax Rate {sales_tax_rate:.2%}")

sales_tax_rate = 0.065
sample1 = f'Sales tax Rate {sales_tax_rate:.2%}'
sample2 = f"Sales Tax Rate {sales_tax_rate:.2%}"
sample3 = f"""Sales Tax Rate {sales_tax_rate:.2%}"""
sample4 = f'''Sales Tax Rate {sales_tax_rate:.2%}'''
print(sample1)
print(sample2)
print(sample3)
print(sample4)


#multiline formatted string  
#method_1
user1 = "Alberto"
user2 = "Babs"
user3 = "Carlos"
output=f"{user1} \n{user2} \n{user3}"
print(output)
#method_2
unit_price = 49.96
quantity = 32
sales_tax_rate = 0.065
subtotal = quantity * unit_price
sales_tax = sales_tax_rate * subtotal
total = subtotal + sales_tax
output = f"""
Subtotal:  ${subtotal:,.2f}
Sales Tax: ${sales_tax:,.2f}
Total:     ${total:,.2f}
"""
print(output)


#Formatting width and alignment
# for left align <  
# for center align ^
# for right align >
unit_price = 49.96
quantity = 32
sales_tax_rate = 0.065
subtotal = quantity * unit_price
sales_tax = sales_tax_rate * subtotal
total = subtotal + sales_tax
output = f"""
Subtotal:  ${subtotal:>9,.2f}
Sales Tax: ${sales_tax:>9,.2f}
Total:     ${total:>9,.2f}
"""
print(output)
#..........doller aligning
unit_price = 49.96
quantity = 32
sales_tax_rate = 0.065
subtotal = quantity * unit_price
sales_tax = sales_tax_rate * subtotal
total = subtotal + sales_tax
#format amount to show as string with leading dollar sign
s_subtotal = "$" + f"{subtotal:,.2f}"
s_sales_tax = "$" + f"{sales_tax:,.2f}"
s_total = "$" + f"{total:,.2f}"
#output the string with dollar sign already attached
output = f"""
Subtotal:  {s_subtotal:>9}
Sales Tax: {s_sales_tax:>9}
Total:     {s_total:>9}
"""
print(output)