...
There are 3 labs in the CSE department are L1, L2, and L3 with a seating capacity of x, y, and z respectively. One of the 3 labs has been allocated for ACE training. Out of the available labs, find the lab which has minimal seating capacity.
Input format:
Input consists of 3 integers and a string
The first input denotes the seating capacity of L1(a)
The second input denotes the seating capacity of L2(b)
The third input denotes the seating capacity of L3(c)
The fourth input denotes the lab which is allocated for ACE training
Output format:
Print the minimal seating capacity lab amongst the available labs.
Refer the Sample output for formatting
Sample Input:
30
40
20
L3
Sample Output:
L1

...

# Function to find the lab with minimal seating capacity
def find_min_capacity_lab(capacity_L1, capacity_L2, capacity_L3, allocated_lab):
    # Create a dictionary to hold lab capacities
    labs = {
        "L1": capacity_L1,
        "L2": capacity_L2,
        "L3": capacity_L3
    }
    if allocated_lab in labs:
        del labs[allocated_lab]
    min_lab = min(labs, key=labs.get)  # Get the lab name with the minimum capacity
    return min_lab
capacity_L1 = int(input())
capacity_L2 = int(input())
capacity_L3 = int(input())
allocated_lab = input().strip()
result_lab = find_min_capacity_lab(capacity_L1, capacity_L2, capacity_L3, allocated_lab)

