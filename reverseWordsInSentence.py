'''
Given a string statement, reverse the words in the statement
Example:
Input - 'i like this program very much'
Output = 'much very program this like i'
'''
s      = "i like this program very much"
words  = s.split(' ')
string = []

# Iterate the split words and insert into list at Index 0
for word in words:
    string.insert(0, word)

# Join the list and print the string
print(" ".join(string))
