for x in range(5):
    print("x:", x)
    for y in range(10, 15):
        if y == 13:
            break

        print("\ty:", y)  # porównaj z `for_nested2.py`
