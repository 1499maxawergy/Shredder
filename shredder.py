import os
import string
import random

class Shredder:

    slash = '/'

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

    #Затирка файла (восстановить нельзя)
    def wipe_file(self, path=None, level=1):
        try:
            valid_chars = string.ascii_letters + string.digits
            filesize = os.path.getsize(path)
            num_lines = sum(1 for line in open(path))
            if(os.path.isfile(path) == True and filesize > 0):
                for temp in range(level):
                    #Записываем в файл всевозможные символы
                    with open(path, 'w') as f:
                        for i in range(num_lines):
                            string_writable = "".join(random.choices(valid_chars, k=filesize)) + '\n'
                            f.write(string_writable)

                    #Переименовываем файл
                    new_name = "".join(random.choices(valid_chars, k=random.choice(range(1, 27))))
                    new_path = f"{self.slash}".join(path.split(f"{self.slash}")[0:-1]) + f"{self.slash}{new_name}"
                    if(len(path.split(f"{self.slash}")) == 1):
                        new_path = new_name
                    os.rename(path, new_path)
                    path = new_path
                
                #Удаляем файл после вайпа
                os.remove(path)
                return True
            else:
                return False
        except Exception:
            return False


    def wipe_multiple(self, path=None):
        pass