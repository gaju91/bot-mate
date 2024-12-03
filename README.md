
# 🤖 BotMate — AI Chatbot for Your Organization 🚀

BotMate is an intelligent chatbot designed to simplify internal communication within large organizations. With BotMate, employees can discover services, find solutions, and collaborate across divisions without relying on external resources. Powered by OpenAI GPT-4 and integrated with Sanity CMS, this chatbot helps unlock your organization's full potential.

---

## 🌟 Features

- 🔍 **Service Discovery**: Quickly find services offered across divisions.
- 🧠 **Contextual Conversations**: Maintains context to handle multi-turn chats effectively.
- 🛠 **Metadata-Driven Responses**: Provides additional insights like timestamps, message IDs, and token usage.
- 🌐 **Seamless Integration**: Backend built with Python (Flask) and ready for integration with Flutter.
- 📈 **Search Trends**: Tracks and displays recent and popular searches.
- 🔒 **Secure & Scalable**: Designed for production environments with robust security features.

---

## 🛠 Tech Stack

### Backend
- **Python** 🐍 with Flask
- **OpenAI GPT-4** for intelligent responses
- **Sanity CMS** for structured data management

### Frontend
- **Flutter** 🦋 (Ready for seamless integration) (Not here 🫠)

### Database
- In-memory structure for initial development (extendable to NoSQL/SQL databases)

---

## 🚀 Getting Started

Follow these steps to set up and run BotMate locally:

### Prerequisites
- Python 3.8+
- OpenAI API key 🔑
- Sanity CMS Project ID and Token
- Flask installed in a virtual environment

### Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/botmate.git
   cd botmate
   ```

2. **Set Up Virtual Environment**
   ```bash
   python3 -m venv your-env-name
   source your-env-name/bin/activate
   pip install -r requirements.txt
   ```

3. **Configure Environment Variables**
   Create a `.env` file in the project root with the following:
   ```env
   OPENAI_API_KEY=your_openai_api_key
   SANITY_PROJECT_ID=your_sanity_project_id
   SANITY_API_TOKEN=your_sanity_api_token
   ```

4. **Run the Server**
   ```bash
   python main.py
   ```

5. **Test the API**
   Use `curl` to test:
   ```bash
   curl -X POST http://127.0.0.1:5000/chat -H "Content-Type: application/json" -d '{"message": "What does Division A do?"}'
   ```

---

## 🛡 Security

- Ensure `.env` is added to `.gitignore` to keep API keys secure.
- Use HTTPS for production deployments to secure communication.
- Restrict API access with IP whitelisting or authentication mechanisms.

---

## 🤔 Future Improvements

- 🌍 **Multi-Language Support**: Add translation capabilities for diverse teams.
- 🔊 **Voice Interaction**: Enable voice-based commands and responses.
- 📊 **Analytics Dashboard**: Monitor chatbot performance and user interactions.
- 💬 **Live Escalation**: Integrate with a human support system.

---

## 🙌 Contributing

We welcome contributions! Please fork the repository and create a pull request with your enhancements.

---

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 🎉 Acknowledgments

- [OpenAI](https://openai.com) for their amazing GPT-4 model.
- [Sanity CMS](https://www.sanity.io) for powerful content management.

---

## 📬 Contact

For questions or feedback, please reach out to `gajanand742@gmail.com`. We'd love to hear from you! 💌