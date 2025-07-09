#this is about list concept in python
# list is a collection of items
# list is mutable, ordered, and allows duplicate elements
# list can contain different data types
my_list=["apple", 42, 3.14, True, "banana"]
print("My list:", my_list)
print("First item:", my_list[0])  # Accessing the first item
print("Last item:", my_list[-1])  # Accessing the last item
print("Items from index 1 to 3:", my_list[1:4])  # Slicing the list
print("Length of the list:", len(my_list))  # Length of the list
my_list.append("orange")  # Adding an item to the end of the list
print("List after appending:", my_list)
my_list.remove("banana")
print("List after removing 'banana':", my_list) 
my_list.insert(1, "kiwi")  # Inserting an item at index 1
print("List after inserting 'kiwi':", my_list)
my_list[2] = 100  # Modifying an item at index 2
print("List after modifying index 2:", my_list)
#loop in list
for item in my_list:
    print(item)
