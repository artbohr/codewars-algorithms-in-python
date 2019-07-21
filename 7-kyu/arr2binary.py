def arr2bin(arr):
    return False if len([x for x in arr if type(x)==int])!=len(arr) else bin(sum(arr))[2:]

'''
Given an array containing only integers, add all the elements and return the
 binary equivalent of that sum.

If the array contains any non-integer element (e.g. an object, a float, a
 string and so on), return false.

Note: The sum of an empty array is zero.

arr2bin([1,2]) == '11'
arr2bin([1,2,'a']) == False
'''
