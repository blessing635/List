#AHURIRA BLESSING
#WRITE A FUNCTION THAT TAKES A LIST OF NUMBERS AND RETURNS HOW MANY ARE ABOVE 50
#COMBINE FUNCTIONS AND LIST

def count_above_50(numbers):
    count = 0
    for number in numbers:
        if number > 50:
            count += 1
    return count
numbers = []
n = int(input("Enter the number of elements in the list: "))
for i in range(n):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)
result = count_above_50(numbers)

print(result)



