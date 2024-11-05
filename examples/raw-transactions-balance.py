
from display_balance import *

ledger = Ledger()

add_transaction(ledger, '2021-01-01', 'dig for gold: person_a',
    'person_a:assets:gold',    100,
    'person_a:equity:mining', -100,
)

add_transaction(ledger, '2021-01-01', 'grow apples: person_b',
    'person_b:assets:apples',  100,
    'person_b:equity:apples', -100,
)

add_transaction(ledger, '2021-01-01', 'barter',
    'person_a:assets:gold',   -50,
    'person_b:assets:gold',    50,
    'person_b:assets:apples', -50,
    'person_a:assets:apples',  50
)

display_balance(ledger)
