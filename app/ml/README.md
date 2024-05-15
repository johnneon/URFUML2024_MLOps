# Запуск ML части проекта

Для создания и активации виртуального окружения выполните следующие команды в терминале:

### Инструкции для Unix/Linux/macOS:
```bash
# Создание виртуального окружения
python -m venv env

# Активация виртуального окружения
source env/bin/activate

# Устанавливаем библиотеки
pip install -r requirements.txt

# Устанавливаем локальные пакеты
pip install -e .
```


### Инструкции для Windows:


#### Установка виртуального окружения

Для создания и активации виртуального окружения выполните следующие команды в командной строке:

```cmd
# Создание виртуального окружения
python -m venv env

# Активация виртуального окружения
.\env\Scripts\activate

# Устанавливаем библиотеки
pip install -r requirements.txt

# Устанавливаем локальные пакеты
pip install -e .
```

Для работы с Kaggle API вам необходимо скачать файл kaggle.json. 

Это можно сделать на странице [настроек Kaggle.](https://www.kaggle.com/settings)

После загрузки файла kaggle.json переместите его в папку src вашего проекта:
```bash
cp kaggle.json src/
```
Запустите следующие скрипты последовательно для обработки данных, 

подготовки модели и тестирования:
```bash
python app/ml/data_preprocessing.py
python app/ml/model_preparation.py
python app/ml/model_testing.py
```