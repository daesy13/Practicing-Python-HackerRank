# The re.sub() tool (sub stands for substitution) evaluates a pattern and, for each valid match, it calls a method (or lambda).
# The method is called for all matches and can be used to modify strings in different ways.
# The re.sub() method returns the modified string as an output.

# Learn more about re.sub().

import re

#Squaring numbers
def square(match):
    number = int(match.group(0))
    return str(number**2)

print re.sub(r "\d+", square, "1 2 3 4 5 6 7 8 9")