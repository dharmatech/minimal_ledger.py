
from core import *
from actions import *
from history_of_balances import *

# reload history_of_balances module

import importlib

import history_of_balances
importlib.reload(history_of_balances)

import display_balance
importlib.reload(display_balance)

from display_balance import *


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


book_value = ledger_all_account_with_values(ledger)['corp:assets']

number_of_shares = 50

price = book_value / number_of_shares

price


issue_shares(ledger, '2021-01-02', 'corp', 'person_a', quantity=10, price=1)

dig_for_gold(ledger, '2021-01-01', 'person_b', 20)

buy_stock(ledger, '2021-01-02', 'person_b', 'person_a', 10, 1, 2)

history_of_balances(ledger)
