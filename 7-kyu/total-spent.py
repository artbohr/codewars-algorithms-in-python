def getTotal(costs, items, tax):
    output = 0

    for x in items:
        output += costs.get(x, 0)

    return round((output * tax) + output,2)

'''
How much will you spend?

Given a dictionary of items and their costs and a array specifying the items
bought, calculate the total cost of the items plus a given tax.

If item doesn't exist in the given cost values, the item is ignored.

Output should be rounded to two decimal places.

Python:

costs = {'socks':5, 'shoes':60, 'sweater':30}
get_total(costs, ['socks', 'shoes'], 0.09)
#-> 5+60 = 65
#-> 65 + 0.09 of 65 = 70.85
#-> Output: 70.85
'''
