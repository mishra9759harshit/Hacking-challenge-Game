from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.spinner import Spinner
from kivy.core.audio import SoundLoader
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from kivy.graphics import Color, Rectangle

import os
import json
import random
import webbrowser

class HackingGame(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.clearcolor = get_color_from_hex("#000000")  # Black background for hacking effect
        self.orientation = 'vertical'
        self.padding = [10, 10, 10, 10]
        self.spacing = 10

        # Title
        self.title_label = Label(
            text="HACKING CHALLENGE",
            font_size=30,
            color=(0.3, 1, 0.3, 1),
            bold=True,
            size_hint=(1, None),
            height=60
        )
        self.add_widget(self.title_label)

        self.current_user = None
        self.score = 0
        self.users_file = "users.json"
        self.users = self.load_users()
        self.question_answers = []
        # Define questions and answers for different difficulty levels
        self.levels = {
            "easy": {
        "questions": {
            "What does 'SQL' stand for?": [
                "1. Secure Query Language", 
                "2. Structured Query Language", 
                "3. Simple Query Language", 
                "4. Standard Query Language"
            ],
            "Which of the following is a common penetration testing tool?": [
                "1. Wireshark", 
                "2. MS Paint", 
                "3. Microsoft Word", 
                "4. Notepad"
            ],
            "What is the primary purpose of a firewall?": [
                "1. To protect against viruses", 
                "2. To manage user accounts", 
                "3. To block unauthorized access", 
                "4. To increase internet speed"
            ],
            "What does HTTP stand for?": [
                "1. Hypertext Transfer Protocol",
                "2. High Transfer Text Protocol",
                "3. Hyperlink Text Transfer Protocol",
                "4. Hypertext Transmission Protocol"
            ],
            "Which protocol is used for secure data transmission over the internet?": [
                "1. FTP",
                "2. HTTP",
                "3. SSH",
                "4. SMTP"
            ],
            "What is a common method to test web application security?": [
                "1. SQL Injection",
                "2. File Transfer Protocol",
                "3. Data Encryption",
                "4. Disk Formatting"
            ],
            "What is the main function of an IDS?": [
                "1. Intrusion Detection System",
                "2. Internet Data Service",
                "3. Internal Defense Strategy",
                "4. Information Data Security"
            ],
            "Which of the following is NOT a type of malware?": [
                "1. Virus",
                "2. Worm",
                "3. Firewall",
                "4. Trojan"
            ],
            "What is social engineering?": [
                "1. Training staff on security",
                "2. Manipulating people to gain confidential information",
                "3. Engineering social networks",
                "4. Conducting surveys"
            ],
            "What type of attack involves overwhelming a system with traffic?": [
                "1. Phishing",
                "2. DDoS",
                "3. SQL Injection",
                "4. Cross-Site Scripting"
            ],
            "What is the function of encryption?": [
                "1. To speed up internet connection",
                "2. To secure data",
                "3. To manage user accounts",
                "4. To prevent hardware damage"
            ],
            "Which of the following is a strong password?": [
                "1. 123456",
                "2. password",
                "3. qwerty",
                "4. P@ssw0rd123"
            ],
            "What does VPN stand for?": [
                "1. Virtual Private Network",
                "2. Verified Private Network",
                "3. Virtual Protected Network",
                "4. Verified Protected Network"
            ],
            "What is a phishing attack?": [
                "1. A fishing technique",
                "2. An email scam",
                "3. A physical attack",
                "4. A network attack"
            ],
            "Which tool can be used to analyze network traffic?": [
                "1. Wireshark",
                "2. Excel",
                "3. Word",
                "4. Notepad"
            ],
            "What does malware stand for?": [
                "1. Malicious software",
                "2. Management software",
                "3. Multi-layer software",
                "4. None of the above"
            ],
            "What is two-factor authentication?": [
                "1. Using two passwords",
                "2. A second layer of security",
                "3. A type of encryption",
                "4. None of the above"
            ],
            "What is a common use of ransomware?": [
                "1. To improve performance",
                "2. To encrypt files for a ransom",
                "3. To enhance security",
                "4. To back up data"
            ],
            "What is the purpose of a password manager?": [
                "1. To store passwords securely",
                "2. To create strong passwords",
                "3. To monitor network activity",
                "4. Both 1 and 2"
            ],
            "What does the acronym 'DNS' stand for?": [
                "1. Dynamic Name Server",
                "2. Domain Name System",
                "3. Digital Network Service",
                "4. Data Network System"
            ],
            "Which is a common attack vector?": [
                "1. Unpatched software",
                "2. Strong passwords",
                "3. Encrypted files",
                "4. Firewalls"
            ],
            "What is an example of a brute-force attack?": [
                "1. Guessing passwords repeatedly",
                "2. Phishing",
                "3. Social engineering",
                "4. SQL Injection"
            ],
            "What is a security policy?": [
                "1. A set of rules to protect information",
                "2. A type of software",
                "3. A method to encrypt data",
                "4. A hardware device"
            ],
            "What is a common characteristic of a secure password?": [
                "1. It includes personal information",
                "2. It is short and simple",
                "3. It has a mix of letters, numbers, and symbols",
                "4. It is the same as the username"
            ],
            "What is the role of an antivirus program?": [
                "1. To manage files",
                "2. To remove malware",
                "3. To optimize performance",
                "4. To create backups"
            ],
            "Which of the following is a type of cyber attack?": [
                "1. DDoS",
                "2. Defragmentation",
                "3. Database backup",
                "4. Disk cleanup"
            ],
            "What is the function of a security token?": [
                "1. To manage user sessions",
                "2. To encrypt data",
                "3. To verify user identity",
                "4. To monitor network traffic"
            ],
            "Which of the following is NOT a characteristic of phishing?": [
                "1. Spoofed email address",
                "2. High urgency",
                "3. Accurate sender information",
                "4. Unusual attachments"
            ],
            "What does the acronym 'SSL' stand for?": [
                "1. Secure Sockets Layer",
                "2. Simple Sockets Layer",
                "3. Secure Server Layer",
                "4. Standard Security Layer"
            ],
            "What is a common characteristic of phishing emails?": [
                "1. Personalized greeting",
                "2. Generic subject lines",
                "3. Secure links",
                "4. None of the above"
            ],
            "What does a 'white hat' hacker do?": [
                "1. Engages in illegal activities",
                "2. Works to improve security",
                "3. Hacks for personal gain",
                "4. None of the above"
            ],
            "Which of the following is an example of a strong password?": [
                "1. password123",
                "2. 12345678",
                "3. P@ssw0rd!23",
                "4. qwerty"
            ],
            "What is the purpose of a digital certificate?": [
                "1. To encrypt data",
                "2. To verify identity",
                "3. To manage passwords",
                "4. To monitor network traffic"
            ],
            "What is the main goal of an ethical hacker?": [
                "1. To steal data",
                "2. To find and fix vulnerabilities",
                "3. To disrupt services",
                "4. None of the above"
            ],
            "What does the term 'hacker' generally refer to?": [
                "1. A computer expert",
                "2. A person who breaks into systems",
                "3. A security professional",
                "4. Both 1 and 2"
            ],
            "What is the purpose of a security audit?": [
                "1. To find vulnerabilities",
                "2. To increase profits",
                "3. To improve performance",
                "4. To manage user accounts"
            ],
            "Which of the following is NOT a type of social engineering attack?": [
                "1. Phishing",
                "2. Vishing",
                "3. Smishing",
                "4. Password reset"
            ],
            "What does the acronym 'CIA' stand for in cybersecurity?": [
                "1. Confidentiality, Integrity, Availability",
                "2. Central Intelligence Agency",
                "3. Computer Information Architecture",
                "4. Cybersecurity Information Agency"
            ],
            "What is the purpose of network segmentation?": [
                "1. To increase speed",
                "2. To enhance security",
                "3. To improve performance",
                "4. None of the above"
            ],
            "Which of the following is an example of a denial of service attack?": [
                "1. Sending too many requests to a server",
                "2. Guessing passwords",
                "3. Phishing for information",
                "4. Encrypting data"
            ],
            "What does 'malware' refer to?": [
                "1. Software that is harmful",
                "2. Software that improves performance",
                "3. Software that manages files",
                "4. None of the above"
            ],
            "What is an exploit?": [
                "1. A security measure",
                "2. A method to compromise a system",
                "3. A tool for analysis",
                "4. A backup solution"
            ],
            "What is the purpose of logging in cybersecurity?": [
                "1. To monitor user activity",
                "2. To store files",
                "3. To increase internet speed",
                "4. To manage hardware"
            ],
            "What is a zero-day vulnerability?": [
                "1. A vulnerability that has existed for a day",
                "2. A vulnerability that is exploited on the same day it is discovered",
                "3. A fixed vulnerability",
                "4. None of the above"
            ],
            "Which of the following is a method of protecting sensitive data?": [
                "1. Data encryption",
                "2. Public sharing",
                "3. Lack of access control",
                "4. None of the above"
            ],
            "What is the function of a VPN?": [
                "1. To create a secure connection over the internet",
                "2. To block malware",
                "3. To manage user accounts",
                "4. To increase bandwidth"
            ],
            "What is a common use of a firewall?": [
                "1. To block unauthorized access",
                "2. To speed up internet",
                "3. To store files",
                "4. None of the above"
            ],
            "Which type of attack attempts to gain sensitive information through deception?": [
                "1. Social engineering",
                "2. Malware",
                "3. Brute-force",
                "4. None of the above"
            ],
            "What is an example of a brute-force attack?": [
                "1. Guessing passwords",
                "2. Phishing",
                "3. Denial of service",
                "4. None of the above"
            ],
            "What does 'XSS' stand for in web security?": [
                "1. Cross-Site Scripting",
                "2. Cross-Site Secure",
                "3. Cross-Site Safety",
                "4. None of the above"
            ],
            "What is a DDoS attack?": [
                "1. Direct Denial of Service",
                "2. Distributed Denial of Service",
                "3. Data Destruction Service",
                "4. None of the above"
            ],
            "What is the main risk of using public Wi-Fi?": [
                "1. High speed",
                "2. Data interception",
                "3. Free internet",
                "4. None of the above"
            ],
            "What is the purpose of malware?": [
                "1. To protect systems",
                "2. To collect data without consent",
                "3. To enhance performance",
                "4. To encrypt data"
            ],
            "What is social engineering?": [
                "1. A method to enhance software",
                "2. Manipulating individuals to disclose confidential information",
                "3. A type of encryption",
                "4. None of the above"
            ],
            # (Continue adding questions until reaching 150 easy questions)
        },
        "answers": {
            "What does 'SQL' stand for?": "2",
            "Which of the following is a common penetration testing tool?": "1",
            "What is the primary purpose of a firewall?": "3",
            "What does HTTP stand for?": "1",
            "Which protocol is used for secure data transmission over the internet?": "3",
            "What is a common method to test web application security?": "1",
            "What is the main function of an IDS?": "1",
            "Which of the following is NOT a type of malware?": "3",
            "What is social engineering?": "2",
            "What type of attack involves overwhelming a system with traffic?": "2",
            "What is the function of encryption?": "2",
            "Which of the following is a strong password?": "4",
            "What does VPN stand for?": "1",
            "What is a phishing attack?": "2",
            "Which tool can be used to analyze network traffic?": "1",
            "What does malware stand for?": "1",
            "What is two-factor authentication?": "2",
            "What is a common use of ransomware?": "2",
            "What is the purpose of a password manager?": "4",
            "What does the acronym 'DNS' stand for?": "2",
            "Which is a common attack vector?": "1",
            "What is an example of a brute-force attack?": "1",
            "What is a security policy?": "1",
            "What is a common characteristic of a secure password?": "3",
            "What is the role of an antivirus program?": "2",
            "Which of the following is a type of cyber attack?": "1",
            "What is the function of a security token?": "3",
            "Which of the following is NOT a characteristic of phishing?": "3",
            "What does the acronym 'SSL' stand for?": "1",
            "What is a common characteristic of phishing emails?": "2",
            "What does a 'white hat' hacker do?": "2",
            "Which of the following is an example of a strong password?": "3",
            "What is the purpose of a digital certificate?": "2",
            "What is the main goal of an ethical hacker?": "2",
            "What does the term 'hacker' generally refer to?": "4",
            "What is the purpose of a security audit?": "1",
            "Which of the following is NOT a type of social engineering attack?": "4",
            "What does the acronym 'CIA' stand for in cybersecurity?": "1",
            "What is the purpose of network segmentation?": "2",
            "Which of the following is an example of a denial of service attack?": "1",
            "What does 'malware' refer to?": "1",
            "What is an exploit?": "2",
            "What is the purpose of logging in cybersecurity?": "1",
            "What is a zero-day vulnerability?": "2",
            "Which of the following is a method of protecting sensitive data?": "1",
            "What is the function of a VPN?": "1",
            "What is a common use of a firewall?": "1",
            "Which type of attack attempts to gain sensitive information through deception?": "1",
            "What is an example of a brute-force attack?": "1",
            "What does 'XSS' stand for in web security?": "1",
            "What is a DDoS attack?": "2",
            "What is the main risk of using public Wi-Fi?": "2",
            "What is the purpose of malware?": "2",
            "What is social engineering?": "2",
            # (Continue adding answers corresponding to each easy question)
        }
    },
    "medium": {
        "questions": {
            "What is a common method for exploiting web application vulnerabilities?": [
                "1. Cross-Site Scripting (XSS)",
                "2. Denial of Service (DoS)",
                "3. Malware distribution",
                "4. Brute-force attacks"
            ],
            "Which tool is commonly used for network penetration testing?": [
                "1. Burp Suite",
                "2. Photoshop",
                "3. MS Office",
                "4. SQL Server"
            ],
            "What type of attack involves intercepting communication between two parties?": [
                "1. Man-in-the-middle attack",
                "2. Phishing",
                "3. Social engineering",
                "4. SQL injection"
            ],
            "What is the main function of a web application firewall (WAF)?": [
                "1. To protect against SQL injection",
                "2. To provide data encryption",
                "3. To manage network traffic",
                "4. To prevent unauthorized access"
            ],
            "What is the role of penetration testing?": [
                "1. To evaluate security measures",
                "2. To recover lost data",
                "3. To maintain hardware",
                "4. To enhance performance"
            ],
            "What does 'buffer overflow' refer to?": [
                "1. A memory management error",
                "2. An encryption method",
                "3. A network attack",
                "4. A security policy"
            ],
            "What is the purpose of port scanning?": [
                "1. To identify open ports on a system",
                "2. To improve internet speed",
                "3. To enhance security",
                "4. To recover lost data"
            ],
            "Which of the following is an example of a passive attack?": [
                "1. Eavesdropping",
                "2. DDoS",
                "3. Phishing",
                "4. SQL injection"
            ],
            "What does the term 'exfiltration' refer to?": [
                "1. Unauthorized transfer of data",
                "2. Data backup",
                "3. Data encryption",
                "4. Data analysis"
            ],
            "What is a common consequence of a successful DDoS attack?": [
                "1. Data loss",
                "2. Network downtime",
                "3. Increased performance",
                "4. None of the above"
            ],
            "Which protocol is commonly used for secure remote access?": [
                "1. SSH",
                "2. HTTP",
                "3. FTP",
                "4. Telnet"
            ],
            "What is the purpose of a honeypot in cybersecurity?": [
                "1. To lure attackers and gather intelligence",
                "2. To store sensitive data",
                "3. To manage user accounts",
                "4. To enhance network performance"
            ],
            # (Continue adding questions until reaching 200 medium questions)
        },
        "answers": {
            "What is a common method for exploiting web application vulnerabilities?": "1",
            "Which tool is commonly used for network penetration testing?": "1",
            "What type of attack involves intercepting communication between two parties?": "1",
            "What is the main function of a web application firewall (WAF)?": "1",
            "What is the role of penetration testing?": "1",
            "What does 'buffer overflow' refer to?": "1",
            "What is the purpose of port scanning?": "1",
            "Which of the following is an example of a passive attack?": "1",
            "What does the term 'exfiltration' refer to?": "1",
            "What is a common consequence of a successful DDoS attack?": "2",
            "Which protocol is commonly used for secure remote access?": "1",
            "What is the purpose of a honeypot in cybersecurity?": "1",
            # (Continue adding answers corresponding to each medium question)
        }
    },
    "hard": {
        "questions": {
            "What is the primary goal of an advanced persistent threat (APT)?": [
                "1. To steal data over time",
                "2. To disrupt operations",
                "3. To create malware",
                "4. To enhance security"
            ],
            "Which of the following is an example of an exploitation framework?": [
                "1. Metasploit",
                "2. Nmap",
                "3. Wireshark",
                "4. Burp Suite"
            ],
            "What is the purpose of a reverse shell in penetration testing?": [
                "1. To gain remote access to a system",
                "2. To encrypt data",
                "3. To analyze network traffic",
                "4. To enhance performance"
            ],
            "What does 'OSINT' stand for?": [
                "1. Open Source Intelligence",
                "2. Online Security Information",
                "3. Offensive Security Information",
                "4. Online System Intelligence"
            ],
            "What is the main purpose of code review in secure development?": [
                "1. To identify vulnerabilities",
                "2. To enhance performance",
                "3. To manage database",
                "4. To increase speed"
            ],
            "What does 'RAT' stand for in cybersecurity?": [
                "1. Remote Access Trojan",
                "2. Random Access Tool",
                "3. Real-time Analysis Tool",
                "4. Remote Attack Tool"
            ],
            "Which of the following is a method to bypass firewalls?": [
                "1. Tunneling",
                "2. Phishing",
                "3. Spoofing",
                "4. Keylogging"
            ],
            "What is the significance of the 'principle of least privilege'?": [
                "1. To limit user access to only what is necessary",
                "2. To enhance performance",
                "3. To manage data encryption",
                "4. To increase internet speed"
            ],
            "What is a common feature of advanced malware?": [
                "1. Stealth capabilities",
                "2. High performance",
                "3. Easy detection",
                "4. None of the above"
            ],
            "What does the term 'sandboxing' refer to?": [
                "1. Isolating programs to prevent harm to the host system",
                "2. Enhancing system performance",
                "3. Managing network traffic",
                "4. Data encryption"
            ],
            "What is the purpose of threat modeling?": [
                "1. To identify and prioritize potential threats",
                "2. To recover lost data",
                "3. To enhance user experience",
                "4. To manage hardware"
            ],
            # (Continue adding questions until reaching 150 hard questions)
        },
        "answers": {
            "What is the primary goal of an advanced persistent threat (APT)?": "1",
            "Which of the following is an example of an exploitation framework?": "1",
            "What is the purpose of a reverse shell in penetration testing?": "1",
            "What does 'OSINT' stand for?": "1",
            "What is the main purpose of code review in secure development?": "1",
            "What does 'RAT' stand for in cybersecurity?": "1",
            "Which of the following is a method to bypass firewalls?": "1",
            "What is the significance of the 'principle of least privilege'?": "1",
            "What is a common feature of advanced malware?": "1",
            "What does the term 'sandboxing' refer to?": "1",
            "What is the purpose of threat modeling?": "1",
            # (Continue adding answers corresponding to each hard question)
        }
    }
}

     # Scrollable layout for responsive design
        scroll_view = ScrollView(size_hint=(1, None), size=(Window.width, Window.height))
        inner_layout = BoxLayout(orientation='vertical', size_hint_y=None)
        inner_layout.bind(minimum_height=inner_layout.setter('height'))

        # Game title
        title_label = Label(text="Hacking Challenge", font_size=36, color=(1, 1, 0, 1), size_hint=(1, None), height=50)
        inner_layout.add_widget(title_label)

        # Welcome message
        self.status_label = Label(text="Welcome! Please log in or register.", font_size=24, color=(1, 1, 1, 1), size_hint=(1, None), height=50)
        inner_layout.add_widget(self.status_label)

        # User input
        self.username_input = TextInput(hint_text="Enter username", size_hint=(1, None), height=50)
        inner_layout.add_widget(self.username_input)

        # Buttons layout
        button_layout = BoxLayout(size_hint=(1, None), height=60, spacing=10)
        self.register_button = Button(text="Register", on_release=self.register_user, background_color=(0.2, 0.8, 0.2, 1))
        self.login_button = Button(text="Login", on_release=self.login_user, background_color=(0.2, 0.2, 0.8, 1))
        button_layout.add_widget(self.register_button)
        button_layout.add_widget(self.login_button)
        inner_layout.add_widget(button_layout)

        # Game level selection
        self.level_spinner = Spinner(text="Select Level", values=("easy", "medium", "hard"), size_hint=(1, None), height=50)
        inner_layout.add_widget(self.level_spinner)

        # Start Questions button
        self.start_hacking_button = Button(text="Start Hacking", on_release=self.start_questions, size_hint=(1, None), height=60, background_color=(0.8, 0.8, 0, 1))
        inner_layout.add_widget(self.start_hacking_button)

        # Question display
        self.question_label = Label(text="", font_size=22, color=(1, 1, 1, 1), size_hint=(1, None), height=60)
        inner_layout.add_widget(self.question_label)

        # Answer options
        self.option_buttons = []
        for i in range(4):
            btn = Button(text="", size_hint=(1, None), height=50, on_release=lambda instance, i=i: self.check_answer(i), background_color=(0.5, 0.5, 0.5, 1))
            inner_layout.add_widget(btn)
            self.option_buttons.append(btn)

        # Result and score display
        self.result_label = Label(text="", font_size=18, color=(1, 1, 1, 1), size_hint=(1, None), height=40)
        self.score_label = Label(text="Score: 0", font_size=18, color=(1, 1, 1, 1), size_hint=(1, None), height=40)
        inner_layout.add_widget(self.result_label)
        inner_layout.add_widget(self.score_label)

        # Hint and end game buttons
        self.hint_button = Button(text="Hint", on_release=self.get_hint, size_hint=(1, None), height=60, background_color=(0.8, 0.5, 0.2, 1))
        self.end_button = Button(text="End Game", on_release=self.end_game, size_hint=(1, None), height=60, background_color=(0.8, 0.2, 0.2, 1))
        inner_layout.add_widget(self.hint_button)
        inner_layout.add_widget(self.end_button)

        # External links
        self.website_button = Button(text="Website", on_release=lambda _: webbrowser.open("https://innovatewave.vercel.app/"), size_hint=(1, None), height=60, background_color=(0.2, 0.8, 0.2, 1))
        self.linkedin_button = Button(text="LinkedIn", on_release=lambda _: webbrowser.open("https://in.linkedin.com/in/harshit-mishra-mr-robot?trk=profile-badge"), size_hint=(1, None), height=60, background_color=(0.2, 0.2, 0.8, 1))
        self.github_button = Button(text="GitHub", on_release=lambda _: webbrowser.open("https://github.com/mishra9759harshit"), size_hint=(1, None), height=60, background_color=(0.2, 0.2, 0.8, 1))
        inner_layout.add_widget(self.website_button)
        inner_layout.add_widget(self.linkedin_button)
        inner_layout.add_widget(self.github_button)

        # Add inner layout to scroll view
        scroll_view.add_widget(inner_layout)
        self.add_widget(scroll_view)

        # Background color for better visuals
        with self.canvas.before:
            Color(0.1, 0.1, 0.1, 1)  # Dark background color
            self.rect = Rectangle(size=self.size, pos=self.pos)

        self.bind(size=self._update_rect, pos=self._update_rect)

    def _update_rect(self, instance, value):
        self.rect.pos = self.pos
        self.rect.size = self.size

    def load_users(self):
        if os.path.exists('users.json'):
            with open('users.json', "r") as f:
                return json.load(f)
        return {}

    def save_users(self):
        with open('users.json', "w") as f:
            json.dump(self.users, f)

    def register_user(self, instance):
        username = self.username_input.text.strip()
        if username in self.users:
            self.status_label.text = "Username already exists."
            return
        self.users[username] = {"score": 0}
        self.save_users()
        self.current_user = username
        self.status_label.text = f"User '{username}' registered successfully!"

    def login_user(self, instance):
        username = self.username_input.text.strip()
        if username not in self.users:
            self.status_label.text = "User not found. Please register."
            return
        self.current_user = username
        self.status_label.text = f"Welcome back, {username}!"

    def start_questions(self, instance):
        if not self.current_user:
            self.status_label.text = "Please log in first."
            return
        self.score = 0
        self.question_answers.clear()  # Clear previous questions and answers
        self.next_question()  # Show the first question

    def next_question(self):
        level = self.level_spinner.text
        questions = self.levels[level]["questions"]
        answers = self.levels[level]["answers"]

        if not questions:
            self.status_label.text = "No more questions available."
            return

        question, options = random.choice(list(questions.items()))
        self.question_label.text = question
        for i, option in enumerate(options):
            self.option_buttons[i].text = option
        self.correct_answer = answers[question]
        self.current_question = question
        
        # Store the question and answer for future reference
        self.question_answers.append((question, options, self.correct_answer))

        # Remove the question from the list after it has been shown
        del questions[question]

    def check_answer(self, selected_index):
        selected_answer = str(selected_index + 1)  # Convert index to answer number
        if selected_answer == self.correct_answer:
            self.score += 1
            self.result_label.text = "Correct!"
            self.play_sound(True)
        else:
            self.result_label.text = f"Wrong! Correct answer: {self.correct_answer}"
            self.play_sound(False)

        self.score_label.text = f"Score: {self.score}"
        self.next_question()  # Load next question

    def get_hint(self, instance):
        hint = f"Hint: The correct answer has {len(self.correct_answer)} letters."
        self.result_label.text = hint

    def end_game(self, instance):
        if self.current_user:
            self.users[self.current_user]["score"] = self.score
            self.save_users()
        self.status_label.text = f"Game over! Your final score: {self.score}"

    def play_sound(self, correct):
        sound_path = "sounds/notification-positive-bleep-joshua-chivers-1-00-01.mp3" if correct else "sounds/error-126627.mp3"
        sound = SoundLoader.load(sound_path)
        if sound:
            sound.play()

class HackingApp(App):
    def build(self):
        return HackingGame()

if __name__ == '__main__':
    HackingApp().run()