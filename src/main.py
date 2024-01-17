from utils import *

OPERATIONS = 'operations.json'

executed = filter_list_only_executed(open_file(OPERATIONS)) # открывает и сортирует по ключу "EXECUTED"
operations = sort_date_operations(executed) # выводит последние 5 операций
dates = modify_date(operations) # модификация даты
card_number = mask_card_number(operations) # скрывает счёт карты
amount_number = mask_amount_number(operations) # скрывает номер счёта

for operation in range(len(operations)):
    print(f"{dates[operation]} {operations[operation]['description']}\n"
          f"{card_number[operation]} -> Счет {amount_number[operation]}\n"
          f"{operations[operation]['operationAmount']['amount']}"
          f"{operations[operation]['operationAmount']['currency']['name']}\n")
