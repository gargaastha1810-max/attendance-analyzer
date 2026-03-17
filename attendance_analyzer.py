import streamlit as st

st.set_page_config(page_title="Attendance Analyzer", page_icon="🎓", layout="centered")

st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap');
        html, body, [class*="css"] { font-family: 'Poppins', sans-serif; }
        .stApp { background-color: #fde3e3; }
        .title-box {
            background-color: #e3f2fd;
            padding: 18px;
            border-radius: 12px;
            text-align: center;
            margin-bottom: 25px;
        }
        .title-box h1 { color: #0d47a1; font-size: 28px; font-weight: 700; margin: 0; }
        .result-box {
            background-color: #e8f5e9;
            border-left: 5px solid #2e7d32;
            padding: 16px 20px;
            border-radius: 10px;
            font-size: 16px;
            color: #1b5e20;
            margin-top: 20px;
        }
        .error-box {
            background-color: #ffebee;
            border-left: 5px solid #c62828;
            padding: 16px 20px;
            border-radius: 10px;
            font-size: 16px;
            color: #b71c1c;
            margin-top: 20px;
        }
        .stTextInput > div > div > input { background-color: #e3f2fd; border-radius: 8px; }
        .stButton > button {
            background-color: #1976d2;
            color: white;
            font-weight: 600;
            border-radius: 10px;
            padding: 10px 30px;
            font-size: 16px;
            width: 100%;
            border: none;
            margin-top: 10px;
        }
        .stButton > button:hover { background-color: #1565c0; }
        label { color: #0d47a1 !important; font-weight: 600; }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="title-box"><h1>🎓 Attendance Analyzer</h1></div>', unsafe_allow_html=True)

total = st.text_input("Total Lectures Conducted")
attended = st.text_input("Lectures Attended")
target = st.text_input("Target Attendance %")

if st.button("Analyze Attendance"):
    try:
        t = int(total)
        a = int(attended)
        tgt = int(target)

        attendance = (a / t) * 100

        x = 0
        while ((a + x) / (t + x)) * 100 < tgt:
            x += 1

        bunk = 0
        while ((a) / (t + bunk + 1)) * 100 >= tgt:
            bunk += 1

        st.markdown(f"""
            <div class="result-box">
                📊 <b>Current Attendance:</b> {attendance:.2f}%<br><br>
                📚 <b>Attend next {x} lectures</b> to reach {tgt}%<br><br>
                😎 <b>You can safely bunk {bunk} lectures</b>
            </div>
        """, unsafe_allow_html=True)

    except:
        st.markdown('<div class="error-box">⚠️ Please enter valid numbers!</div>', unsafe_allow_html=True)
