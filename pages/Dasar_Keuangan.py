import streamlit as st

st.set_page_config(page_title="Dasar Keuangan", page_icon="📚", layout="wide")

st.markdown("""
<style>
    .card-dark {
        background-color: #343a40;
        padding: 1.5rem;
        border-radius: 12px;
        margin-bottom: 1rem;
    }
    .card-dark:hover {
        box-shadow: 0 0 20px rgba(200, 200, 200, 0.4),
            0 0 40px rgba(200, 200, 200, 0.15);
            transform: translateY(-2px);
        }
    .card-light {
        background-color: #e9ecef;
        color: #212529;
        padding: 1.5rem;
        border-radius: 12px;
        margin-bottom: 1rem;
    }
    .card-invest:hover {
        border-top-color: #17a2b8;
        background-color: #3a444e;
    }
    .card-green {
        background-color: #1e3a2f;
        border-left: 4px solid #28a745;
        padding: 1.5rem;
        border-radius: 8px;
        margin-bottom: 1rem;
    }
    .card-green:hover {
        box-shadow: 0 0 20px rgba(129, 199, 132, 0.5),
            0 0 40px rgba(129, 199, 132, 0.2);
            transform: translateY(-2px);
    }
    .card-red {
        background-color: #3a1e1e;
        border-left: 4px solid #dc3545;
        padding: 1.5rem;
        border-radius: 8px;
        margin-bottom: 1rem;
    }
    .card-red:hover {
        box-shadow: 0 0 20px rgba(255, 99, 132, 0.5),
            0 0 40px rgba(255, 99, 132, 0.2);
            transform: translateY(-2px);
    }
    .carousel-container {
        background-color: #343a40;
        padding: 2rem;
        border-radius: 16px;
        text-align: center;
        min-height: 200px;
        display: flex;
        flex-direction: column;
        justify-content: center;
    }
    .alert-warning {
        background-color: #3a3520;
        border-left: 4px solid #ffc107;
        padding: 1rem;
        border-radius: 8px;
        margin: 1rem 0;
    }
    .stApp {
        background: linear-gradient(
            150deg,
            #1a0a0a 0%,
            #1a0a1a 25%,
            #0d0d1a 50%,
            #0a1a1a 75%,
            #0d1117 100%
        );
    }
</style>
""", unsafe_allow_html=True)

st.title("📚 Dasar-Dasar Keuangan")
st.markdown("### Pondasi Sebelum Kamu Mulai Berinvestasi")
st.markdown("---")


st.markdown("## 🏠 Aset vs Liabilitas")
st.markdown("Dua konsep paling fundamental yang wajib kamu pahami:")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="card-green">
        <h3>✅ ASET</h3>
        <p><strong>Segala sesuatu yang MEMASUKKAN uang ke kantongmu.</strong></p>
        <hr style="border-color: #28a745;">
        <p>📌 <strong>Contoh:</strong></p>
        <ul>
            <li>Rumah yang disewakan</li>
            <li>Saham & reksadana</li>
            <li>Bisnis yang menghasilkan profit</li>
            <li>Emas & properti</li>
        </ul>
        <p>💡 <em>Aset bekerja untukmu, bahkan saat kamu tidur.</em></p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card-red">
        <h3>❌ LIABILITAS</h3>
        <p><strong>Segala sesuatu yang MENGELUARKAN uang dari kantongmu.</strong></p>
        <hr style="border-color: #dc3545;">
        <p>📌 <strong>Contoh:</strong></p>
        <ul>
            <li>Kredit mobil konsumtif</li>
            <li>Kartu kredit dengan bunga</li>
            <li>Pinjaman online berbunga tinggi</li>
            <li>Rumah yang ditempati sendiri (belum menghasilkan)</li>
        </ul>
        <p>⚠️ <em>Liabilitas menguras kekayaanmu setiap bulan.</em></p>
    </div>
    """, unsafe_allow_html=True)


st.markdown("""
<div class="alert-warning">
    <strong>⚠️ Fakta Penting:</strong> Banyak orang salah mengira rumah dan mobil sebagai aset. 
    Kalau itu tidak menghasilkan uang dan malah mengeluarkan biaya (pajak, perawatan, BBM), 
    itu adalah <strong>liabilitas</strong>, bukan aset!
</div>
""", unsafe_allow_html=True)

st.markdown("---")


st.markdown("## 💸 Cashflow (Arus Kas)")
st.markdown("Cashflow adalah aliran uang masuk dan keluar setiap bulan. Ada 3 kondisi:")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="card-green">
        <h3>🟢 Positif</h3>
        <p><strong>Pemasukan > Pengeluaran</strong></p>
        <p>Ada sisa untuk ditabung & diinvestasikan. Ini kondisi ideal!</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card-dark">
        <h3>🟡 Impas</h3>
        <p><strong>Pemasukan = Pengeluaran</strong></p>
        <p>Tidak ada sisa. Satu kejadian darurat bisa langsung bikin minus.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card-red">
        <h3>🔴 Negatif</h3>
        <p><strong>Pemasukan < Pengeluaran</strong></p>
        <p>Utang menumpuk. Harus segera diatasi dengan kurangi liabilitas.</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

st.markdown("## 💡 Tips Keuangan Hari Ini")

if 'carousel_idx' not in st.session_state:
    st.session_state.carousel_idx = 0

slides = [
    {
        "emoji": "💰",
        "judul": "Aturan 50/30/20",
        "isi": "Alokasikan 50% untuk kebutuhan, 30% untuk keinginan, dan 20% untuk tabungan & investasi."
    },
    {
        "emoji": "🛡️",
        "judul": "Dana Darurat Dulu",
        "isi": "Sebelum investasi, kumpulkan dana darurat 3-6x pengeluaran bulanan. Simpan di tempat yang mudah dicairkan."
    },
    {
        "emoji": "📉",
        "judul": "Hindari Utang Konsumtif",
        "isi": "Kalau tidak bisa beli 2x dengan uang tunai, jangan dibeli dengan kredit. Bedakan butuh dan ingin."
    },
    {
        "emoji": "📊",
        "judul": "Catat Setiap Pengeluaran",
        "isi": "Kamu tidak bisa mengatur yang tidak kamu ukur. Pakai aplikasi atau buku catatan sederhana."
    },
]

total_slides = len(slides)
current = slides[st.session_state.carousel_idx]

st.markdown(f"""
<div class="carousel-container">
    <h1 style="font-size: 3rem;">{current['emoji']}</h1>
    <h2>{current['judul']}</h2>
    <p style="font-size: 1.1rem;">{current['isi']}</p>
</div>
""", unsafe_allow_html=True)

col1, col2, col3, col4, col5 = st.columns([1, 1, 2, 1, 1])

with col1:
    if st.button("⬅️ Sebelumnya", key="prev"):
        st.session_state.carousel_idx = (st.session_state.carousel_idx - 1) % total_slides
        st.rerun()

with col5:
    if st.button("Selanjutnya ➡️", key="next"):
        st.session_state.carousel_idx = (st.session_state.carousel_idx + 1) % total_slides
        st.rerun()

st.markdown(f"<p style='text-align:center; color:#6c757d;'>Slide {st.session_state.carousel_idx + 1} dari {total_slides}</p>", unsafe_allow_html=True)

st.markdown("---")