import pytest
import sys
import os
from unittest.mock import patch, MagicMock

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from shared.clients import get_llm_client

class TestGetLlmClient:
    @patch.dict(os.environ, {"GOOGLE_API_KEY": "fake_google_key", "OPENAI_API_KEY": "fake_openai_key"}, clear=True)
    @patch("shared.clients.ChatGoogleGenerativeAI")
    def test_prefer_google_when_both_present(self, mock_google):
        """Should return Google client if both keys are present (Priority Rule)."""
        get_llm_client()
        mock_google.assert_called_once()
        # Verify it used the default Gemini model
        assert mock_google.call_args[1]['model'] == "gemini-2.5-flash"

    @patch.dict(os.environ, {"OPENAI_API_KEY": "fake_openai_key"}, clear=True)
    @patch("shared.clients.ChatOpenAI")
    def test_fallback_openai_when_google_missing(self, mock_openai):
        """Should return OpenAI client if Google key is missing."""
        # Ensure GOOGLE_API_KEY is definitely NOT in env (patch.dict with clear=True handles this partially, 
        # but let's be safe regarding 'os.getenv')
        
        get_llm_client()
        mock_openai.assert_called_once()
        # Verify it used the default GPT model
        assert mock_openai.call_args[1]['model'] == "gpt-4o-mini"

    @patch.dict(os.environ, {}, clear=True)
    def test_raise_error_when_no_keys(self):
        """Should raise ValueError if no keys are present."""
        with pytest.raises(ValueError, match="No API keys found"):
            get_llm_client()

    @patch.dict(os.environ, {"GOOGLE_API_KEY": "fake_key"}, clear=True)
    @patch("shared.clients.ChatGoogleGenerativeAI")
    def test_override_model_parameters(self, mock_google):
        """Should allow overriding model name and temperature."""
        get_llm_client(model="gemini-pro-vision", temperature=0.5)
        
        call_kwargs = mock_google.call_args[1]
        assert call_kwargs['model'] == "gemini-pro-vision"
        assert call_kwargs['temperature'] == 0.5
