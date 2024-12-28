# Exa Chat

A conversational interface for Exa's neural search API that allows users to chat with AI-powered search results.

## Features

- 💬 Chat-like interface built with Streamlit
- 🔍 Powered by Exa's neural search
- 📚 Source transparency with expandable references
- ⚙️ Configurable search settings
- 📝 Conversation history tracking

## Project Structure

```
exa_chat/
├── src/
│   ├── app.py            # Streamlit chat interface
│   ├── chat_engine.py    # Core chat and search functionality
├── .env                  # Environment variables (API keys)
├── requirements.txt      # Project dependencies
└── README.md            # Project documentation
```

## Setup

1. Clone the repository
2. Create a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Set up your environment variables:
   - Create a `.env` file in the project root
   - Add your Exa API key: `EXA_API_KEY=your_api_key_here`

## Running the Application

```bash
cd src
streamlit run app.py
```

The application will open in your default web browser.

## Usage

1. Enter your question in the chat input at the bottom
2. The AI will search and respond conversationally
3. Click "View Sources" to see detailed information about the sources
4. Adjust settings in the sidebar:
   - Number of results per query
   - Clear chat history

## Features in Detail

### Chat Interface
- Clean, modern chat UI using Streamlit's chat components
- Real-time search results as you chat
- Expandable source information for each response

### Search Features
- Uses Exa's neural search with content retrieval
- Automatically formats search results into conversational responses
- Shows highlights and relevant snippets from sources

### Settings and Controls
- Adjust number of results per query (1-10)
- Clear chat history option
- Expandable source information for transparency

### Chat History
- Maintains conversation history
- Shows both user queries and AI responses
- Includes timestamps for each message

## Dependencies

- exa-py>=1.7.1
- python-dotenv>=1.0.0
- streamlit>=1.29.0
- pandas>=2.1.0
- altair>=5.2.0

## Contributing

Feel free to submit issues and enhancement requests!
