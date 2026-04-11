import random
secret_number= random.randint(1,10)
while True:
    guess=int(input("guess a number between 1 and 10: "))
    if guess== secret_number:
        print("correct")
        break #stops the loop
    else :
        print ("wrong! the number was",secret_number, "try again!")
