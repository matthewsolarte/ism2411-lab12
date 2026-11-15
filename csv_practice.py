# Reflection
#
# 1. In Excel I could open sales.csv, add a Total column, and filter for orders
#    over $100 by hand, which is quick for one file and easy to see. Python is
#    better when the same steps repeat, because the script runs the whole
#    extract, transform, and load the same way every time with no clicking.
#    Excel is better for quick looks and charts, Python is better for repeatable
#    and larger jobs.
#
# 2. A store closing out the cash register each night could use an append-mode
#    log, adding one line with the date and the day's sales. Append mode fits
#    because it keeps every past entry and only adds the new one, so the
#    history builds up over time and nothing gets overwritten.

import csv


# Exercise 1
# sales.csv was downloaded into the data/ folder.
# It has a header (product, price, quantity) and 12 data rows.


# Exercise 2
print("Exercise 2: raw rows")
with open("data/sales.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)


# Exercise 3
print()
print("Exercise 3: skip the header")
with open("data/sales.csv") as f:
    reader = csv.reader(f)
    header = next(reader)
    print("Header:", header)
    for row in reader:
        print(row)
