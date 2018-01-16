from camel import DomesticCamel

camel1 = DomesticCamel(1)
camel2 = DomesticCamel(2)
camel3 = DomesticCamel(3)

my_camels = [camel1, camel3, camel2]

for camel in my_camels:
    print(camel.get_id())

my_cam = my_camels[0]

print(my_cam.get_id())

my_camels.sort(key=lambda camel: camel.get_id())

# sorted(my_camels, key=lambda camel: camel.get_id())

for camel in my_camels:
    print(camel.get_id())

print(my_cam.get_id())

del my_camels[0]

print(my_cam.get_id())