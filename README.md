## Activity 1: Explore PQC Algorithms [Theory Task]

1. Investigate three NIST digital‑signature algorithms: ML‑DSA, SLH‑DSA and FN‑DSA. List all algorithm variants together with private‑key size, public‑key size and signature size.
2. Study ML‑KEM (Key Encapsulation Mechanism) and compare it against RSA. RSA is vulnerable to Shor’s quantum algorithm; ML‑KEM is lattice‑based and quantum‑resilient, designed for secure key exchange.

## Activity 2: Implement ML‑KEM [Coding Practical]

1. Create the `mlkem` project folder on an Ubuntu VM desktop. Set up a Python virtual environment and install `kyber‑py` and `dilithium‑py` packages.
2. Write `mlkem_demo.py` to run ML‑KEM‑768: Alice generates a key pair. Bob uses Alice’s public key to encapsulate and obtain a shared secret. Alice decapsulates the ciphertext. Both parties derive an identical shared secret.
3. Create a GitHub repository named `post‑quantum‑algorithms` and upload the project code.

> 
> Common pitfalls: Re‑activate the virtual environment for every new terminal session, otherwise modules cannot be found. Older Git defaults to the `master` branch; rename it to `main` before pushing to GitHub.

## Activity 3: Implement ML‑DSA [Coding Practical]

1. Within the same project, create `mldsa_demo.py`. Use ML‑DSA‑65 to generate a keypair, sign a text message and verify the signature. A `True` output indicates a valid signature.
2. Push the new source file to the existing GitHub repository.
3. Write a professional `README.md` explaining the project, environment setup and execution steps. Include links to PQC reference repositories.
4. Add a `.gitignore` file to avoid uploading the local `.venv` virtual‑environment folder.

## Activity 4: Resources for all PQC algorithms [Research Task]

Explore four open‑source GitHub repositories for NIST PQC algorithm implementations. No full implementation code is required for this activity. Add these links to the reference section in README:

- ML‑KEM, ML‑DSA, SLH‑DSA, FN‑DSA source‑code repositories.

### Overall Project Objective

Gain hands‑on experience with NIST‑standard lattice‑based post‑quantum cryptography. Understand cybersecurity risks introduced by quantum computers. Complete demonstration code for ML‑KEM key exchange and ML‑DSA digital signatures, together with local development, Git version control and GitHub repository workflow.

### Important Notes

1. On Ubuntu use `python3`. Run `source .venv/bin/activate` each time you open a new terminal to enable the virtual environment.
2. When pushing to GitHub over HTTPS, use a Personal Access Token instead of your web‑site login password.
3. Never commit and push the `.venv` directory to GitHub.
