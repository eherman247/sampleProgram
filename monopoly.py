# Name: Ethan Herman

# Checking if the player has all of the green properties.
group_prompt = input("Do you own all the green properties? (y/n)")
if(group_prompt == "N" or group_prompt == "n"):
    print("You cannot purchase a hotel until you own "
          "all the properties of a given color group.")
    quit()

# Checking the status of the current properties the player has.
pa_prompt = int(input(
    "What is on Pennsylvania Avenue? (0:nothing,:one house, ... 5:a "
    "hotel)")
)
if(pa_prompt == 5):
    print("You cannot purchase a hotel if the property already "
          "has one.")
    quit()
pc_prompt = int(input(
    "What is on Pacific Avenue? (0:nothing,:one house, ... 5:a hotel)")
)
if(pc_prompt == 5):
    print("Swap Pacific's hotel with Pennsylvania's 4 houses.")
    quit()
nc_prompt = int(input(
    "What is on North Carolina Avenue? (0:nothing,:one house, ... 5:a "
    "hotel)")
)
if(nc_prompt == 5):
    print("Swap North Carolina's hotel with Pennsylvania's 4 "
          "houses.")
    quit()

# Checking if there is a hotel availible to purchase.
hotels_prompt = int(input("How many hotels are there to purchase?"))
if(hotels_prompt == 0):
    print("There are not enough hotels availiable for purchase "
          "at this time.")
    quit()

# Checking to see if there are enough houses to purchase.
pa_house_need = 4 - pa_prompt
pc_house_need = 4 - pc_prompt
nc_house_need = 4 - nc_prompt
houses_needed = pa_house_need + pc_house_need + nc_house_need
houses_prompt = int(input("How many houses are there to purchase?"))
if(houses_needed > houses_prompt):
    print("There are not enough houses to purchase at this time.")
    quit()

# Checking if the player has enough funds for purchase(s).
cash_needed = houses_needed * 200 + 200
cash_prompt = int(input("How much cash do you have to spend?"))
if(cash_prompt < cash_needed):
    print("You do not have sufficient funds to purchase a hotel "
          "at this time.")
    quit()

# Displaying what the player needs to purchase, where it goes, and how
# much it will cost.
print("This will cost $" + str(cash_needed) + ".")
print("\tPurchase 1 hotel and " + str(houses_needed) + " house(s).")
print("\tPut 1 hotel on Pennsylvania and return any houses to the bank.")
if(nc_house_need):
    print("\tPut " + str(nc_house_need) + " house(s) on North Carolina.")
if(pc_house_need):
    print("\tPut " + str(pc_house_need) + " house(s) on Pacific.")
