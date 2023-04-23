import streamlit as st
import cohere
import os
import whisper
import streamlit as st
from pydub import AudioSegment


st.set_page_config(
    page_title="Page Title",
    layout="wide",
)

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

st.title("Enter Your Big Idea")
st.info('Enter some more information')
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


                
    




