
import  datetime
import streamlit as st
from PIL import Image
from streamlit_option_menu import option_menu
import pandas as pd
st.set_page_config(page_title="Mksss kb joshi",page_icon=":book-fill:", layout="wide")

img = Image.open("logo.jpg")

st.image(
            img,
            caption="Established in the year 2003.!!",
            width=800,
     channels="RGB"
 )
with st.sidebar:
    selected = option_menu(

        menu_title=None,
        options=["Home","Cultural Activity","Addmission","Contact","Placements"],
        icons=["house-fill","person-circle", "book-fill", "chat-left-quote-fill","award-fill"],
    
        default_index=0,


    )

if selected == "Home":
    st.title("KB Joshi Institute Of IT")
st.header("About US..!!")
st.subheader("Affiliated to S.N.D.T Women's University. Mumbai karvenagar pune 52")
st.markdown(
            "K.B. Joshi Institute of IT established in the year 2003. Joshi foundation has given a generous donation for "
            "the construction of Institute in the name of Pioneering"
            "  Full time three years Degree course in Computer Applications with English as a medium of instruction"
            "Admissions will be strictly on the basis of merit / score")

img = Image.open("collage_photo.jpeg")

st.image(
            img,
            caption="College Campus!!",
            width=500,
     channels="RGB"
 )

st.title("Principle Massege")
img = Image.open("principalpic.jpeg")

st.image(
            img,
            caption="Dr.Swati Sayankar!!",
            width=500,
     channels="RGB"
 )
st.write("The Power of Mind is like rays of sun dissipated..  When they Concentrate, they illumine.")
st.write("With Blessings of Bharat Ratna Dr. Maharshi Karve ,K.B.Joshi Institute of Information Technology. started in the year 2006 to accomplish the Vision ”Empowerment of Women in IT Education")


if selected == "Placements":
    st.title("Campus Placements.!!")

    img = Image.open("placementpage.jpeg")

    st.image(
        img,
        caption="Students which are placed in last year !!",
        width=400,
        channels="RGB",

    )
st.header("Maharshi Karve Stree Shikshan Samstha’s K.B.Joshi Institute of Information Technology, Admissions are open for BCA , B.Sc (IT), MSC(CS), MCA")
st.subheader("* E-Learning using Online Platform")
st.subheader("* Free Wi-Fi Facility")
st.subheader("* Placement Assistance in MNC’s")
st.subheader("* Students are Toppers in University Merit")
st.subheader("* Spacious Classroom")
st.subheader("* Well equipped Computer labs with Internet")
st.subheader("* Rich Library, Qualified Staff")
st.subheader("* Hostel Facility, Health Club")

if selected == "Cultural Activity":
    st.title("Let's Go To SEE The Cultural Events")
img = Image.open("avishkar.jpeg")
st.header("Avishkar 2024!")
st.image(
        img,
        caption="The Ghost Song !!",
        width=500,
        channels="RGB",

    )
img = Image.open("independant.jpeg")
st.header("Independace Day 2024!")
st.image(
        img,
        caption="Quick Heal Volunters !!",
        width=500,
        channels="RGB",

    )
st.subheader("volunters :")
st.write("1.Pratiksha Mahale")
st.write("2.Rachna Bhilare")
st.write("3.Vaishnavi Podar")
st.write("4.Rajnandini Rai")
st.write("5.Nandani Pednekar")
st.write("6.Anupama Rayphale")
st.write("7.Arpita Gajinkar")
st.write("8.Tejal Tonde")
st.write("9.Sakshi Temghare")

img = Image.open("youth.jpeg")
st.header("SNDT Youth Festival.!")
st.image(
        img,
        caption="Elocution Competation Winner ",
        width=500,
        channels="RGB",

    )

img = Image.open("traditional.jpeg")
st.header("Day's Celebration!")
st.image(
        img,
        caption="Traditional Day 2024!!",
        width=500,
        channels="RGB",

    )
if selected == "Contact":

    st.title("Stay Connected with us!!")
st.subheader("Rama Purushottam Vidya Sankul, 5th Floor,")
st.subheader("Karvenagar, Pune – 411 052 , Maharashtra, India.")
st.subheader("Tel. No.: +91-8767954498")
st.subheader("Fax No.: (020)25477599")
st.subheader("Email: kbjiitbca@maharshikarvebcapune.org / principal@maharshikarvebcapune.org")


if selected == "Addmission":
    st.title("Fill the form")


name = st.text_input("Enter your name: ")
address = st.text_area("Enter your address:")
std = st.selectbox("Enter your class to get addmission",
                           ("FYBCA", "FYBSC-IT", "SYBCA", "SYBSC-IT", "TYBCS", "TYBSC-IT"))
email = st.text_input("Enter Mail:")


age = st.slider("Enter your age", min_value=18, max_value=100, step=2)

date =st.date_input("Enter your birth", value=datetime.date(2023, 4, 13))  # 2023 , 4 , 13 default value
form=st.form('basic')
submitted= form.form_submit_button("submit")
if submitted:
    form.header("Your application has been submitted")
    form.write(name+' please make sure your details')
st.write("[Go to the official page >](https://maharshikarvebcapune.org/)")
st.stop()





