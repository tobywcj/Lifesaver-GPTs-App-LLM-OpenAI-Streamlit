import streamlit as st



############################################################ SIDEBAR widgets ############################################################

with st.sidebar:

    # text_input for the OpenAI API key of user
    api_key = st.text_input("OpenAI API Key", key="api_key", type="password")
    "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"
    "[View the source code](https://github.com/tobywcj/Lifesaver-GPTs-App.git)"
    

############################################################ MAIN PAGE widgets ############################################################

st.title("🧑🏻‍💻 Lifesaver GPTs App")

st.write('''Love or hate it, ChatGPT is changing the game for professionals worldwide. These AI tools won't replace you, they save your time for you to do the things you love.😊🤖
         \nwe have gathered a diverse range of Large Language Model (LLM) AI bots to assist you in various tasks and provide valuable insights. 🚀🔍
         \nEach bot has been designed to cater to specific needs and offer a unique experience.💪🌟''')

st.divider()

st.subheader('📧 AI Email Assistant')
st.write('''Are you tired of spending countless hours writing emails? 
            \nOur AI Email Assistant is here to help! 
            With its natural language processing capabilities, it can generate personalized and professional email drafts for you. 
            Simply provide some context, and let the assistant compose your message effortlessly.
            \nExperience the convenience and efficiency of AI-powered email writing with the AI Email Assistant! 🤖✉️
            ''')

st.divider()

st.subheader('📂 AI Document Consultant')
st.write('''Need help with document creation and editing? 
            \nOur AI Document Consultant is here to lend a hand. Whether it's proofreading your content, suggesting improvements, or generating well-structured documents, 
            this bot can assist you in crafting professional and polished written materials.
            \nThe AI Document Consultant app streamlines the process of working with documents, providing quick and accurate answers to your questions and generating concise summaries. Try it out and experience the power of AI in document analysis and summarization. ✨🤖📚
            ''')

st.divider()

st.subheader('🤖 Custom ChatBot ')
st.write('''Are you tired of generic chatbots that don't understand your specific needs? 
            \nThe Custom ChatBot app offers a personalized and efficient way to interact with an AI-powered chatbot. 
            Tailor the chatbot's role, receive instant professional answers, and enjoy a seamless conversation experience. 
            \nGive it a try and make your interactions with AI more engaging and productive. 🤖💬
            ''')

st.divider()

st.subheader('🏋🏽 One-Click Fitness Trainer')
st.write('''Achieve your fitness goals without pay money to your personal trainer? 
            \nOur One-Click Fitness Trainer takes into account your personal information, preferences, and goals to create a customized fitness plan. 
            It provides you with detailed workout programs, meal plans, grocery lists, and motivational quotes to keep you inspired on your fitness journey.
            \nStart your fitness journey with the One-Click Fitness Trainer app and experience the convenience of personalized fitness planning powered by AI! 🚀🌟
            ''')

st.divider()

st.subheader('🌐 Chat with Internet ')
st.write('''Explore the vast knowledge of the internet through our Chat with Internet bot. 
            \nPowered by cutting-edge technology, this bot can fetch real-time information, answer questions, and provide up-to-date insights on a wide array of topics. 
            Get the latest news, search for specific information, or satisfy your curiosity with this intelligent bot.
            \nTry it out and experience the convenience of an AI-powered chatbot with internet access. 🌐💬
            ''')

st.divider()

st.write("""Each bot has its own unique functionalities and capabilities, ensuring a tailored experience based on your requirements. 
         \nSimply select the bot that aligns with your needs, and enjoy the benefits of AI-powered assistance.
         \nWe invite you to explore our LLM Bot Collection and make the most of these intelligent bots. Empower yourself with their capabilities and streamline your tasks with ease. Happy botting! 🚀🤖""")

    
