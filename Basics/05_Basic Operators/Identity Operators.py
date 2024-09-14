x = [1, 2, 3]
y = x
z = [1, 2, 3]
print(x is y)
# True (both x and y point to the same list)
print(x is not z)
 # True (x and z point to different lists, even though they have the same content)