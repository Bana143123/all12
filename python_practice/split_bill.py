def split_bill_evenly():
    total_amount = float(input("Enter the total amount of the bill: Rs "))
    num_people = int(input("Enter the number of people to split the bill: "))
    if num_people > 0:
        amount_per_person = total_amount / num_people
        print(f"Each person should pay: Rs.{amount_per_person:.2f}")
    else:
        print("The number of people must be greater than zero.")

split_bill_evenly()
