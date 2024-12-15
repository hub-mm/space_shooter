# ./saved_info/bullet_build/info_bullet_gap.py
class InfoBulletGap(object):
    def __init__(self):
        self.file_path = './saved_info/bullet_build/bullets_gap.txt'

        self.bullet_gap = self._read_bullet_gap()
        self._ensure_file_exists()

    def _ensure_file_exists(self):
        try:
            with open(self.file_path, 'r') as read_bullets_gap:
                content = read_bullets_gap.read().strip()
                self.bullet_gap = int(content) if content.isdigit() else 250
        except FileNotFoundError:
            with open(self.file_path, 'w') as write_bullets_gap:
                write_bullets_gap.write('250')

            self.bullet_gap = 250

    def buy_reduce_gap_bullet(self):
        current_bullet_gap = self._read_bullet_gap()
        bullet_gap = current_bullet_gap - 5
        self.update_bullet_gap(bullet_gap)

    def _write_bullet(self):
        with open(self.file_path, 'w') as write_bullets_gap:
            write_bullets_gap.write(str(self.bullet_gap))

    def _read_bullet_gap(self):
        try:
            with open(self.file_path, 'r') as read_bullets_gap:
                content = read_bullets_gap.read().strip()
                self.bullet_gap = int(content) if content.isdigit() else 1
        except FileNotFoundError:
            self.bullet_gap = 250

        return self.bullet_gap

    def update_bullet_gap(self, bullet_gap_count):
        with open(self.file_path, 'w') as f:
            f.write(f"{bullet_gap_count}")
        self.bullet_gap = bullet_gap_count

    def get_bullet_gap(self):
        return self.bullet_gap