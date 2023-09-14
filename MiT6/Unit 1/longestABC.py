# Prints the longest substring that is in alphabetical order

s = 'abcdefghijklmnopqrstuvwxyz'


longest = s[0]
for i in range(len(s)-1):
    if s[i+1] >= s[i]:
        current = s[i] 
        j = i
        while(s[j+1] >= s[j]):
            current = current + s[j+1]
            j += 1
            i += 1
            if len(s[j:]) < 2: 
                break
        if len(current) > len(longest):
            longest = current
print("Longest substring in alphabetical order is: " + longest)            


