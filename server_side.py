import json

def countLogsWith(strings: list[str]):
    counts = {keyword: 0 for keyword in strings}
    try:
        with open("/var/log/syslog", "r") as file:
            for line in file:
                lower_line = line.lower()
                for keyword in counts:
                    counts[keyword] += lower_line.count(keyword.lower())
        return [(keyword, counts[keyword]) for keyword in strings]
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    data = countLogsWith(['INFO', 'WARN', 'ERROR'])
    print(json.dumps(data))    
if __name__ == "__main__":
    main()


