import streamlit as st
from chat_engine import ExaChatEngine
import time

def initialize_chat():
    if 'chat_engine' not in st.session_state:
        st.session_state.chat_engine = ExaChatEngine()

def display_chat_message(message):
    """Display a chat message with proper formatting"""
    with st.chat_message(message['type']):
        st.write(message['content'])
        
        # If it's an assistant message and has results, show them in an expander
        if message['type'] == 'assistant' and 'results' in message:
            with st.expander("View Sources"):
                for idx, result in enumerate(message['results'], 1):
                    st.markdown(f"**Source {idx}: [{result['title']}]({result['url']})**")
                    st.markdown(f"Relevance Score: {result['score']:.2f}")
                    if result['highlights']:
                        st.markdown("**Highlights:**")
                        for highlight in result['highlights']:
                            st.markdown(f"- {highlight}")
                    st.markdown("---")

def main():
    st.title("💬 Exa Chat")
    st.caption("Chat with AI-powered search results")
    
    # Initialize chat engine
    initialize_chat()
    
    # Add a sidebar for settings
    with st.sidebar:
        st.header("Settings")
        num_results = st.slider("Number of results per query", 1, 10, 3)
        
        if st.button("Clear Chat History"):
            st.session_state.chat_engine.clear_chat_history()
            st.rerun()
    
    # Display chat history
    for message in st.session_state.chat_engine.get_chat_history():
        display_chat_message(message)
    
    # Chat input
    if prompt := st.chat_input("Ask me anything..."):
        # Display user message
        with st.chat_message("user"):
            st.write(prompt)
        
        # Display assistant response with typing indicator
        with st.chat_message("assistant"):
            with st.spinner("Searching..."):
                try:
                    results = st.session_state.chat_engine.search_and_format(prompt, num_results)
                    # Get the latest assistant message from chat history
                    latest_message = st.session_state.chat_engine.get_chat_history()[-1]
                    st.write(latest_message['content'])
                    
                    # Show sources in expander
                    with st.expander("View Sources"):
                        for idx, result in enumerate(results, 1):
                            st.markdown(f"**Source {idx}: [{result['title']}]({result['url']})**")
                            st.markdown(f"Relevance Score: {result['score']:.2f}")
                            if result['highlights']:
                                st.markdown("**Highlights:**")
                                for highlight in result['highlights']:
                                    st.markdown(f"- {highlight}")
                            st.markdown("---")
                except Exception as e:
                    st.error(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
