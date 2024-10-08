COUNTRIES = [
    "Австралия",
    "Австрия",
    "Бразилия",
    "Великобритания",
    "Германия",
    "Греция",
    "Дания",
    "Индия",
    "Испания",
    "Италия",
    "Канада",
    "Китай",
    "Мексика",
    "Нидерланды",
    "Новая Зеландия",
    "Норвегия",
    "Польша",
    "Россия",
    "Саудовская Аравия",
    "Сингапур",
    "США",
    "Турция",
    "Украина",
    "Финляндия",
    "Франция",
    "Чехия",
    "Швеция",
    "Швейцария",
    "Южная Корея",
    "Япония",
]

RELIGION = [
    "Учение",
    "Ритуалы и обряды",
    "Мораль",
    "Символы",
    "История",
]

HISTORY = [
    "Главные события",
    "Главные личности",
]

TEORY_AND_PROBLEMS = [
    "Теория",
    "Решение простых задач",
    "Решение сложных задач",
]

TEORY_AND_FACTS = [
    "Теория",
    "Интересные факты",
]

TEORY_WITH_EXAMPLES = [
    "Теория",
    "Примеры",
]

PROGRAMMING_LANGUAGE = [
    "Синтаксис",
    "Структуры данных и типы переменных",
    "Операторы и выражения",
    "Условные конструкции",
    "Циклы",
    "Функции",
    "Встроенные модули и библиотеки",
]

TOPICS = {
    "Наука": {
        "Математика": {
            "Арифметика": {
                "Операции": TEORY_AND_PROBLEMS,
                "Числовые системы": TEORY_AND_PROBLEMS + [
                    "Натуральные числа",
                    "Целые числа",
                    "Рациональные числа",
                    "Иррациональные числа",
                ],
                "Свойства чисел": TEORY_AND_PROBLEMS,
            },
            "Алгебра": {
                "Переменные и константы": TEORY_AND_PROBLEMS,
                "Члены и коэффициенты": TEORY_AND_PROBLEMS,
                "Линейные уравнения": TEORY_AND_PROBLEMS,
                "Квадратные уравнения": TEORY_AND_PROBLEMS,
                "Системы уравнений": TEORY_AND_PROBLEMS,
                "Линейные неравенства": TEORY_AND_PROBLEMS,
                "Квадратные неравенства": TEORY_AND_PROBLEMS,
                "Функции": TEORY_AND_PROBLEMS,
                "Многочлены": TEORY_AND_PROBLEMS,
            },
            "Геометрия": {
                "Планиметрия": {
                    "Треугольник": TEORY_AND_PROBLEMS,
                    "Квадрат": TEORY_AND_PROBLEMS,
                    "Прямоугольник": TEORY_AND_PROBLEMS,
                    "Ромб": TEORY_AND_PROBLEMS,
                    "Трапеция": TEORY_AND_PROBLEMS,
                    "Параллелограмм": TEORY_AND_PROBLEMS,
                    "Пятиугольник": TEORY_AND_PROBLEMS,
                    "Шестиугольник": TEORY_AND_PROBLEMS,
                    "Круг": TEORY_AND_PROBLEMS,
                    "Эллипс": TEORY_AND_PROBLEMS,
                    "Полукруг": TEORY_AND_PROBLEMS,
                },
                "Тригонометрия": {
                    "Связь между углами и сторонами треугольников": TEORY_AND_PROBLEMS,
                    "Тригонометрические функции": TEORY_AND_PROBLEMS,
                },
                "Пространственная": {
                    "Куб": TEORY_AND_PROBLEMS,
                    "Сфера": TEORY_AND_PROBLEMS,
                    "Цилиндр": TEORY_AND_PROBLEMS,
                    "Конус": TEORY_AND_PROBLEMS,
                    "Пирамида": TEORY_AND_PROBLEMS,
                },
            },
            "Математический анализ": {
                "Пределы и непрерывность": {
                    "Предел последовательности": TEORY_AND_PROBLEMS,
                    "Предел функции": TEORY_AND_PROBLEMS,
                    "Непрерывные функции": TEORY_AND_PROBLEMS,
                },
                "Производные и дифференцирование": {
                    "Правила дифференцирования": TEORY_AND_PROBLEMS,
                    "Применение производной": TEORY_AND_PROBLEMS,
                },
                "Интегралы и интегрирование": {
                    "Определенный и неопределенный интеграл": TEORY_AND_PROBLEMS,
                    "Методы интегрирования": TEORY_AND_PROBLEMS,
                },
                "Ряды и последовательности": {
                    "Сходящиеся и расходящиеся ряды": TEORY_AND_PROBLEMS,
                    "Тесты на сходимость": TEORY_AND_PROBLEMS,
                },
            },
            "Дискретная": {
                "Комбинаторика": {
                    "Перестановки": TEORY_AND_PROBLEMS,
                    "Сочетания": TEORY_AND_PROBLEMS,
                    "Размещения": TEORY_AND_PROBLEMS,
                    "Факториалы": TEORY_AND_PROBLEMS,
                },
                "Теория графов": {
                    "Типы графов": TEORY_AND_PROBLEMS,
                    "Связные графы": TEORY_AND_PROBLEMS,
                    "Лемма о рукопожатиях": TEORY_AND_PROBLEMS,
                    "Остовные деревья": TEORY_AND_PROBLEMS,
                },
            },
            "Статистика": {
                "Описательная": TEORY_AND_PROBLEMS,
                "Вероятностные распределения": TEORY_AND_PROBLEMS,
                "Инференциальная": TEORY_AND_PROBLEMS,
                "Корреляционный анализ": TEORY_AND_PROBLEMS,
            },
            "Теория вероятностей": {
                "Основные понятия": TEORY_AND_PROBLEMS,
                "Основные правила": TEORY_AND_PROBLEMS,
                "Условная вероятность": TEORY_AND_PROBLEMS,
                "Распределения вероятностей": TEORY_AND_PROBLEMS,
            },
            "История": HISTORY,
        },
        "Физика": {
            "Механика": {
                "Законы Ньютона": TEORY_AND_FACTS,
                "Динамика и статика": TEORY_AND_FACTS,
                "Кинематика": TEORY_AND_FACTS,
                "Силы и движение": TEORY_AND_FACTS,
                "Энергия и работа": TEORY_AND_FACTS,
            },
            "Термодинамика": {
                "Законы термодинамики": TEORY_AND_FACTS,
                "Тепловые машины": TEORY_AND_FACTS,
                "Изменение внутренней энергии": TEORY_AND_FACTS,
                "Процессы теплопередачи": TEORY_AND_FACTS,
            },
            "Электромагнетизм": {
                "Электрические поля и заряды": TEORY_AND_FACTS,
                "Магнитные поля": TEORY_AND_FACTS,
                "Закон Ома": TEORY_AND_FACTS,
                "Электромагнитная индукция": TEORY_AND_FACTS,
            },
            "Оптика": {
                "Световые волны и их свойства": TEORY_AND_FACTS,
                "Линзы и зеркала": TEORY_AND_FACTS,
                "Интерференция и дифракция": TEORY_AND_FACTS,
                "Оптические приборы": TEORY_AND_FACTS,
            },
            "Квантовая": {
                "Квантовые состояния": TEORY_AND_FACTS,
                "Принцип неопределенности": TEORY_AND_FACTS,
                "Квантовая запутанность": TEORY_AND_FACTS,
                "Структура атома": TEORY_AND_FACTS,
            },
            "История": HISTORY,
        },
        "Химия": {
            "Неорганическая": {
                "Химические элементы и соединения": TEORY_AND_FACTS,
                "Реакции и их механизмы": TEORY_AND_FACTS,
                "Кислоты, основания и соли": TEORY_AND_FACTS,
            },
            "Органическая": {
                "Углеводороды и их производные": TEORY_AND_FACTS,
                "Реакции органических соединений": TEORY_AND_FACTS,
                "Структура и свойства органических молекул": TEORY_AND_FACTS,
            },
            "Биохимия": {
                "Метаболизм": TEORY_AND_FACTS,
                "Структура белков, углеводов и жиров": TEORY_AND_FACTS,
                "Генетическая информация": TEORY_AND_FACTS,
            },
            "История": HISTORY,
        },
        "Биология": {
            "Ботаника": {
                "Структура растений": TEORY_AND_FACTS,
                "Фотосинтез и дыхание растений": TEORY_AND_FACTS,
                "Размножение растений": TEORY_AND_FACTS,
            },
            "Зоология": {
                "Классификация животных": TEORY_AND_FACTS,
                "Поведение животных": TEORY_AND_FACTS,
                "Экосистемы животных": TEORY_AND_FACTS,
            },
            "Микробиология": {
                "Бактерии и вирусы": TEORY_AND_FACTS,
                "Микробные экосистемы": TEORY_AND_FACTS,
                "Применение микробиологии в медицине": TEORY_AND_FACTS,
            },
            "Физиология": {
                "Функции органов и систем организма": TEORY_AND_FACTS,
                "Гомеостаз": TEORY_AND_FACTS,
            },
            "Антропология": {
                "Эволюция человека": TEORY_AND_FACTS,
                "Культурная антропология": TEORY_AND_FACTS,
            },
            "Генетика": {
                "Наследственность и вариации": TEORY_AND_FACTS,
                "Генетическое кодирование": TEORY_AND_FACTS,
            },
            "История": HISTORY,
        },
        "География": {
            "Физическая": {
                "Структура и динамика географической оболочки": TEORY_AND_FACTS,
                "Природные комплексы и их компоненты": TEORY_AND_FACTS,
                "Геоморфология, климатология, гидрология": TEORY_AND_FACTS,
                "Биогеография и зоогеография": TEORY_AND_FACTS,
                "Антропогенные изменения ландшафта": TEORY_AND_FACTS,
            },
            "Социальная": {
                "Распределение населения и культурные аспекты": TEORY_AND_FACTS,
                "Урбанизация и её влияние на общество": TEORY_AND_FACTS,
                "Социальные структуры и их географические проявления": TEORY_AND_FACTS,
            },
            "Экономическая": {
                "Экономические системы и их пространственное распределение": TEORY_AND_FACTS,
                "Влияние природных ресурсов на экономику": TEORY_AND_FACTS,
                "Глобализация и её географические аспекты": TEORY_AND_FACTS,
            },
            "Страны": COUNTRIES,
            "История": HISTORY,
        },
        "Психология": {
            "Социальная": {
                "Изучение группового поведения": TEORY_AND_FACTS,
                "Влияние общества на индивидуальное поведение": TEORY_AND_FACTS,
                "Социальные стереотипы и предвзятости": TEORY_AND_FACTS,
                "Межличностные отношения и коммуникация": TEORY_AND_FACTS,
            },
            "История": HISTORY,
        },
        "Информатика": {
            "Интернет": {
                "Архитектура": TEORY_AND_FACTS,
                "Протоколы и технологии": {
                    "TCP/IP": TEORY_AND_FACTS,
                    "HTTP/HTTPS": TEORY_AND_FACTS,
                    "DNS": TEORY_AND_FACTS,
                },
            },
            "Искуственный интеллект": {
                "Машинное обучение": {
                    "Обучение с учителем": TEORY_AND_FACTS,
                    "Обучение без учителя": TEORY_AND_FACTS,
                    "Обучение с подкреплением": TEORY_AND_FACTS,
                },
                "Применение": {
                    "Компьютерное зрение": TEORY_AND_FACTS,
                    "Обработка естественного языка": TEORY_AND_FACTS,
                    "ChatGPT": TEORY_AND_FACTS,
                    "Робототехника": TEORY_AND_FACTS,
                },
            },
            "Программирование": {
                "Алгоритмы": TEORY_WITH_EXAMPLES,
                "Структуры данных": TEORY_WITH_EXAMPLES,
                "Языки программирования": {
                    "Rust": PROGRAMMING_LANGUAGE + [
                        "Система владения памятью",
                        "Типы данных",
                    ],
                    "Python": PROGRAMMING_LANGUAGE,
                    "C": PROGRAMMING_LANGUAGE + [
                        "Указатели и массивы",
                        "Структуры и объединения",
                    ],
                    "C++": PROGRAMMING_LANGUAGE + [
                        "Шаблоны",
                        "Указатели и ссылки",
                        "Обработка исключений"
                    ],
                },
                "Методы программирования": TEORY_AND_FACTS,
            },
            "Компьютерные системы": {
                "Архитектура компьютера": TEORY_AND_FACTS,
                "Операционные системы": {
                    "Linux": TEORY_AND_FACTS,
                    "Windows": TEORY_AND_FACTS,
                    "MacOS": TEORY_AND_FACTS,
                }
            },
            "История": HISTORY,
        },
        "Лингвистика": {
            "Фонетика": {
                "Звуки языка и их классификация": TEORY_AND_FACTS,
                "Акустическая фонетика и артикуляция звуков": TEORY_AND_FACTS,
                "Фонемы и аллофоны": TEORY_AND_FACTS,
            },
            "Морфология": {
                "Структура слов и морфемы": TEORY_AND_FACTS,
                "Словообразование и словоизменение": TEORY_AND_FACTS,
            },
            "Синтаксис": {
                "Структура предложений и правила их построения": TEORY_AND_FACTS,
                "Типы предложений": TEORY_AND_FACTS,
            },
            "Семантика": {
                "Значение слов и предложений": TEORY_AND_FACTS,
                "Отношения между значениями": TEORY_AND_FACTS,
            },
            "Социолингвистика": {
                "Влияние социокультурных факторов на язык": TEORY_AND_FACTS,
                "Диалекты и регистры языка": TEORY_AND_FACTS,
            },
            "Психолингвистика": {
                "Процессы восприятия языка": TEORY_AND_FACTS,
                "Связь между языком и мышлением": TEORY_AND_FACTS,
            },
            "Языки": {},
            "История": HISTORY,
        },
        "Экономика": {
            "Обшая": {
                "Основные концепции и принципы экономической теории": TEORY_AND_FACTS,
                "Рынки и рыночные механизмы": TEORY_AND_FACTS,
                "Роль государства в экономике": TEORY_AND_FACTS,
                "Социально-экономические институты и их влияние на общество": TEORY_AND_FACTS,
            },
            "Микроэкономика": {
                "Поведение потребителей и производителей": TEORY_AND_FACTS,
                "Теория спроса и предложения": TEORY_AND_FACTS,
                "Ценообразование и рыночные структуры": TEORY_AND_FACTS,
                "Эластичность и её применение в анализе": TEORY_AND_FACTS,
            },
            "Макроэкономика": {
                "Общие показатели экономики": TEORY_AND_FACTS,
                "Экономический рост и циклы": TEORY_AND_FACTS,
                "Фискальная и монетарная политика": TEORY_AND_FACTS,
                "Международная торговля и её влияние на экономику": TEORY_AND_FACTS,
            },
            "Финансовая": {
                "Финансовые рынки и инструменты": TEORY_AND_FACTS,
                "Инвестиции и управление активами": TEORY_AND_FACTS,
                "Риск и доходность": TEORY_AND_FACTS,
                "Банковская система и её функции": TEORY_AND_FACTS,
            },
            "Международная": {
                "Теория международной торговли": TEORY_AND_FACTS,
                "Валютные рынки и обменные курсы": TEORY_AND_FACTS,
                "Глобализация и её последствия для экономики стран": TEORY_AND_FACTS,
                "Экономические отношения между государствами": TEORY_AND_FACTS,
            },
            "Страны": COUNTRIES,
            "История": HISTORY,
        },
        "Медицина": {
            "Специальности": {
                "Неврология": TEORY_AND_FACTS,
                "Психиатрия": TEORY_AND_FACTS,
                "Офтальмология": TEORY_AND_FACTS,
                "Оториноларингология": TEORY_AND_FACTS,
                "Дерматология": TEORY_AND_FACTS,
                "Хирургия": TEORY_AND_FACTS,
            },
            "Заболевания": {
                "Сердечно-сосудистые": TEORY_AND_FACTS,
                "Инсульт": TEORY_AND_FACTS,
                "Диабет": TEORY_AND_FACTS,
                "Рак": TEORY_AND_FACTS,
                "Астма": TEORY_AND_FACTS,
                "Аллергии": TEORY_AND_FACTS,
                "Гипертония": TEORY_AND_FACTS,
                "Депрессия": TEORY_AND_FACTS,
                "Биполярное расстройство": TEORY_AND_FACTS,
                "Шизофрения": TEORY_AND_FACTS,
                "ВИЧ/СПИД": TEORY_AND_FACTS,
                "Туберкулез": TEORY_AND_FACTS,
                "Грипп": TEORY_AND_FACTS,
                "Пневмония": TEORY_AND_FACTS,
                "Желудочно-кишечного тракта": TEORY_AND_FACTS,
            },
            "История": HISTORY,
        },
        "Логика": {
            "Символическая": TEORY_AND_FACTS,
            "Математическая": TEORY_AND_FACTS,
            "Аналитическая": TEORY_AND_FACTS,
            "Дедуктивная": TEORY_AND_FACTS,
            "Индуктивная": TEORY_AND_FACTS,
            "История": HISTORY,
        },
        "Анатомия": {
            "Системная": {
                "Остеология": TEORY_AND_FACTS,
                "Синдесмология": TEORY_AND_FACTS,
                "Миология": TEORY_AND_FACTS,
                "Спланхнология": TEORY_AND_FACTS,
                "Ангиология": TEORY_AND_FACTS,
                "Неврология": TEORY_AND_FACTS,
            },
            "Функциональная": {
                "Связь строения с функцией": TEORY_AND_FACTS,
                "Гемодинамика": TEORY_AND_FACTS,
            },
            "Патологическая": {
                "Изучение заболеваний": TEORY_AND_FACTS,
                "Микроскопическое исследование": TEORY_AND_FACTS,
            },
            "Сравнительная": {
                "Эволюция организмов": TEORY_AND_FACTS,
                "Сравнение анатомии человека и животных": TEORY_AND_FACTS,
            },
            "Эмбриология": {
                "Развитие организма": TEORY_AND_FACTS,
                "Биогенетический закон": TEORY_AND_FACTS,
            },
            "История": HISTORY,
        },
        "Философия": {
            "Онтология": {
                "Природа бытия": TEORY_AND_FACTS,
                "Категории бытия": TEORY_AND_FACTS,
            },
            "Эпистемология": {
                "Теории познания": TEORY_AND_FACTS,
                "Методы научного познания": TEORY_AND_FACTS,
            },
            "Этика": {
                "Моральные теории": TEORY_AND_FACTS,
                "Применение этики в практике": TEORY_AND_FACTS,
            },
            "Эстетика": {
                "Природа красоты": TEORY_AND_FACTS,
                "Эстетические категории": TEORY_AND_FACTS,
            },
            "История": HISTORY,
        },
        "Право": {
            "Конституционное": {
                "Основы конституционного строя": TEORY_AND_FACTS,
                "Права человека и гражданина": TEORY_AND_FACTS,
            },
            "Уголовное": {
                "Классификация преступлений": TEORY_AND_FACTS,
                "Процессуальные нормы": TEORY_AND_FACTS,
            },
            "Гражданское": {
                "Общие положения гражданского законодательства": TEORY_AND_FACTS,
                "Договорное регулирование": TEORY_AND_FACTS,
            },
            "Административное": {
                "Административные процедуры": TEORY_AND_FACTS,
                "Ответственность за административные правонарушения": TEORY_AND_FACTS,
            },
            "Трудовое": {
                "Трудовые отношения": TEORY_AND_FACTS,
                "Защита трудовых прав": TEORY_AND_FACTS,
            },
            "Финансовое": TEORY_AND_FACTS,
            "Международное": TEORY_AND_FACTS,
            "История": HISTORY,
        },
    },
    "Искусство": {
        "Изобразительное искусство": {
            "Живопись": TEORY_AND_FACTS,
            "Графика": TEORY_AND_FACTS,
            "Скульптура": TEORY_AND_FACTS,
            "Фотография": TEORY_AND_FACTS,
            "Инсталляция": TEORY_AND_FACTS,
            "История": HISTORY,
        },
        "Музыка": {
            "Классическая": TEORY_AND_FACTS,
            "Современная": TEORY_AND_FACTS,
            "Фольклорная": TEORY_AND_FACTS,
            "Музыкальная теория": TEORY_AND_FACTS,
            "История": HISTORY,
        },
        "Театр": {
            "Драматический театр": TEORY_AND_FACTS,
            "Музыкальный театр": TEORY_AND_FACTS,
            "Кукольный театр": TEORY_AND_FACTS,
            "Экспериментальный театр": TEORY_AND_FACTS,
            "История": HISTORY,
        },
        "Кинематограф": {
            "Игровое кино": TEORY_AND_FACTS,
            "Документальное кино": TEORY_AND_FACTS,
            "Анимация": TEORY_AND_FACTS,
            "Короткометражное кино": TEORY_AND_FACTS,
            "История": HISTORY,
        },
        "Литература": {
            "Поэзия": TEORY_AND_FACTS,
            "Проза": TEORY_AND_FACTS,
            "Драматургия": TEORY_AND_FACTS,
            "Эссеистика": TEORY_AND_FACTS,
            "История": HISTORY,
        },
        "Дизайн": {
            "Графический": TEORY_AND_FACTS,
            "Продуктовый": TEORY_AND_FACTS,
            "Интерьерный": TEORY_AND_FACTS,
            "Модный": TEORY_AND_FACTS,
            "История": HISTORY,
        },
        "Архитектура": {
            "Историческая": TEORY_AND_FACTS,
            "Современная": TEORY_AND_FACTS,
            "Ландшафтная": TEORY_AND_FACTS,
            "Градостроительство": TEORY_AND_FACTS,
            "История": HISTORY,
        },
        "История": HISTORY,
    },
    "История": {
        "Периоды": {
            "Древняя": {
                "Древние цивилизации": HISTORY,
                "Культура и религия": HISTORY,
            },
            "Средневековая": {
                "Феодализм и его особенности": HISTORY,
                "Крестоносцы и их влияние": HISTORY,
            },
            "Новая": {
                "Эпоха Возрождения": HISTORY,
                "Колонизация и ее последствия": HISTORY,
            },
            "Современная": {
                "Мировые войны": {
                    "I": HISTORY,
                    "II": HISTORY,
                },
                "Холодная война": HISTORY,
            },
        },
        "Страны": COUNTRIES,
    },
    "Религия": {
        "Христианство": RELIGION,
        "Ислам": RELIGION,
        "Индуизм": RELIGION,
        "Буддизм": RELIGION,
        "Страны": COUNTRIES,
    },
}

def _topics(topics, prefix="", separator="", collected=[]):
    if isinstance(topics, dict):
        if topics == {}:
            collected.append(prefix)
        else:
            for inner_prefix, inner_topics in topics.items():
                _topics(inner_topics, prefix + separator + inner_prefix, ". ", collected)
    elif isinstance(topics, list):
        for inner_topic in topics:
            collected.append(prefix + separator + inner_topic)
    return collected

class Topics:
    def __init__(self):
        self.topics = _topics(TOPICS)
        self.counts = {t: 0 for t in self.topics}

    def __len__(self):
        return len(self.topics)

    def choose(self):
        topic, _ = min(self.counts.items(), key=lambda t: t[1])
        self.counts[topic] += 1
        return topic

PROMPT = """
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
- Пиши вопросы которые требуют фактических знаний.
- Пиши как человек.
- Используй мало прилагательных.
"""

CORRECTION_PROMPT = """
# Текст

%s

# Инструкции

- Прочитай текст данный в секции "Текст".
- Затем в ответе напиши скоректированный текст. В ответе пиши только скоректированный текст.

# Коррекция

## Общее

- Если в тексте есть код, перепиши его, следуя общепринятым принципам написания.
- Не слишком укорачивай длину текста.
- Не используй Markdown форматирование.

## Лишняя информация

- Если в предложении слишком много ненужной для понимания темы информации, можно убрать её из текста.
- Не пиши очевидную информацию. Избегай очевидных утверждений и ненужных уточнений.

## LaTeX

- Для одиночных символов (пример: $x$) используй "$" вместо "$$".
- Для всех математических формул используй LaTeX.
"""
