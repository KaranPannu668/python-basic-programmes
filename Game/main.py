from enemy import Enemy, Troll, Vampyre, VampyreKing

dracula = VampyreKing('Dracula')
print(dracula)

dracula.take_damage(12)
print(dracula)

# ugly_troll = Troll('Pug')
# print("Ugly troll - {}".format(ugly_troll))

# another_troll = Troll('Ug')
# print("Another troll - {}".format(another_troll))

# brother = Enemy('Urg')
# print(brother)

# ugly_troll.grunt()

# vamp = Vampyre('Vlad')
# print(vamp)
# vamp.take_damage(3)
# ugly_troll.take_damage(3)
# print(vamp)

# while vamp._alive:
#     vamp.take_damage(1)
    # print(vamp)