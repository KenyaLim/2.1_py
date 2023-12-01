n = int(input("Enter the number of elements in the array: "))

array = []

for i in range(n):
    element = int(input(f"Enter element {i+1}: "))
    array.append(element)

print("The array is: ", array)