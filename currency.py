import requests

base = input("From currency (e.g. USD): ").upper()
target = input("To currency (e.g. INR): ").upper()
amount = float(input("Amount: "))
data = requests.get(f"https://api.frankfurter.app/latest?from={base}&to={target}", timeout=10).json()
rate = data["rates"][target]
print(f"{amount:.2f} {base} = {amount*rate:.2f} {target}")
