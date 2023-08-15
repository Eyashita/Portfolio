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
smart_mirror = load_lottiurl("https://lottie.host/d302d28d-2e74-44dc-b2a5-1bc613d091a1/avsPpI9Ktn.json")
girl_waving = load_lottiurl("https://lottie.host/137392ff-4a64-429f-a011-0cc326c5e097/wXPPPXFA0F.json")
image = Image.open("./Images/Smart Mirror.jpg")
me = Image.open('./Images/Eyashita.JPG')
me = ImageOps.exif_transpose(me)

# --- TITLE ---
st.title("My Portfolio :ledger:")
st.markdown('<style> div.block-container{padding-top: 1rem;}</style>', unsafe_allow_html = True)
st.write('---')

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
   st.title("I am Eyashita Singh")
   st.subheader("Undergrad at VIT AP")
   st.write("""
                I'm a dedicated and passionate individual with a robust computer 
            science background and a deep fascination for data analytics. I possess 
            strong programming skills, a knack for problem-solving, and hands-on experience 
            with data analysis tools. My goal is to leverage technology to drive meaningful 
            change and innovation. I excel in teamwork, effective communication, and adapting to 
            fast-paced environments. I'm eager to contribute my skills to your organization, 
            whether it's through software development, data analysis, or driving data-driven decisions.\n 
            Let's connect and embark on an innovative journey together! :sparkles:
                """)
   
  with col2:
   st_lottie(lottie_coder)
 st.write("---")

 with st.expander("See me!"):
    st.write('''
        This is Eyashita Singh!
    ''')
    st.image(me, width=200)

 with st.container():
  col3, col4 = st.columns(2)
  with col3:
   st.subheader("""
            Education :books:
            - VIT
               - Bachelor of Engineering - Computer Science with Data Analytics Specialization
               - CGPA: 8.89 (currently)

            - St. Peter Senior Seconday School, Chandigarh
               - 12th Grade: 92.1%
                
            - The Gurukul, Panchkula
               - 10th: 93.8%
               """
            )
  with col4:
   st.subheader("""
            Experience :computer:
            - Do It Yourself (DIY) Club President, VIT-AP
               - Led a team of 10+ in organizing and executing art events, ensuring successful promotion and seamless coordination. 
               - Partnered with more than 4 clubs and organizations to co-host and manage successful events. 
              
            - Senior Management Business Development, AIESEC 
               - Conducted market research and implemented a sales strategy to increase AIESEC's market reach among 100+ students.
               - Established and cultivated relationships with key stakeholders, fostering collaboration and support for AIESEC's goals.
               - Facilitated in planning and executing AIESEC's annual fundraising event, 'Forge Your Career', which generated a revenue of around 10k+ through the event.
               """)

if selected == 'Projects':
 with st.container():
  st.header("My Projects")
  st.write("##")
  col5, col6 = st.columns(2)
  with col5:
   st.image(image)
  with col6:
   st.subheader("Smart Mirror")
   st.write("""
            - Developed a Smart Mirror using Raspberry Pi and Python, integrating 10+ technologies. 
            - Improved morning routines by providing innovative features and easy access to information. 
            - Enriched the advancement of smart home technology through this project. 
            """)
   st.markdown("[Visit Github Repo](https://github.com/Eyashita)")
 
if selected == 'Contact':
 st.header("Get in touch!")
 st.write("##")
 st.write("##")

 contact_form = """
 <form action="https://formsubmit.co/eyashitasingh10@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value = "false">
     <input type="text" name="name" placeholder = "Your name" required>
     <input type="email" name="email" placeholder = "Your email" required>
     <textarea name = "message" placeholder = "Your message" required></textarea>
     <button type="submit">Submit</button>
 </form>
 """

 left_col, right_col = st.columns((2,1))
 with left_col:
  st.markdown(contact_form, unsafe_allow_html= True)
 with right_col:
  st_lottie("https://lottie.host/fa1b01ce-41e3-405e-a12d-f648c62ddfdf/FN7FtkSRUq.json")

linkedin = "https://www.linkedin.com/in/eyashita-singh/"
git = "https://github.com/Eyashita"
youtube = "https://www.youtube.com/@thesinghsisters813"

Resume = "./Resume.pdf"

with st.sidebar:
   st.sidebar.header("Connect with me on Social Media!")
   st.write("---")
   # LinkedIn
   if st.button("LinkedIn"):
    wb.open_new_tab(linkedin)
   # Github
   if st.button("Github"):
    wb.open_new_tab(git)
   # Gmail
   if st.button("Gmail"):
    st.write("itsofficial.eyashita10@gmail.com")
   # Youtube
   if st.button("Youtube"):
    wb.open_new_tab(youtube)
   # Resume
   if st.download_button(label="Resume", data = open(Resume, 'rb').read(),file_name = "Resume.pdf",mime = "application/pdf"):
      with st.spinner("Loading..."):
       time.sleep(2)
      st.success("Done!")


 






