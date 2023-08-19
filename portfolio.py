import streamlit as st
from streamlit_option_menu import option_menu
import requests
from streamlit_lottie import st_lottie
from PIL import Image, ImageOps
import webbrowser as wb
import time

st.set_page_config(page_title="Portfolio", page_icon = ":ledger:", layout = "wide")

def load_lottiurl(url):
 r = requests.get(url)
 if r.status_code != 200:
  return None
 return r.json()

def local_css(file_name):
 with open(file_name) as f:
  st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
local_css("./Style/style.css")

lottie_coder = load_lottiurl("https://lottie.host/a9cd8673-69f7-4dba-bac3-2027423521fb/5gAswbWwF4.json")
image = Image.open("./Images/Smart Mirror.jpg")
me = ImageOps.exif_transpose(Image.open('./Images/Eyashita4.png'))
me = ImageOps.exif_transpose(me)
sKart = Image.open("./Images/Shpping1.jpg")
sKart = ImageOps.exif_transpose(sKart)
dashboard = Image.open("./Images/Smart House.jpg")
dashboard = ImageOps.exif_transpose(dashboard)
linkedin = ImageOps.exif_transpose(Image.open("./Images/linkedin_icon.png"))

linkedin = "https://www.linkedin.com/in/eyashita-singh"
git = "https://github.com/Eyashita"
youtube = "https://www.youtube.com/@thesinghsisters813"

Resume = "./Resume.pdf"

# --- TITLE ---
# st.title("My Portfolio :ledger:")
st.markdown('''
            <style> 
            div.block-container
            {
               padding-top: 1rem;
            }
           </style>'''
            , unsafe_allow_html = True)

with st.container():
 selected = option_menu(
    menu_title = None,
    options = ['About', 'Projects', 'Contact'],
    icons = ['person', 'code-slash', 'chat-left-text-fill'],
    orientation = 'horizontal'
    )
 
if selected == 'About':
 with st.container():
  col1, col2 = st.columns(2)
  with col1:
   st.markdown('''
               <div>
                  <h1 style="font-size:60px; text-align:center; padding-top: 3rem">Hi!&#128075;<br> I am Eyashita Singh </h1>
               </div>
               ''', unsafe_allow_html=True)
   st.markdown('<h2 style="text-align: center;">Undergrad at VIT AP</h2>', unsafe_allow_html=True)
   st_lottie(lottie_coder)

  with col2:
   st.write("##")
   st.write("##")
   st.image(me)
 st.write("---")

 with st.container():
   col1, col2 = st.columns([0.4, 0.6])
   with col1:
        st_lottie('https://lottie.host/f6e2bf10-592d-4aa5-b5bc-7d657d142a93/EpNeciup3K.json', width= 400)
   with col2:
     st.markdown("""
    <div style="text-align: center; padding-top: 5rem"> <p style="font-size:120%;">
        I'm a <b>DEDICATE</b> and <b>PASSIONATE</b> individual with a robust computer 
        science &#x1F4BB; background and a deep fascination for data analytics. I possess 
        strong programming skills, a knack for problem-solving, and hands-on experience 
        with data analysis tools &#x1F6E0; . My goal is to leverage technology to drive meaningful 
        change and innovation. I excel in teamwork &#x1F91D;, effective communication, and adapting to 
        fast-paced environments. I'm eager to contribute my skills to your organization, 
        whether it's through software development, data analysis, or driving data-driven decisions.
        <br><br>Let's connect and embark on an innovative journey together!&#x2728;</p>
    </div>
    """, unsafe_allow_html=True)
     

   st.markdown('''<h4> <i>Download my Resume here:</i></h4>''', unsafe_allow_html=True)
   if st.download_button(label="Resume", data = open(Resume, 'rb').read(),file_name = "Resume.pdf",mime = "application/pdf"):
      with st.spinner("Loading..."):
         time.sleep(2)
      st.success("Done!")




if selected == 'Projects':
 with st.container():
  col1, col2 = st.columns([0.3, 0.7 ])
  with col1:
   st.markdown("<h2 style='text-align: left ; font-size: 60px; padding-top:70px'>My Projects</h2>", unsafe_allow_html=True)
   with col2:
    st.image("https://media.giphy.com/media/5ndklThG9vUUdTmgMn/giphy.gif", width = 150)
  st.write("---")

  col5, col6 = st.columns([0.3, 0.7])
  with col5:
   st.image(dashboard, width = 300)
  with col6:
   st.subheader("	:arrow_right: IOT enabled Dynamic Dashboard for HouseHold Systems")
   st.write("""
               - Created a framework to analyze real-time data from IoT sensors in smart homes.
               - Gathered real-time data from diverse IoT sensors.
               -  Managed MongoDB cloud database for data integrity.
               -  Developed an interactive dashboard using Streamlit for data analysis and visualization.
               - Dashboard provided insights into occupancy, energy usage, and environment. Informed decision-making for efficiency optimization and contributed to the advancement of IoT-enabled smart homes.
            """)
   
  col7, col8 = st.columns([0.3, 0.7])
  with col7:
   st.image(dashboard, width = 300)
  with col8:
   st.subheader("	:arrow_right: Visage: Facial Recognition System for Attendance")
   st.write("""
            - Developed a Smart Mirror using Raspberry Pi and Python, integrating 10+ technologies. 
            - Improved morning routines by providing innovative features and easy access to information. 
            - Enriched the advancement of smart home technology through this project. 
            """)

  col1, col2 = st.columns([0.3, 0.7])
  with col1:
   image = ImageOps.exif_transpose(image)
   st.image(image, width= 300)
   
  with col2:
   st.subheader("	:arrow_right: Smart Mirror")
   st.write("""
            - Developed a Smart Mirror using Raspberry Pi and Python, integrating 10+ technologies. 
            - Improved morning routines by providing innovative features and easy access to information. 
            - Enriched the advancement of smart home technology through this project. 
            """)
   
  col3, col4 = st.columns([0.3, 0.7])
  with col3:
   st.image(sKart, width = 300)
  with col4:
   st.subheader("	:arrow_right: IOT enabled Smart ShoppingKart")
   st.write("""
            - Developed a Smart Mirror using Raspberry Pi and Python, integrating 10+ technologies. 
            - Improved morning routines by providing innovative features and easy access to information. 
            - Enriched the advancement of smart home technology through this project. 
            """)
 
if selected == 'Contact':
 st.markdown("<h2 style='text-align:center;'>Get in Touch!</h2>", unsafe_allow_html=True)
 st.write("---")
 st.write("##")

 contact_form = """
<form style="text-align: center;" action="https://formsubmit.co/itsofficial.eyashita10@gmail.com" method="POST">
    <input type="hidden" name="_captcha" value="false">
    <input type="text" name="name" placeholder="Your name" style="width: 100%; padding: 10px; margin-bottom: 10px;" required>
    <input type="email" name="email" placeholder="Your email" style="width: 100%; padding: 10px; margin-bottom: 10px;" required>
    <textarea name="message" placeholder="Your message" style="width: 100%; height: 150px; padding: 10px;" required></textarea>
    <br><button type="submit">Submit</button></br>
</form>



 """

 left_col, right_col = st.columns([0.6, 0.4])
 with left_col:
  st.markdown(contact_form, unsafe_allow_html= True)
 with right_col:
  st_lottie("https://lottie.host/825b4e78-a035-4d52-9fcb-4b34a214b80d/428IZ45rIj.json")


# # --- Sidebar ---
# with st.sidebar:
#    # st.sidebar.title("Connect with me on Social Media!")
#    st.markdown("<h1 style='margin-top: 0;padding-top: 0;'>Connect with me on Social Media!</h1>", unsafe_allow_html=True)
#    st.write("---")


#    col1, col2 = st.columns(2)
   
#    with col1:
#       # LinkedIn
#       # Define the hyperlink text and URL
#       button_text = "LinkedIn1"
#       button_url = "https://www.linkedin.com/in/eyashita-singh"

#    # Create a button that opens the link in a new tab
#       if st.button(button_text):
#          st.markdown(f'<script>window.open("{button_url}", "_blank");</script>', unsafe_allow_html=True)
      
#       if st.button("LinkedIn"):
#        wb.open_new_tab(linkedin)
#       # Github
#       if st.button("Github"):
#          wb.open_new_tab(git)
#       # Gmail
#       if st.button("Gmail"):
#          st.write("itsofficial.eyashita10@gmail.com")
#       # Youtube
#       if st.button("Youtube"):
#          wb.open_new_tab(youtube)
#       # Resume
#       if st.download_button(label="Resume", data = open(Resume, 'rb').read(),file_name = "Resume.pdf",mime = "application/pdf"):
#          with st.spinner("Loading..."):
#             time.sleep(2)
#          st.success("Done!")
#    with col2:
#      st.image("https://media.giphy.com/media/htvPpsP0fEFhTv7HHT/giphy.gif", width = 100)


 






