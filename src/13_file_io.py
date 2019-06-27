"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here: 

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file

# YOUR CODE HERE
with open('foo.txt', 'r') as f:
    read_data = f.read()
    print(read_data)

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE
with open('bar.txt', 'w') as f2:
    f2.write('People.. like to invent monsters and monstrosities. Then they seem less monstrous themselves.\n')
    f2.write(
        'Only death can finish the fight, everything else only interrupts the fighting.\n')
    f2.write('It is easy to kill with a bow, girl. How easy it is to release the bowstring and think, it is not I, it is the arrow. The blood of that boy is not on my hands. The arrow killed him, not I. But the arrow does not dream anything in the night.\n')

f3 = open('bar.txt', 'r')
read_again_data = f3.read()
print(read_again_data)
f3.close()

with open('bar.txt', 'rb') as f4:
    print(f4.read(30))
