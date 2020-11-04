"""
Author: The Last Minute Professor
Title: Sieve of Eratosthenes using Recursion
Description: To list all prime numbers till n
"""
import math
"""
Function name: primes

Input:
    n: the limit till which prime numbers are to be found
    numbers: the list of numbers
    i: prime number whose multiples are to be removed

Output:
    numbers: the list containing the prime numbers
"""
def primes(n,numbers,i):
    if i<=math.sqrt(n):
        #Remove the multiples of i available in the list
        for j in range(2*i,n+1,i):
            #Multiples of a prime number may be already deleted previously, so use exception handling
            try:
                numbers.remove(j)
            except:
                pass
        #Update i as the available prime number next to i
        i=numbers[numbers.index(i)+1]
        #Recursive function call with updated numbers list and i value
        primes(n,numbers,i)
    #Return the list of prime numbers
    return numbers
# Get the number till which you want to find the prime numbers as n
n=int(input("Enter the value of n:"))
# Create a list called numbers containing the values from 2 to n
numbers=[i for i in range(2,n+1)]
# Call the function to implement sieve of Eratosthenes and print the returned result
print(primes(n, numbers,2))


