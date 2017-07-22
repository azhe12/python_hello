# Define a procedure weekend which takes a string as its input, and
# returns the boolean True if it's 'Saturday' or 'Sunday' and False otherwise.
import random

def weekend(day):
    if day == 'Monday' or day == 'Saturday':
        return True
    else:
        return False


print weekend('Monday')
# >>> False

print weekend('Saturday')
# >>> True


for x,y in zip([1,2], [3,4]):
    print x,y

print zip([1,2], [3,4])
