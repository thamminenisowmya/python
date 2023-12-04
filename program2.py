def compress_string(s):
    compressed_string = ""
    count = 1
    # Iterate through the character of the string
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
# If current character is the same as the previous one, increment
            count += 1
        else:
# If current character is different, append the previous character
            compressed_string += s[i-1] + str(count)
            count = 1
# Append the last character and count
    compressed_string += s[-1] + str(count)
    return compressed_string
# Input the string
input_string = input("enter a string:")
str1=sorted(input_string)
#call the function to compress the string
result = compress_string(str1)
#print the compressed string
print("compressed string:", result)