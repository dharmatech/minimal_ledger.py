
from dataclasses import dataclass, field
from decimal     import Decimal
from typing      import List, Dict, Generator

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
