import argparse
import os

class Shredder:
    #Удаление файла без затирки (можно восстановить)
    def delete_file(self, path=None):
        try:
            os.remove(path=path)
            return True
        except Exception:
            return False