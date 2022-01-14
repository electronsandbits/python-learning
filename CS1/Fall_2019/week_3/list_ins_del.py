# list_ins_del.py
# CS 1 class example by THC to show how to insert into and delete from a list.

new_england = ["New Hampshire", "Connecticut", "Massachusetts",
               "Rhode Island", "Vermont", "Maine"]
print(new_england)

del new_england[1]  # removes Connecticut
print(new_england)

new_england.insert(3, "Newyorkachusetts")   # inserts before Vermont
print(new_england)

del new_england[1:4]    # removes Massachusetts, Rhode Island, and Newyorkachusetts
print(new_england)

new_england.insert(17, "New Brunswick")
print(new_england)
