
from actions import *
from history_of_balances import *

# ----------------------------------------------------------------------
def issue_shares(ledger, date, issuer, buyer, quantity, price):
    add_transaction(ledger, date, f'issue shares: {issuer} -> {buyer} : {quantity} shares @ {price}',
        f'{issuer}:equity:shares', -price * quantity,
        f'{buyer}:assets:shares',   price * quantity,

        f'{issuer}:assets:gold',    price * quantity,
        f'{buyer}:assets:gold',    -price * quantity,
    )

def buy_stock(ledger, date, buyer, seller, quantity, original_price, new_price):
    add_transaction(ledger, date, f'buy stock: {buyer} -> {seller} | {quantity} shares @ {new_price} | original price = {original_price}',
        f'{buyer}:assets:gold',  -quantity * new_price,
        f'{seller}:assets:gold',  quantity * new_price,
        f'{seller}:income',      -quantity * (new_price - original_price),

        f'{seller}:assets:shares', -quantity * original_price,
        f'{buyer}:assets:shares',   quantity * new_price,
    )
# ----------------------------------------------------------------------

ledger = Ledger()

dig_for_gold(ledger, '2021-01-01', 'corp', 50)

dig_for_gold(ledger, '2021-01-01', 'person_a', 10)

issue_shares(ledger, '2021-01-02', 'corp', 'person_a', quantity=10, price=1)

dig_for_gold(ledger, '2021-01-01', 'person_b', 20)

buy_stock(ledger, '2021-01-02', 'person_b', 'person_a', 10, 1, 2)

history_of_balances(ledger)
