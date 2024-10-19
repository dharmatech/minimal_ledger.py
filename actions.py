
from core import *

def dig_for_gold(ledger: Ledger, date: str, name: str, amount: Decimal):
    ledger.transactions.append(Transaction(
        date=date,
        description=f'dig for gold: {name}',
        entries=[
            Entry(f'{name}:assets:gold',    amount),
            Entry(f'{name}:equity:mining', -amount),
        ]
    ))

def grow_apples(ledger: Ledger, date: str, name: str, amount: Decimal):
    ledger.transactions.append(Transaction(
        date=date,
        description=f'grow apples: {name}',
        entries=[
            Entry(f'{name}:assets:apples',    amount),
            Entry(f'{name}:equity:farming',  -amount),
        ]
    ))

def barter(ledger: Ledger, date: str, name_a: str, name_b: str, asset_a: str, asset_b: str, amount: Decimal):
    ledger.transactions.append(Transaction(
        date=date,
        description=f'barter: {name_a} {asset_a} <-> {name_b} {asset_b}',
        entries=[
            Entry(f'{name_a}:assets:{asset_a}', -amount),
            Entry(f'{name_b}:assets:{asset_a}',  amount),
            Entry(f'{name_a}:assets:{asset_b}',  amount),
            Entry(f'{name_b}:assets:{asset_b}', -amount)
        ]
    ))