# Prints the number of vowels in a string with lower case characters, s
# Written by Danny

s = 'azcbobobegghakl'

count = 0
for char in s:
    if char=='a' or char=='e' or char=='i' or char=='o' or char=='u':
        count += 1
print("Number of vowels: " + str(count))
