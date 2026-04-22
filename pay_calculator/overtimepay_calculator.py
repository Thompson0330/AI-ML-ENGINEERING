def get_gross_pay(hours, rate):
    # If hours are 40 or less, it's just a simple multiplication
    if hours <= 40:
        return hours * rate
    
    # Otherwise, calculate 40 hours + overtime (extra hours * rate * 1.5)
    overtime_hrs = hours - 40
    return (40 * rate) + (overtime_hrs * rate * 1.5)

# 1. Get user information
name = input("Enter name: ")
try:
    h = float(input("Enter Hours: "))
    r = float(input("Enter Rate: "))
    
    # 2. Calculate the pay using our function
    total_pay = get_gross_pay(h, r)
    
    # 3. Print the result clearly using an f-string
    print(f"{name}'s total pay for the month is ${total_pay:.2f}")

except ValueError:
    print("Error: Please enter numbers for hours and rate.")

    