# ./saved_info/highscore/info_highscore.py
class InfoHighscore(object):
    def __init__(self, enemy, spaceship):
        self.enemy = enemy
        self.spaceship = spaceship

        self.highscore = 0
        self._ensure_file_exists()

    def _ensure_file_exists(self):
        try:
            with open('./saved_info/highscore/highscore.txt', 'r') as read_highscore:
                content = read_highscore.read().strip()
                self.highscore = int(content) if content.isdigit() else 0
        except FileNotFoundError:
            with open('./saved_info/highscore/highscore.txt', 'w') as write_highscore:
                write_highscore.write('0')

            self.highscore = 0

    def update_highscore(self):
        current_score = self.enemy.total_killed * (self.spaceship.coins + 1)
        if current_score > self.highscore:
            self.highscore = current_score
            self._write_highscore()
        else:
            self.highscore = self._read_highscore()

        return self.highscore

    def _write_highscore(self):
        with open('./saved_info/highscore/highscore.txt', 'w') as write_highscore:
            write_highscore.write(str(self.highscore))

    def _read_highscore(self):
        try:
            with open('./saved_info/highscore/highscore.txt', 'r') as read_highscore:
                content = read_highscore.read().strip()
                self.highscore = int(content) if content.isdigit() else 0
        except FileNotFoundError:
            self.highscore = 0

        return self.highscore