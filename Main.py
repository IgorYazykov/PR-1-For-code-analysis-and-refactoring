import math

class Country:
    def __init__(self, name, xl, yl, xh, yh):
        self.name = name
        self.xl = xl
        self.yl = yl
        self.xh = xh
        self.yh = yh
        self.euro = 1000000 

def calculate_days_to_finish(countries):
    for country in countries:
        max_distance = max(country.xh - country.xl, country.yh - country.yl)
        coins = country.euro
        days = 0
        while coins > 0:
            days += 1
            updated_coins = 0  
            for neighbor in countries:
                if neighbor != country:
                    distance = max(abs(country.xl - neighbor.xl), abs(country.yl - neighbor.yl),
                                   abs(country.xh - neighbor.xh), abs(country.yh - neighbor.yh))
                    transportable_coins = min(coins, distance * 1000)
                    neighbor.euro += transportable_coins
                    updated_coins += transportable_coins 
            coins -= updated_coins  
            if updated_coins == 0:
                break 
        country.days_to_finish = days

def simulate_coin_distribution(countries, case_number):
    calculate_days_to_finish(countries)
    sorted_countries = sorted(countries, key=lambda country: (country.days_to_finish, country.name))
    print(f"Case Number {case_number}")
    for country in sorted_countries:
        print(f"{country.name} {country.days_to_finish}")

def main():
    input_data = [
        (3, ["France", 1, 2, 1, 4], ["Spain", 4, 1, 1, 3], ["Portugal", 2, 1, 3, 2]),
        (1, ["Luxembourg", 1, 2, 1, 4]),
        (2, ["Netherlands", 1, 4, 2, 3], ["Belgium", 2, 1, 2, 3])
    ]

    case_number = 1
    for data in input_data:
        c = data[0]
        countries = []
        for country_data in data[1:]:
            name = country_data[0]
            xl, yl, xh, yh = country_data[1:]
            country = Country(name, xl, yl, xh, yh)
            countries.append(country)
        simulate_coin_distribution(countries, case_number)
        case_number += 1

if __name__ == "__main__":
    main()
