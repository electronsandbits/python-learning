# check_sentinel_DLL.py
# CS 1 class example by THC.
# Tests the Sentinel_DLL class.

from sentinel_DLL import Sentinel_DLL

def check_sentinel_DLL():
    # Make a linked list with Maine, Idaho, and Utah.
    l = Sentinel_DLL()
    l.append("Maine")
    l.append("Idaho")
    l.append("Utah")

    # Add Ohio after Idaho.
    node = l.find("Idaho")
    if node != None:
        print(node.get_data())
        l.insert_after(node, "Ohio")
    print(l)

    # Delete Idaho.
    if node != None:
        l.delete(node)
    print(l)

    # Empty out the list, one node at a time.
    while l.first_node() != None:
        l.delete(l.first_node())

    print(l)

check_sentinel_DLL()
