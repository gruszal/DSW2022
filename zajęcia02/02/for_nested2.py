for x in range(5):
    print("x:", x)
    for y in range(10, 15):
        if y == 13:
            break  # break wychodzi tylko z pętli, w której się znajduje
        else:
            print("\ty:", y)
