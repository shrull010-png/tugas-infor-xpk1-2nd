import streamlit as st

st.set_page_config(page_title="Tentang", page_icon="", layout="wide")


st.markdown("""
<style>
    .card-dark {
        background-color: #343a40;
        padding: 1.5rem;
        border-radius: 10px;
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
    .card-light:hover {
        box-shadow: 0 0 25px rgba(220, 220, 220, 0.5),
                    0 0 50px rgba(220, 220, 220, 0.2);    
        }
    .alert-info {
        background-color: #1a3a4a;
        border-left: 4px solid #17a2b8;
        padding: 1rem;
        border-radius: 8px;
        margin: 1rem 0;
    }
    .alert-info:hover {
        box-shadow: 0 0 20px rgba(255, 255, 255, 0.3),
                0    0 40px rgba(255, 255, 255, 0.1);
        transform: translateY(-2px);
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

st.title("Tentang Website Ini")
st.markdown("---")

st.markdown("""
<div class="card-dark" style="text-align:center;">
    <h2>Literasi Finansial</h2>
    <p style="font-size:1.1rem;">Mindset cepat kaya adalah merusak mental</p>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

st.markdown("""
<div class="alert-info">
    <p>Website ini dibuat untuk <strong>menyelesaikan tugas mata pelajaran Informatika dan literasi finansial masyarakat Indonesia bagi yang membacanya</strong> 
    agar setiap orang bisa:</p>
    <ul>
        <li>🧠 Memahami konsep dasar keuangan (aset, liabilitas, cashflow)</li>
        <li>🛡️ Menyiapkan dana darurat yang cukup</li>
        <li>📈 Mulai berinvestasi dengan aman dan sesuai profil risiko</li>
        <li>🚀 Mencapai kebebasan finansial secara bertahap</li>
    </ul>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

st.markdown("## 📋 Yang Ada di Website Ini")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="card-dark">
        <h3>📚 Dasar Keuangan</h3>
        <p>Materi fundamental:</p>
        <ul>
            <li>Aset vs Liabilitas</li>
            <li>Cashflow (arus kas)</li>
            <li>Dana Darurat</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card-dark">
        <h3>📈 Investasi Pemula</h3>
        <p>Panduan memulai:</p>
        <ul>
            <li>Jenis-jenis instrumen</li>
            <li>Profil risiko</li>
            <li>Tips & strategi</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card-dark">
        <h3>💡 Tips & Edukasi</h3>
        <p>Fitur tambahan:</p>
        <ul>
            <li>Carousel tips keuangan</li>
            <li>Rekomendasi profil risiko</li>
            <li>Alert & peringatan</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

st.markdown("## Sumber Informasi Terpercaya")
st.markdown("Materi di website ini disusun berdasarkan sumber-sumber resmi:")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="card-dark" style="text-align:center;">
        <h3>🏛️ OJK</h3>
        <p>Otoritas Jasa Keuangan</p>
        <p><small>Regulator industri keuangan Indonesia</small></p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card-dark" style="text-align:center;">
        <h3>🏦 BI</h3>
        <p>Bank Indonesia</p>
        <p><small>Bank sentral Republik Indonesia</small></p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card-dark" style="text-align:center;">
        <h3>📊 IDX</h3>
        <p>Bursa Efek Indonesia</p>
        <p><small>Bursa saham Indonesia</small></p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

st.markdown("## ⚠️ Disclaimer")
st.markdown("""
<div class="alert-info">
    <ul>
        <li>Website ini dibuat untuk <strong>tujuan edukasi</strong>, bukan sebagai rekomendasi investasi.</li>
        <li>Semua keputusan investasi adalah tanggung jawab masing-masing individu.</li>
        <li>Konsultasikan dengan <strong>perencana keuangan profesional</strong> sebelum mengambil keputusan besar.</li>
    </ul>
</div>
""", unsafe_allow_html=True)

st.markdown("---")
st.markdown("## 📬 Feedback & Saran")

with st.form("form_feedback"):
    nama = st.text_input("Nama (opsional)")
    pesan = st.text_area("Pesan atau saran untuk website ini")
    submitted = st.form_submit_button("📤 Kirim")
    
    if submitted:
        if pesan.strip():
            st.success("✅ Terima kasih! Feedback kamu sangat berarti untuk pengembangan website ini.")
        else:
            st.warning("⚠️ Silakan isi pesan terlebih dahulu.")

st.markdown("---")
st.markdown("""
<div style="text-align:center; color:#6c757d;">
    <p>Dibuat dengan menggunakan Streamlit</p>
    <p><small>© 2024 Website Literasi Finansial</small></p>
</div>
""", unsafe_allow_html=True)