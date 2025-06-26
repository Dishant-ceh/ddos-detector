import time
from collections import defaultdict
# this tool is make by https.dishant.ceh
# Configuration
REQUEST_LIMIT = 10  # Max requests per IP allowed
TIME_WINDOW = 10    # Time window in seconds

# Data Structures
request_log = defaultdict(list)
blacklisted_ips = set()

# Simulated incoming requests
sample_ips = [
    "192.168.1.2", "192.168.1.3", "192.168.1.2", "192.168.1.2",
    "192.168.1.4", "192.168.1.2", "192.168.1.2", "192.168.1.2",
    "192.168.1.2", "192.168.1.2", "192.168.1.2", "192.168.1.2",
]

def process_request(ip):
    current_time = time.time()

    if ip in blacklisted_ips:
        print(f"🚫 BLOCKED: {ip} is blacklisted.")
        return

    # Keep only timestamps within the time window
    request_log[ip] = [t for t in request_log[ip] if current_time - t <= TIME_WINDOW]
    request_log[ip].append(current_time)

    if len(request_log[ip]) > REQUEST_LIMIT:
        blacklisted_ips.add(ip)
        print(f"⚠️ ALERT: {ip} exceeded limit and is now blacklisted.")
    else:
        print(f"✅ ALLOWED: {ip} ({len(request_log[ip])} requests)")

# Simulate requests
for ip in sample_ips:
    process_request(ip)
    time.sleep(0.5)  # Simulate delay
