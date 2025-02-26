import Ssh_client
import pandas as pd
import subprocess
import os
import time

def main():
    ssh = Ssh_client.Ssh_client(r"C:\Users\USER\Desktop\program\cloud\key-pair\my-key-pair.pem", "54.196.189.54", "ubuntu")
    ssh.runRemoteCommand("python3 server_side.py")
    data = None
    subprocess.run(["scp", "-i", r"C:\Users\USER\Desktop\program\cloud\key-pair\my-key-pair.pem", "ubuntu@54.196.189.54:/home/ubuntu/data.txt", r"C:\Users\USER\Desktop\program\cloud\endProject\data.txt"])
    with open(r"C:\Users\USER\Desktop\program\cloud\endProject\data.txt", "r") as file:
        data = file.read()

    formated_data = {"Time stamp": time.time()}
    severity_count = data.split(" ")
    for log in severity_count:
        if log.strip() == "":
            continue
        spilted_log = log.split(":")
        formated_data[spilted_log[0]] = int(spilted_log[1])
    
    if os.path.exists(r"C:\Users\USER\Desktop\program\cloud\endProject\severity_count.csv"):
        df = pd.read_csv(r"C:\Users\USER\Desktop\program\cloud\endProject\severity_count.csv")
        formated_data_df = pd.DataFrame(formated_data, index=[0])
        df = pd.concat([df, formated_data_df], ignore_index=True)
        df.to_csv(r"C:\Users\USER\Desktop\program\cloud\endProject\severity_count.csv", index=False)
    else:
        df = pd.DataFrame(formated_data, index=[0])
        df.to_csv(r"C:\Users\USER\Desktop\program\cloud\endProject\severity_count.csv", index=False)
        os.remove(r"C:\Users\USER\Desktop\program\cloud\endProject\data.txt")
        
if __name__ == "__main__":
    main()