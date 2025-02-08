import requests

def get_wallet_balance(wallet_address):
    url = f"https://arweave.net/wallet/{wallet_address}/balance"
    response = requests.get(url)
    if response.status_code == 200:
        balance = int(response.text) / 10**12  # Convert winston to AR
        return balance
    else:
        raise Exception("Failed to fetch wallet balance")

# Replace with your wallet address
wallet_address = "YOUR_WALLET_ADDRESS"
print(f"Balance: {get_wallet_balance(wallet_address)} AR")
