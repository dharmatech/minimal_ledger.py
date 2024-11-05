
from actions import *
from history_of_balances import *

ledger = Ledger()

dig_for_gold(ledger, '2021-01-01', 'corp', 50)

dig_for_gold(ledger, '2021-01-01', 'person_a', 10)

quantity = 10
price_a = 1

add_transaction(ledger, '2021-01-02', 'issue shares',
    'corp:equity:shares',     -quantity * price_a,
    'person_a:assets:shares',  quantity * price_a,

    'corp:assets:gold',        quantity * price_a,
    'person_a:assets:gold',   -quantity * price_a
)

dig_for_gold(ledger, '2021-01-01', 'person_b', 20)

price_b = 2

add_transaction(ledger, '2021-01-02', 'buy stock open market',
    'person_b:assets:gold',    -quantity * price_b,
    'person_a:assets:gold',     quantity * price_b,
    'person_a:income',         -quantity * (price_b - price_a),
    'person_a:assets:shares',  -quantity * price_a,
    'person_b:assets:shares',   quantity * price_b
)

history_of_balances(ledger)



