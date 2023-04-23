import os
import numpy as np
from io import BytesIO
import streamlit.components.v1 as components
import requests
import streamlit as st
from PIL import Image
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu
from audio_recorder_streamlit import audio_recorder
from st_custom_components import st_audiorec
import cohere
import os
import whisper
from pydub import AudioSegment




st.set_page_config(page_title='_______', page_icon= ":speaker_high_volume:", layout="wide")
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Use Local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("/Users/sophialiang/Desktop/backup/style/style.css")

# load assets
record_animation_url = "https://assets3.lottiefiles.com/packages/lf20_yghxkfhn.json"
lottie_coding = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_PmGV4skHBv.json")



img_speechToText = Image.open("/Users/sophialiang/Desktop/backup/speechToText.png")
img_textToSummary = Image.open("/Users/sophialiang/Desktop/backup/textToSummary.png")
img_summaryToQuestions = Image.open("/Users/sophialiang/Desktop/backup/summaryToQuestions.png")
img_lahacksduck = Image.open("/Users/sophialiang/Desktop/backup/lahacksduck.png")

#st.markdown("![Alt Text](https://media.giphy.com/media/vFKqnCdLPNOKc/giphy.gif)")
#st.markdown(" ![Alt Text](https://media.giphy.com/media/hC2mA1FWFs2OowO60p/giphy.gif) <h3 style='text-align: center; color: #A3866A;'>Hello World! This is Duck.It.We.Ball</h3>  ![Alt Text](https://media.giphy.com/media/hC2mA1FWFs2OowO60p/giphy.gif)", unsafe_allow_html=True)
#st.markdown("![Alt Text](https://media.giphy.com/media/vFKqnCdLPNOKc/giphy.gif)")
st.markdown(
    """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Nanum+Pen+Script&display=swap');
        h1 {
            font-family: 'Nanum Pen Script', cursive;
            text-align: center;
            color: #A3866A;
            margin: 0px;
            font-size: 50px;
            font-weight: bold;
        }
    </style>

    <div style='display: flex; justify-content: center; align-items: center; margin-top: -75px;'>
        <img src='https://media.giphy.com/media/hC2mA1FWFs2OowO60p/giphy.gif' style='padding: 0px 10px; height: 130px; width: 180px;' />
        <h1>Hello World! This is Duck.It.We.Ball</h1>
        <img src='https://media.giphy.com/media/hC2mA1FWFs2OowO60p/giphy.gif' style='padding: 0px 10px; height: 130px; width: 180px;' />
    </div>
    """,
    unsafe_allow_html=True
)



# 1. as sidebar menu
selected = option_menu(
    menu_title = None,
    options= ["Home","Demo", "Record","Contact",],
    icons= ["house", "camera-reels", "record-circle", "envelope" ],
    menu_icon = "cast",
    default_index = 0,
    orientation = "horizontal",
    styles={
            "container": {"padding": "0!important", "background-color": "#DFD7C8"},
            "icon": {"color": "#402909", "font-size": "25px"}, 
            "nav-link": {"font-size": "25px", "text-align": "left", "margin":"0px", "--hover-color": "#A68D7E"},
            "nav-link-selected": {"background-color": "#CCAD9B"},
        }
)
if selected == "Home":
    #st.title(f"You have selected{selected}")
    with st.container():
    
    #st.subheader(" Hello World! This is textToSpeechsilly")
    #st.title(" Hello World! This is textToSpeechsilly")
    #st.markdown("<h1 style='text-align: center; color: #A3866A;'>Hello World! This is textToSpeechsilly</h1>", unsafe_allow_html=True)
        st_lottie(lottie_coding, height = 400, key = "coding")
    #st.image(logo, caption ="Mascot")
    # what we do
    
    with st.container():
        st.write("---")
        left_column, right_column = st.columns(2)
        #with left_column:
        #st.markdown("<h1 style='text-align: center; color: #A3866A;'>What We Do!</h1>", unsafe_allow_html=True)
        #st.write("#")
        image_column, text_column = st.columns((1,2))
        with image_column:
            #insert image
            st.image(img_lahacksduck)
            st.markdown("<p style='text-align: center; color: #CCAD9B;'>pc: LAHacks", unsafe_allow_html=True)
            with text_column:
                st.markdown("<h1 style='text-align: center; color: #A3866A;'>What We Do!</h1>", unsafe_allow_html=True)
                st.markdown("<h5 style='text-align: center; color: #000000;'>Introducing a revolutionary web-based platform that uses cutting-edge speech recognition technology to automatically transcribe audio files into detailed notes. Our interactive speech-to-text website is designed to revolutionize the way we learn, by enabling students and professionals alike to convert lengthy lectures and meetings into concise and organized notes,  in just a matter of minutes with the help of Cohere AI, which is an NLP platform that provides tools for speech-to-text, summarization, and question generation.", unsafe_allow_html=True)
                st.markdown("<h5 style='text-align: center; color: #000000;'> With our platform, you can easily upload any audio file format, such as mp3, and watch as our AI-powered speech recognition engine transcribes every word into clear and accurate text. Our platform is perfect for anyone who wants to improve their learning or productivity, by converting audio files into more efficient notes. It's especially useful for students who need to review lectures, professionals who attend meetings and conferences, and anyone who wants to improve their note-taking skills. Our interactive speech-to-text website is designed to be user-friendly and accessible to everyone, whether you're a tech-savvy individual or not. ", unsafe_allow_html=True)
                st.markdown("<h5 style='text-align: center; color: #000000;'>If you're looking to advance your learning, improve your productivity, or simply make your life easier, our interactive speech-to-text website is the perfect solution. Try it out today and start converting your audio files into more efficient notes, in just a few clicks.", unsafe_allow_html=True)
    with st.container():
        st.write("---")
        st.markdown("<h1 style='text-align: center; color: #A3866A ;'>Duck.It.We.Ball", unsafe_allow_html=True)
        st.write('##')
        image_column, text_column = st.columns((1,2))
        with image_column:
            #insert image
            st.image(img_speechToText)
            with text_column:
                st.markdown("<h2 style='text-align: center; color: #CCAD9B; font-family: Georgia;'> (1) Speech To Text </h2>", unsafe_allow_html=True)
                st.markdown("<p style='text-align: center; color: #000000;'>Are you tired of missing important details during meetings, interviews or lectures? Do you struggle to keep up with fast speakers or accents that are difficult to understand?Transcribing your audio files can be the solution to all these problems. By turning your audio recordings into written transcripts, you'll have a searchable, editable, and easily shareable document that captures every word spoken. Not only will this save you time, but it will also improve accuracy, eliminate misunderstandings, and allow you to revisit key points with ease. So why not convert your audio file into transcribed writing today and experience the benefits for yourself?", unsafe_allow_html=True)

    with st.container():
        image_column, text_column = st.columns((1,2))
        with image_column:
            #insert image
            st.image(img_textToSummary)
            with text_column:
                st.markdown("<h2 style='text-align: center; color: #CCAD9B;font-family: Georgia;'>(2) Text to Summarization", unsafe_allow_html=True)
                st.markdown("<p style='text-align: center; color: #000000;'>Do you have a lot of audio recordings that need to be transcribed but don't have the time or resources to go through every single word? Look no further, because we offer a service that not only transcribes your audio files but also summarizes the most important points. With our transcription and summarization service, you'll get a concise and comprehensive summary of your audio recording, making it easier for you to extract key information and insights. Whether it's for a business meeting, research interview, or educational lecture, our service will help you save time and enhance your productivity. So why settle for just a transcription when you can get a complete summary of your audio recordings? Try our service today and experience the benefits for yourself!", unsafe_allow_html=True)
    with st.container():
        image_column, text_column = st.columns((1,2))
        with image_column:
            #insert image
            st.image(img_summaryToQuestions)
            with text_column:
                st.markdown("<h2 style='text-align: center; color: #CCAD9B;font-family: Georgia;'>(3) Summarization To Questions", unsafe_allow_html=True)
                st.markdown("<p style='text-align: center; color: #000000;'>Are you struggling to retain important information from your lectures, meetings, or interviews? Are you tired of taking notes and still missing key points? Our transcription and question creation service is here to help. We don't just transcribe your audio recordings and summarize them, we also create questions based on the content to help you retain and reinforce the information you need. Our service provides a comprehensive study guide that you can use to enhance your learning and prepare for exams, presentations, or important conversations. With our service, you'll have the convenience of having all the important information in one place and the added benefit of having practice questions to help you remember it all. Don't settle for just a transcription or summary, try our service today and take your learning to the next level!", unsafe_allow_html=True)

if selected == "Demo":

    @st.cache_data
    def wav_to_mp3(f, result):
        AudioSegment.from_wav(f.name).export(result, format="mp3")
        return result

    @st.cache_data
    def whisper_model(f, size):
        model = whisper.load_model(size)
        result = model.transcribe(f)
        return result["text"] 
        

    @st.cache_data
    def export_result(content, file):
        with open(file, "w") as f:
            f.write(content)

    @st.cache_data
    def summarize(input_user, summary_type) -> str:
        if input_user is not None:
            if summary_type == "Bullet":
                response = co.summarize(
                    text=input_user,
                    length="long",
                    format="bullets",
                    model="summarize-xlarge",
                    extractiveness="low",
                    temperature=0.3,

                )

            elif summary_type == "Paragraph":
                response = co.summarize(
                    text=input_user,
                    length="long",
                    format="paragraph",
                    model="summarize-xlarge",
                    extractiveness="low",
                    temperature=0.3,
                )

            st.session_state['output'] = response.summary
            st.write(response.summary)

    @st.cache_data
    def generate_questions(summary, creativity, num_questions):
        prompt = f'Create {num_questions} comprehensive questions about this summary: {summary}'
        # prompt = f'Give me a set of questions about this summary: {summary}'
        response = co.generate(
        model='command-xlarge-nightly',
        prompt=prompt,
        max_tokens=300,
        temperature=creativity,
        k=0,
        stop_sequences=[],
        return_likelihoods='NONE')

        st.session_state['output'] = response.generations[0].text
        st.write(st.session_state.output)

    @st.cache_data
    def analysis(input_user, summary_type, creativity, num_questions):
        summarize(input_user, summary_type)
        generate_questions(input_user, creativity, num_questions)

    @st.cache_data
    def download_test(output_audio_file):
        transcript = whisper_model(str(os.path.abspath(output_audio_file)), whisper_model_type.lower())
        output_txt_file = str(output_audio_file.split('.')[0]+".txt")
        export_result(transcript, output_txt_file)
        output_file = open(output_txt_file,"r")
        output_file_data = output_file.read()


        return output_file_data, output_txt_file

    st.title("Unlock your learning potential with our summarization and question generation tool!")
    st.markdown("<h7 style='text-align: center; color: black; font-family: Georgia;'>Do you find it exhausting to attend lengthy lectures or meetings and find it challenging to retain all the information being presented, which may cause constraints on your active learning process? Our new tool can help! Simply upload a recorded file of the meeting or lecture and in as little as 10 seconds, we'll generate both a summarization and questions based on the text. This will make it easier for you to understand and review the important points discussed. Give it a try and see how it can improve your learning experience!</h7>", unsafe_allow_html=True)
    #st.info("Do you find it exhausting to attend lengthy lectures or meetings and find it challenging to retain all the information being presented, which may cause constraints on your active learning process? Our new tool can help! Simply upload a recorded file of the meeting or lecture and in as little as 10 seconds, we'll generate both a summarization and questions based on the text. This will make it easier for you to understand and review the important points discussed. Give it a try and see how it can improve your learning experience!")
    user_file = st.file_uploader("Upload audio file", type="wav")
    co = cohere.Client('xlCIpQOgoOClGDvT8Z2M7obCCYOPfTdvzyFPkD1I')

    if 'output' not in st.session_state:
        st.session_state['output'] = 'Output:'

    if user_file is not None:
        cond_rep = user_file.read()
        with open(user_file.name, "wb") as f:
            f.write((user_file).getbuffer())
        with st.spinner(f"Processing Audio"):
            output_audio_file = user_file.name.split('.')[0] + '.mp3'
            output_audio_file = wav_to_mp3(user_file, output_audio_file)
            audio_file = open(output_audio_file, 'rb')
            cond_rep = audio_file.read()
        print("Opening ",audio_file)
        section1, section2 = st.columns(2)
        with section1:
            st.markdown("Play Recording")
            st.audio(cond_rep)
        with section2:
            value = st.slider("Model Capacity & Power", value = None, key = "value", min_value=1, max_value=100)
            
            if value is not None:
                if value <= 20 and value >= 1:
                    whisper_model_type = "Tiny"
                elif value <= 40 and value > 20:
                    whisper_model_type = "Base"
                elif value <= 60 and value > 40:
                    whisper_model_type = "Small"
                elif value <= 80 and value > 60:
                    whisper_model_type = "Medium"
                elif value <= 100 and value > 80:
                    whisper_model_type = "Large"

            transcript = whisper_model(str(os.path.abspath(output_audio_file)), whisper_model_type.lower())


        form = st.form(key="user_settings")
        col1, col2, col3 = st.columns(3)
        with form:
            with col1:
                num_questions_input = st.slider("Number of Questions", value = 7.0, key = "num_questions_input", min_value=5.0, max_value=15.0)
            with col2:
                creativity_input = st.slider("Creativity", value = 2.0, key = "creativity_input", min_value = 0.0, max_value=5.0)
            with col3:
                summary_type = st.radio("Choose Summary Format Type", ("Bullet","Paragraph"))
            
        if st.button("Generate Results"):
            with st.spinner(f"Building Transcript"):
                with st.spinner(f"Applying A.I."):
                    analysis(transcript, summary_type, creativity_input, num_questions_input)

        if st.download_button(label="Download Transcript",
                                data=download_test(output_audio_file)[0],
                                file_name=download_test(output_audio_file)[1],
                                mime='text/plain'):
            st.success('Success!')

if selected == "Record":
    st.markdown("<h1 style='text-align: center; color: #CCAD9B;'>Our Personal Audio Converter</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #000000;'>Introducing our revolutionary audio converter that makes it easier for you to use our web-based platform, which utilizes cutting-edge speech recognition technology powered by Cohere AI. Our audio converter allows you to quickly and easily convert any audio file format, such as mp3, to a format that can be processed by our platform. With the help of our audio converter, you can now seamlessly upload your audio files and watch as our AI-powered speech recognition engine transcribes every word into clear and accurate text. Say goodbye to the hassle of manually converting your audio files, and experience the convenience of our audio converter today!</p>", unsafe_allow_html=True)
    st.write("")
    st.write("")
    st.write("")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.write("")
    with col2:
        wav_audio_data = st_audiorec()
    with col3:
        st.write("")


if selected == "Contact":
    with st.container():
        st.write("---")
        st.markdown("<h1 style='text-align: center; color: #A3866A ;'>Any Questions? Get In Touch With Us!", unsafe_allow_html=True)

        st.write("##")
  
        # Documentation
        contact_form = """ 
        <form action="https://formsubmit.co/sopeah04@gmail.com" method="POST">
            <input type="hidden" name ="_captcha" value="false">
            <input type="text" name="name" placeholder= "Your name" required>
            <input type="email" name="email" placeholder= "Your email"required>
            <textarea name="message" placeholder= "Your message here" required></textarea>
            <button type="submit">Send</button>
        </form>
        """
        st.markdown(f'<div align="center">{contact_form}</div>', unsafe_allow_html=True)