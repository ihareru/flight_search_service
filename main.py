from validation import (flight_number_validator, flight_date_validation, flight_time_validation,
                        flight_duration_validation, airport_validator, price_validator)


def show_flights(database, flight_number=None):
    find_count = 0
    if len(database) == 0:
        return f'Информация о рейсах отсутствует'
    if flight_number:
        for flight in database:
            if flight[0] == flight_number:
                return (
                    f'Информация о рейсе: {flight[0]} {flight[1]} {flight[2]} '
                    f'{flight[3]} {flight[4]} {flight[5]} {flight[6]}')
        if find_count == 0:
            return f'Рейс {flight_number} не найден.'
    else:
        for flight in database:
            print(
                f'Информация о рейсе: {flight[0]} {flight[1]} {flight[2]} '
                f'{flight[3]} {flight[4]} {flight[5]} {flight[6]}')


def flight_information():
    print('\nВведите данные рейса:')
    while True:
        number_unverified = input('XXXX - номер рейса: ')
        if flight_number_validator(number_unverified):
            number = number_unverified.upper()
            break
        print('Номер рейса состоит из 4-х символов! Повторите ввод')

    while True:
        date_unverified = input('ДД/ММ/ГГГГ - дата рейса: ')
        if flight_date_validation(date_unverified):
            date = date_unverified
            break
        print('Не верный формат даты! Повторите ввод')

    while True:
        time_unverified = input('ЧЧ:ММ - время вылета: ')
        if flight_time_validation(time_unverified):
            time = time_unverified
            break
        print('Не верный формат веремни! Повторите ввод')

    while True:
        duration_unverified = input('XX.XX - длительность перелета: ')
        if flight_duration_validation(duration_unverified):
            duration = duration_unverified
            break
        print('Не верный формат длительности перелета! Повторите ввод')

    while True:
        departure_airport_unverified = input('XXX - аэропорт вылета: ')
        if airport_validator(departure_airport_unverified):
            departure_airport = departure_airport_unverified.upper()
            break
        print('Не верный формат кода аэропорта! Повторите ввод')

    while True:
        arrival_airport_unverified = input('XXX - аэропорт назначения: ')
        if airport_validator(arrival_airport_unverified):
            arrival_airport = arrival_airport_unverified.upper()
            break
        print('Не верный формат кода аэропорта! Повторите ввод')

    while True:
        price_unverified = input('.XX - стоимость билета (> 0): ')
        if price_validator(price_unverified):
            price = price_unverified
            break
        print('Не верный формат стоимости билета! Повторите ввод')

    flights_db.append([number, date, time, duration, departure_airport, arrival_airport, price])
    print('Информация о рейсе', number, date, time, duration, departure_airport,
          arrival_airport, price, 'добавлена')


def main():
    while True:
        print('\nГлавное меню\n')
        print('1 - ввод рейса')
        print('2 - вывод всех рейсов')
        print('3 - поиск рейса по номеру')
        print('0 - завершение работы\n')
        choice = input('Введите номер пункта меню: ')
        if choice == '1':
            flight_information()
        elif choice == '2':
            show_flights(flights_db)
        elif choice == '3':
            number = input('Введите номер рейса в формате XXXX: ').upper()
            print(show_flights(flights_db, number))
        elif choice == '0':
            print('Работа завершена')
            break
        else:
            print('Введите корректный пункт меню')


flights_db = []

if __name__ == '__main__':
    print('Сервис поиска авиабилетов')
    main()
