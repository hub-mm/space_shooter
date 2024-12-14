# ./saved_info/coins/info_coins.py
import os


class InfoCoins(object):
    def __init__(self, spaceship):
        self.file_path = './saved_info/coins/coins.txt'
        self.spaceship = spaceship
        self._ensure_file_exists()
        self.total_coins = self._read_coins()

    def _ensure_file_exists(self):
        if not os.path.exists(self.file_path):
            with open(self.file_path, 'w') as f:
                f.write('0')

    def update_coins(self):
        self._write_coins()
        return self.total_coins

    def set_total_coins(self, new_total):
        self.total_coins = new_total
        self._write_coins()
        return self.total_coins

    def add_coins(self, amount):
        self.total_coins += amount
        self._write_coins()
        return self.total_coins

    def _write_coins(self):
        with open(self.file_path, 'w') as write_coins:
            write_coins.write(str(self.total_coins))

    def _read_coins(self):
        try:
            with open(self.file_path, 'r') as read_coins:
                content = read_coins.read().strip()
                coins = int(content) if content.isdigit() else 0
                return coins
        except FileNotFoundError:
            return 0