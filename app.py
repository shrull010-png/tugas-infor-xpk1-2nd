import streamlit as st

st.set_page_config(
    page_title="Literasi Finansial",
    page_icon="💵",
    layout="wide"
)


st.markdown("""
<style>
    .navbar {
        display: flex;
        gap: 0.5rem;
        background-color: #343a40;
        padding: 0.8rem 1.2rem;
        border-radius: 12px;
        margin-bottom: 1.5rem;
        flex-wrap: wrap;
        
    }
    .navbar a {
        color: #f8f9fa !important;
        text-decoration: none;
        padding: 0.5rem 1.2rem;
        border-radius: 8px;
        font-weight: 500;
        font-size: 0.95rem;
        transition: all 0.2s;
    }
    .navbar a:hover {
        background-color: #6c757d;
    }
      
    .card-dark {
        border-top-color: #17a2b8;
        background-color: #343a40;
        padding: 1.5rem;
        border-radius: 12px;
        margin-bottom: 1rem;
        border-top: 4px solid #6c757d;
    }
    .card-dark:hover {
        border-top-color: #F1C40F;
        box-shadow: 0 0 20px rgba(255, 193, 7, 0.3),
                    0 0 40px rgba(255, 193, 7, 0.1);
    }
    .alert-info {
        background-color: #1a3a4a;
        border-left: 4px solid #17a2b8;
        padding: 1rem;
        border-radius: 8px;
        margin: 1rem 0;
    }
    .alert-info:hover {
        box-shadow: 0 0 20px rgba(0, 255, 255, 0.3),
                    0 0 40px rgba(0, 200, 200, 0.1);
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
        
    .navbar {
        display: flex;
        gap: 0.5rem;
        background-color: #343a40;
        ...
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="navbar">
    <a href="/" target="_self">🏠 Home</a>
    <a href="/Dasar_Keuangan" target="_self">📚 Dasar Keuangan</a>
    <a href="/Investasi_Pemula" target="_self">📈 Investasi Pemula</a>
    <a href="/Tentang" target="_self">About</a>
</div>
""", unsafe_allow_html=True)


st.title("💵 Literasi Finansial")
st.markdown("### Investasi bukan untuk mempercepat kekayaan tetapi menjaga kekayaan")
st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="card-dark">
        <h3>📚 Dasar Keuangan</h3>
        <p>Pahami perbedaan aset & liabilitas, cara mengatur cashflow, dan pentingnya dana darurat.</p>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Pelajari →", url="/Dasar_Keuangan")

with col2:
    st.markdown("""
    <div class="card-dark">
        <h3>💹 Investasi Pemula</h3>
        <p>Mulai investasi dengan aman. Kenali reksadana, saham, dan sesuai profil risiko kamu.</p>
    </div>
    """, unsafe_allow_html=True)
    st.link_button("Pelajari →", url="/Investasi_Pemula")

st.markdown("---")

st.markdown("""
<div class="alert-info">
    <strong>💡 Fakta:</strong> Secara global, hanya sekitar 33% orang dewasa yang dianggap melek finansial, dengan kesenjangan yang sangat dipengaruhi oleh pendidikan, gender, dan pendapatan regional.
</div>
""", unsafe_allow_html=True)

st.markdown("## 🎯 Kenapa Literasi Finansial Itu Penting?")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div style="background-color:#1f1e1e; color:#afafaf; padding:1.5rem; border-radius:12px;">
        <h4>✅ Dengan Literasi Finansial</h4>
        <ul>
            <li>Terhindar dari utang konsumtif</li>
            <li>Siap menghadapi keadaan darurat</li>
            <li>Bisa pensiun dengan tenang</li>
            <li>Mencapai kebebasan finansial</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style="background-color:#1f1e1e; color:#afafaf; padding:1.5rem; border-radius:12px;">
        <h4>❌ Tanpa Literasi Finansial</h4>
        <ul>
            <li>Gaji habis tanpa tabungan</li>
            <li>Terjebak pinjol & utang berbunga tinggi</li>
            <li>Tidak punya dana darurat</li>
            <li>Stress finansial berkepanjangan</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)


with st.sidebar:
    st.header("📋 About Website")
    st.info("""
    Website ini dibuat untuk memenuhi tugas mata pelajaran Informatika dengan tema literasi finansial masyarakat Indonesia.
    """)
    
    st.markdown("---")
    st.markdown("### Sumber Terpercaya")
    st.markdown("- OJK (Otoritas Jasa Keuangan)")
    st.markdown("- BI (Bank Indonesia)")
    st.markdown("- IDX (Bursa Efek Indonesia)")