import streamlit as st
import os
from streamlit_chat import message
from langchain.agents import initialize_agent, AgentType
from langchain.callbacks import StreamlitCallbackHandler
from langchain.chat_models import ChatOpenAI
from langchain.tools import DuckDuckGoSearchRun



# clear the chat history from streamlit session state
def clear_history():
    if 'internet_cb_history' in st.session_state:
        del st.session_state.internet_cb_history
        st.session_state.internet_cb_history= [
            {"role": "assistant", "content": "Hi, I'm a chatbot who can connect to the internet. How can I help you?"}
        ]


if __name__ == "__main__":

    ############################################################ System Configuration ############################################################

    if "internet_cb_history" not in st.session_state:
        st.session_state.internet_cb_history= [
            {"role": "assistant", "content": "Hi, I'm a chatbot who can connect to the internet, showing my thinking process. I'm transparent, not a black box. How can I help you?"}
        ]

    ############################################################ SIDEBAR widgets ############################################################

    with st.sidebar:

        # Setting up the OpenAI API key via secrets manager
        if 'OPENAI_API_KEY' in os.environ:
            api_key_validity  = True
            llm = ChatOpenAI(model_name="gpt-3.5-turbo", openai_api_key_validity=api_key_validity, streaming=True)
            st.success("Now using OpenAI's ChatGPT-3.5-Turbo")
        # elif 'HUGGINGFACEHUB_API_TOKEN' in st.secrets:
        #     api_key_validity  = True
        #     st.success("Now using Google's FLAN-T5, comparable to GPT-3.")
        #     st.info("To use ChatGPT-3.5-Turbo, please go to Home page.")
        #     llm = HuggingFaceHub(repo_id="google/flan-t5-xxl", model_kwargs={"temperature": temperature, "max_length": 512})
        else:
            st.warning("Please go to Home page to follow the instructions to use our personalized GPTs.")
            api_key_validity  = False

        st.divider()

        if st.button('Clear Chat History'):
            clear_history()


    ############################################################ MAIN PAGE widgets ############################################################

    st.title("🌐 Chat with Internet")

    st.divider()

    for message in st.session_state.internet_cb_history:
        st.chat_message(message["role"]).write(message["content"])

    question = st.chat_input(placeholder="Ask me anything currently on the web")

    if question:
        if api_key_validity:
            st.session_state.internet_cb_history.append({"role": "user", "content": question})
            st.chat_message("user").write(question)

            search = DuckDuckGoSearchRun(name="Search")
            search_agent = initialize_agent([search], llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, handle_parsing_errors=True)
            with st.chat_message("assistant"):
                chatBot = StreamlitCallbackHandler(st.container(), expand_new_thoughts=False)
                response = search_agent.run(st.session_state.internet_cb_history, callbacks=[chatBot])
                st.session_state.internet_cb_history.append({"role": "assistant", "content": response})
                st.write(response)
        elif not api_key_validity:
            st.warning('Please enter your OpenAI API Key to continue.')