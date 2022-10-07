import os

class Shredder:
    #Удаление файла без затирки (можно восстановить)
    def delete_file(self, path=None):
        try:
            os.remove(path=path)
            return True
        except Exception:
            return False
    
    #Удаление директории и файлов без затирки (можно восстановить)
    def delete_muptiple(self, path=None):
        try:
            if os.path.isdir(path):
                for elem in os.listdir(path=path):
                    print('Deleting: ' + str(path) + '/' + str(elem))
                    self.delete_muptiple(path=str(path) + '/' + str(elem))
                os.rmdir(path=path)
            else:
                self.delete_file(path=path)
            return True
        except Exception:
            return False

    
    def wipe_file(self, path=None):
        pass
