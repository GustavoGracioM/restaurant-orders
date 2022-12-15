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


def infos_client(list_request, name_person):
    products = {}
    days = {}
    for name, product, day in list_request:
        if name == name_person:
            if product not in products:
                products[product] = 0
            products[product] += 1
            if day not in days:
                days[day] = 0
            days[day] += 1
    return [products, days]


def infos_requests(list_request: list):
    requests = {}
    days = {}
    for _, request, day in list_request:
        if request not in requests:
            requests[request] = 0
        if day not in days:
            days[day] = 0
        requests[request] += 1
        days[day] += 1
    return [requests, days]


def get_max(list_request: list):
    max_value = 0
    max_name = ""
    for key in list_request:
        if max_value < list_request[key]:
            max_name = key
            max_value = list_request[key]
    return (max_name, max_value)


def get_min(list_request: list):
    min_value = False
    min_name = ""
    for key in list_request:
        if not min_value:
            print(list_request)
            min_value = list_request[key]
        elif list_request[key] < min_value:
            min_name = key
            min_value = list_request[key]
    return (min_name, min_value)


def write_analyze_lg(logs):
    with open("data/mkt_campaign.txt", "w") as file:
        for log in logs:
            file.write(str(log) + "\n")


def analyze_log(path_to_file):
    logs = []
    request = read_file_csv(path_to_file)
    products, days = infos_requests(request)
    product_maria, _ = infos_client(request, "maria")
    product_arnaldo, _ = infos_client(request, "arnaldo")
    product_joao, days_joao = infos_client(request, "joao")
    logs.append(get_max(product_maria)[0])
    logs.append(product_arnaldo["hamburguer"])
    logs.append(
        set(product_joao.keys()).symmetric_difference(set(products.keys()))
    )
    logs.append(set(days_joao.keys()).symmetric_difference(set(days.keys)))
    write_analyze_lg(logs)
