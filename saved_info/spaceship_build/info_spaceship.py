# ./saved_info/spaceship_build/info_spaceship.py
import os


class InfoSpaceship(object):
    def __init__(self):
        self.file_path = './saved_info/spaceship_build/spaceship.txt'
        self.default_speed = 3
        self.default_size = (75, 75)
        self.spaceship_build = self._read_spaceship_build()
        self._ensure_file_exists()

    def _ensure_file_exists(self):
        if not os.path.exists(self.file_path):
            with open(self.file_path, 'w') as f:
                f.write(f"{self.default_speed},({self.default_size[0]},{self.default_size[1]})")

    def _read_spaceship_build(self):
        try:
            with open(self.file_path, 'r') as write_spaceship:
                content = write_spaceship.read().strip()
                if not content:
                    return self.default_speed, self.default_size

                if ',' in content:
                    speed_part, size_part = content.split(',', 1)
                    speed = int(speed_part.strip())

                    size_part = size_part.strip().strip('()')
                    w, h = size_part.split(',')
                    w = int(w.strip())
                    h = int(h.strip())
                    size = (w, h)
                    return speed, size
                else:
                    return self.default_speed, self.default_size
        except FileNotFoundError:
            return self.default_speed, self.default_size

    def buy_speed(self):
        current_speed, current_size = self.get_spaceship_build()
        new_speed = current_speed + 1
        self.update_spaceship_build(new_speed, current_size)

    def update_spaceship_build(self, speed, size):
        with open(self.file_path, 'w') as f:
            f.write(f"{speed},({size[0],size[1]})")
        self.spaceship_build = (speed, size)

    def get_spaceship_build(self):
        return self.spaceship_build