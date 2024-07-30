def sum(numbers):
    if not numbers:
        return 0
    remaining_sum = sum(numbers[1:])
    return numbers[0] + remaining_sum

numbers = [1,2,3,4,5,6]

Total_sum = sum(numbers)
print(Total_sum)
   
   
    