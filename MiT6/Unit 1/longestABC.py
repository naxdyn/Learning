# Prints the longest substring that is in alphabetical order

s = 'azcbobobegghakl'

count = 0

if len(s) == 0:
    print("error")
else:
    longest = s[0]
    for i in range(len(s)):
        # checks if the current longest string is longer than the remainder of the string left to check to end early
        if len(longest) > len(s[i:]):
            break
        for j in range(len(s[i:])):
            if 

    


