'''
A bouncy number is a positive integer whose digits neither increase nor decrease. For example,
1235 is an increasing number, 5321 is a decreasing number, and 2351 is a bouncy number.
By definition, all numbers under 100 are non-bouncy, and 101 is the first bouncy number.
To complete this kata, you must write a function that takes a number and determines if it is bouncy.

Input numbers will always be positive integers, but it never hurts to throw in some error handling : )

For clarification, the bouncy numbers between 100 and 125 are: 101, 102, 103, 104, 105, 106, 107, 108, 109, 120, and 121.
'''

def is_bouncy(number):
    if number<100:
        return False

    decreasing, increasing = False, False
    number = str(number)

    for x in range(len(number) - 1):
        if int(number[x]) < int(number[x+1]):
            decreasing = True

        elif int(number[x]) > int(number[x+1]):
            increasing = True

        if increasing and decreasing:
            return True

    return False

is_bouncy(92722983)
# Returns: True
