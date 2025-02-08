import os
import json
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

def create_wallet():
    # Generate RSA private key
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
    )

    # Get the public key
    public_key = private_key.public_key()

    # Serialize keys
    private_key_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption(),
    )
    public_key_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo,
    )

    # Create a wallet address using the public key (simplified example)
    wallet_address = public_key_pem.hex()[:40]

    # Save keys to files
    os.makedirs("wallets", exist_ok=True)
    with open(f"wallets/{wallet_address}_private.pem", "wb") as f:
        f.write(private_key_pem)
    with open(f"wallets/{wallet_address}_public.pem", "wb") as f:
        f.write(public_key_pem)

    print(f"Wallet created successfully! Address: {wallet_address}")
    return wallet_address

if __name__ == "__main__":
    wallet_address = create_wallet()
    print(f"Your wallet address is: {wallet_address}")
