from shredder import Shredder

def test_delete_1():
    shred = Shredder()
    assert shred.delete_file() == False

if __name__ == "__main__":
    test_delete_1()
    print("OK")