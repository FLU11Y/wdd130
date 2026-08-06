print("Enter a list of numbers, type 0 when finished.")

numbers = []
number = -1

while number != 0:
    number = int(input("Enter number: "))

    if number != 0:
        numbers.append(number)

# The list "numbers" now has all the numbers the user typed

# Step 1: Find the sum or total
sum = 0

for number in numbers:
    sum += number

print(f"The sum is: {sum}")

# Step 2: Find the average
# We can use the sum we just computed...
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
    # We will walk through the numbers again, this time keeping track
    # of the best so far, or the highest number to that point.

    best_so_far = numbers[0]

    for number in numbers[1:]:
        # Check if this number is larger than the best one we have seen so far
        if number > best_so_far:
            # This is the new best number, so save it to that variable
            best_so_far = number

    print(f"The largest number is: {best_so_far}")

    ########################
    # Enhancement
    ########################

    smallest_so_far = None

    for number in numbers:
        if number > 0 and (smallest_so_far is None or number < smallest_so_far):
            # We have a new smallest number
            smallest_so_far = number

    if smallest_so_far is None:
        print("The smallest positive number is: N/A")
    else:
        print(f"The smallest positive number is: {smallest_so_far}")

# Sorting the list
sorted_list = sorted(numbers)

print("The sorted list is:")
for number in sorted_list:
    print(number)