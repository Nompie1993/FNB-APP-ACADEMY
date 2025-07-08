#sets

my_set = {1, 2, 3, 4, 5}  # Creating a set with unique elements
print(my_set)  # Output: {1, 2, 3, 4, 5}

# Adding an element to the set
my_set.add(6)       
print(my_set)  # Output: {1, 2, 3, 4, 5, 6} 
# Removing an element from the set
my_set.remove(3)    
print(my_set)  # Output: {1, 2, 4, 5, 6}
# Checking if an element is in the set
print(2 in my_set)  # Output: True
# Iterating through the set
for element in my_set:
    print(element)  # Output: 1, 2, 4, 5, 6 (order may vary)
    
    set1={1, 2, 3 }
set2={3, 4, 5 }
# Union of two sets 
set_union = set1.union(set2)
print(set_union)  # Output: {1, 2, 3, 4, 5}
# Intersection of two sets      
set_intersection = set1.intersection(set2)
print(set_intersection)  # Output: {3}
# Difference of two sets
set_difference = set1.difference(set2)
print(set_difference)  # Output: {1, 2}