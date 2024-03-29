
from click import option
import requests
from soupsieve import select
import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_lottie import st_lottie_spinner
import pandas as pd
import streamlit.components.v1 as components
import requests as re 
from streamlit_option_menu import option_menu
import pandas as pd
from io import BytesIO
# Page Config




st.set_page_config(layout="wide")
############ NAV BAR ##############
with st.sidebar:
      # selected = option_menu(
      #     menu_title = "User Information",
      #     options =["Login","Registrations"],
      #     icons=['home'],
      #     menu_icon="cast", default_index=1,
      #     )

  #st.set_page_config(page_title="StyleBar", layout="wide")
    st.sidebar.image("logo.png", use_column_width=True,width=300)
  #st.sidebar.title("Haircut & Treatment")

    st.title("About US")
    st.write("""Our Stylebar family was created because quite frankly we were bored of the same old generic salons that keep popping up and offer nothing more than average service in a bland setting. We have done something different, we have a created a luxurious and relaxing environment where you can celebrate just how fabulous you are. Our exceptional hair, nail and beauty services will leave you feeling pampered, rejuvenated and renewed.
  Our leading super salon has everything under one roof offering hair, nails, HD brows and makeup to all other beauty essentials. We have carefully put together a team that are guaranteed to offer you some of the best services around.
  Creativity and the perfection mean that we want to deliver more than good or even excellent, we want to be the number one choice for the style conscious.""")
 

selected3 = option_menu(None, ["Home", "Our Services",  "Booking", 'Notifications','Login','Sign Up'], 
    icons=['house', 'cloud-upload', "list-task", 'gear'], 
    menu_icon="cast", default_index=0, orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "#F0DADD"},
        "icon": {"color": "white", "font-size": "25px"}, 
        "nav-link": {"font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "#BEEABB"},
    }
)

############## END NAV ###############

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
##################

st.markdown("""
        <style>
               .css-18e3th9 {
                    padding-top: 3.52rem;
                    padding-bottom: 10rem;
                    padding-left: 5rem;
                    padding-right: 5rem;
                }
               .css-1d391kg {
                    padding-top: 3.5rem;
                    padding-right: 1rem;
                    padding-bottom: 3.5rem;
                    padding-left: 1rem;
                }
        </style>
        """, unsafe_allow_html=True)


###############
#st.write('<style>div.block-container{padding-top:3.5rem;}</style>', unsafe_allow_html=True)
if (selected3=="Sign Up"):
    st.title("Registration")
    my_form = st.form(key='form-1')
    # creating input fields
    fname = my_form.text_input('First Name:')
    lname = my_form.text_input('Last Name:')
    email = my_form.text_input('Email:')
    # creating radio button
    gender = my_form.radio('Gender', ('Male', 'Female'))
    # creating slider
    age = my_form.slider('Age:', 1, 120)
    # creating date picker
    bday = my_form.date_input('Enter Birthdate:')
    # creating a text area
    address = my_form.text_area('Enter Address:')
    # creating a submit button
    submit = my_form.form_submit_button('Submit')
    # the following gets updated after clicking on submit, printing the details of the fields that are submitted in the form
    if(submit == 'Submit'):
        st.write('Name is '+fname+' '+lname)
        st.write('Email is '+email)
        st.write('Gender is '+gender)
        st.write('Age is '+str(age))
        st.write('Birthday is '+str(bday))
        st.write('Address is '+address)
elif (selected3=="Login"):
  st.title("Login")
  my_form = st.form(key='form-1')
  username = my_form.text_input("UserName")
  passwords = my_form.text_input("Password")
  submit = my_form.form_submit_button('Submit')
  if(submit == 'Submit'):
       # flag = False
        st.balloons()
        st.write("Welcome")
elif (selected3=="Booking"):
      df= pd.read_csv("AllProductList.csv")
      st.header("Request a New Appointment")
      with st.form("my_form"):
        col1, col2 = st.columns(2)
        with col1:
          options = st.multiselect(
      'Select Services',options=list(df['Product List']),default=["Wash and Style"],)
        with col2:
            st.date_input("Date")
        col1, col2 = st.columns(2)
        with col1:
          st.time_input("Time")
        with col2: 
          st.text_input("Email")
        st.subheader("Payment Information")
        col1, col2, col3 = st.columns(3)
        
        with col1:
          st.text_input("Credit Card Number")
        with col2:
          st.text_input("Exp Year:")
        with col3:
          st.text_input("CVC")
        #my_form.form_submit_button()
        submitted = st.form_submit_button("Submit")
elif(selected3=="Our Services"):
      def to_excel(df):
        output = BytesIO()
        writer = pd.ExcelWriter(output, engine='xlsxwriter')
        df.to_excel(writer, index=False, sheet_name='Sheet1')
        workbook = writer.book
        worksheet = writer.sheets['Sheet1']
        format1 = workbook.add_format({'num_format': '0.00'}) 
        worksheet.set_column('A:A', None, format1)  
        writer.save()
        processed_data = output.getvalue()
        return processed_data
      df1 = pd.read_csv("productsList.csv")
      df2 = pd.read_csv("spaList.csv")

      st.subheader("Salon Sevices & Pricing")
      st.table(df1)  
      df_xlsx1 = to_excel(df1)
      st.download_button(label='📥 Download this price list',
                                data=df_xlsx1 ,
                                file_name= 'df_test.xlsx')

      st.subheader("Spa Sevices & Pricing")
      st.table(df2)  
      df_xlsx2 = to_excel(df2)
      st.download_button(label='📥 Download this price list',
                                data=df_xlsx2 ,
                                file_name= 'df_test.xlsx')
      
elif(selected3=="Home"):
  lottie_url_download = "https://assets5.lottiefiles.com/packages/lf20_aabgnkl3.json"


  def load_lottieurl(url: str):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()


  lottie_url_hello = "https://assets5.lottiefiles.com/private_files/lf30_docl0D.json"
    # lottie_url_download = "https://assets5.lottiefiles.com/private_files/lf30_docl0D.json"
  lottie_hello = load_lottieurl(lottie_url_hello)
    # lottie_download = load_lottieurl(lottie_url_download)
  lottie_url_barbar = "https://assets7.lottiefiles.com/packages/lf20_lo5a0g5i.json"
  lottie_barbar =load_lottieurl(lottie_url_barbar)

  st_lottie(lottie_hello, height=100)
  st.markdown("<h1 style='text-align: center; font-family:  Century Gothic	, sans-serif; color: rgb(154, 93, 255);'>STYLE BAR</h1>", unsafe_allow_html=True)
  #st.markdown("<h6 style='text-align: center; font-family:  cursive, sans-serif; color: #CB0B94;'>Made with love 💖</h1>", unsafe_allow_html=True)
  #st_lottie(lottie_barbar,height=200)


  # Search Button
  # options = st.multiselect(
  #      'What are your favoriute brands ',
  #      ['GoodWell', 'HairBotox', 'Hannon', 'Joico'],
  #      ['Moroccanoil', 'Mizani']
  #      )

  # names = pd.DataFrame({'labels':["GoodWell","HairBotox","Hannon","Joico","Moroccanoil","Mizani"]})
  # nameSelect = st.multiselect(
  #     "What are your favorite brands",
  #     options=list(names['labels']), # convert to list
  #     default=["GoodWell"]
  # )




  # if(nameSelect[0]=="GoodWell"):
  #     #col1, col2, col3,col4, col5,col6,col7,col8,col9,co10 = st.columns(10)
  #     col1, col2, col3 = st.columns(3)
  #     with col1:
          
  #         st.image("https://cdn.shopify.com/s/files/1/0282/5961/4817/products/goldwell-soft-colour-10p-pastel-pearl-blonde-150ml-571939_300x.jpg?v=1623337415")
  #         st.text("Pearl Blonde 150ml")
  #     with col2:
          
  #         st.image("https://cdn.shopify.com/s/files/1/0282/5961/4817/products/goldwell-soft-colour-10p-pastel-pearl-blonde-150ml-571939_300x.jpg?v=1623337415")
  #         st.text("Pearl Blonde 150ml")
      
  #     with col3:
          
  #         st.image("https://cdn.shopify.com/s/files/1/0282/5961/4817/products/goldwell-soft-colour-10p-pastel-pearl-blonde-150ml-571939_300x.jpg?v=1623337415")
  #         st.text("Pearl Blonde 150ml")
  #     # with col4:
  #     #     st.text("Goldwell ")
  #     #     st.image("https://cdn.shopify.com/s/files/1/0282/5961/4817/products/goldwell-soft-colour-10p-pastel-pearl-blonde-150ml-571939_300x.jpg?v=1623337415")
  #     # with col5:
  #     #     st.text("Goldwell ")
  #     #     st.image("https://cdn.shopify.com/s/files/1/0282/5961/4817/products/goldwell-soft-colour-10p-pastel-pearl-blonde-150ml-571939_300x.jpg?v=1623337415")

  #     # with col6:
  #     #     st.text("Goldwell ")
  #     #     st.image("https://cdn.shopify.com/s/files/1/0282/5961/4817/products/goldwell-soft-colour-10p-pastel-pearl-blonde-150ml-571939_300x.jpg?v=1623337415")


  # #st.image("https://cdn.shopify.com/s/files/1/0282/5961/4817/files/SB-GENERAL-VISIT-SALON-BANNER_150x.jpg?v=1607415994",width=500)


  # Search Options 
  query = st.text_input("Search Our Services! ")
  st.button("Search")
  # Unsplash API KEY
  #api_key = "JSOFZJXh0Ejyo_FVM5ChHe86RuDrofHVi2qYD2g3rMU"
  url =f"https://unsplash.com/napi/search?query={query}&per_page=10&xp="
  r = re.get(url)

  data = r.json()
  url_array=[]
  name_array=[]

  for item in data['photos']['results']:
      name = item['user']['name']
      name_array.append(name)
      url = item['urls']['thumb']
      url_array.append(url)

  for i in range(0,len(url_array)-3):
      col1, col2 , col3 = st.columns(3)
      with col1:
          st.image(url_array[i])
          st.write(name_array[i])
      with col2: 
          st.image(url_array[i+1])
          st.write(name_array[i+1])
      with col3:
          st.image(url_array[i+2])
          st.write(name_array[i+2])

  st.markdown("<h1 style='text-align: center; font-family:  Consolas, sans-serif; color: rgb(154, 93, 255);'>Why choose Stylebar?</h1>", unsafe_allow_html=True)
  # imageCarouselComponent = components.declare_component("image-carousel-component", path="frontend/public")

  # imageUrls = [
  #         "https://images.unsplash.com/photo-1562322140-8baeececf3df?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1469&q=80",
  #         "https://images.unsplash.com/photo-1559599076-9c61d8e1b77c?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=869&q=80",
  #         "https://images.unsplash.com/photo-1595476108010-b4d1f102b1b1?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=388&q=80",
  #         "https://images.unsplash.com/photo-1580618672591-eb180b1a973f?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=869&q=80",
  #         "https://images.unsplash.com/photo-1581404788767-726320400cea?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=869&q=80",
  #         "https://images.unsplash.com/photo-1580618864180-f6d7d39b8ff6?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=869&q=80",
  #         "https://images.unsplash.com/photo-1600948836101-f9ffda59d250?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=836&q=80",
  #         "https://images.unsplash.com/photo-1521590832167-7bcbfaa6381f?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=870&q=80",
  #         # "https://images.unsplash.com/photo-1513635269975-59663e0ac1ad?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=870&q=80",
  #         # "https://images.unsplash.com/photo-1595867818082-083862f3d630?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=870&q=80",
  #         # "https://images.unsplash.com/photo-1622214366189-72b19cc61597?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=687&q=80",
  #         # "https://images.unsplash.com/photo-1558180077-09f158c76707?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=764&q=80",
  #         # "https://images.unsplash.com/photo-1520106212299-d99c443e4568?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=687&q=80",
  #         # "https://images.unsplash.com/photo-1534430480872-3498386e7856?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=870&q=80",
  #         # "https://images.unsplash.com/photo-1571317084911-8899d61cc464?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=870&q=80",
  #         # "https://images.unsplash.com/photo-1624704765325-fd4868c9702e?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=764&q=80",
  #     ]
  # selectedImageUrl = imageCarouselComponent(imageUrls=imageUrls, height=200)

  # if selectedImageUrl is not None:
  #         st.image(selectedImageUrl)

  # st.snow()
  slider_images ="""
    <!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
* {box-sizing: border-box;}
body {font-family: Verdana, sans-serif;}
.mySlides {display: none;}
img {vertical-align: middle;}
/* Slideshow container */
.slideshow-container {
  max-width: 1000px;
  position: relative;
  margin: auto;
}
/* Caption text */
.text {
  color: #f2f2f2;
  font-size: 15px;
  padding: 8px 12px;
  position: absolute;
  bottom: 8px;
  width: 100%;
  text-align: center;
}
/* Number text (1/3 etc) */
.numbertext {
  color: #f2f2f2;
  font-size: 12px;
  padding: 8px 12px;
  position: absolute;
  top: 0;
}
/* The dots/bullets/indicators */
.dot {
  height: 15px;
  width: 15px;
  margin: 0 2px;
  background-color: #bbb;
  border-radius: 50%;
  display: inline-block;
  transition: background-color 0.6s ease;
}
.active {
  background-color: #717171;
}
/* Fading animation */
.fade {
  animation-name: fade;
  animation-duration: 1.5s;
}
@keyframes fade {
  from {opacity: .4} 
  to {opacity: 1}
}
/* On smaller screens, decrease text size */
@media only screen and (max-width: 300px) {
  .text {font-size: 11px}
}
</style>
</head>
<body>
<div class="slideshow-container">
<div class="mySlides fade">
  <div class="numbertext">1 / 3</div>
  <img src="https://images.unsplash.com/photo-1516975080664-ed2fc6a32937?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=870&q=80" style="width:100%">
  <div class="text">Style Bar</div>
</div>
<div class="mySlides fade">
  <div class="numbertext">2 / 3</div>
  <img src="https://images.unsplash.com/photo-1562322140-8baeececf3df?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=869&q=80" style="width:100%">
  <div class="text">Style Bar</div>
</div>
<div class="mySlides fade">
  <div class="numbertext">3 / 3</div>
  <img src="https://images.unsplash.com/photo-1595475884562-073c30d45670?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=869&q=80" style="width:100%">
  <div class="text">Style Bar</div>
</div>
</div>
<br>
<div style="text-align:center">
  <span class="dot"></span> 
  <span class="dot"></span> 
  <span class="dot"></span> 
</div>
<script>
let slideIndex = 0;
showSlides();
function showSlides() {
  let i;
  let slides = document.getElementsByClassName("mySlides");
  let dots = document.getElementsByClassName("dot");
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";  
  }
  slideIndex++;
  if (slideIndex > slides.length) {slideIndex = 1}    
  for (i = 0; i < dots.length; i++) {
    dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[slideIndex-1].style.display = "block";  
  dots[slideIndex-1].className += " active";
  setTimeout(showSlides, 2000); // Change image every 2 seconds
}
</script>
</body>
</html> 
    
    
    """
  components.html(slider_images,height=600)
  with st.expander("Haircut & treatment"):
      st.write("""
          The chart above shows some numbers I picked for you.
          I rolled actual dice for these, so they're *guaranteed* to
          be random.
      """)
      st.image("https://cdn.shopify.com/s/files/1/0282/5961/4817/files/SB-3-SHOP-NOW-BUTTONS-hair_600x.jpg?v=1587723007")
  with st.expander("Body Massage & treatment"):
      st.write("""
          The chart above shows some numbers I picked for you.
          I rolled actual dice for these, so they're *guaranteed* to
          be random.
      """)
      st.image("https://cdn.shopify.com/s/files/1/0282/5961/4817/files/SB-3-SHOP-NOW-BUTTONS-styling_600x.jpg?v=1587723035")

  with st.expander("Facial & skin treatment"):
      st.write("""
          The chart above shows some numbers I picked for you.
          I rolled actual dice for these, so they're *guaranteed* to
          be random.
      """)
      st.image("https://cdn.shopify.com/s/files/1/0282/5961/4817/files/SB-3-SHOP-NOW-BUTTONS-tools_600x.jpg?v=1587723060")
  with st.expander("Makeover & Beauty"):
      st.write("""
          The chart above shows some numbers I picked for you.
          I rolled actual dice for these, so they're *guaranteed* to
          be random.
      """)
      st.image("https://cdn.shopify.com/s/files/1/0282/5961/4817/files/SB-3-SHOP-NOW-BUTTONS-tools_600x.jpg?v=1587723060")
      
  # st.markdown("<h1 style='text-align: center; font-family:  cursive, sans-serif; color: rgb(154, 93, 255);'><b>Make An Appointment</b></h1>", unsafe_allow_html=True)
  # #st.text_input("")
  # names = pd.DataFrame({'labels':["GoodWell","HairBotox","Hannon","Joico","Moroccanoil","Mizani"]})
  # nameSelect = st.multiselect(
  #     "Type your category:",
  #     options=list(names['labels']), # convert to list
  #     default=["GoodWell"]
  # )
  # st.date_input("Select the date:")
  # st.button("Click Me!")
  st.markdown("<h1 style='text-align: center; font-family:  cursive, sans-serif; color: rgb(154, 93, 255);'><b>Some of Our Brands</b></h1>", unsafe_allow_html=True)
  col1, col2 , col3 = st.columns(3) 
  col4, col5, col6 = st.columns(3)
  with col1: 
      st.image("https://cdn.shopify.com/s/files/1/0282/5961/4817/files/Redken-Logo-Decal-Sticker__07968.1510914044_150x.jpg?v=1587691832")
      
  with col2: 
      st.image("https://cdn.shopify.com/s/files/1/0282/5961/4817/files/download_150x.png?v=1587691680")
  with col3: 
      st.image("https://cdn.shopify.com/s/files/1/0282/5961/4817/files/cropped-NAKHAIR_logo_2018_Large-002-NEW-2019_150x.jpg?v=1587691786")
  with col4:
      st.image("https://cdn.shopify.com/s/files/1/0282/5961/4817/files/a57ba382dc93747415de4a5b4c41e399_150x.jpg?v=1587691957")
  with col5:
      st.image("https://cdn.shopify.com/s/files/1/0282/5961/4817/files/3b5f640f36e3a233f2611a510d047af8_150x.jpeg?v=1587691995")
  with col6:
      st.image("https://cdn.shopify.com/s/files/1/0282/5961/4817/files/schwarzkopf-professional-logo-vector_150x.png?v=1587692029")
  col1 , col2 = st.columns(2)
  with col1:
      st.video("https://youtu.be/IX6_Uip8eA0")

  with col2:
      st.video("https://youtu.be/c0JzlF0eRJs")


  user_ratings ="""
  <!DOCTYPE html>
  <html>
  <head>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <!-- Font Awesome Icon Library -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
  <style>
  * {
    box-sizing: border-box;
  }

  body {
    font-family: Arial;
    margin: 0 auto; /* Center website */
    max-width: 800px; /* Max width */
    padding: 20px;
  }

  .heading {
    font-size: 25px;
    margin-right: 25px;
  }

  .fa {
    font-size: 25px;
  }

  .checked {
    color: orange;
  }

  /* Three column layout */
  .side {
    float: left;
    width: 15%;
    margin-top:10px;
  }

  .middle {
    margin-top:10px;
    float: left;
    width: 70%;
  }

  /* Place text to the right */
  .right {
    text-align: right;
  }

  /* Clear floats after the columns */
  .row:after {
    content: "";
    display: table;
    clear: both;
  }

  /* The bar container */
  .bar-container {
    width: 100%;
    background-color: #f1f1f1;
    text-align: center;
    color: white;
  }

  /* Individual bars */
  .bar-5 {width: 60%; height: 18px; background-color: #04AA6D;}
  .bar-4 {width: 30%; height: 18px; background-color: #2196F3;}
  .bar-3 {width: 10%; height: 18px; background-color: #00bcd4;}
  .bar-2 {width: 4%; height: 18px; background-color: #ff9800;}
  .bar-1 {width: 15%; height: 18px; background-color: #f44336;}

  /* Responsive layout - make the columns stack on top of each other instead of next to each other */
  @media (max-width: 400px) {
    .side, .middle {
      width: 100%;
    }
    .right {
      display: none;
    }
  }
  </style>
  </head>
  <body>

  <span class="heading">User Rating</span>
  <span class="fa fa-star checked"></span>
  <span class="fa fa-star checked"></span>
  <span class="fa fa-star checked"></span>
  <span class="fa fa-star checked"></span>
  <span class="fa fa-star"></span>
  <p>4.1 average based on 254 reviews.</p>
  <hr style="border:3px solid #f1f1f1">

  <div class="row">
    <div class="side">
      <div>5 star</div>
    </div>
    <div class="middle">
      <div class="bar-container">
        <div class="bar-5"></div>
      </div>
    </div>
    <div class="side right">
      <div>150</div>
    </div>
    <div class="side">
      <div>4 star</div>
    </div>
    <div class="middle">
      <div class="bar-container">
        <div class="bar-4"></div>
      </div>
    </div>
    <div class="side right">
      <div>63</div>
    </div>
    <div class="side">
      <div>3 star</div>
    </div>
    <div class="middle">
      <div class="bar-container">
        <div class="bar-3"></div>
      </div>
    </div>
    <div class="side right">
      <div>15</div>
    </div>
    <div class="side">
      <div>2 star</div>
    </div>
    <div class="middle">
      <div class="bar-container">
        <div class="bar-2"></div>
      </div>
    </div>
    <div class="side right">
      <div>6</div>
    </div>
    <div class="side">
      <div>1 star</div>
    </div>
    <div class="middle">
      <div class="bar-container">
        <div class="bar-1"></div>
      </div>
    </div>
    <div class="side right">
      <div>20</div>
    </div>
  </div>

  </body>
  </html>



  """    
  components.html(user_ratings,height=200)

  st.text_area("Write your Opinion")
  st.button("Submit")

  #st.markdown(about_us,unsafe_allow_html=True)
  with st.form("my_form"):
      st.subheader("Contact US")
      col1, col2 = st.columns(2)
      with col1:
          st.text_input("Your Name")
      with col2:
        st.text_input("Your Email")
      col1 , col2 = st.columns(2)
      with col1:
        st.text_input("Subject")
      with col2:
        st.text_area("Message")

      #slider_val = st.slider("Form slider")
      checkbox_val = st.checkbox("Accept our terms and conditions")

      # Every form must have a submit button.
      submitted = st.form_submit_button("Submit")
