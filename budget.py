from math import floor

class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.total = 0

    def deposit(self, amount, description = ""):
        self.ledger.append({"amount": amount, "description": description})
        self.total += amount
    
    def check_funds(self, expense):
        if self.total >= expense:
            return True
        else:
            return False

    def withdraw(self, amount, description = ""):
        if self.check_funds(amount):
            self.total -= amount
            self.ledger.append({"amount": -amount, "description": description})
            return True
        else:
            return False

    def get_balance(self):
        title = "*" * floor((30 - len(self.name)) / 2) + self.name + "*" * floor((30 - len(self.name)) / 2)

        table = title
        for action in self.ledger:
            line_new = '{:<15}  {:>12}'.format(action["description"], action["amount"])
            table += "\n" + line_new

        table += "\nTotal: " + str(self.total)

        return table

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.total -= amount
            self.ledger.append({"amount": -amount, "description": "Transfer to " + category.name})
            category.ledger.append({"amount": amount, "description": "Transfer from " + self.name})
            category.total += amount
            return True
        else:
            return False

def create_spend_chart(categories):
    pass


food = Category("Food")
clothing = Category("Clothing")
rent = Category("Rent")

food.deposit(100000, "initial deposit")
food.withdraw(20, "Get Breafast")
food.withdraw(20, "Get Lunch")
food.withdraw(20, "Get Dinner")
food.transfer(2000, rent)

rent.withdraw(100, "Pay for the month")
rent.transfer(100, clothing)

clothing.withdraw(100, "New Drip unlocked")

print(food.get_balance())
print(rent.get_balance())
print(clothing.get_balance())