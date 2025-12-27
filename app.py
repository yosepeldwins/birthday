import streamlit as st

st.set_page_config(page_title="Selamat Ulang Tahun Inosensia Yesika Cara ❤️", layout="centered")

st.markdown(
    """
    <style>
    body {
        background: linear-gradient(135deg, #ff9a9e, #fad0c4);
    }
    .title {
        text-align: center;
        color: #e91e63;
        font-size: 40px;
        font-weight: bold;
    }
    .message {
        text-align: center;
        font-size: 18px;
        color: #444;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<div class='title'>❤️ Selamat Ulang Tahun ❤️</div>", unsafe_allow_html=True)

st.image(
    "https://images.unsplash.com/photo-1517841905240-472988babdf9",
    use_container_width=True
)

st.markdown("""
<div class='message'>
<p>Hari ini adalah hari yang sangat spesial, karena dunia diberkahi dengan kehadiranmu.</p>
<p>Terima kasih sudah menjadi bagian terindah dalam hidupku.</p>
<p>Semoga semua impianmu tercapai dan senyummu selalu menghiasi harimu.</p>
<p><strong>Aku mencintaimu sepenuh hati 💕</strong></p>
</div>
""", unsafe_allow_html=True)

if st.button("Klik untuk pelukan virtual 🤗"):
    st.success("Pelukan hangat dariku untukmu 💖")
