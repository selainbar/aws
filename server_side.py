def countLogsWith(strings: list[str]):
    data = []
    try:
        with open("/var/log/syslog", "r") as file:
            logs = file.read()
        for keyword in strings:
            data.append((keyword, logs.lower().count(keyword.lower())))
        return data
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    data = countLogsWith(['INFO','WARN','ERROR'])
    formated_data = ''
    for item in data:
        formated_data += f'{item[0]}:{item[1]} '
    print(formated_data)
    
if __name__ == "__main__":
    main()

    
