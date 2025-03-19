### Exercises: Level 1
#1
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
len(it_companies)
print("Length of the set:")

#2
it_companies.add('Twitter')
print(it_companies)

#3
it_companies.update(["Tesla","Amazon", "Kodak"])
print(it_companies)

#4
it_companies.remove("Apple")
print(it_companies)
                
#5
it_companies.discard("IBM")
print(it_companies)

### Exercises: Level 2
#1
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
union_set = A.union(B)
print("Union:", union_set)

#2
intersection_set = A.intersection(B)
print("Intersection:", intersection_set)

#3
is_subset = A.issubset(B)
print("Is A a subset of B?:", is_subset)

#4
are_disjoint = A.isdisjoint(B)
print("Are A and B disjoint sets?:", are_disjoint)

#5
A_union_B = A.union(B)
B_union_A = B.union(A)

#6
print("A joined with B:", A_union_B)
print("B joined with A:", B_union_A)

#7
symmetric_diff = A.symmetric_difference(B)
print("Symmetric Difference:", symmetric_diff)

#8
del A
del B

### Exercises: Level 3
age = [22, 19, 24, 25, 26, 24, 25, 24]

#1
ages_set = set(age)
length_list = len(age)
length_set = len(ages_set)

print("Length of the list:", length_list)
print("Length of the set:", length_set)

if length_list > length_set:
    print("The list is bigger.")
elif length_list < length_set:
    print("The set is bigger.")
else:
    print("They have the same length.")

#2
