

# Example

[examples/raw-transactions.py](examples/raw-transactions.py)

Adding transactions to the ledger in a traditional way:

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

This being Python, you can abstract out commonly formatted transactions into functions.

E.g., instead of the above transaction for digging for gold, we can define:

```python
def dig_for_gold(ledger: Ledger, date: str, name: str, amount: Decimal):
    ledger.transactions.append(Transaction(
        date=date,
        description=f'dig for gold: {name}',
        entries=[
            Entry(f'{name}:assets:gold',    amount),
            Entry(f'{name}:equity:mining', -amount),
        ]
    ))
```

[examples/actions.py](examples/actions.py)

```python
from actions import *
from history_of_balances import *

ledger = Ledger()

dig_for_gold(ledger, '2021-01-01', 'person_a', 100)
grow_apples( ledger, '2021-01-02', 'person_b', 100)
barter(ledger, '2021-01-03', 'person_a', 'person_b', 'gold', 'apples', 50)

history_of_balances(ledger)
```

![image](https://github.com/user-attachments/assets/4eb8b2b2-e5eb-4aa3-b2c2-8cfb793bff4d)

# history_of_balances

As you can see in the examples above, `history_of_balances` shows the balance sheet after each transaction, so that you can see the effects of the transactions on the accounts.
Lines that have green or red in them indicate changed accounts.

    Green = increased
    Red = decreased
