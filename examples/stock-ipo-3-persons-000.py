
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
# ----------------------------------------------------------------------

ledger = Ledger()

dig_for_gold(ledger, '2021-01-01', 'corp', 300)



book_value = ledger_all_account_with_values(ledger)['corp:assets']

number_of_shares = 300

price = book_value / number_of_shares

price




dig_for_gold(ledger, '2021-01-01', 'person_a', 100)
dig_for_gold(ledger, '2021-01-01', 'person_b', 100)
dig_for_gold(ledger, '2021-01-01', 'person_c', 100)

issue_shares(ledger, '2021-01-02', 'corp', 'person_a', quantity=100, price=1)
issue_shares(ledger, '2021-01-02', 'corp', 'person_b', quantity=100, price=1)
issue_shares(ledger, '2021-01-02', 'corp', 'person_c', quantity=100, price=1)

dig_for_gold(ledger, '2021-01-01', 'person_d', 20)

buy_stock(ledger, '2021-01-02', 'person_d', 'person_a', quantity=10, original_price=1, new_price=2)

history_of_balances(ledger)
