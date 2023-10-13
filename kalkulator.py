# Fungsi hitung Body Mass Index (BMI)
def BMI(tinggi,berat):
        bmi = berat/(tinggi/100)**2
        bmi_rapi = str(round(bmi,2))
        if bmi < 18.5:
            hasil=("Indeks Massa Tubuhmu adalah: "+bmi_rapi+" dan termasuk kategori : Kurang")
        elif bmi < 25:
            hasil=("Indeks Massa Tubuhmu adalah: "+bmi_rapi+" dan termasuk kategori : Normal")
        elif bmi < 30:
            hasil=("Indeks Massa Tubuhmu adalah: "+bmi_rapi+" dan termasuk kategori : Berlebih")
        else:
            hasil=("Indeks Massa Tubuhmu adalah: "+bmi_rapi+" dan termasuk kategori : Obesitas")
        return hasil

# Fungsi hitung Basal Metabolic Rate (BMR)
def BMR(tinggi,berat,umur,gender):
        if gender == "L" :
            bmr = (10*berat)+(6.25*tinggi)-(5*umur)+5
            bmr_rapi = round(bmr,2)
            hasil = "{:,.2f}".format(bmr_rapi)
        elif gender == "P":
            bmr = (10*berat)+(6.25*tinggi)-(5*umur)-161
            bmr_rapi = round(bmr,2)
            hasil = "{:,.2f}".format(bmr_rapi)
        return hasil

# Fungsi Kebutuhan air
def AAH(berat):
        aah = berat*0.033
        hasil = round(aah,2)
        return hasil

# Fungsi Berat Badan Ideal (BBI)
def BBI(tinggi,berat):
        BBI_bawah = round((18.5*(tinggi/100)**2),2)
        BBI_atas = round((24.9*(tinggi/100)**2),2)
        hasil = ("Berat badan ideal untukmu ada di kisaran "+str(BBI_bawah)+" - "+str(BBI_atas)+" kilogram")
        return hasil

# Fungsi AKG
def AKG(berat,tinggi,umur,gender,aktif):
        if gender == "L":
            if aktif == 1:
                akg = 1.2*(66+(13.7*berat)+(5*tinggi)-(6.8*umur))
                hasil = round(akg,2)
                return hasil
            elif aktif == 2:
                akg = 1.375*(66+(13.7*berat)+(5*tinggi)-(6.8*umur))
                hasil = round(akg,2)
                return hasil
            elif aktif == 3:
                akg = 1.55*(66+(13.7*berat)+(5*tinggi)-(6.8*umur))
                hasil = round(akg,2)
                return hasil
            elif aktif == 4:
                akg = 1.725*(66+(13.7*berat)+(5*tinggi)-(6.8*umur))
                hasil = round(akg,2)
                return hasil
            else:
                akg = 1.9*(66+(13.7*berat)+(5*tinggi)-(6.8*umur))
                hasil = round(akg,2)
                return hasil
        elif gender == "P":
            if aktif == 1:
                akg = 1.2*(655+(9.6*berat)+(1.8*tinggi)-(4.7*umur))
                hasil = round(akg,2)
                return hasil
            elif aktif == 2:
                akg = 1.375*(655+(9.6*berat)+(1.8*tinggi)-(4.7*umur))
                hasil = round(akg,2)
                return hasil
            elif aktif == 3:
                akg = 1.55*(655+(9.6*berat)+(1.8*tinggi)-(4.7*umur))
                hasil = round(akg,2)
                return hasil
            elif aktif == 4:
                akg = 1.725*(655+(9.6*berat)+(1.8*tinggi)-(4.7*umur))
                hasil = round(akg,2)
                return hasil
            else:
                akg = 1.9*(655+(9.6*berat)+(1.8*tinggi)-(4.7*umur))
                hasil = round(akg,2)
                return hasil

# Fungsi kebutuhan nutrisi
def nutrisi(AKG, berat, umur, gender, aktif):
    karbo = round((0.65*AKG(berat,umur,gender,aktif)),2)
    protein = round((0.15*AKG(berat,umur,gender,aktif)),2)
    lemak = round((0.2*AKG(berat,umur,gender,aktif)),2)
    return karbo, protein, lemak