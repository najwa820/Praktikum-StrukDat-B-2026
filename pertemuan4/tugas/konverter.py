import kurs

def konversi(jumlah, dari, ke):
    if dari == ke:
        return jumlah

    elif dari == "IDR":
        return jumlah / kurs.kurs[ke]
    
    elif ke == "IDR":
        return jumlah * kurs.kurs[dari]
    
    else:
        jumlah_idr = jumlah * kurs.kurs[dari]
        return jumlah_idr / kurs.kurs[ke]