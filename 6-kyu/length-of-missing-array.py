def get_length_of_missing_array(arrays):
    try:
        o_list = sorted(len(x) for x in arrays)
        output = [o_list[i]+1 for i in range(len(o_list)-1) if o_list[i+1] - o_list[i] > 1]
        return output[0] if len(output) == 1 else 0
    except:
        return 0

'''
You get an array of arrays.
If you sort the arrays by their length, you will see, that their length-values are consecutive.
But one array is missing!

You have to write a method, that return the length of the missing array.

Example:
[[1, 2], [4, 5, 1, 1], [1], [5, 6, 7, 8, 9]] --> 3

If the array of arrays is null/nil or empty, the method should return 0.

When an array in the array is null or empty, the method should return 0 too!
There will always be a missing element and its length will be always between the given arrays
'''
