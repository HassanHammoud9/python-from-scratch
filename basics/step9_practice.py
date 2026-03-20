# # STEP 9 PRACTICE: Lists
# # Type each exercise 3-4 times with different items

# # Exercise 9.1: Create a list
# colors = ["red", "blue", "green"]
# print(colors)

# # Exercise 9.2: Access specific items
# numbers = [10, 20, 30, 40]
# print(numbers[0])
# print(numbers[2])

# # Exercise 9.3: Add items to list
# shopping = ["milk"]
# shopping.append("bread")
# shopping.append("eggs")
# print(shopping)

# # Exercise 9.4: Loop through a list
# animals = ["cat", "dog", "bird"]
# for animal in animals:
#     print(animal)


players =["messi", "ronaldo", "neymar"]
for player in players:
    print(player)


players =["messi", "ronaldo", "neymar"]
for player in players:
    print(player, end=" ")


players =["messi", "ronaldo", "neymar"]
for player in players:
    print(", ".join(players))

players.append("robinho")
print(players)