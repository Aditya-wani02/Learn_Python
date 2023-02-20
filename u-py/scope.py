# en=1
# def incen():
#     en =3
#     print(en)

# incen()
# print(en)

# Local scope
# def drink_potion():
#     potion_strength=3
#     print(potion_strength)

# drink_potion()


# Global Variable
# health = 10
# def drink_potion():
#     potion_strength=3
#     print(health+potion_strength)

# drink_potion()


# game_level = 1

# def create_enemy():
#     enemies =["Skeleton","Zombie","Alien"]
#     if game_level<2:
#         print(enemies[0])


# create_enemy()




# Manipulation of global variable in local scope

# en=1

# def incen():
#     global en  #this is added to change the global variable
#     en +=1
#     print(en)

# incen()
# print(en)

# global constants
PI=3.14159

def calc():
    print(PI+4)

calc()