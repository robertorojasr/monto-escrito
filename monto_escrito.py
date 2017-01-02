
def unidad(unidad, decena=None, grande=False):
    texto = ""

    if grande and (unidad in ["0","1"]):
        return ""

    if unidad == "0":
        texto = "cero" if decena == None else ""

    elif unidad == "1":
        texto = "" if decena == "1" else "uno"

    elif unidad == "2":
        texto = "" if decena == "1" else "dos"

    elif unidad == "3":
        texto = "" if decena == "1" else "trés"

    elif unidad == "4":
        texto = "" if decena == "1" else "cuatro"

    elif unidad == "5":
        texto = "" if decena == "1" else "cinco"

    elif unidad == "6":
        texto = "seis"

    elif unidad == "7":
        texto = "siete"

    elif unidad == "8":
        texto = "ocho"

    elif unidad == "9":
        texto = "nueve"

    return texto

def decena(decena, unidad):
    texto = ""

    if decena == "1":
        if unidad == "0":
            texto = "diez"

        elif unidad == "1":
            texto = "once"

        elif unidad == "2":
            texto = "doce"

        elif unidad == "3":
            texto = "trece"

        elif unidad == "4":
            texto = "catorce"

        elif unidad == "5":
            texto = "quince"

        else:
            texto = "dieci"

    elif decena == "2":
        texto = "veinte" if unidad == "0" else "veinti"

    elif decena == "3":
        texto = "treinta" if unidad == "0" else "treinta y "

    elif decena == "4":
        texto = "cuarenta" if unidad == "0" else "cuarenta y "

    elif decena == "5":
        texto = "cincuenta" if unidad == "0" else "cincuenta y "

    elif decena == "6":
        texto = "sesenta" if unidad == "0" else "sesenta y "

    elif decena == "7":
        texto = "setenta" if unidad == "0" else "setenta y "

    elif decena == "8":
        texto = "ochenta" if unidad == "0" else "ochenta y "

    elif decena == "9":
        texto = "noventa" if unidad == "0" else "noventa y "

    return texto

def centena(centena, decena, unidad):
    texto = ""

    if centena == "1":
        if decena and unidad == "0":
            texto = "cién"

        else:
            texto = "ciento "

    elif centena == "2":
        texto = "doscientos"

        if decena or unidad != "0":
            texto += " "

    elif centena == "3":
        texto = "trescientos"

        if decena or unidad != "0":
            texto += " "


    elif centena == "4":
        texto = "cuatrocientos"

        if decena or unidad != "0":
            texto += " "


    elif centena == "5":
        texto = "quinientos"

        if decena or unidad != "0":
            texto += " "


    elif centena == "6":
        texto = "seiscientos"

        if decena or unidad != "0":
            texto += " "


    elif centena == "7":
        texto = "setecientos"

        if decena or unidad != "0":
            texto += " "


    elif centena == "8":
        texto = "ochocientos"

        if decena or unidad != "0":
            texto += " "


    elif centena == "9":
        texto = "novecientos"

        if decena or unidad != "0":
            texto += " "

    return texto


if __name__ == "__main__":

    texto = ""
    monto = input("Ingrese monto --> ")
    otnom = monto[::-1]

    ## Millones
    if len(monto) > 8:
        texto += centena(centena=otnom[8], decena=otnom[7], unidad=otnom[6])

    if len(monto) > 7:
        texto += decena(decena=otnom[7], unidad=otnom[6])
        texto += unidad(decena=otnom[7], unidad=otnom[6], grande=True)
        texto += " millones "

    if len(monto) == 7:
        if otnom[6] == "1":
            texto += " un millón "
        else:
            texto += unidad(unidad=otnom[6], grande=True)
            texto += " millones "

    ## Miles
    if len(monto) > 5:
        texto += centena(centena=otnom[5], decena=otnom[4], unidad=otnom[3])

    if len(monto) > 4:
        texto += decena(decena=otnom[4], unidad=otnom[3])
        texto += unidad(decena=otnom[4], unidad=otnom[3], grande=True)
        if (len(monto) > 3 and int(otnom[3])) or (len(monto) > 4 and (int(otnom[3] or int(otnom[4])))) or \
                                    (len(monto) > 5 and (int(otnom[3]) or int(otnom[4]) or int(otnom[5]))):
            texto += " mil "

    if len(monto) == 4:
        texto += unidad(unidad=otnom[3], grande=True)
        texto += " mil "

    ## Cientos
    if len(monto) > 2:
        texto += centena(centena=otnom[2], decena=otnom[1], unidad=otnom[0])

    if len(monto) > 1:
        texto += decena(decena=otnom[1], unidad=otnom[0])
        texto += unidad(decena=otnom[1], unidad=otnom[0])

    else:
        texto += unidad(unidad=otnom[0])

    print(texto.strip().replace("  ", " "))

