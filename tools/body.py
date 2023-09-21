def bmi(h,w):
    try:
        return round(w/pow(h,2),2)
    except ZeroDivisionError:
        print('Podany wzrost wynosi 0')
        return -1
    except TypeError:
        print("Podane wartości muszą być liczbami")
        return -1
    except Exception as e:
        print(f"Inny wyjątek: {type(e)} {e}")