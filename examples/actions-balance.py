
from actions import *
from history_of_balances import *
from display_balance import *

ledger = Ledger()

dig_for_gold(ledger, '2021-01-01', 'person_a', 100)
grow_apples( ledger, '2021-01-02', 'person_b', 100)
barter(ledger, '2021-01-03', 'person_a', 'person_b', 'gold', 'apples', 50)

display_balance(ledger)
