# Routing Diagram

```mermaid
flowchart LR
  Tool[Claude Code Compatible Tool] --> Env[ANTHROPIC env vars]
  Env --> Anthropic[Anthropic]
  Env --> OpenRouter[OpenRouter]
  Env --> LiteLLM[LiteLLM]
  LiteLLM --> Ollama[Ollama]
  LiteLLM --> DeepSeek[DeepSeek]
```

