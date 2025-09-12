import time

def monitor_log(log_file, keyword, timeout=5):
    with open(log_file, 'r') as f:
        f.seek(0, 2)  # Go to the end of the file
        last_check = time.time()

        while True:
            line = f.readline()
            if not line:
                # If no new line has appeared for `timeout` seconds, print "No error found"
                if time.time() - last_check >= timeout:
                    print("No error found")
                    last_check = time.time()
                time.sleep(1)
                continue

            if keyword in line:
                print(f"[ALERT] Found '{keyword}': {line.strip()}")
                last_check = time.time()

if __name__ == "__main__":
    monitor_log("/var/log/nginx/error.log", "error")

