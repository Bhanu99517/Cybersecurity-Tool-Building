"""
===============================================================================
                        CYBERSECURITY TOOL FRAMEWORK
                    Defensive / Ethical Security Toolkit

 Modules:
 1. Port Scanner (Network auditing)
 2. Password Strength Analyzer
 3. Hash Generator (SHA-256)
 4. File Integrity Monitor
 5. Log Analyzer
 6. Threat Detection Engine
 7. Reporting Module
===============================================================================
"""

import socket
import hashlib
import os
import time
import re
from datetime import datetime


# =============================================================================
# 1️⃣ PORT SCANNER (DEFENSIVE USE)
# =============================================================================

class PortScanner:
    """
    Checks open ports on a target host.
    Used for auditing your own system.
    """

    def scan(self, host, ports):
        print(f"\nScanning {host}...")
        open_ports = []

        for port in ports:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)

            result = sock.connect_ex((host, port))
            if result == 0:
                print(f"Port {port} is OPEN")
                open_ports.append(port)

            sock.close()

        return open_ports


# =============================================================================
# 2️⃣ PASSWORD STRENGTH CHECKER
# =============================================================================

class PasswordAnalyzer:
    """
    Evaluates password strength.
    """

    def analyze(self, password):
        score = 0

        if len(password) >= 8:
            score += 1
        if re.search(r"[A-Z]", password):
            score += 1
        if re.search(r"[a-z]", password):
            score += 1
        if re.search(r"[0-9]", password):
            score += 1
        if re.search(r"[!@#$%^&*]", password):
            score += 1

        print(f"Password Strength Score: {score}/5")
        return score


# =============================================================================
# 3️⃣ HASH GENERATOR
# =============================================================================

class HashGenerator:
    """
    Generates SHA-256 hash.
    Useful for verifying file integrity.
    """

    def sha256(self, text):
        hash_value = hashlib.sha256(text.encode()).hexdigest()
        print("SHA-256:", hash_value)
        return hash_value


# =============================================================================
# 4️⃣ FILE INTEGRITY MONITOR
# =============================================================================

class FileIntegrityMonitor:
    """
    Detects if a file has been modified.
    """

    def calculate_hash(self, filepath):
        with open(filepath, "rb") as f:
            file_hash = hashlib.sha256(f.read()).hexdigest()
        return file_hash

    def monitor(self, filepath):
        print("\nMonitoring file:", filepath)
        baseline = self.calculate_hash(filepath)

        time.sleep(2)  # simulate delay

        current_hash = self.calculate_hash(filepath)

        if baseline != current_hash:
            print("File integrity compromised!")
        else:
            print("File is unchanged.")


# =============================================================================
# 5️⃣ LOG ANALYZER
# =============================================================================

class LogAnalyzer:
    """
    Analyzes logs for suspicious activity.
    """

    def detect_failed_logins(self, logfile):
        print("\nAnalyzing logs...")

        suspicious_count = 0

        with open(logfile, "r") as f:
            for line in f:
                if "FAILED LOGIN" in line:
                    suspicious_count += 1

        print("Failed login attempts:", suspicious_count)
        return suspicious_count


# =============================================================================
# 6️⃣ THREAT DETECTION ENGINE
# =============================================================================

class ThreatDetectionEngine:
    """
    Basic rule-based anomaly detection.
    """

    def analyze_activity(self, failed_attempts):
        if failed_attempts > 5:
            print("Potential Brute Force Attack Detected!")
        else:
            print("Activity normal.")


# =============================================================================
# 7️⃣ REPORTING MODULE
# =============================================================================

class ReportGenerator:
    """
    Generates simple security report.
    """

    def generate(self, open_ports, password_score):
        print("\n=== SECURITY REPORT ===")
        print("Open Ports:", open_ports)
        print("Password Strength Score:", password_score)
        print("Generated at:", datetime.now())


# =============================================================================
# MAIN EXECUTION PIPELINE
# =============================================================================

def main():

    # 1. Port scan (localhost only)
    scanner = PortScanner()
    open_ports = scanner.scan("127.0.0.1", [22, 80, 443, 8080])

    # 2. Password analysis
    password_tool = PasswordAnalyzer()
    password_score = password_tool.analyze("Secure@123")

    # 3. Hash generation
    hash_tool = HashGenerator()
    hash_tool.sha256("SensitiveData")

    # 4. File monitoring (create sample file)
    sample_file = "sample.txt"
    with open(sample_file, "w") as f:
        f.write("Original content")

    monitor = FileIntegrityMonitor()
    monitor.monitor(sample_file)

    # 5. Log analysis (create sample log)
    sample_log = "log.txt"
    with open(sample_log, "w") as f:
        f.write("FAILED LOGIN\nFAILED LOGIN\nSUCCESS\n")

    analyzer = LogAnalyzer()
    failed_attempts = analyzer.detect_failed_logins(sample_log)

    # 6. Threat detection
    threat_engine = ThreatDetectionEngine()
    threat_engine.analyze_activity(failed_attempts)

    # 7. Reporting
    report = ReportGenerator()
    report.generate(open_ports, password_score)


if __name__ == "__main__":
    main()
