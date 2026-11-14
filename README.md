# 🧪 QA Guru — Pet Project

### Учебный проект по автоматизации тестирования на Python

[![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)](https://www.python.org/)
[![Pytest](https://img.shields.io/badge/pytest-9.x-green?logo=pytest)](https://docs.pytest.org/)
[![Selenium](https://img.shields.io/badge/Selenium-4.x-brightgreen?logo=selenium)](https://www.selenium.dev/)
[![Code style](https://img.shields.io/badge/code%20style-Black%20%7C%20isort%20%7C%20Flake8-black)](https://github.com/psf/black)

## 📌 О проекте

QA Guru Pet Project — учебный проект по автоматизации тестирования программного обеспечения на Python в рамках обучения в школе [QA.GURU](https://qa.guru/).

В репозитории собраны практические задания, примеры Python-кода и первые автоматизированные UI-тесты с использованием Selenium и Pytest.

Проект развивается постепенно: от изучения основ Python до написания и поддержки автоматизированных тестов.

## 🎯 Цели проекта

- Изучение Python для задач QA Automation.
- Практика написания автотестов с использованием Pytest.
- Знакомство с Selenium WebDriver.
- Работа с Git и GitHub.
- Освоение инструментов форматирования и проверки качества кода.
- Настройка автоматических проверок перед Git commit.

## 🛠 Технологии и инструменты

| Инструмент | Назначение |
|---|---|
| Python | Основной язык программирования |
| Pytest | Запуск и организация тестов |
| Selenium WebDriver | Автоматизация браузера |
| PyCharm | Среда разработки |
| Git | Контроль версий |
| GitHub | Хранение исходного кода |
| pre-commit | Автоматический запуск проверок перед commit |
| Black | Форматирование Python-кода |
| isort | Сортировка импортов |
| Flake8 | Проверка качества и стиля кода |

## 📂 Структура проекта

```text
qa_guru_pet_project/
│
├── .flake8                  # Конфигурация Flake8
├── .gitignore               # Исключения Git
├── .pre-commit-config.yaml  # Настройки pre-commit hooks
├── README.md                # Описание проекта
├── requirements.txt         # Зависимости проекта
│
├── task_01.py               # Практическое задание
└── test_task_01.py          # Автоматизированные UI-тесты
```

## 🚀 Установка и запуск

### 1. Клонирование репозитория

```bash
git clone https://github.com/redrepublics/qa_guru_pet_project.git
cd qa_guru_pet_project
```

### 2. Создание виртуального окружения

```bash
python -m venv .venv
```

### 3. Активация виртуального окружения

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 4. Установка зависимостей

```bash
python -m pip install -r requirements.txt
```

### 5. Запуск тестов

```bash
python -m pytest
```

## 🔍 Контроль качества кода

В проекте настроен pre-commit, который автоматически запускает проверки перед созданием Git commit.

Используются три инструмента:

- **isort** — сортировка импортов.
- **Black** — автоматическое форматирование кода.
- **Flake8** — статическая проверка кода.

Проверки настроены для Python-файлов, расположенных непосредственно в корне проекта.

### Установка pre-commit

```bash
python -m pip install pre-commit
```

### Установка Git hooks

```bash
pre-commit install
```

### Проверка всех файлов

```bash
pre-commit run --all-files
```

После установки Git hooks проверки будут автоматически запускаться при каждом `git commit`.

## 📚 Обучение

Проект создаётся в рамках обучения автоматизации тестирования на Python в школе QA.GURU.

Каждое новое задание помогает закрепить знания Python, освоить инструменты автоматизации и сформировать практические навыки QA Automation Engineer.

## 👨‍💻 Автор

Владислав Жеребьёв

QA Engineer | Python Automation

[GitHub](https://github.com/redrepublics)

---

⭐ Проект находится в разработке. Новые задания, тесты и улучшения будут добавляться по мере обучения.