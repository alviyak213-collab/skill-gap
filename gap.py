skills = [
    "Python",
    "Linux",
    "Networking",
    "Web Security",
    "Incident Response"
]

required_level = {
    "Python": 3,
    "Linux": 3,
    "Networking": 3,
    "Web Security": 3,
    "Incident Response": 3
}

level_names = {
    1: "Basic",
    2: "Intermediate",
    3: "Advanced"
}

questions = [
    {
        "level": 1,
        "question": "Which brackets are used to create a list in Python?",
        "options": ["{ }", "[ ]", "( )", "< >"],
        "answer": "B"
    },
    {
        "level": 1,
        "question": "Which function is used to display output in Python?",
        "options": ["display()", "show()", "print()", "output()"],
        "answer": "C"
    },
    {
        "level": 2,
        "question": "What is the primary purpose of try-except in Python?",
        "options": [
            "To create loops",
            "To handle errors or exceptions",
            "To declare variables",
            "To delete files"
        ],
        "answer": "B"
    },
    {
        "level": 2,
        "question": "Which method can be used to safely retrieve a value from a Python dictionary?",
        "options": ["get()", "find()", "search()", "value()"],
        "answer": "A"
    },
    {
        "level": 3,
        "question": "What is the primary use of asyncio in Python?",
        "options": [
            "Image editing",
            "Asynchronous programming",
            "Database creation",
            "Operating system installation"
        ],
        "answer": "B"
    },
    {
        "level": 3,
        "question": "Which standard Python module is commonly used for hashing?",
        "options": ["hashlib", "securitylib", "securehash", "cryptolib"],
        "answer": "A"
    },
    {
        "level": 1,
        "question": "Which Linux command displays the current working directory?",
        "options": ["pwd", "dir", "where", "locate"],
        "answer": "A"
    },
    {
        "level": 1,
        "question": "Which Linux command is used to list files and directories?",
        "options": ["show", "ls", "listall", "files"],
        "answer": "B"
    },
    {
        "level": 2,
        "question": "Which Linux command is used to change file permissions?",
        "options": ["chmod", "chfile", "permission", "access"],
        "answer": "A"
    },
    {
        "level": 2,
        "question": "What is the common use of the grep command?",
        "options": [
            "Compress files",
            "Search for text or patterns",
            "Create users",
            "Shut down the system"
        ],
        "answer": "B"
    },
    {
        "level": 3,
        "question": "What is the purpose of sudo in Linux?",
        "options": [
            "Connect to the internet",
            "Execute commands with elevated privileges",
            "Compress files",
            "Generate passwords"
        ],
        "answer": "B"
    },
    {
        "level": 3,
        "question": "What information is primarily provided by the Linux ss command?",
        "options": [
            "Network sockets and connections",
            "Disk formatting",
            "User passwords",
            "File encryption"
        ],
        "answer": "A"
    },
    {
        "level": 1,
        "question": "What is the primary purpose of an IP address?",
        "options": [
            "To identify and address a device or network interface",
            "To store passwords",
            "To encrypt files",
            "To design websites"
        ],
        "answer": "A"
    },
    {
        "level": 1,
        "question": "What is the main purpose of DNS?",
        "options": [
            "To resolve domain names into IP addresses",
            "To compress files",
            "To encrypt passwords",
            "To shut down a computer"
        ],
        "answer": "A"
    },
    {
        "level": 2,
        "question": "What does the 'S' in HTTPS generally stand for?",
        "options": ["Simple", "Secure", "System", "Server"],
        "answer": "B"
    },
    {
        "level": 2,
        "question": "Which is an important characteristic of TCP?",
        "options": [
            "Connection-oriented and reliable communication",
            "Always faster than UDP",
            "No error handling",
            "Only local communication"
        ],
        "answer": "A"
    },
    {
        "level": 3,
        "question": "What is the primary purpose of subnetting?",
        "options": [
            "To divide a network into smaller logical networks",
            "To change passwords",
            "To host websites",
            "To encrypt data"
        ],
        "answer": "A"
    },
    {
        "level": 3,
        "question": "What is the primary security role of a firewall?",
        "options": [
            "To allow or block network traffic based on defined rules",
            "To increase CPU speed",
            "To automatically back up files",
            "To generate passwords"
        ],
        "answer": "A"
    },
    {
        "level": 1,
        "question": "Which is an important characteristic of a strong password?",
        "options": [
            "Using only your name",
            "Keeping it very short",
            "Making it long and difficult to guess",
            "Using the same password everywhere"
        ],
        "answer": "C"
    },
    {
        "level": 1,
        "question": "What does HTTPS provide for website communication?",
        "options": [
            "An encrypted connection",
            "Free internet",
            "A faster processor",
            "Unlimited storage"
        ],
        "answer": "A"
    },
    {
        "level": 2,
        "question": "SQL Injection is primarily what type of vulnerability?",
        "options": [
            "Database or query-related injection vulnerability",
            "Hardware failure",
            "Network cable problem",
            "Operating system update"
        ],
        "answer": "A"
    },
    {
        "level": 2,
        "question": "What is the difference between authentication and authorization?",
        "options": [
            "Authentication verifies identity; authorization determines permissions",
            "Both are exactly the same",
            "Authentication gives permissions",
            "Authorization verifies identity"
        ],
        "answer": "A"
    },
    {
        "level": 3,
        "question": "In an XSS vulnerability, where can malicious content execute?",
        "options": [
            "In the victim's browser",
            "Inside the keyboard",
            "Inside the monitor hardware",
            "Inside the router power supply"
        ],
        "answer": "A"
    },
    {
        "level": 3,
        "question": "What does the principle of least privilege mean?",
        "options": [
            "Giving only the minimum permissions required",
            "Giving everyone administrator access",
            "Removing passwords",
            "Disabling security checks"
        ],
        "answer": "A"
    },
    {
        "level": 1,
        "question": "Which of the following can be considered a cybersecurity incident?",
        "options": [
            "Unauthorized access or a suspicious security event",
            "Normal document editing",
            "Changing a computer wallpaper",
            "A normal software update"
        ],
        "answer": "A"
    },
    {
        "level": 1,
        "question": "What is an important action after noticing a suspicious security incident?",
        "options": [
            "Preserve evidence and report it to the appropriate team",
            "Delete all files",
            "Erase the logs",
            "Ignore the incident"
        ],
        "answer": "A"
    },
    {
        "level": 2,
        "question": "What is the purpose of containment in incident response?",
        "options": [
            "To limit the impact or spread of the incident",
            "To destroy evidence",
            "To publicly share passwords",
            "To permanently delete the system"
        ],
        "answer": "A"
    },
    {
        "level": 2,
        "question": "Why are security logs useful during incident investigation?",
        "options": [
            "They provide records of events and activities",
            "They increase computer speed",
            "They automatically change passwords",
            "They increase internet speed"
        ],
        "answer": "A"
    },
    {
        "level": 3,
        "question": "What does eradication mean in incident response?",
        "options": [
            "Removing the root cause or malicious presence",
            "Ignoring the incident",
            "Deleting logs",
            "Permanently removing users"
        ],
        "answer": "A"
    },
    {
        "level": 3,
        "question": "What is the main purpose of the lessons learned phase?",
        "options": [
            "To prevent future incidents and improve response",
            "To delete evidence",
            "To unnecessarily format the system",
            "To hide the incident"
        ],
        "answer": "A"
    }
]

skill_scores = {
    "Python": 0,
    "Linux": 0,
    "Networking": 0,
    "Web Security": 0,
    "Incident Response": 0
}

def run_terminal_quiz():
    total_score = 0

    print("\n===== SKILLSAARTHI CYBERSECURITY QUIZ =====")
    print("Total Questions:", len(questions))
    input("\nPress Enter to start...")

    for index, q in enumerate(questions):
        print("\nQuestion", index + 1, "of", len(questions))
        print("Level:", level_names[q["level"]])
        print(q["question"])

        for i, option in enumerate(q["options"]):
            print(chr(65 + i) + ".", option)

        user_answer = input("Your answer (A/B/C/D): ").upper().strip()

        if user_answer == q["answer"]:
            print("Correct!")
            total_score += 1
        else:
            print("Wrong!")
            print("Correct Answer:", q["answer"])

    print("\n===== FINAL RESULT =====")
    print("Total Questions:", len(questions))
    print("Correct Answers:", total_score)
    print("Wrong Answers:", len(questions) - total_score)
    print("Percentage:", round((total_score / len(questions)) * 100, 2), "%")


if __name__ == "__main__":
    run_terminal_quiz()