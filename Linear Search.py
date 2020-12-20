"""
Author: The Last Minute Professor
Explanation available at:

"""
numbers=[int(x) for x in input("Enter the list of values separated by a comma").split(",")]
search=int(input("Enter the number to search:"))
for i in range(len(numbers)):
    if numbers[i]==search:
        print("Element found at index",i)
        break
else:
    print("Element not found")
