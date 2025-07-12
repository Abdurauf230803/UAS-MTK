import streamlit as st
import matplotlib.pyplot as plt

# Judul Aplikasi
st.title("📊 Simulasi Antrian - Model M/M/1")
st.markdown("Aplikasi ini menghitung parameter penting dalam teori antrian M/M/1.")

# Input
st.sidebar.header("Input Parameter")
lambda_val = st.sidebar.number_input("λ (Rata-rata Kedatangan per satuan waktu)", min_value=0.01, step=0.1, value=5.0)
mu_val = st.sidebar.number_input("μ (Rata-rata Pelayanan per satuan waktu)", min_value=0.01, step=0.1, value=8.0)

# Validasi
if lambda_val >= mu_val:
    st.error("λ harus lebih kecil dari μ untuk menghindari sistem tidak stabil (ρ < 1)")
else:
    # Perhitungan M/M/1
    rho = lambda_val / mu_val           # Utilisasi
    L = lambda_val / (mu_val - lambda_val)  # Pelanggan dalam sistem
    Lq = rho**2 / (1 - rho)             # Pelanggan dalam antrian
    W = 1 / (mu_val - lambda_val)       # Waktu dalam sistem
    Wq = lambda_val / (mu_val * (mu_val - lambda_val))  # Waktu dalam antrian

    # Output
    st.subheader("📈 Hasil Perhitungan:")
    st.write(f"**ρ (Utilisasi Sistem):** {rho:.2f}")
    st.write(f"**L (Rata-rata pelanggan dalam sistem):** {L:.2f}")
    st.write(f"**Lq (Rata-rata pelanggan dalam antrian):** {Lq:.2f}")
    st.write(f"**W (Waktu rata-rata dalam sistem):** {W:.2f} satuan waktu")
    st.write(f"**Wq (Waktu rata-rata dalam antrian):** {Wq:.2f} satuan waktu")

    # Visualisasi Diagram Antrian
    st.subheader("📉 Diagram Antrian (Pelanggan vs Waktu Tunggu)")

    pelanggan = list(range(1, 11))
    waktu_tunggu = [Wq + i*(W-Wq)/10 for i in pelanggan]

    fig, ax = plt.subplots()
    ax.plot(pelanggan, waktu_tunggu, marker='o', linestyle='-', color='blue')
    ax.set_xlabel("Jumlah Pelanggan")
    ax.set_ylabel("Estimasi Waktu Tunggu")
    ax.set_title("Simulasi Antrian M/M/1")
    st.pyplot(fig)
