# ЗАДАНИЕ

Есть массив объектов, которые имеют поля id и parent, через которые их можно связать в дерево и некоторые произвольные
поля.

Нужно написать класс, который принимает в конструктор массив этих объектов и реализует 4 метода:

- `getAll()` - Должен возвращать изначальный массив элементов.
- `getItem(id)` - Принимает id элемента и возвращает сам объект элемента;
- `getChildren(id)` - Принимает id элемента и возвращает массив элементов, являющихся дочерними для того элемента,
  чей id получен в аргументе. Если у элемента нет дочерних, то должен возвращаться пустой массив;
- `getAllParents(id)` - Принимает id элемента и возвращает массив из цепочки родительских элементов,
  начиная от самого элемента, чей id был передан в аргументе и до корневого элемента,
  т.е. должен получиться путь элемента наверх дерева через цепочку родителей к корню дерева. Порядок элементов важен!

## Требования:

Максимальное быстродействие, следовательно, минимальное количество обходов массива при операциях,
в идеале, прямой доступ к элементам без поиска их в массиве.

## Исходные данные:

```python
class TreeStore:
    pass


items = [
    {"id": 1, "parent": "root"},
    {"id": 2, "parent": 1, "type": "test"},
    {"id": 3, "parent": 1, "type": "test"},
    {"id": 4, "parent": 2, "type": "test"},
    {"id": 5, "parent": 2, "type": "test"},
    {"id": 6, "parent": 2, "type": "test"},
    {"id": 7, "parent": 4, "type": None},
    {"id": 8, "parent": 4, "type": None}
]

```

## Примеры использования:

```python
ts = TreeStore(items)
ts.getAll()
# [{"id": 1, "parent": "root"}, {"id": 2, "parent": 1, "type": "test"},
# {"id": 3, "parent": 1, "type": "test"}, {"id": 4, "parent": 2, "type": "test"},
# {"id": 5, "parent": 2, "type": "test"}, {"id": 6, "parent": 2, "type": "test"},
# {"id": 7, "parent": 4, "type": None}, {"id": 8, "parent": 4, "type": None}]

ts.getItem(7)  # {"id": 7, "parent": 4, "type": None}

ts.getChildren(4)  
# [{"id": 7, "parent": 4, "type": None}, 
# {"id": 8, "parent": 4, "type": None}]

ts.getChildren(5)  # []

ts.getAllParents(7)  
# [{"id": 4, "parent": 2, "type": "test"}, 
# {"id": 2, "parent": 1, "type": "test"}, 
# {"id": 1, "parent": "root"}]

```

## Установка и запуск

### Необходимые инструменты и технологии

- [Python 3.10+](https://www.python.org/)

### Клонируйте репозиторий

```bash
git clone https://github.com/joerude/status-test-assignment
cd status-test-assignment
```


### Запуск тестов

```bash
python3 tests.py
```