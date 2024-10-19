
from core import *
from display_balances_with_changes import *

def history_of_balances(ledger: Ledger):
    tmp_ledger = Ledger()
        
    for transaction in ledger.transactions:
        before = tmp_ledger.clone()
        tmp_ledger.transactions.append(transaction)
        
        print(f"{transaction.date} {transaction.description}")
        print()
        display_balances_with_changes(before, tmp_ledger)
        print()
        # display_money_supply(tmp_ledger)
        # print()