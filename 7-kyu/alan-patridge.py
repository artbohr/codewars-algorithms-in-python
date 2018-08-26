def part(arr):
    ap = ["Partridge","PearTree","Chat","Dan","Toblerone","Lynn","AlphaPapa","Nomad"]

    result = sum([arr.count(x) for x in ap])

    if result == 0:
        return "Lynn, I've pierced my foot on a spike!!"
    else:
        return "Mine's a Pint{}".format('!' * result)

'''
To celebrate today's launch of my Hero's new book: Alan Partridge: Nomad,
 We have a new series of kata arranged around the great man himself.

Given an array of terms, if any of those terms relate to Alan Partridge, return Mine's a Pint!

The number of ! after the t should be determined by the number of Alan related terms you
find in the provided array (x). The related terms are:

Partridge
PearTree
Chat
Dan
Toblerone
Lynn
AlphaPapa
Nomad

If you don't find any related terms, return 'Lynn, I've pierced my foot on a spike!!'

All Hail King Partridge

Other katas in this series:
'''
