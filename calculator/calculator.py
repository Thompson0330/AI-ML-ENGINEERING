while True:
    try:
        first_number=float(input("num1: "))
        second_number=float(input("num2: "))
    except ValueError: 
        print("input a number")
        continue
    operator=input("operator: ")
    if operator=='+':
        result=first_number + second_number
    elif operator=='-':
        result=first_number - second_number
    elif operator=='x':
        result=first_number * second_number
    elif operator=='/':
        if second_number==0:
            print("cannot divide by 0")
            continue
        else:
            result=first_number / second_number
    else:
        print('not an operator')
        continue
    print (result)
