days=int(input("Enter the number of days:"))
heights=[]
for i in range(1,days+1):
    height=int(input(f"Enter the height in day {i}:"))
    heights.append(height)
for i in range(days):
    print(f"Day {i+1}:{heights[i]}cm")
first=heights[0]
last=heights[-1]
change=last-first

print(f"First height:{first}cm")
print(f"Last height:{last}cm")

print(f"Change:{change}cm")