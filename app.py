import streamlit as st

st.header("Selamat Datang di SAUSA Kalkulator")
st.subheader("Kalkulator Kesehatan yang Lengkap & Informatif!")

# Variabel Gender
gender = st.selectbox("Masukkan jenis kelaminmu! (Perempuan/Laki-laki): ", ["Perempuan", "Laki-laki"], key="gender")

# Variabel Tinggi Badan
tinggi = st.number_input("Masukkan tinggi badanmu! (cm): ", min_value=1.0, format="%.2f", key="tinggi")

# Variabel Berat Badan
berat = st.number_input("Masukkan berat badanmu! (kg): ", min_value=1.0, format="%.2f", key="berat")

# Variabel Umur
umur = st.number_input("Masukkan umurmu hari ini! (tahun): ", min_value=1, max_value=100, step=1, key="umur")

aktivitas = st.radio("Jenis Aktivitas Fisik Sehari-hari: ", 
                    ["Sangat Jarang Berolahraga", 
                    "Jarang olahraga (1-3 kali per minggu)", 
                    "Cukup olahraga (3-5 kali per minggu)", 
                    "Sering olahraga (6-7 kali per minggu)", 
                    "Sangat sering olahraga (sekitar 2 kali dalam sehari)"],
                    key="aktivitas")

# Konversi jenis aktivitas ke nilai numerik
if aktivitas == "Sangat Jarang Berolahraga":
    aktif = 1
elif aktivitas == "Jarang olahraga (1-3 kali per minggu)":
    aktif = 2
elif aktivitas == "Cukup olahraga (3-5 kali per minggu)":
    aktif = 3
elif aktivitas == "Sering olahraga (6-7 kali per minggu)":
    aktif = 4
elif aktivitas == "Sangat sering olahraga (sekitar 2 kali dalam sehari)":
    aktif = 5


if st.button("Submit"):
    # Proses perhitungan atau apapun yang Anda ingin lakukan dengan data tersebut
    st.write("Data telah disubmit!")
