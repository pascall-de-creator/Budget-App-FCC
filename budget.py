from math import *

class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.total = 0
        self.total_expenditure = 0

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
    chart = "Percentage spent by category\n"
    percent = 100
    max_category_name = 0

    for category in categories:
        stats.append({"category": category.name, "percentage": int(round(category.total_expenditure / (category.total + category.total_expenditure) * 100, -1)) }) # round (10)

    while percent >= 0:
        chart += '{:>3}|'.format(percent)
        for bar in stats:
            if len(bar["category"]) > max_category_name:
                max_category_name = len(bar["category"])

            if bar["percentage"] >= percent:
                chart += ' o '

        chart += "\n"
        percent -= 10

    chart += "    " + "-" * (len(stats) ** 2 + 1)

    letter_index = 0
    while max_category_name >= letter_index:
        chart += "\n" + "    "
        for bar in stats:
            if len(bar["category"]) > letter_index:
                chart += " " + bar["category"][letter_index] + " "
            else:
                chart += "   "

        letter_index += 1

    return chart

food = Category("Food")
entertainment = Category("entertainment")
business = Category("business")

food.deposit(900, "deposit")
entertainment.deposit(900, "deposit")
business.deposit(900, "deposit")

food.withdraw(105.55)
entertainment.withdraw(33.40)
business.withdraw(10.99)

print(create_spend_chart([business, food, entertainment]))

# Percentage spent by category
# 100|
#  90|
#  80|
#  70|    o
#  60|    o
#  50|    o
#  40|    o
#  30|    o
#  20|    o  o
#  10|    o  o
#   0| o  o  o
#     ----------
#      B  F  E
#      u  o  n
#      s  o  t
#      i  d  e
#      n     r
#      e     t
#      s     a
#      s     i
#            n
#            m
#            e
#            n
#            t