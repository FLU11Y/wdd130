print("Enter a list of numbers, type 0 when finished.")

numbers = []
number = -1

while number != 0:
    number = int(input("Enter number: "))

    if number != 0:
        numbers.append(number)

# Step 1: Find the sum or total
sum = 0

for number in numbers:
    sum += number

print(f"The sum is: {sum}")

# Step 2: Find the average

count = len(numbers)

if count == 0:
    print("No numbers were entered.")
    print("The average is: N/A")
    print("The largest number is: N/A")
    print("The smallest positive number is: N/A")
else:
    average = sum / count

    print(f"The average is: {average}")

 # Step 3: Find the max

    best_so_far = numbers[0]

    for number in numbers[1:]:
        if number > best_so_far:
            best_so_far = number

    print(f"The largest number is: {best_so_far}")

    smallest_so_far = None

    for number in numbers:
        if number > 0 and (smallest_so_far is None or number < smallest_so_far):
            smallest_so_far = number

    if smallest_so_far is None:
        print("The smallest positive number is: N/A")
    else:
        print(f"The smallest positive number is: {smallest_so_far}")

sorted_list = sorted(numbers)

print("The sorted list is:")
for number in sorted_list:
    print(number)