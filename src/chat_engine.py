from exa_py import Exa
import os
from dotenv import load_dotenv
from typing import List, Dict, Any, Optional
from datetime import datetime

class ExaChatEngine:
    def __init__(self):
        load_dotenv()
        api_key = os.getenv('EXA_API_KEY')
        if not api_key:
            raise ValueError("EXA_API_KEY environment variable is not set")
        self.exa = Exa(api_key)
        self.chat_history = []

    def _format_result(self, result) -> Dict[str, Any]:
        """Format a search result into a chat-friendly format"""
        return {
            'title': getattr(result, 'title', 'No Title'),
            'url': getattr(result, 'url', '#'),
            'content': getattr(result, 'text', ''),
            'highlights': getattr(result, 'highlights', []),
            'score': getattr(result, 'score', 0.0),
            'timestamp': datetime.now().isoformat()
        }

    def search_and_format(self, query: str, num_results: int = 3) -> List[Dict[str, Any]]:
        """Search using Exa and format results for chat"""
        try:
            # Perform a neural search with content retrieval
            response = self.exa.search_and_contents(
                query,
                num_results=num_results,
                type="neural",
                use_autoprompt=True,
                text=True,
                highlights=True
            )

            if response and hasattr(response, 'results'):
                results = [self._format_result(result) for result in response.results]
                
                # Add to chat history
                self.chat_history.append({
                    'type': 'user',
                    'content': query,
                    'timestamp': datetime.now().isoformat()
                })
                
                # Format assistant response
                response_content = self._generate_chat_response(query, results)
                self.chat_history.append({
                    'type': 'assistant',
                    'content': response_content,
                    'results': results,
                    'timestamp': datetime.now().isoformat()
                })
                
                return results
            return []
        except Exception as e:
            raise Exception(f"Search failed: {str(e)}")

    def _generate_chat_response(self, query: str, results: List[Dict[str, Any]]) -> str:
        """Generate a conversational response based on search results"""
        if not results:
            return "I couldn't find any relevant information about that. Could you try rephrasing your question?"

        # Create a response using the most relevant result
        top_result = results[0]
        response = f"Based on my search, {top_result['title']} seems most relevant. "

        if top_result['highlights']:
            response += f"Here's what I found: {' '.join(top_result['highlights'][:2])}"
        elif top_result['content']:
            # Take first 200 characters of content if no highlights
            response += f"Here's what I found: {top_result['content'][:200]}..."

        if len(results) > 1:
            response += f"\n\nI also found {len(results)-1} other relevant sources. Would you like to know more about those?"

        return response

    def get_chat_history(self) -> List[Dict[str, Any]]:
        """Get the full chat history"""
        return self.chat_history

    def clear_chat_history(self):
        """Clear the chat history"""
        self.chat_history = []
