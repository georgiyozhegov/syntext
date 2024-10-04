from g4f.client import Client
import json
from knowledge import Topics, PROMPT

client = Client()


def generate(prompt):
    response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            response_format="json",
    )
    return response.choices[0].message.content

topics = Topics()

with open("dataset.jsonl", "a") as output:
    while True:
        text = "Rate limit"
        while True:
            topic = topics.choose()
            prompt = PROMPT % topic
            try:
                text = generate(prompt)
                if not text.startswith("Rate limit") or text.startswith("One message"):
                    break
            except Exception as exception:
                print("Error:", exception)
        data = {
            "topic": topic,
            "text": text,
        }
        data = json.dumps(data, ensure_ascii=False) + "\n"
        print(data)
        output.write(data)
