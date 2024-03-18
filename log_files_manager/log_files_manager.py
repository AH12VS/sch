import os
from datetime import datetime

USER_WORK_SPACE = os.path.expanduser("~")
LOG_FILES_DIR = [f"../sch/logs/", f"{USER_WORK_SPACE}/logs/sch/"]
FILE_NAME = (datetime.now()).strftime("%Y-%m-%d-%H-%M-%S")

stat = 0

for dir in LOG_FILES_DIR:
    for file in os.listdir(dir):
        if os.stat(f"{dir}/{file}").st_size > 10485760: # 10485760B = 10MB
            try:
                os.replace(f"{dir}/{file}", f"{dir}/[{FILE_NAME}]{file}.bak")
                stat = 1
            except:
                stat = 0

if __name__ == "__main__":
    if stat:
        print("+-------------+")
        print("|Files Changed|")
        print("+-------------+")
    else:
        print("+----------------------+")
        print("|Failed to Change Files|")
        print("+----------------------+")
