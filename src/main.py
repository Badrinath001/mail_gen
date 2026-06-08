from ollama import Client

def generate_email(subject: str, audience: str, tone: str) -> str:
    prompt = (
        f"Write a professional email about {subject} "
        f"for {audience} in a tone {tone}."
    )
    
    client = Client()
    response = client.generate(model="llama3", prompt=prompt)
    return response.response or ""