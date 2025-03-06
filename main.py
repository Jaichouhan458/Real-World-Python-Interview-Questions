## Q1 -  h is a list find duplicates in it?

h = [45, 12, 12, 253, 45, 56, 253, 13]
v = set()  # Store found duplicates

for i in h:
    if h.count(i) > 1 and i not in v:  # Check if the element appears more than once
        print(i)
        v.add(i)  # Mark as seen
        
## Q2 - what is Deep copy and shallow copy and its differences?
## Ans - Check python notes list comprehension file.

## Q3 - what is Pickle files?
## Ans - Check python notes list comprehension file.

## Q4 - what is Python(oop)?
## Q5 - Difference between Abstraction method and encapsulation.
## Q6 - what is for loop and while loop and which is universal Loop?
## Q7 - h is a list find second largest no. in it?
        h = [45, 12, 12, 253, 45, 56, 253, 13]
        
        # Given list of numbers
h = [45, 12, 12, 253, 45, 56, 253, 13]

# Convert the list into a set to remove duplicate values
unique_numbers = set(h)  # {45, 12, 253, 56, 13}

# Sort the unique numbers in ascending order
sorted_numbers = sorted(unique_numbers)  # [12, 13, 45, 56, 253]

# Select the second last element, which is the second largest number
second_largest = sorted_numbers[-2]  # 56

# Print the result
print("Second Largest Number:", second_largest)