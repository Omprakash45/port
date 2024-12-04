import streamlit as st
from PIL import Image

# Load an image for the background
bg_image = "profile.jpg"  # Replace with your image path

# Set background image
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url({bg_image});
        background-size: cover;
        background-attachment: fixed;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Adding a sidebar
st.sidebar.title("Navigation")
st.sidebar.write("Use the navigation below to browse through the portfolio.")
sections = ["Home", "Skills", "Experience", "Education", "Certifications", "Contact"]
selection = st.sidebar.radio("Go to:", sections)

# Home Section
if selection == "Home":
    st.title("👋 Om Choudhary")
    st.subheader("Aspiring Data Scientist | AI & ML Enthusiast")
    st.markdown("""
    <div style='text-align: justify; color: white;'>
    I'm an aspiring Data Scientist with a knack for turning data into actionable insights. Currently pursuing my BCA Full Stack Development at Jaipur National University, I have a solid foundation in Python, HTML5, CSS3, and an avid interest in Artificial Intelligence and Machine Learning.
    </div>
    """, unsafe_allow_html=True)

    st.write("---")
    # Adding Profile Image
    profile_image = Image.open("profile.jpg")  # Replace with your profile image path
    st.image(profile_image, width=200, caption="Om Choudhary")

# Skills Section
elif selection == "Skills":
    st.header("🔧 Top Skills")
    st.markdown("""
    - **Python (Programming Language)**
    - **Data Analysis & Visualization**
    - **HTML5 & CSS3 Development**
    - **Artificial Intelligence & Machine Learning**
    """, unsafe_allow_html=True)
    
# Experience Section
elif selection == "Experience":
    st.header("💼 Experience")
    st.write("### ImaginXP")
    st.write("**Role:** Student")
    st.write("**Duration:** August 2023 - Present")
    st.write("**Location:** Jaipur, Rajasthan, India")

    st.write("### CollegeDekho")
    st.write("**Role:** Student")
    st.write("**Duration:** August 2023 - April 2024")
    st.write("**Location:** Jaipur, Rajasthan, India")

# Education Section
elif selection == "Education":
    st.header("🎓 Education")
    st.write("### Jaipur National University")
    st.write("**Degree:** BCA Full Stack Development")
    st.write("**Duration:** August 2023 - August 2026")
    st.write("**Location:** Jaipur, Rajasthan, India")
    
    st.write("### Ranabai School Bagoat")
    st.write("**Class 12, Science Bio**")
    st.write("**Duration:** July 2021 - April 2023")

# Certifications Section
elif selection == "Certifications":
    st.header("🏅 Certifications")
    st.write("""
    - **Microsoft Learn Student Ambassador**
    - **LetsUpgrade**
    - **Programming Hub**
    """)
    
# Contact Section
elif selection == "Contact":
    st.header("📞 Contact Information")
    st.write("**Email:** [op548017@gmail.com](mailto:op548017@gmail.com)")
    st.write("**LinkedIn:** [omprakash818](https://www.linkedin.com/in/omprakash818)")

    st.write("---")
    st.subheader("Get in Touch")
    st.text_input("Enter your name:")
    st.text_input("Enter your email:")
    st.text_area("Message:")
    if st.button("Send"):
        st.success("Your message has been sent!")

# Adding custom styles for text
st.markdown(
    """
    <style>
    .stButton>button {
        background-color: #4CAF50; /* Green */
        border: none;
        color: white;
        padding: 10px 24px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
        border-radius: 12px;
    }
    .stTextInput>div>div>input {
        border: 2px solid #3498db;
        padding: 10px;
    }
    </style>
    """, unsafe_allow_html=True
)
