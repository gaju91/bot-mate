from openai import OpenAI
from app.sanity_connector import fetch_services
from app.config import OPENAI_API_KEY

client = OpenAI(
    api_key=OPENAI_API_KEY
)

def chatbot_response(user_query):
    """
    Generates a chatbot response using the GPT-4 model based on user query and company data.
    """
    # Fetch services data from Sanity CMS
    context = fetch_services()

    # Build the AI prompt with the system message
    messages = [
        {"role": "system", "content": "You are a helpful assistant that answers questions based on company data."},
        {"role": "user", "content": f"Based on this data:\n{context}\n\nAnswer the question: {user_query}"}
    ]

    # Generate a response using OpenAI GPT-4
    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=messages,
            max_tokens=300
        )

        # Extract and return the content of the first choice
        first_choice = response.choices[0]
        return first_choice.message.content.strip()
    except AttributeError as e:
        return f"AttributeError: {e}"
    except Exception as e:
        return f"An error occurred: {e}"