def nome_mes(m):
    if m == 1:
        return 'January'
    elif m == 2:
        return 'February'
    elif m == 3:
        return 'March'
    elif m == 4:
        return 'April'
    elif m == 5:
        return 'May'
    elif m == 6:
        return 'June'
    elif m == 7:
        return 'July'
    elif m == 8:
        return 'August'
    elif m == 9:
        return 'September'
    elif m == 10:
        return 'October'
    elif m == 11:
        return 'November'
    else:
        return 'December'

m = int(input())
print(nome_mes(m))
