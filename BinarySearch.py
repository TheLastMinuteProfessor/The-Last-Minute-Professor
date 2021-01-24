def binary_search(values,x,starting_index,ending_index):
    if(starting_index<=ending_index):
        middle_index=(starting_index+ending_index)//2
        if values[middle_index]==x:
            print("Element found at Index:",middle_index)
            return
        elif values[middle_index]<x:
            binary_search(values,x,middle_index+1,ending_index)
        else:
            binary_search(values,x,starting_index,middle_index-1)
    else:
        print("Element not found")
numbers=[int(x) for x in input("Enter the list of values separated by a comma").split(",")]
search=int(input("Enter the number to search:"))
binary_search(numbers,search,0,len(numbers)-1)
"""
Code Explained at 
https://www.youtube.com/watch?v=becSj9Kpm6U
"""    
