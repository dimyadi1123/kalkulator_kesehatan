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