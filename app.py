import streamlit as st
import base64


def home():
    
    st.set_page_config(
        page_title="Mark Nikko B. Cortes' Portfolio",
    )

    with open("styles/main.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    with open("assets/Nikko.png", "rb") as img_file:
        img = "data:image/png;base64," + base64.b64encode(img_file.read()).decode()

    with open("assets/Cortes, Mark Nikko B.pdf", "rb") as pdf_file:
        pdf_bytes = pdf_file.read()

    st.write(f"""<div class="title">Hi! My name is <strong> Mark Nikko B. Cortes</strong></div>""", unsafe_allow_html=True)

    st.write("##")

    st.write(f"""
    <div style="display: flex; justify-content: center;">
        <img src="{img}" alt="Mark Nikko B. Cortes" width="300" height="300" styles="border-radius: 50%; object-fit: cover; margin-top: 40px; margin-bottom: 40px;">
    </div>
        """, unsafe_allow_html=True)
    
    st.write("##")
    
    st.write(f"""<div class="subtitle" style="text-align: center;">Bachelor of Science in Information Tecnhology</div>""", unsafe_allow_html=True)

    st.write("##")

    st.subheader("About Me")
    st.write("""
        - I am a 4th yr student in Cebu Institute of Technology - University, taking up BSIT (Bachelor of Science in Information Technology).
             
        - My hobbies are playing basketball and playing video games.

        - Excellent in english communication skills.

        - Proficient in MS Office (Word, Excel, Powerpoint).

        - Knowledgeable in C, Java, HTML, Python, etc.  
             
    """)

    st.write("##")

    st.download_button(
        label="Download my CV",
        data=pdf_bytes,
        file_name="Cortes, Mark Nikko B.pdf",
        mime="application/pdf",
    )
    
    st.write("##")

    st.write(f"""<div class="subtitle" style="text-align: center;">Thank you!</div>""", unsafe_allow_html=True)

  
if __name__ == "__main__":

    home()