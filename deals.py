deals = []

new_deal = input("enter a new deal or type done: ")
while new_deal != "done":
 if new_deal != "done":
   deals.append(new_deal)
   new_deal = input("enter a new deal or type done: ")

print("your deals:",deals)