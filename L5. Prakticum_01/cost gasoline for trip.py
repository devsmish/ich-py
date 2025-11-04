'''Напишите программу, которая принимает расстояние в километрах, расход бензина на 100 км и цену за литр
бензина. Программа должна рассчитать стоимость бензина для поездки.
Пример вывода:
Введите расстояние (в км): 300
Введите расход бензина на 100 км: 8
Введите цену за литр бензина: 60
Стоимость бензина для поездки: 1440.0'''
distance = int(input("Enter your distance (km): "))
fuel_consumption = int(input("Enter your fuel consumption (per 100 km): "))
price_fuel = float(input("Enter your price fuel (per liter): "))

cost_fuel = distance / 100 * fuel_consumption * price_fuel
print("Стоимость топлива для поездки: " + str(cost_fuel))