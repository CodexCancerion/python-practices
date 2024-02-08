amount_to_pay = int(input('Enter amount to pay: '))
payment = int(input('Enter your payment: '))
change = payment - amount_to_pay

five_hundred = 0
one_hundred = 0
fifty = 0
twenty = 0
ten = 0
five = 0
peso = 0

while change != 0:
    if change > 500:
        five_hundred = change/500
        change %= 500
    if change > 100:
        one_hundred = change/100
        change %= 100
    if change > 50:
        fifty = change/50
        change %= 50
    if change > 20:
        twenty = change/20
        change %= 20
    if change > 10:
        ten = change/10
        change %= 10
    if change > 5:
        five = change/5
        change %= 5
    if change >= 1:
        peso = change/1
        change %= 1

print(f"Your change is: {payment-amount_to_pay}")
print(f"500: {five_hundred.__floor__()}")
print(f"100: {one_hundred.__floor__()}")
print(f"50: {fifty.__floor__()}")
print(f"20: {twenty.__floor__()}")
print(f"10: {ten.__floor__()}")
print(f"5: {five.__floor__()}")
print(f"1: {peso.__floor__()}")