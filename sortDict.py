#Min, Max and Sorting the dictionary

groceries = {"Beer" : 99,
             "Cola" : 40,
             "Bread" : 15,
             "Lemon" : 10,
             "Coffee" : 400
             }

print(min(zip(groceries.values(), groceries.keys())))
print(max(zip(groceries.values(), groceries.keys())))
print(sorted(zip(groceries.values(), groceries.keys())))

print(min(zip(groceries.keys(), groceries.values())))
print(max(zip(groceries.keys(), groceries.values())))
print(sorted(zip(groceries.keys(), groceries.values())))
