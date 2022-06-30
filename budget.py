from math import *
class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.total = 0
        self.total_expenditure = 0

    def __str__(self):
        table = "*" * floor((30 - len(self.name)) / 2) + self.name + "*" * floor((30 - len(self.name)) / 2) # create title in table
        
        for action in self.ledger:
            truncated_description = ""
            # truncate action description
            for ( index, letter ) in enumerate(action["description"]):
                if index + 1 <= 23:
                    truncated_description += letter

            # align description and amount in tabular form        | convert integer to  decimal place float 
            line_new = '{:<23}{:>7}'.format(truncated_description, '{:.2f}'.format(action["amount"] + .00))
            table += "\n" + line_new

        # add total at the end
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
        # get category name and total_expenditure
        stats.append({ "category": category.name, "amount_spent": category.total_expenditure })
        total_spent += category.total_expenditure

    while chart_percent >= 0:
        chart += '{:>3}| '.format(chart_percent) # align percentage range
        for bar in stats:
            if int(round(bar["amount_spent"] * 100 / total_spent)) >= chart_percent: # determine height of bar
                chart += 'o  '
            else:
                chart += '   ' # prevent excess characters from wrapping to end

            if len(bar["category"]) > max_name_len:
                max_name_len = len(bar["category"]) # update longest category name 

        chart += "\n"
        chart_percent -= 10

    chart += "    " + "-" * (len(stats) ** 2 + 1) # add seperation of frequency and category based on num of categories

    while max_name_len >= letter_index:
        chart += "\n     "
        for bar in stats:
            if len(bar["category"]) > letter_index:
                chart += bar["category"][letter_index] + "  "
            else:
                chart += "   " # prevent category name from wrapping

        letter_index += 1

    return chart