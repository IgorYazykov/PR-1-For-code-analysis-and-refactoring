class Country:
    def __init__(self, name, xl, yl, xh, yh):
        # Инициализация атрибутов объекта страны
        self.name = name  # Название страны
        self.xl = xl  # Нижняя граница координаты x
        self.yl = yl  # Нижняя граница координаты y
        self.xh = xh  # Верхняя граница координаты x
        self.yh = yh  # Верхняя граница координаты y
        self.coins = 1000000  # Количество монет, начальное значение 1 миллион

def calculate_days_to_finish(countries):
    # Функция для расчета количества дней для завершения обращения монет в каждой стране
    for country in countries:
        # Вычисление максимального расстояния до соседней страны по координатам
        max_distance = max(country.xh - country.xl, country.yh - country.yl)
        coins = country.coins  # Извлечение начального количества монет в стране
        days = 0  # Счетчик дней, инициализация
        while coins > 0:  # Пока есть монеты в стране
            days += 1  # Увеличение счетчика дней на 1
            total_transportable_coins = 0  # Общее количество перевозимых монет, инициализация
            # Перебор соседних стран
            for neighbor in countries:
                if neighbor != country:  # Проверка, что соседняя страна не является текущей страной
                    # Вычисление расстояния до соседней страны по координатам
                    distance = max(abs(country.xl - neighbor.xl), abs(country.yl - neighbor.yl),
                                   abs(country.xh - neighbor.xh), abs(country.yh - neighbor.yh))
                    # Вычисление количества монет, которое можно передать соседней стране
                    transportable_coins = min(coins, distance * 1000)
                    neighbor.coins += transportable_coins  # Добавление монет к соседней стране
                    total_transportable_coins += transportable_coins  # Обновление общего количества перевозимых монет
            coins -= total_transportable_coins  # Вычитание переданных монет из текущей страны
            # Проверка условия завершения обращения монет в стране:
            if total_transportable_coins == 0 or coins == 0:
                break
        country.days_to_finish = days  # Установка количества дней для завершения обращения монет в стране

def simulate_coin_distribution(countries, case_number):
    # Функция для симуляции распределения монет и вывода результатов
    calculate_days_to_finish(countries)  # Расчет количества дней для завершения обращения монет
    # Сортировка стран по количеству дней до завершения обращения монет и их названиям
    sorted_countries = sorted(countries, key=lambda country: (country.days_to_finish, country.name))
    print(f"Case Number {case_number}")  # Вывод номера случая
    # Вывод названий стран и соответствующего количества дней до завершения обращения монет
    for country in sorted_countries:
        print(f"{country.name} {country.days_to_finish}")

def main():
    input_data = [
        # Примеры входных данных, содержащие названия стран и их координаты
        (3, ["France", 1, 2, 1, 4], ["Spain", 4, 1, 1, 3], ["Portugal", 2, 1, 3, 2]),
        (1, ["Luxembourg", 1, 2, 1, 4]),
        (2, ["Netherlands", 1, 4, 2, 3], ["Belgium", 2, 1, 2, 3])
    ]

    case_number = 1  # Номер случая, инициализация
    for data in input_data:
        c = data[0]  # Количество стран в случае
        countries = []  # Список стран, инициализация
        # Извлечение данных о стране и создание объектов страны
        for country_data in data[1:]:
            name = country_data[0]
            xl, yl, xh, yh = country_data[1:]
            country = Country(name, xl, yl, xh, yh)
            countries.append(country)
        # Симуляция распределения монет и вывод результатов
        simulate_coin_distribution(countries, case_number)
        case_number += 1  # Увеличение номера случая для следующей итерации

if __name__ == "__main__":
    main()  # Выполнение основной функции, если скрипт запущен как главная программа
