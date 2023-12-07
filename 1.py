def main():
    try:
        sas = int(input())
        sys = int(input())
        kek = sas + sys
    except ValueError:
        print("!ERROR! \nВведите целочисленные числа")
    else:
        print(kek)



if __name__ == "__main__":
    main()
