# creates empty set
s = set()

# add elements to set
s.add(1)
s.add(2)
s.add(3)
s.add(3)  # will not appear twice

s.remove(2)  # 2 will be removed from sets

print(s)

# len will show you how many elements you have in sets
print(f"the sets has {len(s)} elements")
