import streamlit as st
st.title("Hello,2208!")
st.header("标题")
st.subheader("二级标题")
st.text("文本")

st.markdown("this is an image:\nhttps://img-s-msn-com.akamaized.net/tenant/amp/entityid/BB1nzH55.img?w=612&h=344&m=6&x=40&y=126&s=462&d=220")

if st.checkbox("Show/Hide"):
    st.text("you checked the box")

status = st.radio("select gender:",
                 ('male','female'))

if status == 'male':
    st.success("Male")
else:
    st.success("Female")

hobbies = st.multiselect("Hobbies:",
    ['Reading',
     'Writing',
     'Coding',
     'Traveling'])
st.write("you selected:",hobbies)

if st.button("about"):
    st.text("Streamlit is a great tool")

name = st.text_input("enter your name:")
if st.button("Submit"):
    st.write("Hello,",name)

level = st.slider("Select your level",1,5)
st.write("You selected:",level)

from fastai.vision.all import *
upload_img = st.file_uploader("Upload an image",
                             type=['jpg',
                                  'png'])

if upload_img is not None:
    img = PILImage.create(upload_img)
    st.image(img.to_thumb(256,256),
            caption="Uploaded image")

