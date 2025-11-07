from src.checksum import modulo11_checksum


def test_good():
    assert modulo11Checksum("2-266-11156-8")


def test_bad():
    assert not modulo11Checksum("2-266-11156-3")
