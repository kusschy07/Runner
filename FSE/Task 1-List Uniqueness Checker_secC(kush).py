items = ["apple", "banana", "orange", "apple", "mango"]


for item in items:
    if items.count(item) > 1:
        print("Duplicate element found:", item)
        break
else:
    print("All elements are unique.")




