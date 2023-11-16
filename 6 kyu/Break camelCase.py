"""
Complete the solution so that the function will break up camel casing, using a space between words.

Example
"camelCasing"  =>  "camel Casing"
"identifier"   =>  "identifier"
""             =>  ""
"""


def solution(s):
    string = ""

    for letter in s:
        if letter.upper() == letter:
            string += " " + letter
        else:
            string += letter

    return string




x = solution("part LookTake")
print(x)

