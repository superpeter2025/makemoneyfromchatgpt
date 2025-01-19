import streamlit as st

def main():
    st.title("Make Money from ChatGPT")

    # Initialize session state to track navigation
    if "step" not in st.session_state:
        st.session_state.step = "main_question"

    # Main navigation logic
    if st.session_state.step == "main_question":
        main_question()
    elif st.session_state.step == "sales_letter_question":
        sales_letter_question()
    elif st.session_state.step == "ebook_question":
        ebook_question()
    elif st.session_state.step == "web_app_question":
        web_app_question()
    elif st.session_state.step == "physical_product":
        st.write("Future versions of this chatbot will help you to create content and marketing campaigns to sell your physical product. Please send us an email at peter.sheceo@gmail.com to be notified when we update this chatbot")
    elif st.session_state.step == "digital_product":
        st.write("A digital product is usually easier to sell, and future versions of this chatbot will show you in detail and step by step how you can sell your digital product easily and efficiently. Please send us an email at peter.sheceo@gmail.com to be notified when we update this chatbot")
    elif st.session_state.step == "fiction":
        st.write("Future versions of this chatbot will teach you how to write Fiction with ChatGPT. Please send us an email at peter.sheceo@gmail.com to be notified when we update this chatbot")
    elif st.session_state.step == "non_fiction":
        st.write("Future versions of this chatbot will teach you how to write nonfiction. Please send us an email at peter.sheceo@gmail.com to be notified when we update this chatbot")
    elif st.session_state.step == "educational":
        st.write("Future versions of this chatbot will show you how to create interactive web-based applications that will teach your students everything they need to learn even while you are sleeping. Please send us an email at peter.sheceo@gmail.com to be notified when we update this chatbot")
    elif st.session_state.step == "qualifying_chatbot":
        st.write("Future versions of this chatbot will show you how to qualify prospects in order to generate high-quality leads. Please send us an email at peter.sheceo@gmail.com to be notified when we update this chatbot")
    elif st.session_state.step == "sales_chatbot":
        st.write("Future versions of this chatbot will show you how to create a complete sales process through a chatbot. Please send us an email at peter.sheceo@gmail.com to be notified when we update this chatbot")

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
