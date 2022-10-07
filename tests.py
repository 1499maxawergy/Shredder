from shredder import Shredder
shred = Shredder()

def test_delete_1():
    assert shred.delete_file() == False

def test_delete_2():
    assert shred.delete_file(path="TEST_DIR/k1.txt") == True

def test_delete_3():
    assert shred.delete_file(path="KKKSSSS/KISKIS.txt") == False

def test_delete_4():
    assert shred.delete_muptiple(path="TEST_DIR") == True

if __name__ == "__main__":
    test_delete_1()
    test_delete_2()
    test_delete_3()
    test_delete_4()
    print("OK")