from bitcoinlib.wallets import Wallet

passphrase = ""

try:
    w = Wallet.create("capyboss", keys=passphrase, network='bitcoin')
    print("Wallet created successfully.")
except Exception as e:
    print("Error creating wallet:", e)