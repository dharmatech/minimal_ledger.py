
from actions import *
from history_of_balances import *

# ----------------------------------------------------------------------
def issue_shares(ledger, date, issuer, buyer, quantity, price):
    add_transaction(ledger, date, f'issue shares: {issuer} -> {buyer}',
        f'{issuer}:equity:shares', -price * quantity,
        f'{buyer}:assets:shares',   price * quantity,

        f'{issuer}:assets:gold',    price * quantity,
        f'{buyer}:assets:gold',    -price * quantity,
    )



def buy_stock(ledger, date, buyer, seller, quantity, original_price, new_price):
    add_transaction(ledger, date, f'buy stock: {quantity} {buyer} <- {seller}',
        f'{buyer}:assets:gold',  -quantity * new_price,
        f'{seller}:assets:gold',  quantity * new_price,
        f'{seller}:income',      -quantity * (new_price - original_price),

        f'{seller}:assets:shares', -quantity * original_price,
        f'{buyer}:assets:shares',   quantity * new_price,
    )

# def dig_for_gold_(ledger, date, name, amount: float):
#     add_transaction(ledger, date, f'dig for gold: {name}',
#         f'{name}:revenue',     -(amount + amount * 0.2),
#         f'{name}:expenses',     (         amount * 0.2),
#         f'{name}:assets:gold', amount
#     )


# def dig_for_gold__(ledger, date, name, amount: float, expenses_percent: float = 0):
#     add_transaction(ledger, date, f'dig for gold: {name}',
#         f'{name}:revenue',     -(amount + amount * expenses_percent),
#         f'{name}:expenses',     (         amount * expenses_percent),
#         f'{name}:assets:gold', amount
#     )

def dig_for_gold(ledger, date, name, amount: float):
    add_transaction(ledger, date, f'dig for gold: {name}',
        f'{name}:revenue:mining', -amount,
        f'{name}:assets:gold',     amount
    )

def dig_for_gold_with_expenses(ledger, date, name, amount: float, expenses: float):
    add_transaction(ledger, date, f'dig for gold: {name}',
        f'{name}:revenue:mining',     -(amount + expenses),
        f'{name}:expenses:mining',               expenses,
        f'{name}:assets:gold',          amount
    )    




def deposit_gold(ledger, date, name, bank, amount):
    add_transaction(ledger, date, f'deposit gold {name} -> {bank} : {amount}',
        'person_a:assets:gold',      -amount,
        'bank:assets:reserves:gold',  amount,

        'bank:liabilities:deposits:person_a', -amount,
        'person_a:assets:deposits:bank',       amount
    )

def get_loan(ledger, date, name, bank, amount):
    add_transaction(ledger, date, f'get loan {bank} -> {name} : {amount}',
        f'{bank}:assets:reserves:gold',  -amount,
        f'{name}:assets:gold',            amount,

        f'{bank}:assets:loan:corp',       amount,
        f'{name}:liabilities:loan',      -amount,
    )
# ----------------------------------------------------------------------

ledger = Ledger()

# dig_for_gold__(ledger, '2021-01-01', 'person_a', 100)

# dig_for_gold__(ledger, '2021-01-01', 'person_a', 100, expenses_percent=0)

dig_for_gold(ledger, '2021-01-01', 'person_a', 100)

dig_for_gold_with_expenses(ledger, '2021-01-01', 'person_a', 100, 20)

history_of_balances(ledger)