from shredder import Shredder
shred = Shredder()

path = input("Enter name of file/directory: ")
is_wipe = input("Do u want to wipe? (1-yes/0-no): ")
if is_wipe == '1':
    level = input("Enter level of wipe(1..+inf): ")
    print(shred.wipe_multiple(path=path, level=int(level)))
elif is_wipe == '0':
    print(shred.delete_muptiple(path=path))
else:
    print("Bad input")
    exit()