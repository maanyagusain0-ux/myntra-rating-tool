import streamlit as st
import os
from main import main

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Myntra Product Rating Extraction",
    page_icon="🛍️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------
# Custom CSS
# -----------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

html,
body,
[class*="css"]{
font-family:'Poppins',sans-serif;
}
#MainMenu{
visibility:hidden;
}

footer{
visibility:hidden;
}

            
.stDeployButton{
display:none;
}

.stApp{
    background: linear-gradient(
        135deg,
        #FFD1E8 0%,
        #FFB3D9 40%,
        #FFCCE6 70%,
        #FFEAF5 100%
    );
}

/* Sidebar */

[data-testid="stSidebar"]{

    background: linear-gradient(
        180deg,
        #FFD54F 0%,
        #FFA726 50%,
        #FB8C00 100%
    );

    border-right:3px solid #EF6C00;

    padding:25px;

    box-shadow:0 10px 25px rgba(0,0,0,.08);

}
/* Buttons */

.stButton>button{

width:100%;

height:55px;

background:#FF2E63;

color:white;

border:none;

border-radius:12px;

font-size:18px;

font-weight:600;

transition:.3s;

}

.stButton>button:hover{

background:#e73561;

transform:translateY(-2px);

box-shadow:0px 6px 18px rgba(255,63,108,.25);

}

/* Download */

.stDownloadButton>button{

width:100%;

height:55px;

background:#10b981;

color:white;

border:none;

border-radius:12px;

font-size:18px;

font-weight:600;

}

.stDownloadButton>button:hover{

background:#059669;

}

/* Progress */

.stProgress > div > div > div > div{

background:linear-gradient(
90deg,
#ff3f6c,
#ff6b95
);

}

/* Upload */

[data-testid="stSidebar"]{

background:linear-gradient(
180deg,
#FFF7ED 0%,
#FFEDD5 50%,
#FFE4C4 100%
);

border-right:2px solid #FDBA74;

}

/* Metric */

[data-testid="metric-container"]{

background:white;

padding:18px;

border-radius:15px;

box-shadow:0px 3px 10px rgba(0,0,0,.06);

}

/* Success */

[data-testid="stSuccess"]{

border-radius:12px;

}

/* Info */

[data-testid="stInfo"]{

border-radius:12px;

}

</style>
""",unsafe_allow_html=True)

# -----------------------------
# Sidebar
# -----------------------------
with st.sidebar:

    st.image("assets/logo.png", width=200)

    st.markdown("## Product Rating Tool")

    st.caption("Internal Automation Portal")

    st.divider()

    st.success("🟢 System Ready")

    st.info(
        """
### Workflow

📂 Upload Excel

🚀 Start Extraction

📥 Download Report
"""
    )

    st.divider()

    st.markdown("### Application")

    st.write("**Version:** 1.0")

    st.write("**Environment:** Production")

    st.write("**Status:** Online")

# -----------------------------
# Header
# -----------------------------

left, right = st.columns([1.2, 8])

with left:

    st.image("assets/logo.png", width=200)

with right:

    st.markdown("""
    <h1 style="
    margin-bottom:0px;
    color:#222;
    font-size:38px;
    font-weight:700;
    ">
    Product Rating Extraction
    </h1>
    """, unsafe_allow_html=True)

    st.markdown("""
    <p style="
    color:#6b7280;
    font-size:17px;
    margin-top:0;
    ">
    Myntra Internal Automation Portal
    </p>
    """, unsafe_allow_html=True)

st.divider()

# -----------------------------
# Upload Section
# -----------------------------

st.subheader("📂 Upload Product Excel")

uploaded_file = st.file_uploader(
    "",
    type=["xlsx","xls"],
    label_visibility="collapsed"
)

if uploaded_file is not None:

    os.makedirs("data", exist_ok=True)

    input_path = os.path.join("data", uploaded_file.name)

    with open(input_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success("Excel uploaded successfully!")

    st.write("")

    # Dashboard
    col1,col2,col3 = st.columns(3)

    with col1:
        st.metric(
            "File Name",
            uploaded_file.name
        )

    with col2:
        st.metric(
            "Status",
            "Ready"
        )

    with col3:
        st.metric(
            "Version",
            "1.0"
        )

    st.write("---")

    if st.button("🚀 Start Rating Extraction"):

        st.subheader("Extraction Progress")

        progress_bar = st.progress(0)

        status = st.empty()

        with st.spinner("Opening Chrome and extracting ratings..."):

            output_file = main(
                input_path,
                progress_bar=progress_bar,
                status_text=status
            )

        progress_bar.progress(100)

        status.success("✅ Rating Extraction Completed")

        st.balloons()

        st.success("🎉 Report Generated Successfully!")

        st.write("")

        with open(output_file, "rb") as file:

            st.download_button(
                label="📥 Download Product Rating Report",
                data=file,
                file_name="ProductRatings.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                use_container_width=True
            )

st.write("---")
st.caption("© 2026 Myntra Product Rating Extraction Tool | Internal Use")