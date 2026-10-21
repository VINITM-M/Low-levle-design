class Splitwise:

    def __init__(self, members, expenses):
        self.members = members
        self.expenses = expenses

    def calculate_borrowers_and_lenders_balances(self):
        
        lenders = {}; borrowers = {} 
        member_balances = self.calculate_per_member_balances()
        
        for member, balance in member_balances.items():
            if balance > 0:
                lenders[member] = balance 
            elif balance < 0:
                # Keep borrower balances POSITIVE for easier math in the loop
                borrowers[member] = abs(balance)  
        return borrowers, lenders 
    
    def calculate_per_member_balances(self):
        each_share = self.calculate_per_member_share()
        balances = {}
        for member in self.members:
            expense_of_member = sum([x[1] for x in self.expenses if x[0] == member])
            balances[member] = round(expense_of_member - each_share, 2)
        return balances
    
    def calculate_per_member_share(self):
        if not self.members:
            return 0.0
        sum_of_expenses = float(sum(x[1] for x in self.expenses))
        return sum_of_expenses / len(self.members) 

    def split_expense(self):
        borrowers, lenders = self.calculate_borrowers_and_lenders_balances() 
        transactions = [] 

        for borrower, borrowed_amt in borrowers.items():
            # Round to prevent floating-point precision issues
            borrowed_amt = round(borrowed_amt, 2)
            
            while borrowed_amt > 0.01:  # Threshold to account for tiny rounding errors
                # Find the lender who is owed the most money
                lender = max(lenders, key=lenders.get)
                lenders_amt = round(lenders[lender], 2)
                
                if lenders_amt <= 0:
                    break

                # Determine how much can be paid right now
                amount_to_pay = round(min(borrowed_amt, lenders_amt), 2)

                # Execute transaction
                lenders[lender] = round(lenders[lender] - amount_to_pay, 2)
                borrowed_amt = round(borrowed_amt - amount_to_pay, 2)
                
                transactions.append([borrower, lender, amount_to_pay])
                
        return transactions