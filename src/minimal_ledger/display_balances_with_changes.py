
from .core import *
from .display_balance import *

# def get_substrings(input_str: str) -> List[str]:
#     result = []
#     parts = input_str.split(':')
#     for i in range(len(parts), 0, -1):
#         result.append(':'.join(parts[:i]))
#     return result

# def ledger_leaf_accounts(ledger: Ledger) -> List[str]:
#     return [entry.description for entry in ledger.entries()]

# def ledger_all_accounts(ledger: Ledger) -> List[str]:
#     return sorted(
#         set(
#             sub
#             for acc in ledger_leaf_accounts(ledger)
#             for sub in get_substrings(acc)
#         )
#     )

# def transform_account(account: str) -> str:
#     parts = account.split(':')
#     category = parts[-2] if parts[-1] == '' else parts[-1]
#     indent_level = len(parts) - 2 if parts[-1] == '' else len(parts) - 1
#     indent = '  ' * indent_level
#     return f"{indent}{category}"

def display_balances_with_changes(ledger_a: Ledger, ledger_b: Ledger, output_type='terminal'):

    accounts_a = ledger_all_accounts(ledger_a)    
    accounts_b = ledger_all_accounts(ledger_b)

    accounts = sorted(set(accounts_a + accounts_b))
    
    output = ''

    max_account_length = max(len(transform_account(account)) for account in accounts)

    for account in accounts:

        total_a = sum(entry.amount for entry in ledger_a.entries() if entry.description.startswith(account))
        total_b = sum(entry.amount for entry in ledger_b.entries() if entry.description.startswith(account))

        account = transform_account(account)

        total_a = round(total_a, 2)
        total_b = round(total_b, 2)

        if output_type == 'terminal':
            if total_a != total_b:
                diff = total_b - total_a
                
                # terminal
                color = "\033[32m" if diff > 0 else "\033[31m"  # Green for positive, Red for negative
                reset = "\033[0m"
                output += f"{account:<{max_account_length}}: {total_b:>7.2f} {color}{diff:+.2f}{reset}\n"
            else:
                output += f"{account:<{max_account_length}}: {total_b:>7.2f}\n"

    print(output)

