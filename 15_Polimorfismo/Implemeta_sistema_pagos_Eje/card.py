from pay import Pay

class Card(Pay):
    def __init__(self, card_number):
        if len(card_number) != 16:
            raise Exception("La tarjeta debe tener 16 dígitos")
        self.card_number = card_number

    def make_pay(self, amount):
        pay_info = super().make_pay(amount)
        pay_info["last_card_numbers"] = self.card_number[-4:]
        return pay_info