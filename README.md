
# Minimal implementation of plain text accounting in Python.

This is a minimal implementation intended for experimentation.

In this initial version, the core file is only 44 lines. The entire library with all utility functions is 156 lines.

```
$ wc --lines *.py
  33 actions.py
  44 core.py
  63 display_balances_with_changes.py
  16 history_of_balances.py
 156 total
```

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

history_of_balances(ledger)
```

![image](https://github.com/user-attachments/assets/52f70af5-7064-4f3b-977c-3337f3f58cb6)


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

# core

Here's the `core` module, which shows the essence of the ledger system:

```python
@dataclass
class Entry:
    description: str
    amount: Decimal

    def clone(self) -> 'Entry':
        return Entry(self.description, self.amount)

@dataclass
class Transaction:
    date: str
    description: str
    entries: list[Entry]

    def clone(self) -> 'Transaction':
        return Transaction(self.date, self.description, [entry.clone() for entry in self.entries])

@dataclass
class Ledger:
    transactions: List[Transaction] = field(default_factory=list)
    
    def entries_gen(self) -> Generator[Entry, None, None]:
        return (
            entry 
            for transaction in self.transactions 
            for entry       in transaction.entries
        )

    def entries(self) -> List[Entry]:
        return list(self.entries_gen())

    def clone(self) -> 'Ledger':
        return Ledger([transaction.clone() for transaction in self.transactions])
    
def add_transaction(ledger, date, description, *entries):

    entries_ = [Entry(acc, amt) for acc, amt in zip(entries[::2], entries[1::2])]

    ledger.transactions.append(Transaction(date, description, entries_))
```
