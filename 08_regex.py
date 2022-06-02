# [a-zA-Z_]\w*
# A letter or underscore, followed by 0 or more letters, digits, or underscores
# a_variable_name -> match
# v -> match
# 9_variable -> would not match -> starts with a digit

# (1-)?[0-9]{3}-[0-9]{3}-[0-9]{4}
# A north american phone number with optional 1-prefix
# 1-905-721-8668 -> match
# 905-721-8668 -> match
# 9057218668 -> would not match -> needs dashes between number sets 

import re # imports regular expression package for Python

#define a regex -> recognize a name -> capital letter followed by 0 or more lowercase letters
# [A-Z][a-z]*
nameRE = re.compile('[A-Z][a-z]*')
match = nameRE.match('Walt Breslin')
print(match)
if match: #will execute if the string is a match
    print('Start: ', match.start())
    print('End: ', match.end())
    print('Text: ', match.group())
print('All names: ', nameRE.findall('Walt Breslin'))
print('All names: ', nameRE.findall('Joaquin El Chapo Guzman'))


# Regex used in a function 
def validate_name(name):
    nameRE = re.compile('[A-Z][a-z]*')
    match = nameRE.match(name)
    if match:
        print(match)
        return True
    print(match)
    return False
print(validate_name('Walt Breslin'))
print(validate_name('905-721-8668'))