import streamlit as st

def main():
    st.title("ChatGPT Money-Making Guide")

    # Step 1: Initial Question
    if "step" not in st.session_state:
        st.session_state.step = "main_question"

    # Handle navigation
    if st.session_state.step == "main_question":
        main_question()
    elif st.session_state.step == "sales_letter_question":
        sales_letter_question()
    elif st.session_state.step == "ebook_question":
        ebook_question()
    elif st.session_state.step == "web_app_question":
        web_app_question()
    elif st.session_state.step == "physical_product":
        st.write("Do this for physical product")
    elif st.session_state.step == "digital_product":
        st.write("Do that for digital product")
    elif st.session_state.step == "fiction":
        st.write("Write this fiction")
    elif st.session_state.step == "non_fiction":
        st.write("Write this non-fiction")
    elif st.session_state.step == "educational":
        st.write("Learn this ADDIE")
    elif st.session_state.step == "qualifying_chatbot":
        st.write("Choose this")
    elif st.session_state.step == "sales_chatbot":
        st.write("Close this deal")

def main_question():
    st.write("**QUESTION**: What would you like to do?")
    if st.button("Create a sales letter"):
        st.session_state.step = "sales_letter_question"
    if st.button("Create an ebook"):
        st.session_state.step = "ebook_question"
    if st.button("Create a web app"):
        st.session_state.step = "web_app_question"

def sales_letter_question():
    st.write("**QUESTION**: What type of product?")
    if st.button("Physical product"):
        st.session_state.step = "physical_product"
    if st.button("Digital product"):
        st.session_state.step = "digital_product"

def ebook_question():
    st.write("**QUESTION**: What type of ebook?")
    if st.button("Fiction"):
        st.session_state.step = "fiction"
    if st.button("Non-fiction"):
        st.session_state.step = "non_fiction"

def web_app_question():
    st.write("**QUESTION**: What type of web app?")
    if st.button("Educational"):
        st.session_state.step = "educational"
    if st.button("Qualifying chatbot"):
        st.session_state.step = "qualifying_chatbot"
    if st.button("Sales chatbot"):
        st.session_state.step = "sales_chatbot"

if __name__ == "__main__":
    main()
