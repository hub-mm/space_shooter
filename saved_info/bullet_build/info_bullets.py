# ./saved_info/bullet_build/info_bullet.py
class InfoBullets(object):
    def __init__(self):
        self.file_path = './saved_info/bullet_build/bullets.txt'

        self.bullet_max = self._read_bullet()
        self._ensure_file_exists()

    def _ensure_file_exists(self):
        try:
            with open(self.file_path, 'r') as read_bullets:
                content = read_bullets.read().strip()
                self.bullet_max = int(content) if content.isdigit() else 1
        except FileNotFoundError:
            with open(self.file_path, 'w') as write_bullets:
                write_bullets.write('1')

            self.bullet_max = 1

    def buy_extra_bullet(self):
        current_bullet = self._read_bullet()
        bullet_count = current_bullet + 1
        self.update_bullet(bullet_count)

    def _write_bullet(self):
        with open(self.file_path, 'w') as write_bullets:
            write_bullets.write(str(self.bullet_max))

    def _read_bullet(self):
        try:
            with open(self.file_path, 'r') as read_bullets:
                content = read_bullets.read().strip()
                self.bullet_max = int(content) if content.isdigit() else 1
        except FileNotFoundError:
            self.bullet_max = 1

        return self.bullet_max

    def update_bullet(self, bullet_count):
        with open(self.file_path, 'w') as f:
            f.write(f"{bullet_count}")
        self.bullet_max = bullet_count

    def get_bullet(self):
        return self.bullet_max