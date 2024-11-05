
from actions import *
from history_of_balances import *

ledger = Ledger()

dig_for_gold(ledger, '2021-01-01', 'corp', 50)

dig_for_gold(ledger, '2021-01-01', 'person_a', 10)

add_transaction(ledger, '2021-01-02', 'issue shares',
    'corp:equity:shares',     -10 * 1,
    'person_a:assets:shares',  10 * 1,

    'corp:assets:gold',        10 * 1,
    'person_a:assets:gold',   -10 * 1
)

dig_for_gold(ledger, '2021-01-01', 'person_b', 20)

add_transaction(ledger, '2021-01-02', 'buy stock open market',
    'person_b:assets:gold', -10 * 2,
    'person_a:assets:gold',   10 * 2,
    'person_a:income',       -10 * 1,

    'person_a:assets:shares',  -10 * 1,
    'person_b:assets:shares',   10 * 2,
)

history_of_balances(ledger)
