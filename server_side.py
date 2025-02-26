def countLogsWith(string: str):
    try:
        with open("/var/log/syslog", "r") as file:
            logs = file.read()
        count = logs.lower().count(string.lower())
        return count
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    data = []
    output = countLogsWith("INFO")
    data.append(('INFO',output))
    output = countLogsWith("WARN")
    data.append(('WARN',output))
    output = countLogsWith("ERROR")
    data.append(('ERROR',output))
    with open("data.txt", "w") as file:
        for item in data:
            file.write(f"{item[0]}:{item[1]} ")

if __name__ == "__main__":
    main()
    
