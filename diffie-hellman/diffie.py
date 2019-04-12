def findroot(prootnum):
  ##prime = int(raw_input("Enter a prime number: "))
  prime = prootnum
  num_to_check = 0
  p_minus_1_range = range(1,prime)
  print "If you entered a large number (4+ digits) this could take a long time."
  print ""
  print "Working..."
  primitive_roots = []
  for each in range(1, prime):
	num_to_check += 1
	candidate_prim_roots = []
	for i in range(1, prime):
		modulus = (num_to_check ** i) % prime
		candidate_prim_roots.append(modulus)
		cleanedup_candidate_prim_roots = set(candidate_prim_roots)
		if len(cleanedup_candidate_prim_roots) == len(range(1,prime)):
			primitive_roots.append(num_to_check)
 # print "Primitive roots of %d are:" % prime
  print "-----------------------------------"
 # print primitive_roots,
  return primitive_roots


## main --------------------------------------------------------------

p = 23

primitiver = findroot(p)


g = primitiver[0]

print "p is : " , p
print "g is : " , g


## choose A and B
a = 4
b = 3

A = pow(g,a) % p
print (A)
B = pow(g,b) % p
print (B)

s1 = pow(B,a) % p
s2 = pow(A,b) % p

print "secret: " , s1
print "secret: " , s2






