price = int(input())
good_credit_score = True
down_payment = 0

if good_credit_score: 
    down_payment = price * 0.1
else: 
    down_payment = price * 0.2
print(f"Down payment: ${down_payment}")