
# Secure-Password-Generator-Python-

This project is a simple but powerful tool I built to help people create strong, random passwords without the hassle. Instead of relying on guesswork or insecure generators, it uses Python’s `secrets` module to make sure every password is truly unpredictable and safe.  

It’s interactive and easy to use: you choose the length and whether to include uppercase letters, digits, or symbols, and it instantly gives you a secure password. If you want another one, just say yes — it keeps going until you’re done.  

I built this project to practice writing clean, user‑friendly code while keeping security in mind. It’s a small step, but it shows how thoughtful design and simple tools can make everyday tasks safer and easier.

---

## What You Can Do With It

- **Choose your own strength**: Decide how long your password should be (minimum 4 characters).  
- **Customize the mix**: Pick whether to include uppercase letters, digits, and symbols — or keep it simple.  
- **Get instant results**: As soon as you confirm your choices, the generator produces a secure password on the spot.  
- **Keep going until you’re happy**: Don’t like the first one? Just say “yes” and it will generate another.  
- **Exit gracefully**: When you’re done, type “no” and the program closes with a friendly goodbye.  

---

## How to Run
1. Clone this repository:
   ```bash
   git clone https://github.com/Mzi06/password-generator.git
2. Navigate into the project folder:
    ```bash
    cd password-generator
3. Make sure you have Python 3 installed, then run:
   ```bash
   python password_generator.py
4. Follow the prompts:
   - Enter the desired password length (minimum 4).
   - Choose whether to include uppercase letters, digits, and symbols.
   - A secure password will be generated instantly.
   - You can generate more passwords until you choose to exit.

---

## Example Usage
- Enter password length (minimum 4): 10
- Include uppercase letters? (y/n): y
- Include digits? (y/n): y
- Include symbols? (y/n): n
- Generated password: aB9xqzHkLm

Generate another password? (y/n): n
Goodbye!

---
## Screenshots

**Interactive Prompt**
<img width="1009" height="117" alt="preferences" src="https://github.com/user-attachments/assets/59f82e7c-3c1d-48cc-a919-285f7891f3b4" />
This shows how the program asks for your preferences before generating a password.

**Generated Password with Entropy & Strength**
<img width="982" height="264" alt="Entrophy" src="https://github.com/user-attachments/assets/f5d78438-5c7c-4bc5-83ad-02a857555a78" />
Here you can see the generated password, its entropy calculation, and the strength rating.

**Blacklist Check In Action**
<img width="995" height="143" alt="Blacklist" src="https://github.com/user-attachments/assets/f6110116-6398-42a4-85bb-816d1c92e5c3" />
If a weak or common password is generated, the blacklist check catches it and regenerates a stronger one.

---

## Where This Project Could Go Next

This password generator is just the beginning. Here are some ideas I’d love to explore:

- **A simple desktop app**: Wrap the script in a friendly interface so anyone can click a button and get a password.  
- **Web deployment**: Turn it into a small web app using Flask or Django, hosted on AWS, so people can generate passwords from anywhere.  
- **Clipboard integration**: Add a feature that copies the password directly to your clipboard, saving time.    
- **Customization options**: Let users exclude certain symbols or characters if they want passwords that are easier to type.  
- **Mobile version**: Package it as a lightweight app for Android/iOS, so secure passwords are always in your pocket.  

---

## What I Learned

Working on this project taught me more than just writing Python code:

- **The importance of secure randomness**: I discovered why the `secrets` module is better than `random` for generating passwords, and how small choices in code can have big impacts on security.  
- **Input validation matters**: By adding loops to check password length and yes/no answers, I learned how to make programs more user‑friendly and error‑proof.  
- **Structuring code for clarity**: Separating logic into functions like `generate_password` and `get_yes_no` helped me see how clean design makes code easier to read, reuse, and explain.  
- **Thinking like a user**: Instead of just making the program “work,” I focused on how someone would interact with it — from prompts to exit messages — and that mindset made the project feel more polished.  
- **Documentation is part of the project**: Writing this README showed me that explaining *why* and *how* I built something is just as important as the code itself.  
