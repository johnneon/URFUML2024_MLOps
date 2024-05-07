# URFUML2024_MLOps

## MLOps final project

## California Housing Prices
### Описание DataSet
Данные относятся к домам, найденным в данном районе Калифорнии, 

и некоторой сводной статистики о них, основанной на данных переписи 1990 года. 

Имейте в виду, что данные не очищены, поэтому требуется несколько шагов предварительной обработки! 

### Описание колонок

- longitude -  долгота

- latitude  - широта

- housing_median_age - Средний возраст жилья

- total_rooms - Общее количество комнат

- total_bedrooms - Общее количество спален

- population - Население

- households - домохозяйства  

- median_income - Средний доход

- median_house_value - Средняя стоимость жилья  

- ocean_proximity - Близость к океану  


Для того что запустить проект вам нужно: 

Для создания и активации виртуального окружения выполните следующие команды в терминале:


### Инструкции для Unix/Linux/macOS:
```bash
# Создание виртуального окружения
python -m venv env

# Активация виртуального окружения
source env/bin/activate

# Устанавливаем библиотеки
pip install -r requirements.txt


```


### Инструкции для Windows:

```markdown
# Установка виртуального окружения

Для создания и активации виртуального окружения выполните следующие команды в командной строке:

```cmd
# Создание виртуального окружения
python -m venv env

# Активация виртуального окружения
.\env\Scripts\activate

# Устанавливаем библиотеки
pip install -r requirements.txt

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
python src/data_preprocessing.py
python src/model_preparation.py
python src/model_testing.py

```

Над проектом трудились:

- Ильин В.Б. – лидер проекта [GitHub](https://github.com/Viktor-125142).
- Кравцов А.В. – инженер по машинному обучению [GitHub](https://github.com/Baddogel).
- Ефимович Е.А. – Full Stack-разработчик [GitHub](https://github.com/johnneon).
- Крючков В.В. – документалист/технический писатель [GitHub](https://github.com/Tifles).
- Чашников С.Ю.– Инженер MLOps [GitHub](https://github.com/SergeyChashnikov).
- Салов А.С. – Scrum-мастер [GitHub](https://github.com/TonyStranger404).