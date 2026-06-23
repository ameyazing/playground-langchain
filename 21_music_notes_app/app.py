import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel, Field
#from dotenv import load_dotenv
import pandas as pd

#load_dotenv()
st.title("Music notes app")
st.markdown(" ##### by Rio")
api_key = st.text_input("Pls enter you API key" , type = "password")
song_name = st.text_input("Type your message here:")

#chat_model = ChatGoogleGenerativeAI(model="gemini-3.1-flash-lite", google_api_key=api_key)

class MusicNotes(BaseModel):
    sr_no: list[int] = Field(description="Serial number starting from 1")
    lyric: list[str] = Field(description="Lyrics for that particular line of the song. Put (Blank) if that particular music line does not have any lyrics e.g. interlude in the song")
    chord: list[str] = Field(description="Chord for that particular line of the song. Put (Blank) if that particular music line does not have any chord. There can be multiple chords per line")
    notes: list[str] = Field(description="Notes for that particular line of the song. The notes must also have spaces in between them to indicate the interval between note. Put + or - sign if the notes are jumping an octave up or down respectively Put (Blank) if that particular music line does not have any notes e.g. if that line only has a chord to play but no notes. If there are copyright issues you may give the notes in a different scale, but adjust the chords accordingly.")

#structured_model = chat_model.with_structured_output(MusicNotes)

prompt_template = PromptTemplate(
    template = "Provide piano notes for the song {song_name}. Provide the notes in A B C format (you can also use sharps of flats) for the full song, along with the chords. Use existing information on the net such as sheeet music, videos, etc,. The output needs to be displayed in tabular format with 4 columns: Sr. No, Lyrics, Chord, Notes. Each row of the table will correspond to a line of the song. If there are copyright issues you may give the notes in a different scale, but adjust the chords accordingly. If the correct note are not found you may put a blank.",
    input_variables=["song_name"]
)
if st.button("Send"):
    if not api_key:
        st.error("Please enter a valid API key first!")
    elif not song_name:
        st.warning("Please enter a song name!")
    else:
        with st.spinner("Generating music notes..."):
            try:
                # Initialize the model inside the execution block
                chat_model = ChatGoogleGenerativeAI(
                    model="gemini-3.1-flash-lite", 
                    google_api_key=api_key # Use api_key parameter directly
                )
                structured_model = chat_model.with_structured_output(MusicNotes)

                chain = prompt_template | structured_model
                
                
                response = chain.invoke({"song_name": song_name})
                df = pd.DataFrame({
                    "Sr. No": response.sr_no,
                    "Lyrics": response.lyric,
                    "Chord": response.chord,
                    "Notes": response.notes
                    })
                st.table(df)
                st.success("Done!")
            except Exception as e:
                st.error(f"An error occurred: {e}")
