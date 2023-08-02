# Prints the number of times "bob" appears in a string of lower case characters, s

s = 'azcbobobegghakl'

count = 0
if len(s) < len('bob'):
    print("Number of times bob occurs is: 0")
else:
    # Use len-2 so that we do not go out of bounds
    for char in range(len(s)-2):  
        if s[char] == 'b':
            if s[char+1] == 'o' and s[char+2] == 'b':
                count+=1
                char+=1
        char+=1
print("Number of times bob occurs is: " + str(count))
