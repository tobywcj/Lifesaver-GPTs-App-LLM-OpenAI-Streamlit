import streamlit as st
from dotenv import load_dotenv, find_dotenv
from streamlit_chat import message
from langchain.chat_models import ChatOpenAI
from langchain.schema import(
    SystemMessage, # set the behavior of the assistant
    HumanMessage, # what we ask
    AIMessage #  store prior responses
)



# clear the chat history from streamlit session state
def clear_history():
    if 'custom_cb_history' in st.session_state:
        del st.session_state.custom_cb_history
        st.session_state.custom_cb_history = list()


if __name__ == "__main__":

    ############################################################ System Configuration ############################################################

    load_dotenv(find_dotenv(), override=True)

    # creating the history (chat history) in the Streamlit session state
    if 'custom_cb_history' not in st.session_state:
        st.session_state.custom_cb_history = []


    ############################################################ SIDEBAR widgets ############################################################

    with st.sidebar:

        # text_input for the OpenAI API key of user
        api_key = st.text_input("OpenAI API Key", key="api_key", type="password")
        "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"

        st.divider()

        # Response Configuration Expander
        with st.expander('Response Configuration'):
            temperature = st.slider('Temperature:', min_value=0.0, max_value=2.0, value=0.5, step=0.1)
            st.warning('Larger the number, More Creative is the response.')
        
        llm = ChatOpenAI(model_name='gpt-3.5-turbo', temperature=temperature)
        
        with st.form('Send a message'):
            system_role = st.text_input(label='System role', placeholder='A helpful Assistant (default)') # streamlit text input widget for the system message (role)
            user_prompt = st.text_area(label='Send a message') # streamlit text area input widget for the user message
            submitted = st.form_submit_button("Ask")
        

        if system_role:
            if not any(isinstance(x, SystemMessage) for x in st.session_state.custom_cb_history):
                st.session_state.custom_cb_history.append(
                    SystemMessage(content=system_role)
                    )
            

        # if the user entered a question
        if user_prompt:
            if api_key:
                st.session_state.custom_cb_history.append(
                    HumanMessage(content=user_prompt)
                )

                # adding a default SystemMessage if the user didn't entered one
                if len(st.session_state.custom_cb_history) >= 1:
                    if not isinstance(st.session_state.custom_cb_history[0], SystemMessage):
                        st.session_state.custom_cb_history.insert(0, SystemMessage(content='You are a helpful assistant.'))

                with st.spinner('Working on your request ...'):
                    # creating the ChatGPT response
                    response = llm(st.session_state.custom_cb_history)

                # adding the response's content to the session state
                st.session_state.custom_cb_history.append(AIMessage(content=response.content))
            elif not api_key:
                st.warning('Please enter your OpenAI API Key to continue.')

        if st.button('Clear Chat History'):
            clear_history()


    ############################################################ MAIN PAGE widgets ############################################################

    st.title('🤖 Custom ChatBot')

    st.divider()

    if not st.session_state.custom_cb_history:
        message('Hi mate, how can I help you? I can instantly provide a professional answer to you as the role you give me.', is_user=False, key=f'{system_role}') # ChatGPT response

    # displaying the history (chat history)
    for i, msg in enumerate(st.session_state.custom_cb_history[1:]):
        if i % 2 == 0:
            message(msg.content, is_user=True, key=f'user_{i}') # user's question
        else:
            message(msg.content, is_user=False, key=f'AI_{i}') # ChatGPT response

# run the app: streamlit run ./project_streamlit_custom_chatgpt.py