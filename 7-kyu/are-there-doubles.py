def double_check(strng):
    strl = strng.lower()
    for i,x in enumerate(strl[:-1]):
        if x==strl[i+1]:
            return True
    return False

'''
Your job is to build a function which determines whether or not
 there are double characters in a string (including whitespace
 characters). For example aa, !! or .

You want the function to return true if the string contains double
 characters and false if not. The test should not be case sensitive;
 for example both aa & aA return true.

Examples:

  double_check("abca")
  #returns False

  double_check("aabc")
  #returns True

  double_check("a 11 c d")
  #returns True

  double_check("AabBcC")
  #returns True

  double_check("a b  c")
  #returns True

  double_check("a b c d e f g h i h k")
  #returns False

  double_check("2020")
  #returns False

  double_check("a!@€£#$%^&*()_-+=}]{[|\"':;?/>.<,~")
  #returns False
'''