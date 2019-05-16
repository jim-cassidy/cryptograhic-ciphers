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
for x in range(0, 27):
    for y in range(0, 27):
        # Set each element in the list to an incremented number.
	set_element(elements, x, y, i % 26)
        i += 1


print ( get_element(elements, 1, 0 ) )
print ( "--- ")

phrase1 = "zest"
key = "aeys"

num = 4


let1 = phrase1[0]
let2 = key[0]

a =  ord(let1) - 97
b =  ord(let2) - 97

print a
print b

c = get_element ( elements, a , b )

print c


print ("************")

solution=[0 for i in range(10)]

for x in range(num):
    let1 = phrase1[x]
    let2 = key[x]
    a =  ord(let1) - 97
    b =  ord(let2) - 97
    print a
    print b
    solution[x] = get_element ( elements, a, b )
    
print ("here is solution")

for x in range(num):
    print chr(solution[x] + 97)
