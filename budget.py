from math import *

class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.total = 0
        self.total_expenditure = 0

    def __str__(self):
        title = "*" * floor((30 - len(self.name)) / 2) + self.name + "*" * floor((30 - len(self.name)) / 2)
        table = title

        for action in self.ledger:
            truncated_description = ""

            for ( index, letter ) in enumerate(action["description"]):
                if index + 1 <= 23:
                    truncated_description += letter

            line_new = '{:<23}{:>7}'.format(truncated_description, '{:.2f}'.format(action["amount"] + .00))
            table += "\n" + line_new

        table += "\nTotal: " + str(self.total)

        return table

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
            self.total_expenditure += amount
            self.ledger.append({"amount": -amount, "description": description})
            return True
        else:
            return False

    def get_balance(self):
        return self.total
    
    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.total -= amount
            self.total_expenditure += amount
            self.ledger.append({"amount": -amount, "description": "Transfer to " + category.name})

            category.ledger.append({"amount": amount, "description": "Transfer from " + self.name})
            category.total += amount
            return True
        else:
            return False
    
def create_spend_chart(categories):
    stats = []
    chart_percent = 100
    max_name_len = 0
    letter_index = 0
    total_spent = 0
    chart = "Percentage spent by category\n"

    for category in categories:
        stats.append({ "category": category.name, "amount_spent": category.total_expenditure }) 
        total_spent += category.total_expenditure

    while chart_percent >= 0:
        chart += '{:>3}|'.format(chart_percent)
        for bar in stats:
            if int(round(bar["amount_spent"] * 100 / total_spent)) >= chart_percent:
                chart += ' o '
            else:
                chart += '   '

            if len(bar["category"]) > max_name_len:
                max_name_len = len(bar["category"])

        chart += "\n"
        chart_percent -= 10

    chart += "    " + "-" * (len(stats) ** 2 + 1)

    while max_name_len >= letter_index:
        chart += "\n" + "    "
        for bar in stats:
            if len(bar["category"]) > letter_index:
                chart += " " + bar["category"][letter_index] + " "
            else:
                chart += "   "

        letter_index += 1

    return chart

food = Category("Food")
entertainment = Category("Entertainment")
business = Category("Business")

food.deposit(900, "deposit")
entertainment.deposit(900, "deposit")
business.deposit(900, "deposit")
food.withdraw(105.55)
entertainment.withdraw(33.40)
business.withdraw(10.99)

print(create_spend_chart([business, food, entertainment]))