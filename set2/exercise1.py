"""
Commenting skills:

TODO: above every line of code comment what you THINK the line below does.
TODO: execute that line and write what actually happened next to it.

See example for first print statement
"""
import platform

# I think this will print "hello! Let's get started" by calling the print function.
print("hello! Let's get started")  # it printed "hello! Let's get started"
#creates a list
some_words = ['what', 'does', 'this', 'line', 'do', '?']
#prints each word in the list
for word in some_words:
    print(word)
#Excludes first value
for x in some_words:
    print(x)
#prints the full list
print(some_words)
#tests to see if the list has more than three words
if len(some_words) > 3:
    print('some_words contains more than 3 words')
#gets operating system, computer name, operating system release, version and processor
def usefulFunction():
    """
    You may want to look up what uname does before you guess
    what the line below does:
    https://docs.python.org/3/library/platform.html#platform.uname
    """
    print(platform.uname())

usefulFunction()
