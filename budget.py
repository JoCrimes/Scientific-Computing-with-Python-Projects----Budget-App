class Category (object):
    def __init__ (self,name):
        self.name = name
        self.ledger = []
        self.balance = 0
        self.withdrawals = self.get_total_withdrawals()
    def deposit(self,amount,description=''):
        self.ledger = self.ledger + [{"amount":amount, "description":description}]
        #print("deposit: " + (str(amount)))
        return None
    def withdraw(self,amount,description=''):
        if (self.check_funds(amount) is True):
            self.ledger = self.ledger + [{"amount":-amount, "description":description}]
            #print("withdrawal: " + (str(amount)))
            return True
        else:
            #print("Insufficient funds!")
            return False
    def get_balance(self):
        self.balance = 0
        for entry in self.ledger:
            #print(str(i))
            self.balance += entry['amount']
        return self.balance
    def check_funds(self,amount):
        if (self.get_balance() >= amount):
            return True
        else:
            return False
    def transfer(self,amount,category):
        if self.withdraw(amount,"Transfer to "+category.name) is True:
            category.deposit(amount,"Transfer from "+str(self.name))
            return True
        else:
            return False
    def __str__(self):
        budget_str = ''
        #print(str(self.name).center(30, '*'))
        budget_str = str(self.name).center(30, '*')+'\n'
        for entry in self.ledger:
            #print(str(entry['description'])[:23])
            #print(str(entry['description'])[:23].ljust(23)+'{:.2f}'.format(entry['amount']).rjust(7))
            budget_str += str(entry['description'])[:23].ljust(23)+'{:.2f}'.format(entry['amount']).rjust(7)+'\n'
            #total += entry['amount']
        budget_str += 'Total: '+str(self.get_balance())
        return budget_str
    def get_total_withdrawals(self):
        total_withdrawals = 0
        for entry in self.ledger:
            if entry['amount'] < 0:
                #print(entry['amount'])
                total_withdrawals += entry['amount']
        return total_withdrawals

        
def create_spend_chart(categories):
    bar_graph = 'Percentage spent by category\n'
    y_axis = list(range(100,-10,-10))
    x_axis = ''
    dashes = '    -'
    names = [cat.name for cat in categories]
    withdrawals = [cat.get_total_withdrawals() for cat in categories]
    #tot_withdrawals = 0
    #tot_withdrawals = sum(withdrawals)
    percentages = [int(w/sum(withdrawals)*10)*10 for w in withdrawals]
    #print(str(sum(percentages)))
    if sum(percentages) > 100:
        print(str(max(percentages)))
    #p = [(w/sum(withdrawals)*100) for w in withdrawals]
    #print(str(p))
    #print(str(percentages))
    # Generate the numerical portion of the graph
    for y in y_axis:
        bar_graph += (str(y).rjust(3)+'|')
        for p in percentages:
            if p >= y:
                bar_graph += ' o '
            else:
                bar_graph += '   '
        bar_graph += ' \n'
    # Generate the x-axis
    # Find the longest name, store length in num_digits and name in longest
    num_digits = 0
    test = 0
    longest = ''
    for n in names:
        dashes += '---'
        test = len(n)
        if test > num_digits:
            num_digits = len(n)
            longest = n
    for i in range(num_digits):
        #print(str(i))
        x_axis += '\n     '
        for n in names:
            if i < len(n):
                x_axis += n[i] + '  '
            else:
                x_axis += '   '
        #x_axis += '\n'      
    bar_graph += dashes + x_axis
    #print(str(len(bar_graph)))
    return bar_graph.rstrip() + '  '