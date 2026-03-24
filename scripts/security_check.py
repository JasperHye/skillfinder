import sys
import argparse
import urllib.parse
import re

# Suspicious code patterns (for basic static scanning of target code)
SUSPICIOUS_PATTERNS = [
    r"eval\s*\(",
    r"exec\s*\(",
    r"os\.system\s*\(",
    r"subprocess\.\w+\s*\(.+shell\s*=\s*True",
    r"__import__\s*\(",
    r"compile\s*\(.+exec",
]

# Sensitive path keywords (check if the code attempts to access high-risk directories)
SENSITIVE_PATHS = [
    ".ssh", ".env", "credentials", "id_rsa",
    "passwd", "shadow", "token", "secret",
]

def validate_target(target):
    """
    Validate the format of the incoming scan target.
    Allows valid URLs (http/https), package slugs, or local file paths.
    """
    parsed = urllib.parse.urlparse(target)
    if parsed.scheme in ("http", "https") and parsed.netloc:
        return True
    
    # Allow local path formats containing path separators and extensions
    if all(c.isalnum() or c in "-_./\\" for c in target):
        return True
    return False

def scan_content(content):
    """
    Perform a basic static pattern matching scan on the code text content.
    Returns a list of detected suspicious signals.
    """
    findings = []
    for i, line in enumerate(content.split("\n"), 1):
        for pattern in SUSPICIOUS_PATTERNS:
            if re.search(pattern, line):
                findings.append(f"L{i}: Suspicious call pattern detected")
                break
        for path_kw in SENSITIVE_PATHS:
            if path_kw in line.lower():
                findings.append(f"L{i}: Sensitive path keyword involved")
                break
    return findings

def scan_skill(target):
    """
    Execute basic security compliance checks on the specified target.
    This script is a pure Python implementation and doesn't rely on external CLI tools.
    Exit code: 0 = Pass, 1 = Fail.
    """
    if not validate_target(target):
        print("[!] Invalid input format. Only accepts http/https links or alphanumeric slugs.")
        sys.exit(1)

    print(f"[*] Performing basic compliance check on target: {target} ...")

    # If it's a URL, only perform format validation (content scanning requires download first)
    parsed = urllib.parse.urlparse(target)
    if parsed.scheme in ("http", "https"):
        print("[+] URL format check passed. Deep content scanning will execute after download.")
        sys.exit(0)

    # If it's a local path or slug, attempt to read and scan
    try:
        with open(target, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
        findings = scan_content(content)
        if findings:
            print(f"[!] Detected {len(findings)} suspicious signals:")
            count = 0
            for f_item in findings:
                if count >= 5: break
                print(f"    - {f_item}")
                count += 1
            sys.exit(1)
        else:
            print("[+] Basic compliance check passed. No suspicious patterns found.")
            sys.exit(0)
    except FileNotFoundError:
        # Slug mode, no local file to scan, only format validation done
        print(f"[+] Slug '{target}' format check passed.")
        sys.exit(0)
    except Exception:
        print("[-] An unknown error occurred during the check.")
        sys.exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Built-in Compliance Scanner")
    parser.add_argument("target", help="URL, local file path, or component slug to check")
    args = parser.parse_args()
    scan_skill(args.target)
