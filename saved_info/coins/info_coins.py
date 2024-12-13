# ./saved_info/coins/info_coins.py


class InfoCoins(object):
    def __init__(self, spaceship):
        self.spaceship = spaceship
        self.total_coins = self._read_coins()
        self._ensure_file_exists()

    def _ensure_file_exists(self):
        try:
            with open('./saved_info/coins/coins.txt', 'r') as read_coins:
                content = read_coins.read().strip()
                self.total_coins = int(content) if content.isdigit() else 0
        except FileNotFoundError:
            with open('./saved_info/coins/coins.txt', 'w') as write_coins:
                write_coins.write('0')

            self.total_coins = 0

    def update_coins(self):
        current_coins = self.spaceship.coins
        self.total_coins += current_coins
        self._write_coins()
        return self.total_coins

    def _write_coins(self):
        with open('./saved_info/coins/coins.txt', 'w') as write_coins:
            write_coins.write(str(self.total_coins))

    def _read_coins(self):
        try:
            with open('./saved_info/coins/coins.txt', 'r') as read_coins:
                content = read_coins.read().strip()
                self.total_coins = int(content) if content.isdigit() else 0
        except FileNotFoundError:
            self.total_coins = 0

        return self.total_coins