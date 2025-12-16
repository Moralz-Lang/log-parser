import json
import re
import sys

def parse_log_line(line):
    """
    Parse Linux auth.log style entries.
    Windows logs should be exported to text before parsing.
    """
    pattern = r'^(\w+\s+\d+\s+\d+:\d+:\d+)\s+([\w.-]+)\s+([\w/-]+)\[(\d+)\]:\s+(.*)'
    match = re.match(pattern, line)
    if not match:
        return None

    timestamp, host, service, pid, message = match.groups()

    ip_match = re.search(r'(\d+\.\d+\.\d+\.\d+)', message)
    ip = ip_match.group(1) if ip_match else None

    return {
        "timestamp": timestamp,
        "host": host,
        "service": service,
        "pid": pid,
        "message": message,
        "ip": ip,
        "raw": line.strip()
    }

def main():
    if len(sys.argv) != 2:
        print("Usage: python log_parser.py <logfile>")
        sys.exit(1)

    logfile = sys.argv[1]
    parsed = []

    with open(logfile, "r", errors="ignore") as f:
        for line in f:
            result = parse_log_line(line.strip())
            if result:
                parsed.append(result)

    with open("../output/parsed_logs.json", "w") as out:
        json.dump(parsed, out, indent=4)

    print(f"[+] Parsed {len(parsed)} log entries")

if __name__ == "__main__":
    main()
