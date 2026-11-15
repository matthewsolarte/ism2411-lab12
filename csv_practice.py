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


# Exercise 4
print()
print("Exercise 4: totals")
total_revenue = 0
with open("data/sales.csv") as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        product = row[0]
        price = float(row[1])
        quantity = int(row[2])
        line_total = price * quantity
        total_revenue = total_revenue + line_total
        print(f"{product}: {quantity} units × ${price:.2f} = ${line_total:.2f}")
print(f"Total revenue: ${total_revenue:.2f}")


# Exercise 5
print()
print("Exercise 5: filter and write")
original_count = 0
written_count = 0
with open("data/sales.csv") as infile, open("data/cleaned.csv", "w", newline="") as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)
    next(reader)
    writer.writerow(["Product", "Price", "Qty", "Total"])
    for row in reader:
        original_count = original_count + 1
        price = float(row[1])
        quantity = int(row[2])
        line_total = price * quantity
        if line_total > 100:
            writer.writerow([row[0], f"{price:.2f}", quantity, f"{line_total:.2f}"])
            written_count = written_count + 1
print(f"Wrote {written_count} of {original_count} rows to data/cleaned.csv")
