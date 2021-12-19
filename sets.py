my_set = {1, 2, 3}
my_set2 = {"Hola ", "mundo", 3, 4, 5}

print(my_set.union(my_set2)) # my_set | my_set2
print(my_set.intersection(my_set2)) # my_set & my_set2
print(my_set.difference(my_set2)) # my_set - my_set2
print(my_set.symmetric_difference(my_set2)) # my_set ^ my_set2

# remove_duplicate = lambda some_list: list(set(some_list))