# MLOps final project

Это АПИ приложение предсказывающие цену на жилье по входным параметрам.

**Инструкции по отдельному запуску ML части проекта можно найти тут** - [app/ml/README.md](./app/ml/README.md)

**Инструкции по отдельному запуску API части проекта можно найти тут** - [app/README.md](./app/README.md)

## Инструкция по запуску

### Сборка и запуск приложения в контенере docker:
```
docker compose up --build
```
Приложение будет доступно на порту 8000

Сейчас же достаточно сделать - [app/README.md](./app/README.md).

## API
### FastApi
В качестве фреймворка для организации REST-API был выбран FastApi 
#### Структура проекта
```
/app -> основное приложение
    - /ml -> ML часть проекта
    - /routing -> роуты апи
    - /schemas -> схемы апи
    - /services -> бизнес логика
    - /main.py -> основной файл для запуска приложения
```

#### Пример запроса
Пример запроса:
```js
(async () => {
    try {
    /**
     * Тут нужно подставить домен на котором
     * запущено приложение
     * */
    const BASE = 'http://127.0.0.1:8000';
    const res = await fetch(`${BASE}/predict`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
        "longitude": 1.2,
        "latitude": 1.2,
        "housing_median_age": 1.2,
        "total_rooms": 1.2,
        "total_bedrooms": 1.2,
        "population": 1.2,
        "households": 1.2,
        "median_income": 1.2,
        "median_house_value": 1.2,
        "ocean_proximity": 'test',
      })
    })
    const a = await res.json();
    console.log(a);
    } catch(e) {
        e.toString()
    }
})()
```
<i>Что бы быстро проверить работу АПИ, можно открыть окно
бразера, нажать F12 (если вы пользуетесь Google Chrome),
перейти во вкладку Console, вставить и выполнить код выше.<i>

## ML
### California Housing Prices
#### Описание DataSet
Данные относятся к домам, найденным в данном районе Калифорнии, 

и некоторой сводной статистики о них, основанной на данных переписи 1990 года. 

Имейте в виду, что данные не очищены, поэтому требуется несколько шагов предварительной обработки! 

#### Описание колонок

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

## Тестирование
### Установка pytest
```
pip install pytest
```
### Для тестирования 
```
pytest 
```
  
## Jenkins  
### Инструкция по запуску  
1. Создать стандартный пайплайн в Jenkins
2. Указать настройки пайплайна как на скриншоте![Screen-977](https://github.com/johnneon/URFUML2024_MLOps/assets/127988202/4e16d29d-9c6f-4934-90e7-1918d9969d9e)

3. Запустить сборку пайплайна

### Этапы пайплайна в Jenkinsfile:
1. Настройка виртуального окружения и установка зависимостей 
2. Предобработка данных
3. Тренировка модели
4. Тестирование модели
5. Запуск юнит-тестов
6. Сборка контейнера Docker
7. Запуск контейнера Docker
## DVC
Версии дата сета хранятся в [Google Drive](https://drive.google.com/drive/folders/1EWmKWhjIQ0AQOPBnS-vTie2MMtcNQFPI?usp=drive_link)  
Путь также отображается в файле [config](./.dvc/config)
### Пример загрузки разных версий
Базовая версия файла (до изменений)
![Снимок экрана 2024-05-19 160421](https://github.com/johnneon/URFUML2024_MLOps/assets/53440318/a0918b19-e614-4f8f-9e92-5c30fd7ca164)

Версия файла после внесения изменений
![Снимок экрана 2024-05-19 160518](https://github.com/johnneon/URFUML2024_MLOps/assets/53440318/ec7e0828-f03e-4615-b063-7241882a024e)

### Для работы с разными версиями датасета
Нужно переключиться на нужный коммит, например через команду ниже  
Вместо ### вставить нужный номер коммита, как на скришоте выше  
```
git checkout ###
```
После переключения на нужный коммит - скачать датасет командой
```
dvc pull -r mydisk
```
### После внесения изменений в датасет
Его можно заверсионировать, для этого нужно воспользоваться командой  
```
dvc add dataset
```
Полсе внести изменения на Git  
```
git add dataset.dvc
```
И наконец отправить измененную версию датасета на удаленное хранилище
```
dvc push -r mydisk
```


## Над проектом трудились

- Ильин В.Б. – лидер проекта [GitHub](https://github.com/Viktor-125142).
- Кравцов А.В. – инженер по машинному обучению [GitHub](https://github.com/Baddogel).
- Ефимович Е.А. – Full Stack-разработчик [GitHub](https://github.com/johnneon).
- Крючков В.В. – документалист/технический писатель [GitHub](https://github.com/Tifles).
- Чашников С.Ю.– Инженер MLOps [GitHub](https://github.com/SergeyChashnikov).
- Салов А.С. – Scrum-мастер [GitHub](https://github.com/TonyStranger404).
