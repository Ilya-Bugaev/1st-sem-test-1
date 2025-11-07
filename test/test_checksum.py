from src.checksum import modulo11_checksum

def test_valid_isbn10_with_hyphens():
    #Тесты с дефисами
    assert modulo11_checksum("2-266-11156-8")
    assert modulo11_checksum("0-7475-3269-9")
    assert modulo11_checksum("1-56619-909-3")


def test_valid_isbn10_without_hyphens():
    #Тест без дефисов
    assert modulo11_checksum("2266111568")
    assert modulo11_checksum("0747532699")
    assert modulo11_checksum("1566199093")

def test_invalid_isbn10():
    #Тесты невалидности
    assert not modulo11_checksum("2-266-11156-3")
    assert not modulo11_checksum("0-7475-3269-8")
    assert not modulo11_checksum("1566199095")
