import json
import time
def countLogsWith(strings: list[str]):
    counts = {keyword: 0 for keyword in strings}
    try:
        with open("/var/log/syslog", "r") as file:
            content = file.read()
        logs = content.split("\n")
        for log in logs:
            words = log.split()
            lower_words = [word.lower() for word in words]
            for keyword in counts:
                if keyword.lower() in lower_words:
                    counts[keyword] += 1
                    break  # only count once per log!
        data = {"timestamp": time.time()}
        data.update(counts)
        return data
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    data = countLogsWith(['INFO', 'WARN', 'ERROR'])
    print(json.dumps(data))    
if __name__ == "__main__":
    main()


