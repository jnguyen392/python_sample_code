"""
Exercise that takes as input a first, middle and last name and uses a function to print the results.

The following code features another example of function usage.
The function uses an OPTIONAL argument this time.

"""
def format(first, last, middle=''):
        if middle:
                full = f"{first} {middle} {last}"
        else:
                full = f"{first} {last}"
        return full.title()

user_001 = format('alice', 'cartman')
print(user_001)

user_002 = format('alice', 'cartman', 'lisa')
print(user_002)
