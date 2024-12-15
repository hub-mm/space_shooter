# ./saved_info/extra_coin_value/info_extra_coin_value.py
import os


class InfoExtraCoin(object):
    def __init__(self):
        self.file_path = './saved_info/extra_coin_value/info_extra_coin_value.txt'
        self._ensure_file_exists()
        self.total_coin_extra = self._read_extra_coin()

    def _ensure_file_exists(self):
        if not os.path.exists(self.file_path):
            with open(self.file_path, 'w') as f:
                f.write('1')

    def add_extra_coins(self):
        self.total_coin_extra += 1
        self._write_extra_coins()
        return self.total_coin_extra

    def _write_extra_coins(self):
        with open(self.file_path, 'w') as write_coins:
            write_coins.write(str(self.total_coin_extra))

    def _read_extra_coin(self):
        try:
            with open(self.file_path, 'r') as read_coins:
                content = read_coins.read().strip()
                self.total_coin_extra = int(content) if content.isdigit() else 1
                return self.total_coin_extra
        except FileNotFoundError:
            return 1

    def get_extra_coin(self):
        return self.total_coin_extra