from readback_check import check

assert check("DLH4AB descend flight level 110 squawk 2741", "descend FL110, squawk 2741, DLH4AB") == []
assert check("descend flight level 110", "descend flight level 100") == ["level: expected 110, got 100"]
assert check("contact Langen one two four decimal seven two", "124.72 DLH4AB") == []
assert check("turn left heading 270, QNH 1013", "left heading 270, QNH 1031") == ["altimeter: expected 1013, got 1031"]
assert check("line up runway 25C", "lining up runway 25L") == ["runway: expected 25c, got 25l"]
assert check("squawk two seven four one", "squawk 2741") == []
print("all tests passed")
