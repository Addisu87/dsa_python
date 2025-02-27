   
# HT: Group Anagrams (⚡Interview Question)
# You have been given an array of strings, 
# where each string may contain only lowercase English letters.
# You need to write a function group_anagrams(strings) that groups the anagrams
# in the array together using a hash table (dictionary).
# The function should return a list of lists, 
# where each inner list contains a group of anagrams.

# "canonical" means the standardized or normalized form of a string 
# that can be used to compare it to other strings to see if they are anagrams.

def group_anagrams(strings):
   # create an empty hash table
   anagram_groups = {}
   
   # iterate through each string in the array
   for string in strings:
      # sort each string to get its canonical form
      # sorted("eat") returns ['a', 'e', 't']
      # "".join(['a', 'e', 't']) converts the array of chars to 'aet' string
      canonical = ''.join(sorted(string))
      
      # check to see if the canonical form of the string exists in the hash table
      if canonical in anagram_groups:
         # if it does then add the string there
         anagram_groups[canonical].append(string)
      else:
         # otherwise create new canonical form and add the string there
         anagram_groups[canonical] = [string]
   # convert the hash table to a list of lists
   return list(anagram_groups.values())

print("1st set:")
print( group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) )

print("\n2nd set:")
print( group_anagrams(["abc", "cba", "bac", "foo", "bar"]) )

print("\n3rd set:")
print( group_anagrams(["listen", "silent", "triangle", "integral", "garden", "ranged"]) )