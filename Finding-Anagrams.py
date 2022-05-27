# Check if a word is an anagrams 
# Example:
# find_anagrams("hello") --> False
# find_anagrams("racecar") --> True


# Check if Two Strings are Anagrams of Each Other
def find_anagrams(str1, str2): 
    # [assignment] Add your code here
    strs1_anagram = sorted(str1)
    strs2_anagram = sorted(str2)
    
    if strs1_anagram == strs2_anagram:
        return True
    else:
        return False

find_anagrams("rescue", "secure")

