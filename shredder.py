import os
import string
import random

class Shredder:

    slash = '/' # Дефолтный слэш в вашей системе (иногда требует \\)

    def delete_file(self, path=None):
        """
        Удаление файла без затирки
        При таком удалении файл можно восстановить
        path - Путь до файла (по умолчанию: None)
        """
        try:
            os.remove(path=path)
            return True
        except Exception:
            return False
    
    def delete_muptiple(self, path=None):
        """
        Удаление и файла, и директории рекурсивно
        Является производной от метода delete_file()
        path - Путь до файла/директории (по умолчанию: None)
        Если указана директория, то удаляется все, что в ней есть, и она сама
        """
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
    def wipe_file(self, path=None, level=2):
        """
        Затирка с последующим переименованием файла
        path - Путь до файла (по умолчанию: None)
        level - Уровень затирки (сколько раз файл будет перезатираться) (по умолчанию: 2)
        """
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
                self.delete_file(path=path)
                return True
        except Exception:
            return False

    def wipe_multiple(self, path=None, level=2):
        """
        Затирка с последующим переименованием файлов в папке
        Является производной от метода wipe_file()
        path - Путь до файла (по умолчанию: None)
        level - Уровень затирки (сколько раз файл будет перезатираться) (по умолчанию: 2)
        Примечание: в конце метода сама папка просто удаляется, так как затирать в ней будет нечего
        """
        try:
            if os.path.isdir(path):
                for elem in os.listdir(path=path):
                    print('Deleting: ' + str(path) + '/' + str(elem))
                    self.wipe_multiple(path=str(path) + '/' + str(elem))
                os.rmdir(path=path)
            else:
                self.wipe_file(path=path, level=level)
            return True
        except Exception:
            return False