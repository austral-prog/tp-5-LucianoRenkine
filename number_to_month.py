# Replace the "ANSWER HERE" for your answer

def number_to_month(month):
    if 1<=int(month) and int(month)<=12:
        if month == 1:
            return "enero"
        elif month == 2:
            return "febrero"
        elif month == 3:
            return "marzo"
        elif month == 4:
            return "abril"
        elif month == 5:
            return "mayo"
        elif month == 6:
            return "junio"
        elif month == 7:
            return "julio"
        elif month == 8:
            return "agosto"
        elif month == 9:
            return "septiembre"
        elif month == 10:
            return "octubre"
        elif month == 11:
            return "noviembre"
        else:
            return "diciembre"
    else:
        return "ANSWER HERE"
