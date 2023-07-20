# Adding elements to a list
my_list = [1, 2, 3]

# Adding a single element at the end
my_list.append(4)
print(my_list)  # Output: [1, 2, 3, 4]

# Adding multiple elements at the end
my_list.extend([5, 6])
print(my_list)  # Output: [1, 2, 3, 4, 5, 6]

# Adding an element at a specific index
my_list.insert(2, 'a')
print(my_list)  # Output: [1, 2, 'a', 3, 4, 5, 6]