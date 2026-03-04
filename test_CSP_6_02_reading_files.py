import CSP_6_02_reading_files

from CSP_6_02_reading_files import toString, toBinary, longestLine

def test_toString():
    assert toString("sample2.txt")=="Here is the text\ni am another line"

def test_longestLine():
    assert longestLine("sample4.txt")=="the longest line is here\n"

def test_toBinary():
    assert toBinary("sample3.txt") == ['01101001', '00101010', '1010']
