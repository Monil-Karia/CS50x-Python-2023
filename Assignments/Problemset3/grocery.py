from collections import Counter

# Prompt the user for items
print("Enter your grocery items, one per line (press control-d when finished):")
items = []
while True:
    try:
        item = input().strip().lower()
        items.append(item)
    except EOFError:
        break

# Count the number of times each item appears in the list
item_counts = Counter(items)

# Output the grocery list in all uppercase, sorted alphabetically by item,
# prefixing each line with the number of times the user inputted that item
print("Here is your grocery list:")
for item, count in sorted(item_counts.items()):
    print(f"{count} x {item.upper()}")
