# short circuit in py

a = 0 and 1/0 # what is the output? - having fun with py!
b = 1 or 1/0


print(a,b)

# an error:
"""ab = 1/0 and 0
print (ab)"""

# what about this?
c = 0 and 1
d = 0 or 1

print(c, d)

# And this
e = 1 and 2
f = 1 or 2

print(e, f)
