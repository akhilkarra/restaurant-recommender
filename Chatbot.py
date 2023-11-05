import streamlit as st
import palm2_system

st.title("💬 Restaurant Recommender")
st.caption("🚀 A streamlit chatbot powered by Google PaLM 2 LLM")

# TODO: Find a way to make Streamlit run this only once
response = palm2_system.setup()

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    answer = palm2_system.chat(response, prompt)
    st.session_state.messages.append({"role": "assistant", "content": response.last})
    st.chat_message("assistant").write(response.last)
