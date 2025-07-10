my_set={"apple", "banana", "cherry"}
for i in range(len(my_set)):
    print(list(my_set)[i])

my_set.add(input("Enter a new fruit to add: "))
my_set.remove(input("Enter a fruit to remove: "))
if "mango" in my_set:
    for item in my_set:
        print(item)