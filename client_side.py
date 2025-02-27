import Ssh_client
import pandas as pd
import os
import time
import json

def main():
    ssh = Ssh_client.Ssh_client(r"C:\Users\USER\Desktop\program\cloud\key-pair\my-key-pair.pem", "54.196.189.54", "ubuntu")
    data,error = ssh.runRemoteCommand("python3 server_side.py")
    formated_data = json.loads(data)
    if os.path.exists(r"C:\Users\USER\Desktop\program\cloud\endProject\severity_count.csv"):
        df = pd.read_csv(r"C:\Users\USER\Desktop\program\cloud\endProject\severity_count.csv")
        formated_data_df = pd.DataFrame(formated_data)
        df_filtered = df.dropna(axis=1, how='all')
        formated_data_df_filtered = formated_data_df.dropna(axis=1, how='all')
        df = pd.concat([df_filtered, formated_data_df_filtered], ignore_index=True)
        df.to_csv(r"C:\Users\USER\Desktop\program\cloud\endProject\severity_count.csv", index=False)
    else:
        df = pd.DataFrame(formated_data, index=[0])
        df.to_csv(r"C:\Users\USER\Desktop\program\cloud\endProject\severity_count.csv", index=False)        
if __name__ == "__main__":
    main()