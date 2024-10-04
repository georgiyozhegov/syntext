import json

def main():
    with open("dataset.jsonl") as file:
        for line in file:
            data = json.loads(line)
            text = data["text"]

            _, text = text.split("# Тема")
            topic, text = text.split("# Вопросы")
            questions, text = text.split("# Текст")
            
            topic = topic.strip()
            questions = questions.strip().split("\n")
            text = text.strip()

            questions = list(map(lambda q: q.split(" ", 1)[1], questions))

            data = {
                    "topic": topic,
                    "questions": questions,
                    "answer": text,
            }
            data = json.dumps(data, ensure_ascii=False) + "\n"
            print(data, end="")

if __name__ == "__main__":
    main()
