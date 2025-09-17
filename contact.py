    
import streamlit as st
from PIL import Image

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def contact():
    st.write("##")
    col1, col2, col3 = st.columns([1,1,2])
    contact_form = '''
        <form action="https://formsubmit.co/tokas.2sonu@gmail.com" method="POST">
            <input type="hidden" name="_autoresponse" value="Thank You for spending your valuable time on my website. I will contact you soon.">
            <input type="hidden" name="_template" value="table">
            <input type="hidden" name="_next" value="https://vivek-2567-book-recommendation-system-app-y9vhhy.streamlit.app">
            <input type="text" name="name" id = 'input' placeholder = "Your Name" required>
            <input type="email" name="email" id = 'input' placeholder = "Your Email" required>
            <textarea name = 'message' id = 'input' placeholder = 'Your Message' required></textarea>
            <button onclick="document.getElementById('input').value = ''" type="submit">Send</button>
        </form>
    '''

    with col1:
        st.subheader("Meet the Developer")
        pp = Image.open("profile pic/profile-pic.png")
        st.image(pp, output_format='PNG',width = 230)
        st.write("  Developer : Vivek Goel")


    with col2:
        for _ in range(6):
            st.write("")

        st.write("Connect with me at:")
        st.write("[Github](https://github.com/vivek-2567)")
        st.write("[Linkedin](https://www.linkedin.com/in/vivek-goel-0207/)")
        st.write("Mail me @")
        st.write("[Mail](mailto:vivekgoel0207@gmail.com)")

    with col3:
        st.subheader("Send me a Message :rocket:")
        st.markdown(contact_form,unsafe_allow_html=True)
        local_css("style/style.css")
   