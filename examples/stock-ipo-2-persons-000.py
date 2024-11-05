
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

def dig_for_gold_(ledger, date, name, amount: float):
    add_transaction(ledger, date, f'dig for gold: {name}',
        f'{name}:revenue',     -(amount + amount * 0.2),
        f'{name}:expenses',    (amount * 0.2),
        f'{name}:assets:gold', amount
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

dig_for_gold_(ledger, '2021-01-01', 'person_a', 100)

deposit_gold(ledger, '2021-01-01', 'person_a', 'bank', 100)

# shares = 100

add_transaction(ledger, '2021-01-01', 'initial investment from investors',
    'corp:equity:original-investment', -100,
    'corp:assets:gold',                 100
)

get_loan(ledger, '2021-01-01', 'corp', 'bank', 50)

dig_for_gold_(ledger, '2021-01-01', 'corp', 100)

def book_value(ledger, name):
    assets      = ledger_all_account_with_values(ledger)[f'{name}:assets']
    liabilities = ledger_all_account_with_values(ledger)[f'{name}:liabilities']

    return assets - (-liabilities)

# book_value(ledger, 'corp')

# shares / book_value(ledger, 'corp')

# price per share of original investors:

# shares / ledger_all_account_with_values(ledger)['corp:equity:original-investment']

# new_shares = 100

# book_value(ledger, 'corp')


# total_shares = shares + new_shares

# market_price_per_share = 1

# market_cap = total_shares * market_price_per_share

# book_value(ledger, 'corp')


# qty = 50
# price_per_share = 1

# add_transaction(ledger, '2021-01-01', 'issue shares to new investors',
#     'corp:equity:shares',     -qty * price_per_share,
#     'person_a:assets:shares',  qty * price_per_share,

#     'corp:assets:gold',        qty * price_per_share,
#     'person_a:assets:gold',   -qty * price_per_share
# )

issue_shares(ledger, '2021-01-01', 'corp', 'investor_a', 50, 1)

issue_shares(ledger, '2021-01-01', 'corp', 'person_a', 50, 1)
issue_shares(ledger, '2021-01-01', 'corp', 'person_b', 50, 1)

history_of_balances(ledger)


shares_table = {}

# shares_table['corp']

shares_table.get('corp', 0) + 100

shares_table['corp'] = shares_table.get('corp', 0) + 100

def increment_shares(shares_table, name, quantity):
    shares_table[name] = shares_table.get(name, 0) + quantity

shares_table

increment_shares(shares_table, 'corp', 50)

# DEALER
# dividends       liabilities
# expenses        equity
# assets          revenue

# book_value = ledger_all_account_with_values(ledger)['corp:assets']

# number_of_shares = 300

# price = book_value / number_of_shares

# price




# dig_for_gold(ledger, '2021-01-01', 'person_a', 100)
# dig_for_gold(ledger, '2021-01-01', 'person_b', 100)
# dig_for_gold(ledger, '2021-01-01', 'person_c', 100)

# issue_shares(ledger, '2021-01-02', 'corp', 'person_a', quantity=100, price=1)
# issue_shares(ledger, '2021-01-02', 'corp', 'person_b', quantity=100, price=1)
# issue_shares(ledger, '2021-01-02', 'corp', 'person_c', quantity=100, price=1)

# dig_for_gold(ledger, '2021-01-01', 'person_d', 20)

# buy_stock(ledger, '2021-01-02', 'person_d', 'person_a', quantity=10, original_price=1, new_price=2)

# history_of_balances(ledger)
