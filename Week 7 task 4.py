owasp_top_10 = {
    "A01: Broken Access Control":
        "Users can access data or perform actions that they are not authorized to access.",

    "A02: Cryptographic Failures":
        "Sensitive data is exposed because encryption or other data protection methods are weak or missing.",

    "A03: Injection":
        "An attacker sends malicious input, such as SQL commands, that the application mistakenly executes.",

    "A04: Insecure Design":
        "Security problems occur because the application was designed without enough security controls.",

    "A05: Security Misconfiguration":
        "Incorrect or insecure system settings create vulnerabilities that attackers can exploit.",

    "A06: Vulnerable and Outdated Components":
        "Using old or vulnerable software libraries and components can expose an application to known attacks.",

    "A07: Identification and Authentication Failures":
        "Weak login or authentication systems can allow attackers to access other users' accounts.",

    "A08: Software and Data Integrity Failures":
        "Applications may trust modified or unverified software, updates, or data, leading to security risks.",

    "A09: Security Logging and Monitoring Failures":
        "Poor logging and monitoring can prevent organizations from detecting and responding to attacks.",

    "A10: Server-Side Request Forgery (SSRF)":
        "An attacker tricks a server into making requests to unauthorized internal or external resources."
}

for risk, summary in owasp_top_10.items():
    print(f"{risk}: {summary}")
