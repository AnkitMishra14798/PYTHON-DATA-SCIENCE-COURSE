A = {1,2,3,4,5}
B = {4,5,6,7,8}
print(A | B)

print(A.union(B))

print(B.union(A))

#intercecction use '&' operator

print(A & B)

#set difference

A = {1,2,3,4,5}
B = {4,5,6,7,8}

print(A - B)

print(A.difference(B))

print(B-A)

#set symmetric difference

A = {1,2,3,4,5}
B = {4,5,6,7,8}

print(A^B)

print(A.symmetric_difference(B))