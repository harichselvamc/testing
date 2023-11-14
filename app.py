import streamlit as st
from src.sound import sound

def main():
    title = "Simple Sound Recorder"
    st.title(title)

    if st.button('Record'):
        with st.spinner("Recording..."):
            sound.record()
        st.success("Recording completed")

    if st.button('Play'):
        try:
            audio_file = open(sound.WAVE_OUTPUT_FILE, 'rb')
            audio_bytes = audio_file.read()
            st.audio(audio_bytes, format='audio/wav')
        except FileNotFoundError:
            st.write("Please record sound first")

if __name__ == '__main__':
    main()
