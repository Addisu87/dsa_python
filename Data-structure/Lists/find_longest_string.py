# List: Find Longest String (⚡Interview Question)
# Write a Python function called find_longest_string that takes a list of strings
# as an input and returns the longest string in the list.


def find_longest_string(string_list):
   # Initialize the variable to store the longest string to an empty string
    longest_string = ""
   #  Loop through each string in the list of strings
    for string in string_list:
      #  Check if the length of the current string is greater than the
      # length of the current longest string
        if len(string) > len(longest_string):
            # If so, update the longest string to be the current string
            longest_string = string
    #  Return the longest string
    return longest_string


# Example
string_list = ['apple', 'banana', 'kiwi', 'pear']
longest = find_longest_string(string_list)
print(longest)  # expected output: 'banana'
