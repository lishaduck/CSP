def bill(total, tip_percent):
    tip = tip_percent / 100
    tip_amount = tip * total
    final_bill = total + tip_amount
    print("You're tip is: ", tip)
    print("Total bill is", final_bill)
    return final_bill


print(bill(25.56, 20))
