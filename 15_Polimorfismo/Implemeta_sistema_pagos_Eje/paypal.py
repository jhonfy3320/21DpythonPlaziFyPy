from pay import Pay

class PayPal(Pay):
    def __init__(self, email):
        self.email = email

    def make_pay(self, amount):
        pay_info = super().make_pay(amount)
        pay_info["platform"] = "PayPal"
        pay_info["email"] = self.email
        return pay_info