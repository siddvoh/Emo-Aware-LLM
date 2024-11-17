from openai import OpenAI
import os

def get_response(prompt):
    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a helpful assistant. Acknowledge the user's emotion and answer accordingly"},
                {"role": "user", "content": prompt}
            ],
            max_tokens=150,
            temperature=0.7,
        )
        answer = response.choices[0].message.content.strip()
        return answer
    except Exception as e:
        print(f"Error communicating with OpenAI: {e}")
        return None