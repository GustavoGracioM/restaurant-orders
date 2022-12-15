import csv
import os


def read_file_csv(path_to_file):
    _, extension = os.path.splitext(path_to_file)
    if extension != ".csv":
        raise FileNotFoundError(f"Extensão inválida: '{path_to_file}'")
    try:
        with open(path_to_file) as file:
            reader = csv.reader(file)
            myList = list(reader)

        return myList
    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo inexistente: '{path_to_file}'")


def formatter(list_request: list):
    result_list = {}
    for name, prato, day in list_request:
        if name not in result_list:
            result_list[name] = {}
        if day not in result_list[name]:
            result_list[name][day] = {}
        if prato not in result_list[name][day]:
            result_list[name][day][prato] = 0
        result_list[name][day][prato] += 1

    return result_list


def product_set(list_request: list, name: str):
    set_request = {}
    for day in list_request[name]:
        for product in list_request[name][day]:
            if product not in set_request:
                set_request[product] = 0
            set_request[product] += list_request[name][day][product]

    return set_request


def infos_client(list_request: list):
    requests = set()
    days = set()
    for _, request, day in list_request:
        if request not in requests:
            requests.add(request)
        if day not in days:
            days.add(day)
    return [requests, days]


def days_set(list: list, name):
    days = set()
    for day in list[name]:
        if day not in days:
            days.add(day)
    return days


def max_request(formatedet, name):
    request = product_set(formatedet, name)
    max_quantity = 0
    name_product = ""
    for r in request:
        if max_quantity < request[r]:
            max_quantity = request[r]
            name_product = r
    return name_product


def get_quatity(formatedet, name, product):
    return product_set(formatedet, name)[product]


def get_not_product(formatedet, products, name):
    result = set(product_set(formatedet, name).keys())
    return result.symmetric_difference(products)


def get_not_day(formatedet, days, name):
    return days_set(formatedet, name).symmetric_difference(days)


def write_analyze_lg(logs):
    with open("data/mkt_campaign.txt", "w") as file:
        for log in logs:
            file.write(str(log) + "\n")


def analyze_log(path_to_file):
    logs = []
    request = read_file_csv(path_to_file)
    request_formated = formatter(request)
    pratos, days = infos_client(request)
    logs.append(max_request(request_formated, "maria"))
    logs.append(get_quatity(request_formated, "arnaldo", "hamburguer"))
    logs.append(get_not_product(request_formated, pratos, "joao"))
    logs.append(get_not_day(request_formated, days, "joao"))
    write_analyze_lg(logs)
