# Streamlit을 활용해 UI 만들기
import streamlit as st
import google.generativeai as genai

# API 키 설정
genai.configure(api_key='')

# 모델 설정 및 챗봇 시작
model = genai.GenerativeModel('gemini-1.5-flash', system_instruction="Chat like you're my very close friend")
chat = model.start_chat(history=[])

# Streamlit UI 설정
st.title("Gemini 챗봇")

if 'history' not in st.session_state:
    st.session_state.history = []

if 'user_ipnut' not in st.session_state:
    st.session_state.user_input = ""
    
def send_message():
    user_input = st.session_state.user_input
    if user_input:
        for i in range(5):
            try:
                response = chat.send_message(user_input)
            except:
                print(i)
                continue
            else:
                break                
        reply = response.text.replace("\n\n", "\n").strip()
        st.session_state.history.append(f"You: {user_input}")
        st.session_state.history.append(f"Gemini: {reply}")
        st.session_state.user_input = ""
        
# 대화 기록 표시
for message in st.session_state.history:
    st.write(message)
    
st.text_input("You: ", key="user_input", on_change=send_message)
