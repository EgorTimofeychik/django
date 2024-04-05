import requests

def convert_usd_to_byn(amount):
    url = "https://www.nbrb.by/api/exrates/rates?periodicity=0"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        json_data = response.json()
        for rate in json_data:
            if rate["Cur_ID"] == 431:
                rate_value = rate["Cur_OfficialRate"]
                result = amount * rate_value
                return result
        print("Ошибка: Не удалось найти курс для доллара")
        return None
    else:
        print("Ошибка при получении данных")
        return None

# Пример использования функции
usd_amount = 100
byn_amount = convert_usd_to_byn(usd_amount)
if byn_amount:
    print(f"{usd_amount} USD равно {byn_amount} BYN")