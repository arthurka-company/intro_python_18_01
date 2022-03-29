# Обменник USD-UAH, CLI
# usd, uah - курс uah/usd
# COURSE <>
# EXCHANGE <currency> <amount>
# SET_COURSE <currency> <rate>
# STOP
import requests
import pickle
import os


rate_url = 'https://api.exchangerate-api.com/v4/latest/uah'


class Currency:
    def __init__(self, code):
        self.code = code
        self.amount = 0.0
        if self.code.lower() == 'uah':
            self.rate = 1
        else:
            self.rate = self.get_current_rate()

    def add_money_amount(self, number):
        self.amount += float(number)

    def get_current_rate(self):
        response = requests.get(f'{rate_url}')
        if response.status_code == 200:
            rate = response.json()['rates'].get(self.code.upper(), 0)
            return rate
        raise Exception('Currency url not responding!')


class Wallet:
    def __init__(self):
        self.currencies = []

    def add_currency_to_wallet(self, code):
        for currency in self.currencies:
            if code == currency.code:
                raise Exception('Currency exists!')
        self.currencies.append(Currency(code=code))

    def get_currency_obj_by_code(self, code):
        for currency in self.currencies:
            if code == currency.code:
                return currency
        return None

    def print_available_money(self):
        for currency in self.currencies:
            print(f'{currency.code}: {currency.amount}')




def main():
    if os.path.isfile('wallet.pkl'):
        with open('wallet.pkl', 'rb') as f:
            wallet = pickle.load(f)
    else:
        wallet = Wallet()
    wallet.print_available_money()
    while True:
        command = input('Введите команду (COURSE, EXCHANGE, STOP):\n')

        if 'create' in command.lower():
            code = command.lower().split()[-1]
            wallet.add_currency_to_wallet(code=code)
        elif 'course' in command.lower():
            code = command.lower().split()[-1]
            currency = wallet.get_currency_obj_by_code(code)
            print(f'Course of {code}: {currency.rate}')
        elif 'add' in command.lower():
            code = command.lower().split()[1]
            amount = command.lower().split()[-1]
            currency = wallet.get_currency_obj_by_code(code)
            currency.add_money_amount(amount)
            print(f'Available of {code}: {currency.amount}')
        elif 'stop' in command.lower():
            print('STOPPED')
            break

        with open('wallet.pkl', 'wb') as f:
            pickle.dump(wallet, f)


if __name__ == '__main__':
    main()
