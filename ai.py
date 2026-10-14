total = 0
count = 0
below = 0
in_range_count = 0  # Renamed from 'range' to avoid shadowing Python's built-in range()
above = 0

def calculate_average(total, count):
    if count == 0:
        return 0
    return total / count

def classify(value):
    if value < 148:
        return "Below range"
    elif value > 152:
        return "Above range"
    else:
        return "In range"

number_soap = int(input("Enter the number of soap bars: "))

for _ in range(number_soap):
    weight = int(input("Enter the soap bar weight: "))
    total += weight
    count += 1
    
    result = classify(weight)
    print(result)
    
    # Count categories based on the returned classification
    if result == "Below range":
        below += 1
    elif result == "In range":
        in_range_count += 1
    elif result == "Above range":
        above += 1

print(f"Total weight: {total} g")
print(f"Average weight: {calculate_average(total, count)} g")
print(f"Below range: {below}")
print(f"In range: {in_range_count}")
print(f"Above range: {above}")