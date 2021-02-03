"""
Program Explanation with Example
https://youtu.be/EbJMjLZmqiI
"""

a=[int(x) for x in input("Enter the list of values separated by a comma").split(",")]
n=len(a)
for i in range(n-1):
    print("Pass",i+1)
    for j in range(n-i-1):
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
        print(a)
print("Bubble Sort Result:",a)
