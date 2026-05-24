import streamlit as st

st.set_page_config(page_title="Investasi Pemula", page_icon="📈", layout="wide")

st.markdown("""
<style>
    .card-dark {
        background-color: #343a40;
        padding: 1.5rem;
        border-radius: 12px;
        margin-bottom: 1rem;
        height: 100%;
    }
    .card-light {
        background-color: #e9ecef;
        color: #212529;
        padding: 1.5rem;
        border-radius: 12px;
        margin-bottom: 1rem;
    }
    .card-invest {
        background-color: #343a40;
        padding: 1.5rem;
        border-radius: 12px;
        margin-bottom: 1rem;
        border-top: 4px solid #6c757d;
        transition: all 0.2s;
    }
    .card-invest:hover {
        border-top-color: #17a2b8;
        background-color: #3a444e;
    }
    .carousel-container {
        background-color: #343a40;
        padding: 2rem;
        border-radius: 16px;
        text-align: center;
        min-height: 180px;
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
    .alert-info {
        background-color: #1a3a4a;
        border-left: 4px solid #17a2b8;
        padding: 1rem;
        border-radius: 8px;
        margin: 1rem 0;
    }
    .alert-info:hover {
        }
    .risk-card {
        padding: 1rem;
        border-radius: 10px;
        text-align: center;
        cursor: pointer;
        border: 2px solid transparent;
    }
    .risk-active {
        border: 2px solid #17a2b8 !important;
        background-color: #1a3a4a !important;
    }
    .stApp {
        background: linear-gradient(
            135deg,
            #1a1a0f 0%,
            #0d1a1a 25%,
            #0a0e27 50%,
            #0d1a0f 75%,
            #1a0f0f 100%
        );
    }
</style>
""", unsafe_allow_html=True)

st.title("📈 Investasi untuk Pemula")
st.markdown("### Mulai investasi dengan aman dan sesuai dengan kondisi keuangan anda")
st.markdown("---")

st.markdown("""
<div class="alert-warning">
    <strong>⚠️ Aturan 1 Investasi:</strong> Jangan investasikan uang yang kamu butuhkan dalam waktu dekat. 
    Pastikan dana darurat sudah siap sebelum mulai berinvestasi.
</div>
""", unsafe_allow_html=True)

st.markdown("---")

st.markdown("## 🎯 Jenis-Jenis Instrumen Investasi")
st.markdown("### Dari yang paling aman dan paling bikin cepat kaya atau cepat miskin:")

row1_col1, row1_col2 = st.columns(2)
row2_col1, row2_col2 = st.columns(2)

with row1_col1:
    st.markdown("""
    <div class="card-invest">
        <h3>🏦 Tabungan & Deposito</h3>
        <p><strong>Risiko:</strong> Sangat Rendah</p>
        <p><strong>Return:</strong> 2-5% per tahun</p>
        <hr>
        <p>✅ Cocok untuk dana darurat</p>
        <p>✅ Dijamin LPS hingga Rp 2 M</p>
        <p>❌ Return kalah oleh inflasi</p>
    </div>
    """, unsafe_allow_html=True)

with row1_col2:
    st.markdown("""
    <div class="card-invest">
        <h3>📊 Reksadana Pasar Uang</h3>
        <p><strong>Risiko:</strong> Rendah</p>
        <p><strong>Return:</strong> 4-6% per tahun</p>
        <hr>
        <p>✅ Likuid, bisa dicairkan kapan saja</p>
        <p>✅ Cocok untuk pemula</p>
        <p>✅ Bisa mulai dari Rp 10.000</p>
    </div>
    """, unsafe_allow_html=True)

with row2_col1:
    st.markdown("""
    <div class="card-invest">
        <h3>📈 Reksadana Saham</h3>
        <p><strong>Risiko:</strong> Tinggi</p>
        <p><strong>Return:</strong> 10-15% per tahun (historikal)</p>
        <hr>
        <p>✅ Potensi return tertinggi</p>
        <p>✅ Dikelola manajer investasi</p>
        <p>❌ Bisa turun dalam jangka pendek</p>
    </div>
    """, unsafe_allow_html=True)

with row2_col2:
    st.markdown("""
    <div class="card-invest">
        <h3>🥇 Emas</h3>
        <p><strong>Risiko:</strong> Sedang</p>
        <p><strong>Return:</strong> 5-8% per tahun (rata-rata)</p>
        <hr>
        <p>✅ Lindung nilai terhadap inflasi</p>
        <p>✅ Aset fisik yang stabil</p>
        <p>❌ Tidak menghasilkan cashflow</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# --- CAROUSEL TIPS ---
st.markdown("## 💡 Tips Investasi untuk Pemula")

# Session state
if 'tips_idx' not in st.session_state:
    st.session_state.tips_idx = 0

tips = [
    {
        "emoji": "🎯",
        "judul": "Tentukan Tujuan Dulu",
        "isi": "Investasi tanpa tujuan seperti naik mobil tanpa arah. Tentukan: untuk pensiun? beli rumah? pendidikan anak?"
    },
    {
        "emoji": "📚",
        "judul": "Pahami Sebelum Membeli",
        "isi": "Jangan investasi di sesuatu yang tidak kamu pahami. Pelajari dulu instrumennya, risikonya, dan return ekspektasinya."
    },
    {
        "emoji": "⏰",
        "judul": "Mulai Sedini Mungkin",
        "isi": "Waktu adalah teman terbaik investor. Semakin awal mulai, semakin besar efek compounding bekerja untukmu."
    },
    {
        "emoji": "🧺",
        "judul": "Diversifikasi",
        "isi": "Jangan taruh semua telur di satu keranjang. Sebarkan investasi di berbagai instrumen untuk mengurangi risiko."
    },
    {
        "emoji": "😌",
        "judul": "Jangan Panik Saat Turun",
        "isi": "Pasar naik-turun itu normal. Investor sukses justru membeli saat harga sedang diskon (turun)."
    },
]

total_tips = len(tips)
current_tip = tips[st.session_state.tips_idx]

st.markdown(f"""
<div class="carousel-container">
    <h1 style="font-size: 3rem;">{current_tip['emoji']}</h1>
    <h2>{current_tip['judul']}</h2>
    <p style="font-size: 1.1rem;">{current_tip['isi']}</p>
</div>
""", unsafe_allow_html=True)

# Navigasi
col1, col2, col3, col4, col5 = st.columns([1, 1, 2, 1, 1])
with col1:
    if st.button("⬅️ Sebelumnya", key="prev_tip"):
        st.session_state.tips_idx = (st.session_state.tips_idx - 1) % total_tips
        st.rerun()
with col5:
    if st.button("Selanjutnya ➡️", key="next_tip"):
        st.session_state.tips_idx = (st.session_state.tips_idx + 1) % total_tips
        st.rerun()

st.markdown(f"<p style='text-align:center; color:#6c757d;'>Tip {st.session_state.tips_idx + 1} dari {total_tips}</p>", unsafe_allow_html=True)

st.markdown("---")

st.markdown("## Ada 3 metode yang bisa anda gunakan")
st.markdown("Tergantung dengan tujuan anda")

# Session state untuk profil risiko
if 'selected_risk' not in st.session_state:
    st.session_state.selected_risk = None

col1, col2, col3 = st.columns(3)

with col1:
    konservatif_border = "2px solid #17a2b8" if st.session_state.selected_risk == "konservatif" else "2px solid transparent"
    st.markdown(f"""
    <div style="background-color:#343a40; padding:1.5rem; border-radius:12px; border:{konservatif_border}; cursor:pointer;" 
         onclick="alert('Klik button di bawah')">
        <h3 style="text-align:center;">🛡️</h3>
        <h4 style="text-align:center;">Konservatif</h4>
        <p style="text-align:center;">Keamanan utama, tidak nyaman dengan fluktuasi</p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Pilih Konservatif", key="btn_konservatif"):
        st.session_state.selected_risk = "konservatif"
        st.rerun()

with col2:
    moderat_border = "2px solid #17a2b8" if st.session_state.selected_risk == "moderat" else "2px solid transparent"
    st.markdown(f"""
    <div style="background-color:#343a40; padding:1.5rem; border-radius:12px; border:{moderat_border};">
        <h3 style="text-align:center;">⚖️</h3>
        <h4 style="text-align:center;">Moderat</h4>
        <p style="text-align:center;">Siap dengan fluktuasi sedang untuk return lebih tinggi</p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Pilih Moderat", key="btn_moderat"):
        st.session_state.selected_risk = "moderat"
        st.rerun()

with col3:
    agresif_border = "2px solid #17a2b8" if st.session_state.selected_risk == "agresif" else "2px solid transparent"
    st.markdown(f"""
    <div style="background-color:#343a40; padding:1.5rem; border-radius:12px; border:{agresif_border};">
        <h3 style="text-align:center;">🚀</h3>
        <h4 style="text-align:center;">Agresif</h4>
        <p style="text-align:center;">Berani ambil risiko tinggi demi potensi return maksimal</p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Pilih Agresif", key="btn_agresif"):
        st.session_state.selected_risk = "agresif"
        st.rerun()

if st.session_state.selected_risk:
    st.markdown("---")
    st.markdown("### 🎯 Rekomendasi untuk Kamu")
    
    if st.session_state.selected_risk == "konservatif":
        st.markdown("""
        <div class="alert-info">
            <strong>🛡️ Konservatif — Rekomendasi:</strong>
            <ul>
                <li>70% di <strong>Reksadana Pasar Uang</strong> atau Deposito</li>
                <li>20% di <strong>Obligasi</strong> atau Reksadana Pendapatan Tetap</li>
                <li>10% di <strong>Emas</strong></li>
            </ul>
            <p>Fokus pada keamanan dan likuiditas. Return moderat tapi tidur nyenyak.</p>
        </div>
        """, unsafe_allow_html=True)
    
    elif st.session_state.selected_risk == "moderat":
        st.markdown("""
        <div class="alert-info">
            <strong>⚖️ Stabilitas — Rekomendasi:</strong>
            <ul>
                <li>40% di <strong>Reksadana Pendapatan Tetap</strong> atau Obligasi</li>
                <li>40% di <strong>Reksadana Saham</strong></li>
                <li>20% di <strong>Emas</strong> atau Pasar Uang</li>
            </ul>
            <p>Seimbang antara pertumbuhan dan keamanan. Cocok untuk jangka menengah-panjang.</p>
        </div>
        """, unsafe_allow_html=True)
    
    elif st.session_state.selected_risk == "agresif":
        st.markdown("""
        <div class="alert-info">
            <strong>🚀 High Risk High Return — Rekomendasi:</strong>
            <ul>
                <li>60-70% di <strong>Reksadana Saham</strong> atau Saham langsung</li>
                <li>20% di <strong>Obligasi</strong> untuk penyeimbang</li>
                <li>10% di <strong>Emas</strong> atau Pasar Uang</li>
            </ul>
            <p>Potensi return tertinggi, tapi harus siap dengan fluktuasi jangka pendek.</p>
        </div>
        """, unsafe_allow_html=True)

st.markdown("---")

st.markdown("---")
st.markdown("""
<div style="text-align:center; color:#6c757d;">
    <p><em>⚠️ Disclaimer: Ini hanya edukasi, bukan rekomendasi investasi. 
    Selalu riset sendiri atau konsultasi dengan profesional sebelum berinvestasi.</em></p>
</div>
""", unsafe_allow_html=True)