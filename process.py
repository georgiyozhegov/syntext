import json
import mdtex2html

def main():
    with open("dataset.jsonl") as file:
        for line in file:
            data = json.loads(line)
            text = data["text"]

            try:
                _, text = text.split("# Тема")
                topic, text = text.split("# Вопросы")
                questions, text = text.split("# Текст")
                
                topic = topic.strip()

                questions = questions.strip().split("\n")
                questions = list(map(lambda q: q.split(" ", 1)[1], questions))

                text = mdtex2html.convert(text.strip())
                text = text.replace("xmlns=\"http://www.w3.org/1998/Math/MathML\" ", "")

                data = {
                        "topic": topic,
                        "questions": questions,
                        "article": text,
                }

                data = json.dumps(data, ensure_ascii=False) + "\n"
                print(data, end="")
            except:
                ...

if __name__ == "__main__":
    main()
