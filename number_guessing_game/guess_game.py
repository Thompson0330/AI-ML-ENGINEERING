import random
secret_number=random.randint(1,10)
while True:
    guess=int(input("guess what the actual number is: "))
    if 1<= guess <=10:
        if guess== secret_number:
            print("correct")
            break #stops the loop
        else:
            print ("wrong! try again")
    else:
        print("out of range")