# 🧑🏻‍💻 Lifesaver-GPTs-App (LLM + OpenAI + Streamlit)
Love or hate it, ChatGPT is changing the game for professionals worldwide. These AI tools won't replace you, they save your time for you to do the things you love.

## Overview of the App
Various GPTs are built to make different sectors of your life easier, such as workplace, health, student life and entertainment.
This app showcases a collection of helpful GPTs:

- AI Email Assistant
- One-Click Fitness Trainer
- Ask your Document
- Chat with Internet
- Custom ChatBot

## Try It for Free!
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://lifesaver-gpts-app.streamlit.app/)

### Enter the OpenAI API key in Streamlit Community Cloud

To set the OpenAI API key as an environment variable in Streamlit apps:

1. At the lower right corner, click on < Manage app then click on the vertical "..." followed by clicking on Settings.
2. This brings the App settings, next click on the Secrets tab and paste the API key into the text box as follows:
    ```sh
    OPENAI_API_KEY='xxxxxxxxxx'
    ```

### Get an OpenAI API key 🔑
1. Set up your OpenAI API Key by entering it in the app's sidebar. You can obtain an API key from the OpenAI Platform. 🔑
2. Go to https://platform.openai.com/account/api-keys.
3. Click on the `+ Create new secret key` button.
4. Click on the `Create secret key` button.

## Run it locally

1. Download this repository to your local machine. 📥
2. Open the terminal or command prompt and navigate to the directory where you downloaded the folder. 💻
3. Create a Python virtual environment for the project. Run the following commands in the terminal: 🛠️
    ```sh
    python -m venv [project_venv]
    .\[project_venv]\Scripts\activate (Windows)
    source ./[project_venv]/bin/activate (macOS/Linux)
    pip install -r requirements.txt
    ```
4. Start the Streamlit app by running the following command in the terminal: 💭
    ```sh
    streamlit run Home.py
    ```



## 1. 📧 AI Email Assistant

With AI-powered templates tailored to your chosen scenario, writing professional emails in ONE CLICK. Say goodbye to lengthy messages and hello to concise summaries. Respond effortlessly with perfectly fitting replies, all thanks to this AI chatbot. Simplify your email management and make it a breeze with this powerful tool. 📅💻

### Features 🌟
- Schedule a meeting: Generate concise and polite emails to set up meetings or calls.
- Follow up on a lead or client: Craft persuasive follow-up emails to nurture business relationships.
- Request information or action: Draft respectful and concise emails to ask for information or assistance.
- Provide project updates: Create well-structured emails to keep stakeholders informed about project progress.
- Send professional invoices: Generate polite emails with attached invoices for your clients.
- Apologize to customers: Compose sincere apology emails to address customer concerns.
- Request testimonials: Prompt emails asking for testimonials or referrals from clients.
- Decline invitations: Craft polite and professional emails to decline invitations gracefully.
- Job application: Compose job application emails showcasing your enthusiasm and qualifications.

### How to Use 📋
1. Select an email scenario and fill in the sidebar blanks
2. Hit generate and watch it create an email for you!
3. Tweak the email by chatting with the assistant


## 2. 🏋🏽 One-Click Fitness Trainer

Welcome to the One-Click Fitness Trainer app! 💪📲
This AI-powered Language Model (LLM) app is designed to make your fitness journey easier and more personalized. It creates custom diet and exercise plans based on your individual needs and preferences. 🥦🏋️‍♂️

## Features 🌟
- Create a personalized diet and exercise plan in just a few clicks
- Generate a detailed workout program tailored to your goals
- Get a comprehensive meal plan with customized recipes
- Generate a grocery list with quantities of each item
- Receive motivational quotes to keep you inspired

## How to Use 📋
1. Fill in your personal information, including age, gender, height, and weight.
2. Provide details about your medical conditions, food allergies, fitness goals, workout preferences, diet preferences, and more.
3. Click "Create your Personal Fitness Plan" to generate your customized plan.
4. Explore the generated plan, including the summary, workout program, meal plan, and grocery list.
5. Ask any fitness-related questions using the chat interface.
6. Clear the chat history by clicking the "Clear Chat History" button in the sidebar to start a new conversation. 🔄📜


## 3. 📂 AI Document Consultant
Don't spend money to hire a consultant for your business! This AI consultant harnesses the capabilities of OpenAI's GPT-3.5-Turbo language model to make your life easier when working with documents. 💼

### Features 🌟
- Ask Questions: You can ask any question about the content of your document and receive intelligent responses from the AI model. 🗣️❓
- Generate Summaries: With the click of a button, you can generate a concise summary of your document that covers the key points. 📝✨
- Flexible Configuration: The app provides configuration options to adjust the length, creativity, and relevance of the responses, allowing you to tailor the AI's output to your specific needs. 🛠️⚙️
- Multiple Summarization Approaches: The app offers three different summarization approaches: "Stuff," "Map Reduce," and "Refine." Each approach provides a unique way to summarize your document, catering to different document sizes and requirements. 📄✂️
- Document Chunking and Embedding: The app automatically splits your document into manageable chunks and creates embeddings using OpenAI's OpenAIEmbeddings. This ensures efficient processing and accurate responses. 📑

### How to Use 📋
1. Upload your document (in PDF, DOCX, or TXT format) using the "Upload a Document" section. 📂📄
2. Adjust the response configuration settings, such as chunk size, response length, and temperature, in the sidebar. ⚙️🔧
3. Ask questions about the document by entering them in the chat input field. 🗣️❓
4. Click the "Generate Summary" button to obtain a concise summary of the document. 📝✨
5. Explore the app's features and experiment with different settings to achieve the desired results. 🧪🔍
6. Clear the chat history by clicking the "Clear Chat History" button in the sidebar to start a new conversation. 🔄📜


## 4. 🌐 Chat with Internet 
The Chat with Internet app leverages the power of OpenAI's GPT-3.5-Turbo language model to provide you with a chatbot that can access the internet. This AI-powered chatbot can assist you with any questions or queries you have by retrieving information from the web. 🤖🌍

## Features 🌟
- Internet Connectivity: The chatbot is equipped with the ability to connect to the internet and retrieve relevant information for your queries. 🌍🔌
- OpenAI Integration: Powered by OpenAI's GPT-3.5-Turbo, the chatbot provides intelligent and context-aware responses. 🚀🧠
- Interactive Chat Interface: Engage in a conversational chat interface that allows you to ask questions and receive informative answers. 💭💡


## How to Use 📋
1. Start a conversation by asking a question in the chat input field. The chatbot will provide an intelligent response based on internet search results. 💬🔍
2. Enjoy a natural language conversation with the chatbot, asking follow-up questions or seeking clarification as needed. 🤝❓
3. Clear your chat history if needed with the "Clear Chat History" button. 🗑️


## 5. 🤖 Custom ChatBot 
The Custom ChatBot app utilizes OpenAI's GPT-3.5-Turbo language model to create a customizable chatbot. This AI-powered chatbot can assist you with various inquiries and provide professional answers based on the role assigned to it. 🚀🧠

## Features 🌟
- Role-based Chat: Assign a specific role to the chatbot, such as a helpful assistant, and receive responses tailored to that role. 👥💡
- Response Temperature: Adjust the temperature setting to control the creativity and variability of the chatbot's answers. 🌡️🔀
- Interactive Chat Interface: Engage in a conversation by sending messages to the chatbot and receiving replies in real-time. 💬🔄

## How to Use 📋
1. Customize the chatbot's role by specifying a system message in the sidebar. This defines the behavior of the assistant.
2. Adjust the response temperature using the slider in the sidebar to control the creativity of the chatbot's responses.
3. Type your message in the "Send a message" text area and click "Ask" to send it to the chatbot.
4. View the chat history in the main section of the app, with user messages and chatbot responses displayed sequentially.
6. Clear the chat history by clicking the "Clear Chat History" button in the sidebar to start a new conversation. 🔄📜