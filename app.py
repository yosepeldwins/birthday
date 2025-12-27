import streamlit as st
import time
import random

st.set_page_config(
    page_title="Untuk Inosensia ❤️",
    layout="centered"
)

# =====================
# STATE
# =====================
if "dark" not in st.session_state:
    st.session_state.dark = False

if "step" not in st.session_state:
    st.session_state.step = 0

# =====================
# MODE MALAM
# =====================
def toggle_dark():
    st.session_state.dark = not st.session_state.dark

bg = "#121212" if st.session_state.dark else "#fff0f3"
card = "#1e1e1e" if st.session_state.dark else "#ffffff"
text = "#f5f5f5" if st.session_state.dark else "#444"

st.markdown(f"""
<style>
body {{
    background-color: {bg};
}}
.card {{
    background: {card};
    padding: 30px;
    border-radius: 20px;
    text-align: center;
    box-shadow: 0 15px 40px rgba(0,0,0,0.3);
}}
.title {{
    font-size: 36px;
    color: #e91e63;
    font-weight: bold;
}}
.text {{
    color: {text};
    font-size: 17px;
    line-height: 1.7;
}}
.heart {{
    font-size: 30px;
    animation: float 2s infinite;
}}
@keyframes float {{
    0% {{ transform: translateY(0); }}
    50% {{ transform: translateY(-10px); }}
    100% {{ transform: translateY(0); }}
}}
</style>
""", unsafe_allow_html=True)

# =====================
# HEADER
# =====================
st.button("🌙 Mode Malam" if not st.session_state.dark else "☀️ Mode Terang", on_click=toggle_dark)

st.audio("musik.mp3", autoplay=True, loop=True)

st.markdown("<div class='card'>", unsafe_allow_html=True)

# =====================
# STEP 0 – OPENING
# =====================
if st.session_state.step == 0:
    st.markdown("<div class='title'>❤️ Selamat Ulang Tahun ❤️</div>", unsafe_allow_html=True)
    st.markdown("<div class='text'>Untuk Inosensia Yesika Cara</div>", unsafe_allow_html=True)
    st.image("foto.jpg", use_container_width=True)

    if st.button("💌 Buka pesanku"):
        st.session_state.step = 1

# =====================
# STEP 1 – SURAT PERTAMA
# =====================
elif st.session_state.step == 1:
    st.markdown("""
    <div class='text'>
    Hari ini bukan sekadar tanggal di kalender.  
    Hari ini adalah hari di mana seseorang yang sangat berarti hadir ke dunia.
    </div>
    """, unsafe_allow_html=True)

    if st.button("➡️ Lanjut"):
        st.session_state.step = 2

# =====================
# STEP 2 – SURAT KEDUA
# =====================
elif st.session_state.step == 2:
    st.markdown("""
    <div class='text'>
    Ino,  
    terima kasih sudah menjadi dirimu yang tulus, hangat, dan penuh cinta.  
    Kehadiranmu membuat hidupku terasa lebih lengkap.
    </div>
    """, unsafe_allow_html=True)

    if st.button("🤍 Aku masih di sini"):
        st.session_state.step = 3

# =====================
# STEP 3 – HADIAH RAHASIA
# =====================
elif st.session_state.step == 3:
    st.markdown("<div class='text'><strong>Ada hadiah kecil buat kamu 🎁</strong></div>", unsafe_allow_html=True)

    if st.button("🎁 Buka hadiahnya"):
        st.session_state.step = 4

# =====================
# STEP 4 – PESAN TERAKHIR
# =====================
elif st.session_state.step == 4:
    hearts = " ".join(random.choice(["❤️", "💖", "🤍"]) for _ in range(10))
    st.markdown(f"<div class='heart'>{hearts}</div>", unsafe_allow_html=True)

    st.markdown("""
    <div class='text'>
    Aku bersyukur dipertemukan denganmu.  
    Semoga hari-harimu selalu dipenuhi kebahagiaan.  

    <br><br>
    <strong>Aku mencintaimu, hari ini, esok, dan seterusnya ❤️</strong>
    </div>
    """, unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)
