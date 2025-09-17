from helper import get_few_shot_db_chain
import streamlit as st
from contact import contact
from streamlit_option_menu import option_menu
from table import discounts,t_shirt


st.set_page_config(page_title="SQL Interaction System", layout="wide")

page_style = '''
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                </style>
            '''

st.markdown(page_style,unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: Dark Gray;'>SQL Interaction System</h1>",
            unsafe_allow_html=True)

selected_tab = option_menu(
    menu_title = None,
    options = ['Interaction', 'Tables',"Get in Touch with Me"],
    icons = ['chat-left-text','table','envelope-open'],
    menu_icon = 'cast',
    default_index = 0,
    orientation = 'horizontal',
    styles={
        "icon": {"font-size": "20px"},
        "nav-link": {"font-size": "18px"}
    }
)

if selected_tab == 'Interaction':
    col1,col2,col3 = st.columns([2,5,2])
    with col2:
        ques = st.text_input("Question: ")
        # but = st.button("Answer")
        if ques:
            chain = get_few_shot_db_chain()
            # if but:
            result = chain(ques)
            print(result)
            st.header("Answer:")
            st.write("SQL: " + result['intermediate_steps'][2]['sql_cmd'])
            st.subheader("Answer: " + result['result'])
                # st.write(result)

elif selected_tab == 'Tables':
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("T-Shirt Data")
        st.dataframe(t_shirt)
    with col2:
        st.subheader("Discount Data")
        st.dataframe(discounts)

elif selected_tab == 'Get in Touch with Me':
    contact()