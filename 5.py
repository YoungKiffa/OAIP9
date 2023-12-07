def main():
    try:
        sas = int(input())
        sys = int(input())
        kek = sas // sys
    except ZeroDivisionError:
        print("!ERROR! \nДелить на 0 нельзя!")
    except ValueError:
        print("!ERROR! \nВведите целочисленные числа")
    else:
        print(kek)
    finally:
        print("Выход из программы!")


if __name__ == "__main__":
    main()
