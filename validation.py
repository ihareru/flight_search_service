def flight_number_validator(number):
    if len(number) == 4:
        return True
    return False


def flight_date_validation(date):
    if ((len(date) == 10) and (1 <= int(date[0:2]) <= 31) and (date[2] == '/') and (1 <= int(date[3:5]) <= 31) and
            (date[5] == '/') and (999 < int(date[6:10]) <= 9999)):
        return True
    return False


def flight_time_validation(time):
    if (len(time) == 5) and (0 <= int(time[0:2]) <= 23) and (time[2] == ':') and (0 <= int(time[3:5]) <= 59):
        return True
    return False


def flight_duration_validation(duration):
    if ((len(duration) == 5) and (0 <= int(duration[0:2]) <= 24) and (duration[2] == '.')
            and (0 <= int(duration[3:5]) <= 59)):
        return True
    return False


def airport_validator(departure):
    count = 0
    for sym in departure:
        if sym.isalpha():
            count += 1
    if count == 3:
        return True
    return False


def price_validator(price):
    if ',' in price:
        price_list = price.split(',')
        num_str = '.'.join(price_list)
        num = float(num_str)
    else:
        num = float(price)
    if num > 0:
        return True
    return False
