# Sydney Ly | Lab 4 | Intro to Python


# Ticket 2
# Set up a control variable
keep_checking = "yes"

while keep_checking == "yes":
# Ask the user to enter an age
    print("Please enter in an age: ")
    age = input()
# Check if age is 13 or older and print the result
    if int(age) >= 13:
        print(f"{age}: Access granted!")
    else:
        print(f"{age}: Too young!")
# Ask if they want to check another age
    print("Would you like to check another age? ")
# Store their answer in keep_checking
    keep_checking = input().lower()

# Ticket 3


while True:
# Ask the user: enter an age or type "stop"
    answer = input("Enter an age or type 'stop': ")
# If they typed "stop", break out of the loop
    if answer.lower() == "stop":
        break
# Otherwise check the age and print the result
    elif int(answer) >= 13:
        print("Welcome back")
    else:
        print("Sorry, too young")

# Ticket 4
def can_access(age):
    if age >= 13:
        return True
    else:
        return False

ages = [17, 11, 25, 13, 9]

for age in ages:
    if can_access(age):
        print(f"{age}: Access granted!")
    else:
        print(f"{age}: Too young!")

# Ticket 5

signups = [22, 10, 15, 8, 19, 13]

def signup_report(ages):
    approved = 0
    print("--- StreamPass Signup Report ---")
    for number, age in enumerate(ages, start=1): 
                        # (1, 22), (2, 10), (3, 15) ...
        if can_access(age) == True: # if age >= 13:
            print(f"Signup #{number} | Age {age} - Access granted!")
            approved += 1 # approved = approved + 1
        else: # if age is less than 13
            print(f"Signup #{number} | Age {age} - Too young")
    print(f"Approved: {approved} out of {len(ages)}")

signup_report(signups)
    

            
            



