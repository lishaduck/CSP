def f(n):
    if int(n) == n:
        if n % 2 == 0:
            if n % 3 == 0:
                print("n is a multiple of 6!")
            else:
                print("n is ... even?")
        else:
            print("n is odd.")
    else:
        print("n is not an int...")
