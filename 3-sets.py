# lists are mutable, can be modified
# sets are mutable, can be modified, no duplicates allowed
# tuples are immutable, cannot be modified

friends = {"Bob", "Rolf", "Anne"}
abroad = {"Bob", "Anne"}
local = friends.difference(abroad)
print(local)

local = {"Rolf"}
abroad = {"Bob", "Anne"}
friends = local.union(abroad)
print(friends)

art = {"Bob", "Jen", "Rolf", "Charlie"}
science = {"Bob", "Jen", "Adam", "Anne"}
both = art.intersection(science)
print(both)
