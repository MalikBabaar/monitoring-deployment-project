import psutil

def check_resources():
    cpu = psutil.cpu_percent()
    mem = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent

    if cpu > 80:
        print(f"[ALERT] High CPU Usage: {cpu}%")
    if mem > 80:
        print(f"[ALERT] High Memory Usage: {mem}%")
    if disk > 80:
        print(f"[ALERT] Low Disk Space: {disk}%")

if __name__ == "__main__":
    check_resources()

