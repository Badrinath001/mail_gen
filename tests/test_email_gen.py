from ollama import Client
from src.main import generate_email


class DummyResponse:
    def __init__(self, response: str):
        self.response = response


def test_generate_email(monkeypatch):
    def fake_generate(self, model: str = "", prompt: str | None = None, **kwargs):
        assert model == "llama3"
        assert "Write a professional email" in prompt
        return DummyResponse(
            "Hello team,\n\nI am excited to share the update about the new product launch..."
        )

    monkeypatch.setattr(Client, "generate", fake_generate)

    email = generate_email("product launch", "a customer", "friendly")
    assert email.startswith("Hello team")
    assert "product launch" in email.lower() or "new product launch" in email.lower()
