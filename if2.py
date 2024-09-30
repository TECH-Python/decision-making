...

 There are 3 labs in the CSE department. The labs are L1, L2, and L3 with a seating capacity of x, y, and z respectively. A single lab needs to be allocated to a class of 'n' students. The labs need to be utilized to the maximum i.e the number of systems used should not be minimal. Which lab needs to be allocated to this class?
Input format:
Input consists of 4 integers
The first input denotes 'x'
The second input denotes 'y'
The third input denotes 'z'
The fourth input denotes 'n'
Output format:
Print the lab which is suitable for  'n' number of students
Refer the Sample output for formatting
Sample Input:
30
40
20
25
Sample Output:
L1

...
def lab(capacity_L1, capacity_L2, capacity_L3, num_students):
    suitable_labs = []
    if capacity_L1 >= num_students:
        suitable_labs.append(("L1", capacity_L1))
    if capacity_L2 >= num_students:
        suitable_labs.append(("L2", capacity_L2))
    if capacity_L3 >= num_students:
        suitable_labs.append(("L3", capacity_L3))
    if suitable_labs:
       labs.sort(key=lambda x: x[1], reverse=True)
        return labs[0][0]  # Return the lab name with max capacity
    else:
        return "No suitable lab"
capacity_L1 = int(input())
capacity_L2 = int(input())
capacity_L3 = int(input())
num_students = int(input())
result_lab = lab(capacity_L1, capacity_L2, capacity_L3, num_students)
print(result_lab)
