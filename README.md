# MartLLM provider for Agent Zero

Use [MartLLM](https://martllm.com) models in [Agent Zero](https://github.com/agent0ai/agent-zero) as a chat model provider.

MartLLM is a marketplace of third-party sellers with an OpenAI-compatible API. Each request is sent to a third-party provider that serves the requested model. MartLLM is not the maker of any model and is not an official endpoint of any model maker. MartLLM maintains this plugin. It is not affiliated with Agent Zero.

## Why a plugin?

Agent Zero can already reach MartLLM through its "Other OpenAI compatible" option. This plugin adds **MartLLM** to the provider dropdown, sets the base URL `https://api.martllm.com/v1`, loads the model list, and maps your key to `MARTLLM_API_KEY`.

## Install

Install **MartLLM Provider** from the Plugin Hub in Agent Zero.

## Configure

1. Create a key at [martllm.com/signup](https://martllm.com/signup). Accounts are prepaid.
2. In Agent Zero's model settings, set the provider of the main model to **MartLLM**, choose a model, and paste your key into the API key field.
3. Save.

## Models

Agent Zero reads the list from `https://api.martllm.com/v1/models` (public, no key needed). Model ids carry the maker as a prefix. Examples from that list:

- `anthropic/claude-sonnet-5.5`
- `openai/gpt-6.1-sol`
- `google/gemini-4-neon`
- `deepseek/deepseek-v4-flash`
- `moonshotai/kimi-k3.1-pro`

Prices per model: [martllm.com/models](https://martllm.com/models). The plugin registers chat models only.

## Security and footprint

- **Network:** Agent Zero sends your requests, including prompts and any files or images in them, to `https://api.martllm.com` with your MartLLM key. MartLLM passes each request to a third-party provider. See [martllm.com/docs/privacy](https://martllm.com/docs/privacy).
- **Code:** configuration only: one provider entry. No code runs, no tools are added, no dependencies.
- **Credentials:** Agent Zero holds the key. The plugin stores no secrets.
- **Telemetry:** none.

## Check

```
python tests/test_plugin_contract.py
```

## Remove

Remove the plugin in Agent Zero's plugin settings. Your other providers stay as they are.

## License

MIT
