class Category:
    def __init__(self,name):
        self.name = name
        self.ledger = []

    def deposit(self,amount,description = ''):
        self.ledger.append({
            'amount': amount,
            'description': description
        })

    def withdraw(self,amount,description = ''):
        if self.check_funds(amount):
            self.ledger.append({
                'amount': abs(amount) * -1,
                'description': description
            })
            return True
        return False

    def get_balance(self):
        return sum([
            value
            for entry in self.ledger
            for key, value in entry.items() if key == 'amount'
        ])

    def transfer(self,amount,destination):
        try:
            if self.check_funds(amount):
                self.withdraw(amount,f'Transfer to {destination.name}')
                destination.deposit(amount,f'Transfer from {self.name}')
            else:
                return False
        except Exception:
            return False
        else:
            return True

    def check_funds(self,amount):
        if amount <= self.get_balance():
            return True
        return False

    def __str__(self):
        result = f"{self.name[:30]:*^30}\n"
        for entry in self.ledger:
            result += f"{entry['description'][:23]:<23}{entry['amount']:>7.2f}\n"
        result += f'Total: {self.get_balance()}'
        return result

import math

def create_spend_chart(categories):
    output = 'Percentage spent by category\n'
    category_data = []
    max_name_len = 0
    spend_total = 0
    for category in categories:
        max_name_len = len(category.name) if len(category.name) > max_name_len else max_name_len
        withdraw_amount = abs(sum([
            value
            for entry in category.ledger
            for key, value in entry.items() if key == 'amount' and value < 0
        ]))
        spend_total += withdraw_amount
        category_data.append({
            'name': category.name,
            'withdraw_total': withdraw_amount
        })
    # display graph
    for row in range(100, -1, -10):
        data = ''
        elements = len(categories)
        for index, value in enumerate([value['withdraw_total'] for value in category_data]):
            percentage = 100 * value / spend_total
            data += ' o ' if percentage >= row else '   '
            if index == elements -1:
                data += ' '
        output += f"{row:>3}|{data}\n"
    output += f"    {'-' * len(data)}\n"

    for row in range(0,max_name_len):
        data = '    '
        for index, value in enumerate([value['name'] for value in category_data]):
            try:
                data += f" {value[row]} "
            except IndexError:
                data += '   '
        if index == elements -1:
            data += ' '
        output += data
        if row < max_name_len-1:
            output += '\n'
    return output

food = Category('Food')
food.deposit(1000, 'initial deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
print(food)

print(create_spend_chart([food,clothing]))