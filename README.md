# SynText

Set of scripts that uses g4f to generate synthetic texts. You can find dataset generated using this tool [here](https://huggingface.co/datasets/georgiyozhegov/syntext).

# Usage

Generate dataset:

```bash
python generate.py
```

Then, process it:

```bash
python process.py > dataset-processed.jsonl
```

# Data

One generated row looks like this:

```
{
    "topic": "Экономический рост Испании в последние десятилетия",
    "questions": [
        "Каковы основные факторы, способствовавшие экономическому росту Испании?",
        "Как глобальные кризисы повлияли на экономику Испании?",
        "Какое значение имеет Испания в экономике Европейского Союза?"
    ],
    "article": "Испания, как одна из ведущих стран Европы, за последние ..."
}
```

Prompt used to instruct ChatGPT:

````
# Инструкции

- Для начала придумай какую-то тему которая относится к "%s". Напиши её в секции "Тема".
- В секции "Вопросы" напиши 3 вопроса, относящихся к этой теме.
- В секции "Текст" напиши статью, отвечающую на все 3 вопроса. 

# Формат вывода

```
# Тема

<тема>

# Вопросы

- <первый вопрос>
- <второй вопрос>
- <третий вопрос>

# Текст

<текст ответа>
```

# Требования

- Текст должен быть написан в стиле статьи или рассуждения.
- Не используй Markdown форматирование.
- Для математических формул используй LaTeX. Для выделения используй $$ (двойной знак доллара).
- Для выделения блоков кода используй ``` (тройные кавычки).
- Придерживайся традиционных понятий и норм русского менталитета.
- Старайся использовать простые слова в тексте когда это возможно.
- Пиши вдумчиво, кратка и понятно.
- Не дели статью на части по вопросам.
````

If you want to change topics used to generate questions, you can edit the `knowledge.py` file.

# References

- [g4f](https://github.com/xtekky/gpt4free)
