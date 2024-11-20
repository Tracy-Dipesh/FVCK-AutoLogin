🚀 FVCK - Auto Login Py Script 🦖

A powerful, interactive, and automated login tool that makes navigating web logins easy, fast, and efficient! Perfect for educational purposes, testing, and understanding HTTP sessions.

✨ Features
🔑 CSRF Token Handling: Dynamically extracts CSRF tokens for secure authentication.
🔁 Retry Logic: Automatically retries login attempts for user-defined limits.
📄 HTML Export: Saves the post-login page's HTML for offline analysis.
💻 Interactive CLI: Simple and intuitive prompts for seamless user experience.
🕒 Timestamp Logging: Logs login attempt timestamps for detailed tracking.
🛠️ Setup & Usage
1️⃣ Clone the Repository
bash
Copy code
git clone https://github.com/your-username/LoginRaptor.git
cd LoginRaptor
2️⃣ Install Dependencies
Ensure you have Python installed. Install required libraries:

bash
Copy code
pip install -r requirements.txt
3️⃣ Run the Tool
bash
Copy code
python loginraptor.py
4️⃣ Follow the Prompts
Enter the URL of the login page.
Provide valid credentials and the number of retries.
Save the successful login page as an HTML file.

⚡ How It Works
🌐 Fetches the Login Page: Initiates a session and retrieves the login form.
🔎 Parses CSRF Token: Scans and extracts CSRF tokens dynamically for secure requests.
🎯 Attempts Login: Automates login attempts with retry functionality.
💾 Saves Results: On success, exports the HTML of the redirected page to your chosen file path.
🚨 Disclaimer
⚠️ This tool is for educational purposes only.
Use responsibly and ensure you have permission to interact with the targeted website. Unauthorized use may violate laws and terms of service.

🌟 Contributing
Contributions are welcome! Feel free to fork, submit PRs, or suggest features.

🧰 Dependencies
requests
beautifulsoup4
datetime
Install them using:

bash
Copy code
pip install -r requirements.txt
🎉 Credits
Developed with ❤️ by [Your Name or Username].

🐙 License
This project is licensed under the MIT License. See LICENSE for details.

🚀 Happy Hacking!
