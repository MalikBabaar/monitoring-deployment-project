import shutil
import os
from datetime import datetime

def backup_nginx_conf():
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    src = "/etc/nginx/nginx.conf"
    dest = f"/home/ubuntu/nginx_backup/nginx.conf.{timestamp}"
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    shutil.copy2(src, dest)
    print(f"[INFO] Backed up nginx.conf to {dest}")

if __name__ == "__main__":
    backup_nginx_conf()

