from kyber_py.ml_kem import ML_KEM_768

# Alice generates her key pair
ek, dk = ML_KEM_768.keygen()

print("Alice's encapsulation key:", len(ek), "bytes")
print("Alice's decapsulation key:", len(dk), "bytes")

# Bob uses Alice's public key to establish a shared secret
shared_secret_bob, ciphertext = ML_KEM_768.encaps(ek)

print("Ciphertext:", len(ciphertext), "bytes")
print("Bob's shared secret:", shared_secret_bob.hex())

# Alice decapsulates the ciphertext
shared_secret_alice = ML_KEM_768.decaps(dk, ciphertext)

print("Alice's shared secret:", shared_secret_alice.hex())

# Check that both sides obtained the same secret
if shared_secret_alice == shared_secret_bob:
    print("ML-KEM shared secret successfully established!")
else:
    print("Something went wrong!")
