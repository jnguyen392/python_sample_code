"""
Sample exercise from Chapter 8:

The following example code shows how to return a value via a function.
"""
def format_name(first_n, last_n):
        full_n = f"{first_n} {last_n}"
        return full_n.title()

musician = format_name('john', 'nguyen')
print(musician)
