import requests
import json
import matplotlib.pyplot as plt

# Отримання курсу валют із сайту НБУ за попередній тиждень за допомогою Postman
url = "https://bank.gov.ua/NBU_Exchange/exchange_site?start=20241216&end=20241222&valcode=usd&json"

# Отримання курсу валют із сайту НБУ за попередній тиждень з використанням python-бібліотеки requests
get_response = requests.get(url)
response_dictionary = json.loads(get_response.content)

# Виведення запиту у зручному форматі
print("Курс долара за попередній тиждень 16.12.2024 - 22.12.2024:")
for item in response_dictionary:
    print(f"На {item['exchangedate']} курс долара становить {item['rate']} грн.")


# Побудова графіку зміни курсів валют за допомогою бібліотеки matplotlib
exchange_dictionary = {}
for item in response_dictionary:
    exchange_dictionary[item['exchangedate']] = item ['rate']

fig, ax = plt.subplots()
ax.plot(exchange_dictionary.keys(), exchange_dictionary.values())
plt.show()
