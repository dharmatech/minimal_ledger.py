

# Example

[examples/raw-transactions.py](examples/raw-transactions.py)

```python
from history_of_balances import *

ledger = Ledger()

add_transaction(ledger, '2021-01-01', 'dig for gold: person_a',
    'person_a:assets:gold',    100,
    'person_a:equity:mining', -100,
)

add_transaction(ledger, '2021-01-01', 'grow apples: person_a',
    'person_a:assets:apples',  100,
    'person_a:equity:apples', -100,
)

add_transaction(ledger, '2021-01-01', 'barter',
    'person_a:assets:gold',   -50,
    'person_b:assets:gold',    50,
    'person_b:assets:apples', -50,
    'person_a:assets:apples',  50
)

history_of_balances(ledger)
```

![image](https://github.com/user-attachments/assets/ec0f9934-63e6-48e6-8fb6-4ec6bcda5e91)

# Example

[[examples/actions.py]]

```python
from actions import *
from history_of_balances import *

ledger = Ledger()

dig_for_gold(ledger, '2021-01-01', 'person_a', 100)
grow_apples( ledger, '2021-01-02', 'person_b', 100)
barter(ledger, '2021-01-03', 'person_a', 'person_b', 'gold', 'apples', 50)

history_of_balances(ledger)
```
