total=0
count=0
below_range=0
in_range=0
above_range=0
def calculate_average(total, count):
    return total/count
def classify(weight):
    if weight<148:
        return "below range"
    if weight>152:
        return"greater than range"
    else:
        return"in range"
number_soap=int(input("Enter the numnber of soaps:"))
for i in range(number_soap):
    weight=int(input("Enter the weight of the soap:"))
    total+=weight
    count+=1
    classification=classify(weight)
    print(classification)
    if classification=="below range":
        below_range+=1
    if classification=="greater than range":
        above_range+=1
    if classification=="in range":
        in_range+=1
print(f"Total weight:{total}g")
print(f"Avarage weight:{calculate_average(total,count)}g")
print(f"Below range:{below_range}")
print(f"In range:{in_range}")
print(f"Above range:{above_range}")