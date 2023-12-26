# Get the number of elements from the user
num_elements = int(input("Enter the number of elements: "))

# Initialize an empty list to store the elements
user_list = []

# Loop to get elements from the user and add them to the list
for i in range(num_elements):
    # Get element from the user
    element = float(input(f"Enter element {i + 1}: "))

    # Add the element to the list
    user_list.append(element)

# Calculate the average of the values in the list
if num_elements > 0:
    average = sum(user_list) / num_elements
    print(f"\nList: {user_list}")
    print(f"Average: {average}")
else:
    print("Error: Number of elements should be greater than 0.")
