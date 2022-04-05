
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

# Page Config
st.set_page_config(layout="wide")


hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

#st.set_page_config(page_title="StyleBar", layout="wide")
st.sidebar.image("logo.png", use_column_width=True,width=300)
#st.sidebar.title("Haircut & Treatment")
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
st.markdown("<h1 style='text-align: center; font-family:  cursive, sans-serif; color: rgb(154, 93, 255);'>STYLE BAR</h1>", unsafe_allow_html=True)
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
query = st.text_input("Search Our Products! ")
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

st.markdown("<h1 style='text-align: center; font-family:  cursive, sans-serif; color: rgb(154, 93, 255);'>OUR SERVICES</h1>", unsafe_allow_html=True)
imageCarouselComponent = components.declare_component("image-carousel-component", path="frontend/public")

imageUrls = [
        "https://images.unsplash.com/photo-1562322140-8baeececf3df?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1469&q=80",
        "https://images.unsplash.com/photo-1559599076-9c61d8e1b77c?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=869&q=80",
        "https://images.unsplash.com/photo-1595476108010-b4d1f102b1b1?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=388&q=80",
        "https://images.unsplash.com/photo-1580618672591-eb180b1a973f?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=869&q=80",
        "https://images.unsplash.com/photo-1581404788767-726320400cea?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=869&q=80",
        "https://images.unsplash.com/photo-1580618864180-f6d7d39b8ff6?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=869&q=80",
        "https://images.unsplash.com/photo-1600948836101-f9ffda59d250?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=836&q=80",
        "https://images.unsplash.com/photo-1521590832167-7bcbfaa6381f?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=870&q=80",
        # "https://images.unsplash.com/photo-1513635269975-59663e0ac1ad?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=870&q=80",
        # "https://images.unsplash.com/photo-1595867818082-083862f3d630?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=870&q=80",
        # "https://images.unsplash.com/photo-1622214366189-72b19cc61597?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=687&q=80",
        # "https://images.unsplash.com/photo-1558180077-09f158c76707?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=764&q=80",
        # "https://images.unsplash.com/photo-1520106212299-d99c443e4568?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=687&q=80",
        # "https://images.unsplash.com/photo-1534430480872-3498386e7856?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=870&q=80",
        # "https://images.unsplash.com/photo-1571317084911-8899d61cc464?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=870&q=80",
        # "https://images.unsplash.com/photo-1624704765325-fd4868c9702e?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=764&q=80",
    ]
selectedImageUrl = imageCarouselComponent(imageUrls=imageUrls, height=200)

if selectedImageUrl is not None:
        st.image(selectedImageUrl)

st.snow()

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
     
st.markdown("<h1 style='text-align: center; font-family:  cursive, sans-serif; color: rgb(154, 93, 255);'><b>Make An Appointment</b></h1>", unsafe_allow_html=True)
#st.text_input("")
names = pd.DataFrame({'labels':["GoodWell","HairBotox","Hannon","Joico","Moroccanoil","Mizani"]})
nameSelect = st.multiselect(
     "Type your category:",
     options=list(names['labels']), # convert to list
     default=["GoodWell"]
 )
st.date_input("Select the date:")
st.button("BOOM")
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
    st.video("https://youtu.be/IX6_Uip8eA0")


with st.sidebar:
    selected = option_menu(
        menu_title = "Main Menu",
        options =["Home","Message","Login","Registrations"],
        icons=['house', 'message'],
        menu_icon="cast", default_index=1,
        )

user_ratings ="""
<link href="//maxcdn.bootstrapcdn.com/bootstrap/3.3.0/css/bootstrap.min.css" rel="stylesheet" id="bootstrap-css">
<script src="//maxcdn.bootstrapcdn.com/bootstrap/3.3.0/js/bootstrap.min.js"></script>
<script src="//code.jquery.com/jquery-1.11.1.min.js"></script>
<!------ Include the above in your HEAD tag ---------->

<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
    <meta name="description" content="">
    <meta name="author" content="">
    <link rel="icon" href="favicon.ico">

    <title>Fixed Top Navbar Example for Bootstrap</title>

    <!-- Bootstrap core CSS -->
    <link href="css/bootstrap.min.css" rel="stylesheet">

    <!-- IE10 viewport hack for Surface/desktop Windows 8 bug -->
    <link href="css/ie10-viewport-bug-workaround.css" rel="stylesheet">

    <!-- Custom styles for this template -->
    <link href="css/navbar-fixed-top.css" rel="stylesheet">

    <!-- Just for debugging purposes. Don't actually copy these 2 lines! -->
    <!--[if lt IE 9]><script src="assets/js/ie8-responsive-file-warning.js"></script><![endif]-->
    <script src="js/ie-emulation-modes-warning.js"></script>

    <!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
    <!--[if lt IE 9]>
      <script src="https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"></script>
      <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
    <![endif]-->
  </head>

  <body>

    <!-- Fixed navbar -->
    <nav class="navbar navbar-default navbar-fixed-top">
      <div class="container">
        <div class="navbar-header">
          <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="false" aria-controls="navbar">
            <span class="sr-only">Toggle navigation</span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
          <a class="navbar-brand" href="#">Demo</a>
        </div>
        <div id="navbar" class="navbar-collapse collapse">
          <ul class="nav navbar-nav navbar-right">
            <li><a href="../navbar/">Default</a></li>
          </ul>
        </div><!--/.nav-collapse -->
      </div>
    </nav>

    <div class="container">
    			
		<div class="row">
			<div class="col-sm-3">
				<div class="rating-block">
					<h4>Average user rating</h4>
					<h2 class="bold padding-bottom-7">4.3 <small>/ 5</small></h2>
					<button type="button" class="btn btn-warning btn-sm" aria-label="Left Align">
					  <span class="glyphicon glyphicon-star" aria-hidden="true"></span>
					</button>
					<button type="button" class="btn btn-warning btn-sm" aria-label="Left Align">
					  <span class="glyphicon glyphicon-star" aria-hidden="true"></span>
					</button>
					<button type="button" class="btn btn-warning btn-sm" aria-label="Left Align">
					  <span class="glyphicon glyphicon-star" aria-hidden="true"></span>
					</button>
					<button type="button" class="btn btn-default btn-grey btn-sm" aria-label="Left Align">
					  <span class="glyphicon glyphicon-star" aria-hidden="true"></span>
					</button>
					<button type="button" class="btn btn-default btn-grey btn-sm" aria-label="Left Align">
					  <span class="glyphicon glyphicon-star" aria-hidden="true"></span>
					</button>
				</div>
			</div>
			<div class="col-sm-3">
				<h4>Rating breakdown</h4>
				<div class="pull-left">
					<div class="pull-left" style="width:35px; line-height:1;">
						<div style="height:9px; margin:5px 0;">5 <span class="glyphicon glyphicon-star"></span></div>
					</div>
					<div class="pull-left" style="width:180px;">
						<div class="progress" style="height:9px; margin:8px 0;">
						  <div class="progress-bar progress-bar-success" role="progressbar" aria-valuenow="5" aria-valuemin="0" aria-valuemax="5" style="width: 1000%">
							<span class="sr-only">80% Complete (danger)</span>
						  </div>
						</div>
					</div>
					<div class="pull-right" style="margin-left:10px;">1</div>
				</div>
				<div class="pull-left">
					<div class="pull-left" style="width:35px; line-height:1;">
						<div style="height:9px; margin:5px 0;">4 <span class="glyphicon glyphicon-star"></span></div>
					</div>
					<div class="pull-left" style="width:180px;">
						<div class="progress" style="height:9px; margin:8px 0;">
						  <div class="progress-bar progress-bar-primary" role="progressbar" aria-valuenow="4" aria-valuemin="0" aria-valuemax="5" style="width: 80%">
							<span class="sr-only">80% Complete (danger)</span>
						  </div>
						</div>
					</div>
					<div class="pull-right" style="margin-left:10px;">1</div>
				</div>
				<div class="pull-left">
					<div class="pull-left" style="width:35px; line-height:1;">
						<div style="height:9px; margin:5px 0;">3 <span class="glyphicon glyphicon-star"></span></div>
					</div>
					<div class="pull-left" style="width:180px;">
						<div class="progress" style="height:9px; margin:8px 0;">
						  <div class="progress-bar progress-bar-info" role="progressbar" aria-valuenow="3" aria-valuemin="0" aria-valuemax="5" style="width: 60%">
							<span class="sr-only">80% Complete (danger)</span>
						  </div>
						</div>
					</div>
					<div class="pull-right" style="margin-left:10px;">0</div>
				</div>
				<div class="pull-left">
					<div class="pull-left" style="width:35px; line-height:1;">
						<div style="height:9px; margin:5px 0;">2 <span class="glyphicon glyphicon-star"></span></div>
					</div>
					<div class="pull-left" style="width:180px;">
						<div class="progress" style="height:9px; margin:8px 0;">
						  <div class="progress-bar progress-bar-warning" role="progressbar" aria-valuenow="2" aria-valuemin="0" aria-valuemax="5" style="width: 40%">
							<span class="sr-only">80% Complete (danger)</span>
						  </div>
						</div>
					</div>
					<div class="pull-right" style="margin-left:10px;">0</div>
				</div>
				<div class="pull-left">
					<div class="pull-left" style="width:35px; line-height:1;">
						<div style="height:9px; margin:5px 0;">1 <span class="glyphicon glyphicon-star"></span></div>
					</div>
					<div class="pull-left" style="width:180px;">
						<div class="progress" style="height:9px; margin:8px 0;">
						  <div class="progress-bar progress-bar-danger" role="progressbar" aria-valuenow="1" aria-valuemin="0" aria-valuemax="5" style="width: 20%">
							<span class="sr-only">80% Complete (danger)</span>
						  </div>
						</div>
					</div>
					<div class="pull-right" style="margin-left:10px;">0</div>
				</div>
			</div>			
		</div>			
		
		<div class="row">
			<div class="col-sm-7">
				<hr/>
				<div class="review-block">
					<div class="row">
						<div class="col-sm-3">
							<img src="http://dummyimage.com/60x60/666/ffffff&text=No+Image" class="img-rounded">
							<div class="review-block-name"><a href="#">nktailor</a></div>
							<div class="review-block-date">January 29, 2016<br/>1 day ago</div>
						</div>
						<div class="col-sm-9">
							<div class="review-block-rate">
								<button type="button" class="btn btn-warning btn-xs" aria-label="Left Align">
								  <span class="glyphicon glyphicon-star" aria-hidden="true"></span>
								</button>
								<button type="button" class="btn btn-warning btn-xs" aria-label="Left Align">
								  <span class="glyphicon glyphicon-star" aria-hidden="true"></span>
								</button>
								<button type="button" class="btn btn-warning btn-xs" aria-label="Left Align">
								  <span class="glyphicon glyphicon-star" aria-hidden="true"></span>
								</button>
								<button type="button" class="btn btn-default btn-grey btn-xs" aria-label="Left Align">
								  <span class="glyphicon glyphicon-star" aria-hidden="true"></span>
								</button>
								<button type="button" class="btn btn-default btn-grey btn-xs" aria-label="Left Align">
								  <span class="glyphicon glyphicon-star" aria-hidden="true"></span>
								</button>
							</div>
							<div class="review-block-title">this was nice in buy</div>
							<div class="review-block-description">this was nice in buy. this was nice in buy. this was nice in buy. this was nice in buy this was nice in buy this was nice in buy this was nice in buy this was nice in buy</div>
						</div>
					</div>
					<hr/>
					<div class="row">
						<div class="col-sm-3">
							<img src="http://dummyimage.com/60x60/666/ffffff&text=No+Image" class="img-rounded">
							<div class="review-block-name"><a href="#">nktailor</a></div>
							<div class="review-block-date">January 29, 2016<br/>1 day ago</div>
						</div>
						<div class="col-sm-9">
							<div class="review-block-rate">
								<button type="button" class="btn btn-warning btn-xs" aria-label="Left Align">
								  <span class="glyphicon glyphicon-star" aria-hidden="true"></span>
								</button>
								<button type="button" class="btn btn-warning btn-xs" aria-label="Left Align">
								  <span class="glyphicon glyphicon-star" aria-hidden="true"></span>
								</button>
								<button type="button" class="btn btn-warning btn-xs" aria-label="Left Align">
								  <span class="glyphicon glyphicon-star" aria-hidden="true"></span>
								</button>
								<button type="button" class="btn btn-default btn-grey btn-xs" aria-label="Left Align">
								  <span class="glyphicon glyphicon-star" aria-hidden="true"></span>
								</button>
								<button type="button" class="btn btn-default btn-grey btn-xs" aria-label="Left Align">
								  <span class="glyphicon glyphicon-star" aria-hidden="true"></span>
								</button>
							</div>
							<div class="review-block-title">this was nice in buy</div>
							<div class="review-block-description">this was nice in buy. this was nice in buy. this was nice in buy. this was nice in buy this was nice in buy this was nice in buy this was nice in buy this was nice in buy</div>
						</div>
					</div>
					<hr/>
					<div class="row">
						<div class="col-sm-3">
							<img src="http://dummyimage.com/60x60/666/ffffff&text=No+Image" class="img-rounded">
							<div class="review-block-name"><a href="#">nktailor</a></div>
							<div class="review-block-date">January 29, 2016<br/>1 day ago</div>
						</div>
						<div class="col-sm-9">
							<div class="review-block-rate">
								<button type="button" class="btn btn-warning btn-xs" aria-label="Left Align">
								  <span class="glyphicon glyphicon-star" aria-hidden="true"></span>
								</button>
								<button type="button" class="btn btn-warning btn-xs" aria-label="Left Align">
								  <span class="glyphicon glyphicon-star" aria-hidden="true"></span>
								</button>
								<button type="button" class="btn btn-warning btn-xs" aria-label="Left Align">
								  <span class="glyphicon glyphicon-star" aria-hidden="true"></span>
								</button>
								<button type="button" class="btn btn-default btn-grey btn-xs" aria-label="Left Align">
								  <span class="glyphicon glyphicon-star" aria-hidden="true"></span>
								</button>
								<button type="button" class="btn btn-default btn-grey btn-xs" aria-label="Left Align">
								  <span class="glyphicon glyphicon-star" aria-hidden="true"></span>
								</button>
							</div>
							<div class="review-block-title">this was nice in buy</div>
							<div class="review-block-description">this was nice in buy. this was nice in buy. this was nice in buy. this was nice in buy this was nice in buy this was nice in buy this was nice in buy this was nice in buy</div>
						</div>
					</div>
				</div>
			</div>
		</div>
		
    </div> <!-- /container -->


    <!-- Bootstrap core JavaScript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>
    <script>window.jQuery || document.write('<script src="assets/js/vendor/jquery.min.js"><\/script>')</script>
    <script src="js/bootstrap.min.js"></script>
    <!-- IE10 viewport hack for Surface/desktop Windows 8 bug -->
    <script src="js/ie10-viewport-bug-workaround.js"></script>
  </body>
</html>



"""    
components.html(user_ratings,height=600)