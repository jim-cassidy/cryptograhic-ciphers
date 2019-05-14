def get_element(elements, x, y):
    # Get element with two coordinates.
    return elements[x + (y * 26)]

def set_element(elements, x, y, value):
    # Set element with two coordinates.
    elements[x + (y * 26)] = value

# Create a list of 100 elements.
elements = []
for i in range(0, 1000):
    elements.append(0)

i = 0
for x in range(0, 26):
    for y in range(0, 26):
        # Set each element in the list to an incremented number.
	set_element(elements, x, y, i % 25)
        i += 1

print ( get_element( elements, 2,0 ))
