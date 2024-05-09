# MLOps final project

Это АПИ приложение предсказывающие цену на жилье по входным параметрам.

**Инструкции по отдельному запуску ML части проекта можно найти тут** - [app/ml/README.md](./app/ml/README.md)

**Инструкции по отдельному запуску API части проекта можно найти тут** - [app/README.md](./app/README.md)

## Инструкция по запуску

Тут опишем чуть позже инструкции по запуску проекта целиком Jenkins+Docker.

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

## Над проектом трудились

- Ильин В.Б. – лидер проекта [GitHub](https://github.com/Viktor-125142).
- Кравцов А.В. – инженер по машинному обучению [GitHub](https://github.com/Baddogel).
- Ефимович Е.А. – Full Stack-разработчик [GitHub](https://github.com/johnneon).
- Крючков В.В. – документалист/технический писатель [GitHub](https://github.com/Tifles).
- Чашников С.Ю.– Инженер MLOps [GitHub](https://github.com/SergeyChashnikov).
- Салов А.С. – Scrum-мастер [GitHub](https://github.com/TonyStranger404).