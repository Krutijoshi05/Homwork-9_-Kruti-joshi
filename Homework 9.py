#Calculate the sum of the first n positive integers 
def calculate_sum(n):
    return n*(n+1)//2

#Calculate and print the sum for the first 10 positive integers 
sum_10 = calculate_sum(10)
print(f"The sum of the first 10 integers is: {sum_10}")

#Calculate and print the sum for the first 100 positive integers 
sum_100 = calculate_sum(100)
print(f"The sum of the first 100 positive integers is: {sum_100}")
