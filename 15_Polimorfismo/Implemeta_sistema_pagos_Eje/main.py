from paypal import PayPal
from card import Card
from cash import Cash

def process_pay(payment_method, amount):
    return payment_method.make_pay(amount)

paypal_payment = PayPal("user@example.com")
card_payment = Card("1234567890123456")
cash_payment = Cash()

paypal_result = process_pay(paypal_payment, 100)
card_result = process_pay(card_payment, 50)
cash_result = process_pay(cash_payment, 30)

print(paypal_result)
print(card_result)
print(cash_result)
