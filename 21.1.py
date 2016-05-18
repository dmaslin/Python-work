from Map21_1 import Map

m = Map(4, .5)

m.put(26, "hello")
m.put(26, "world")
m.put(22,"I")
m.put(20, "love")
m.put(20, "using")
m.put(30, "python")

print("Entry set in map: " + str(m.items()))
print("The value for 26 is " + str(m.get(26)))
print("Is 6 in the map? " + str(m.containsKey(6)))
print("Is 26 in the map? " + str(m.containsKey(26)))
print("Is value \"Java\" in the map? " + str(m.containsValue("Java")))
print("Is value \"python\" in the map? " + str(m.containsValue("python")))
print("Is age \"python\" in the map? " + str(m.containsValue("python")))
print("All values for 26? " + str(m.getAll(26)))
print("keys are " + str(m.keys()))
print("values are " + str(m.values()))

m.remove(22)
print("The map is " + m.getTable())

m.clear()
print("The map is " + m.getTable())
