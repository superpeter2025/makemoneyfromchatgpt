import streamlit as st
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(user_email):
    # Gmail SMTP setup 
    # Email content to Peter
    subject_to_peter = "New Email Subscription"
    body_to_peter = f"A new user has subscribed to updates with the email address: {user_email}"

    # Email content to user
    subject_to_user = "Thanks for Subscribing!"
    body_to_user = (
        "Thanks for subscribing, we will notify you whenever the 'Make Money From ChatGPT' chatbot is updated! "
        "This will enable you to learn how to profit from ChatGPT! - Peter (connect to me if you wish, at www.linkedin.com/in/superpeter)"
    )

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, sender_password)

            # Send email to Peter
            message_to_peter = MIMEMultipart()
            message_to_peter["From"] = sender_email
            message_to_peter["To"] = recipient_email
            message_to_peter["Subject"] = subject_to_peter
            message_to_peter.attach(MIMEText(body_to_peter, "plain"))
            server.sendmail(sender_email, recipient_email, message_to_peter.as_string())

            # Send email to user
            message_to_user = MIMEMultipart()
            message_to_user["From"] = sender_email
            message_to_user["To"] = user_email
            message_to_user["Subject"] = subject_to_user
            message_to_user.attach(MIMEText(body_to_user, "plain"))
            server.sendmail(sender_email, user_email, message_to_user.as_string())

        st.success("Thank you! Your email has been submitted, and we've sent you a confirmation email.")
    except Exception as e:
        st.error(f"An error occurred: {e}")

def main():
    st.title("ChatGPT Money-Making Guide")

    # Step 1: Initial Question
    if "step" not in st.session_state:
        st.session_state.step = "main_question"

    # Ensure email form is only processed once per submission
    if "email_submitted" not in st.session_state:
        st.session_state.email_submitted = False

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

    # Email subscription field
    with st.form(key="email_form"):
        email = st.text_input(
            "Please enter your email address to be notified whenever we update this (amazing) app! (Your email is kept confidential and NEVER shared without your express permission)."
        )
        submit_button = st.form_submit_button(label="Submit")

        if submit_button and email and not st.session_state.email_submitted:
            send_email(email)
            st.session_state.email_submitted = True

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
