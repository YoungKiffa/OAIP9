def main():
    sas = int(input())
    sys = int(input())
    try:
        kek = sas // sys
    except ZeroDivisionError:
        print("!ERROR! \nДелить на 0 нельзя!")
    else:
        print(kek)


if __name__ == "__main__":
    main()
