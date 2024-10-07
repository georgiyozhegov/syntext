from g4f.client import Client
import json
from knowledge import CORRECTION_PROMPT

client = Client()

def generate(prompt):
    response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            response_format="json",
    )
    return response.choices[0].message.content

with open("dataset-corrected.jsonl", "a") as output:
    for line in open("dataset.jsonl"):
        data = json.loads(line)
        text = data["article"]
        
        prompt = CORRECTION_PROMPT % text
        text = "Rate limit"
        while True:
            try:
                text = generate(prompt)
                if not (text.startswith("Rate limit") or text.startswith("One message")):
                    break
            except Exception as exception:
                print("Error:", exception)

        data = {
            "topic": data["topic"],
            "questions": data["questions"],
            "article": text,
        }

        data = json.dumps(data, ensure_ascii=False) + "\n"
        print(data)
        output.write(data)
