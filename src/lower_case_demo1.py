"""
Given a string, implement a function that returns the string with all lowercase
characters.

Example 1:

Input: "LambdaSchool"
Output: "lambdaschool"

Example 2:

Input: "austen"
Output: "austen"

Example 3:

Input: "LLAMA"
Output: "llama"

*Note: You must implement the function without using the built-in method on
string objects in Python. Think about how character encoding works and explore
if there is a mathematical approach that you can take.*
"""
def to_lower_case(string):
    # Your code here
    # U - convert char to ascii 'a' = 97, 'b' = 98, so on.
    # Plan - how to tell if it's lowercase. ascii 97-122, all lowercase a-z. All uppercase is ascii 65-90. from a-z 77 + 32 = 109

    # create empty answer_string
    answer_string = ""
    # loop through each char of input_string
    for char in string:
        # for each char convert to ascii
        ascii_char = ord(char)
        # check if number is between 65 and 90
        if 65 <= ascii_char <= 90: 
            #  the letter is uppercase, so lets convert to lower
            lower_char_num = ascii_char + 32
            #  convert the new ascii num back to character
            lower_char = chr(lower_char_num)
            #  add lower_char to our answer_string
            answer_string += lower_char
        else:
            # add the character to answer_string
            answer_string += char

    return answer_string


print(to_lower_case('LambdaSchool'))
print(to_lower_case('LLAMA'))


    # if ascii < 90 .add(32)
    #     return ascii
    # ans = ""

    # for char >= 65 and char <= 90:
    #     newChar = ord(char) + 32
    #     ans += newChar

    # return ans
