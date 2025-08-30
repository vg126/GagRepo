---
title: "External Application Guide | Poe Creator Platform"
source: "https://creator.poe.com/docs/external-applications/external-application-guide"
author:
published:
created: 2025-08-30
description: "External applications exist outside the Poe client UI. They connect to Poe via a Poe user's API key, and use the Poe API to query Poe bots and models."
tags:
  - "clippings"
---
External applications exist outside the Poe client UI. They connect to Poe via a Poe user's API key, and use the Poe API to query Poe bots and models on behalf of that user, spending the user's points in the process.

Examples of possible external applications:

- Browser toolbars
- Shell scripts
- Alternative chat interfaces
- Specialized client applications like IDEs

## Querying Poe bots via an API key

All Poe API keys are associated with a user account. As a creator, you can use your own API key, meaning points will be charged to your own Poe account, or you can ask users of your product to provide their Poe API key, meaning points will be charge to their Poe account. Note that if you are creating a server bot, you can charge requests directly to the user's account without requiring an API key via [Accessing other bots on Poe](https://creator.poe.com/docs/server-bots/accessing-other-bots-on-poe).

> ❗️ Warning
> 
> This API makes the API key owner's entire point balance available to any bot that is queried, so you may want to be careful about calling bots that are not your own or are not marked as official.

#### Get an API Key

Navigate to [poe.com/api\_key](https://poe.com/api_key) and copy your user API key (or ask your users to do the same).

![Image](https://files.readme.io/2b74562b026bc968fe54d746148458d34537899901fe4b9fb223e956d2a1d68b-Poe_API_Key_2025-04-03_at_4.06.13_PM.jpg)

#### Install Dependencies

To use the fastapi\_poe library in your project, you'll need to install it first. This can be done using pip, Python's package installer. The command `pip install fastapi-poe` will download and install the latest version of the library and its dependencies from PyPI (Python Package Index).

Run this command in your terminal or command prompt to complete the installation.

#### Call "get\_bot\_response" or "get\_bot\_response\_sync".

In a python shell, run the following after replacing the placeholder with an API key.

```python
import fastapi_poe as fp

api_key = <api_key> # replace this with your API key
message = fp.ProtocolMessage(role="user", content="Hello world")

for partial in fp.get_bot_response_sync(messages=[message], bot_name="GPT-3.5-Turbo", api_key=api_key):
    print(partial)
```

For asynchronous applications, use `fp.get_bot_response` instead of `fp.get_bot_response_sync`.

```python
import asyncio
import fastapi_poe as fp

async def get_response():
    api_key = <api_key> # replace this with your API key
    message = fp.ProtocolMessage(role="user", content="Hello world")
    async for partial in fp.get_bot_response(messages=[message], bot_name="GPT-3.5-Turbo", api_key=api_key): 
        print(partial)

def main():
    asyncio.run(get_response())

if __name__ == "__main__":
    main()
```

#### Sending files in the query

Use `fp.upload_file` to upload the files before sending them in the request.

```python
import fastapi_poe as fp

api_key = <api_key> # replace this with your API key
pdf_attachment = fp.upload_file_sync(open("draconomicon.pdf", "rb"), api_key=api_key)
message = fp.ProtocolMessage(role="user", content="Hello world", attachments=[pdf_attachment])

for partial in fp.get_bot_response_sync(messages=[message], bot_name="GPT-3.5-Turbo", api_key=api_key):
    print(partial)
```

Limitations:

- Requests are rate-limited to 500 requests per minute per user.
- Compute points are deducted directly from the account associated with the API key.

## Questions?

Please [contact us](https://creator.poe.com/docs/resources/how-to-contact-us) if you would like a higher limit or want to request any other changes to support your external application.

---
title: "OpenAI Compatible API | Poe Creator Platform"
source: "https://creator.poe.com/docs/external-applications/openai-compatible-api"
author:
published:
created: 2025-08-30
description: "Use the Poe API with an OpenAI Chat Completions API."
tags:
  - "clippings"
---
The Poe API provides access to hundreds of AI models and bots through a single OpenAI-compatible endpoint. Switch between frontier models from all major labs, open-source models, and millions of community-created bots using the same familiar interface.

**Key benefits:**

- Use your existing Poe subscription points with no additional setup
- Access models across all modalities: text, image, video, and audio generation
- OpenAI-compatible interface works with existing tools like [Cursor, Cline, Continue, and more](https://creator.poe.com/docs/external-applications/interface-configuration)
- Single API key for hundreds of models instead of managing multiple provider keys

If you're already using the OpenAI libraries, you can use this API as a low-cost way to switch between calling OpenAI models and Poe hosted models/bots to compare output, cost, and scalability, without changing your existing code. If you aren't already using the OpenAI libraries, we recommend that you use our [Python SDK](https://creator.poe.com/docs/external-applications/external-application-guide).

## Using the OpenAI SDK

## Options

1. **Poe Python Library** (✅ recommended)
	Install with `pip install fastapi-poe` for a native Python interface, better error handling, and ongoing feature support.
	→ See the [External Application Guide](https://creator.poe.com/docs/external-applications/external-application-guide) to get started.
2. **OpenAI-Compatible API** (for compatibility use cases only)
	Poe also supports the `/v1/chat/completions` format if you're migrating from OpenAI or need a REST-only setup.
	Base URL: `https://api.poe.com/v1`

> For new projects, use the Python SDK--it's the most reliable and flexible way to build on Poe.

## Known Issues & Limitations

### Bot Availability

- **Private bots are not currently supported** - Only public bots can be accessed through the API
- **The Assistant bot is not available** via the OpenAI-compatible API endpoint
- **Image, video, and audio bots** should be called with `stream=False` for optimal performance and reliability

### Parameter Handling

- **Best-effort parameter passing** - We make our best attempts to pass down parameters where possible, but some model-specific parameters may not be fully supported across all bots

### Additional Considerations

- Some community bots may have varying response formats or capabilities compared to standard language models

### API behavior

Here are the most substantial differences from using OpenAI:

- The **`strict`** parameter for function calling is ignored, which means the tool use JSON is not guaranteed to follow the supplied schema.
- Audio input is not supported; it will simply be ignored and stripped from input
- Most unsupported fields are silently ignored rather than producing errors. These are all documented below.

## Detailed OpenAI Compatible API Support

### Request fields

| **Field** | **Support status** |
| --- | --- |
| **`model`** | Use poe bot names |
| **`max_tokens`** | Fully supported |
| **`max_completion_tokens`** | Fully supported |
| **`stream`** | Fully supported |
| **`stream_options`** | Fully supported |
| **`top_p`** | Fully supported |
| **`tools`** | Fully Supported |
| **`tool_choice`** | Fully Supported |
| **`parallel_tool_calls`** | Fully Supported |
| **`stop`** | All non-whitespace stop sequences work |
| **`temperature`** | Between 0 and 2 (inclusive). |
| **`n`** | Must be exactly 1 |
| **`logprobs`** | Ignored |
| **`store`** | Ignored |
| **`metadata`** | Ignored |
| **`response_format`** | Ignored |
| **`prediction`** | Ignored |
| **`presence_penalty`** | Ignored |
| **`frequency_penalty`** | Ignored |
| **`seed`** | Ignored |
| **`service_tier`** | Ignored |
| **`audio`** | Ignored |
| **`logit_bias`** | Ignored |
| **`user`** | Ignored |
| **`modalities`** | Ignored |
| **`top_logprobs`** | Ignored |
| **`reasoning_effort`** | Ignored |

### Response fields

| **Field** | **Support status** |
| --- | --- |
| **`id`** | Fully supported |
| **`choices[]`** | Will always have a length of 1 |
| **`choices[].finish_reason`** | Fully supported |
| **`choices[].index`** | Fully supported |
| **`choices[].message.role`** | Fully supported |
| **`choices[].message.content`** | Fully supported |
| **`choices[].message.tool_calls`** | Fully supported |
| **`object`** | Fully supported |
| **`created`** | Fully supported |
| **`model`** | Fully supported |
| **`finish_reason`** | Fully supported |
| **`content`** | Fully supported |
| **`usage.completion_tokens`** | Fully supported |
| **`usage.prompt_tokens`** | Fully supported |
| **`usage.total_tokens`** | Fully supported |
| **`usage.completion_tokens_details`** | Always empty |
| **`usage.prompt_tokens_details`** | Always empty |
| **`choices[].message.refusal`** | Always empty |
| **`choices[].message.audio`** | Always empty |
| **`logprobs`** | Always empty |
| **`service_tier`** | Always empty |
| **`system_fingerprint`** | Always empty |

The compatibility layer maintains consistent error formats with the OpenAI API. However, the detailed error messages may not be equivalent. We recommend only using the error messages for logging and debugging.

All errors return:

```markdown
{
  "error": {
    "code": 401,
    "type": "authentication_error",
    "message": "Invalid API key",
    "metadata": {...}
  }
}
```

| HTTP / `code` | `type` | When it happens |
| --- | --- | --- |
| **400** | `invalid_request_error` | malformed JSON, missing fields |
| **401** | `authentication_error` | bad/expired key |
| **402** | `insufficient_credits` | balance ≤ 0 |
| **403** | `moderation_error` | permission denied or authorization issues |
| **404** | `not_found_error` | wrong endpoint / model |
| **408** | `timeout_error` | model didn't start in a reasonable time |
| **413** | `request_too_large` | tokens > context window |
| **429** | `rate_limit_error` | rpm/tpm cap hit |
| **502** | `upstream_error` | model backend not working |
| **529** | `overloaded_error` | transient traffic spike |

**Retry tips**

- Respect `Retry-After` header on 429/503.
- Exponential back‑off (starting at 250 ms) plus jitter works well.
- Idempotency: resubmit the exact same payload to safely retry.

### Header compatibility

While the OpenAI SDK automatically manages headers, here is the complete list of headers supported by Poe's API for developers who need to work with them directly.

Response Headers:

| **Header** | **Definition** | **Support Status** |
| --- | --- | --- |
| **`openai-organization`** | OpenAI org | Unsupported |
| **`openai-processing-ms`** | Time taken processing your API request | Supported |
| **`openai-version`** | REST API version (**`2020-10-01`)** | Supported |
| **`x-request-id`** | Unique identifier for this API request (troubleshooting) | Supported |

**Rate Limit Headers**

Our rate limit is 500 rpm, but theres no planned support for any of the following rate limit headers at this time:

- `x-ratelimit-limit-requests` (how many requests allowed for the time window)
- `x-ratelimit-remaining-requests` (how many requests remaining for the time window)
- `x-ratelimit-reset-requests` (timestamp of when the time window resets)

## Getting Started

## Streaming

You can also use OpenAI's streaming capabilities to stream back your response:

## Migration checklist (OpenAI → Poe in 60 s)

1. Swap base URL - `https://api.openai.com/v1` → `https://api.poe.com/v1`
2. Replace key env var - `OPENAI_API_KEY` → `POE_API_KEY`
3. Select the model/bot you want to use e.g. `Claude-Opus-4.1`
4. Delete any `n > 1`, audio, or `parallel_tool_calls` params.
5. Run tests - output should match except for intentional gaps above.

## Pricing & Availability

All Poe subscribers can use their existing subscription points with the API at no additional cost.

This means you can seamlessly transition between the web interface and API without worrying about separate billing structures or additional fees. Your regular monthly point allocation works exactly the same way whether you're chatting directly on Poe or accessing bots programmatically through the API.

If your Poe subscription is not enough, you can now purchase add-on points to get as much access as your application requires. Our intent in pricing these points is to charge the same amount for model access that underlying model providers charge. Any add-on points you purchase can be used with any model or bot on Poe and work across both the API and Poe chat on web, iOS, Android, Mac, and Windows.

## Support

Feel free to [reach out to support](https://creator.poe.com/docs/external-applications/) if you come across some unexpected behavior when using our API or have suggestions for future improvements.
---
title: "Interface Configuration | Poe Creator Platform"
source: "https://creator.poe.com/docs/external-applications/interface-configuration"
author:
published:
created: 2025-08-30
description: "Step-by-step setup guides for using Poe API with popular AI coding tools like Cursor, Cline, and Roo Code"
tags:
  - "clippings"
---
This guide walks you through setting up Poe API with popular AI coding tools. With Poe's OpenAI-compatible API, you can access hundreds of AI models including GPT-4o, Claude Sonnet 4, Gemini 2.5 Pro, and more through your existing coding workflow.

## Prerequisites

Before setting up any interface, you'll need:

1. **Poe API Key**: Get your API key from [poe.com/api\_key](https://poe.com/api_key)
2. **Poe Subscription**: An active Poe subscription to access the models
3. **Base URL**: `https://api.poe.com/v1/`

## Available Models

Popular models you can use include:

- `GPT-4o` - OpenAI's latest model
- `Claude-Sonnet-4` - Anthropic's most capable model
- `Gemini-2.5-Pro` - Google's flagship model
- `Llama-3.1-405B` - Meta's largest open-source model
- `Grok-4` - xAI's latest model

For a complete list, visit the [models endpoint](https://api.poe.com/v1/models) or check available models in the Poe web interface.

---

## Cursor Setup

[Cursor](https://cursor.sh/) is an AI-powered code editor built for pair-programming with AI.

### Step-by-Step Configuration

1. **Open Cursor Settings**
	- Press `Cmd/Ctrl + ,` to open settings
	- Or go to **Cursor** → **Preferences** (Mac) / **File** → **Preferences** (Windows/Linux)
2. **Navigate to Models**
	- Click on **Models** in the left sidebar
	- Look for the **Chat** or **AI Models** section
3. **Add Custom Model Provider**
	- Click **Add Model** or **Configure Custom Provider**
	- Select **OpenAI Compatible** or **Custom OpenAI**
4. **Configure Poe API Settings**
	```markdown
	Provider Name: Poe
	Base URL: https://api.poe.com/v1/
	API Key: [Your Poe API Key from poe.com/api_key]
	```
5. **Select a Model**
	- Choose from available models like:
		- `Claude-Sonnet-4`
		- `GPT-4o`
		- `Gemini-2.5-Pro`
6. **Test the Configuration**
	- Open a new chat with `Cmd/Ctrl + L`
	- Send a test message to verify the setup

### Usage Tips for Cursor

- Use `Cmd/Ctrl + K` for inline code generation
- Use `Cmd/Ctrl + L` for chat-based assistance
- The AI can see your entire codebase context automatically

---

## Cline Setup

[Cline](https://github.com/cline/cline) is an autonomous coding agent that works as a VS Code extension.

### Step-by-Step Configuration

1. **Install Cline Extension**
	- Open VS Code
	- Go to Extensions (`Cmd/Ctrl + Shift + X`)
	- Search for "Cline" and install it
2. **Open Cline Settings**
	- Click the Cline icon in the Activity Bar
	- Or press `Cmd/Ctrl + Shift + P` and search "Cline: Open"
3. **Configure API Settings**
	- In the Cline panel, click the ⚙️ icon (Settings)
	- Select **OpenAI Compatible** as the API Provider
4. **Enter Poe Configuration**
	```markdown
	API Provider: OpenAI Compatible
	Base URL: https://api.poe.com/v1/
	OpenAI Compatible API Key: [Your Poe API Key from poe.com/api_key]
	Model ID: Claude-Sonnet-4
	```
	Recommended models:
	- Claude-Sonnet-4
	- Claude-Opus-4
	- Gemini-2.5-Pro
5. **Model Configuration**
	- Cline supports: images, browser use
	- Cline does not support prompt caching
	- Optional: You can use different models for Plan and Act modes
6. **Verify Setup**
	- Start a new conversation with Cline
	- Give it a simple coding task to test

### Usage Tips for Cline

- Cline uses complex prompts and works best with Claude models
- Cline can read, write, and execute code autonomously
- It works best with specific, well-defined tasks
- Always review code changes before accepting them

---

## Roo Code Setup

Roo Code is an AI coding assistant that integrates with various development environments.

### Step-by-Step Configuration

1. **Install Roo Code**
	- Install Roo Code for your preferred development environment
2. **Access Settings**
	- Click the Roo Code icon in your editor
	- Click the ⚙️ icon (Settings) to open the configuration panel
	- Navigate to the **Providers** section
3. **Configure API Provider**
	- Select **OpenAI Compatible** from the API Provider dropdown
4. **Enter Poe Configuration**
	```markdown
	Base URL: https://api.poe.com/v1/
	API Key: [Your Poe API Key from poe.com/api_key]
	Model: [Select a model like Claude-Sonnet-4]
	```
	Recommended models:
	- Claude-Sonnet-4
	- Claude-Opus-4
	- Gemini-2.5-Pro
5. **Optional Settings**
	- Enable streaming for real-time responses
	- Include max output tokens if needed
	- Set Context Window Size (e.g., 128000)
	- Configure other settings based on your needs
6. **Test Connection**
	- Start a new conversation to confirm setup

### Usage Tips for Roo Code

- Roo Code works best with gpt-4o for general coding tasks
- Some models support images, check the "Image Support" indicator
- Note that Poe models may not support computer use or prompt caching
- Experiment with different models for different tasks

---

## LLM (Command Line Tool) Setup

[LLM](https://llm.datasette.io/en/stable/setup.html) is a command-line tool for working with Large Language Models. It provides a simple way to prompt various AI models directly from your terminal.

### Step-by-Step Configuration

1. **Install LLM**
	Choose one of the following installation methods:
2. **Configure Poe API Key**
	Set your Poe API key using LLM's key management:
	```bash
	llm keys set poe
	# Enter your Poe API key when prompted
	```
	Alternatively, use an environment variable:
	```bash
	export POE_API_KEY='your_poe_api_key_here'
	```
3. **Test Basic Setup**
	Try a simple prompt to verify the setup:
	```bash
	# Using stored key
	llm "Hello, world!" --key poe --api-base https://api.poe.com/v1
	# Using environment variable
	llm "Hello, world!" --key $POE_API_KEY --api-base https://api.poe.com/v1
	```
4. **Create Model Aliases**
	For easier access, create aliases for your favorite Poe models:
	```bash
	# Set Claude Sonnet 4 as default
	llm models default claude-sonnet-4 --api-base https://api.poe.com/v1 --key poe
	# Or create specific aliases
	llm alias claude "Claude-Sonnet-4" --api-base https://api.poe.com/v1 --key poe
	llm alias gpt4 "GPT-4o" --api-base https://api.poe.com/v1 --key poe
	```
5. **Configuration File Setup**
	For persistent configuration, you can set up a configuration file. The config location varies by OS:
	- **macOS**: `~/Library/Application Support/io.datasette.llm/`
	- **Linux**: `~/.config/io.datasette.llm/`
	Create or edit the configuration to include Poe settings.

### Usage Examples

**Basic prompting:**

```bash
# Simple prompt with specific model
llm "Explain quantum computing" -m Claude-Sonnet-4 --api-base https://api.poe.com/v1 --key poe

# Using alias (if configured)
llm "Write a Python function to calculate fibonacci" -m claude
```

**Interactive chat:**

```bash
# Start an interactive session
llm chat -m GPT-4o --api-base https://api.poe.com/v1 --key poe
```

**File input:**

```bash
# Process a file
cat mycode.py | llm "Review this code for bugs" -m Claude-Sonnet-4 --api-base https://api.poe.com/v1 --key poe

# Save conversation to file
llm "Explain machine learning" -m Gemini-2.5-Pro --api-base https://api.poe.com/v1 --key poe > explanation.txt
```

**Using templates:**

```bash
# Create a template for code review
llm template code-review "Review this code and suggest improvements: {code}"

# Use the template
llm -t code-review -v code "$(cat script.py)" -m Claude-Sonnet-4 --api-base https://api.poe.com/v1 --key poe
```

### Environment Setup

For convenience, you can set these environment variables in your shell profile:

```bash
# Add to ~/.bashrc, ~/.zshrc, or equivalent
export POE_API_KEY='your_poe_api_key_here'
export LLM_API_BASE='https://api.poe.com/v1'

# Create aliases for common commands
alias llm-poe='llm --api-base $LLM_API_BASE --key $POE_API_KEY'
alias llm-claude='llm -m Claude-Sonnet-4 --api-base $LLM_API_BASE --key $POE_API_KEY'
alias llm-gpt='llm -m GPT-4o --api-base $LLM_API_BASE --key $POE_API_KEY'
```

### Usage Tips for LLM

- **Logging**: LLM automatically logs conversations to SQLite. Use `llm logs off` to disable or `llm logs on` to enable
- **Multiple Models**: Easily switch between Poe models using the `-m` flag
- **Streaming**: LLM supports streaming responses for real-time output
- **Plugins**: Extend functionality with LLM plugins for specialized tasks
- **Templates**: Create reusable prompt templates for common workflows
- **Pipes**: LLM works great with Unix pipes for processing files and command output

### Advanced Configuration

**Custom model configuration:**

```bash
# List available models from Poe
curl -H "Authorization: Bearer $POE_API_KEY" https://api.poe.com/v1/models

# Use any model from the list
llm "Your prompt here" -m "Llama-3.1-405B" --api-base https://api.poe.com/v1 --key poe
```

**Batch processing:**

```bash
# Process multiple prompts from a file
while IFS= read -r prompt; do
  echo "Prompt: $prompt"
  llm "$prompt" -m Claude-Sonnet-4 --api-base https://api.poe.com/v1 --key poe
  echo "---"
done < prompts.txt
```

---

## Troubleshooting

### Common Issues

**"Invalid API Key" Error**

- Verify your API key from [poe.com/api\_key](https://poe.com/api_key)
- Ensure there are no extra spaces or characters
- Check that your Poe subscription is active

**"Model Not Found" Error**

- Verify the model name is spelled correctly
- Use exact model names like `Claude-Sonnet-4` (model names are case-insensitive, but avoid including space characters)
- Check if the model is available with your subscription

**Connection Timeout**

- Verify the base URL: `https://api.poe.com/v1`
- Check your internet connection
- Try a different model if one seems unresponsive

**Rate Limiting**

- Poe has a 500 requests per minute limit
- Wait a moment before retrying
- Consider upgrading your subscription for higher limits

### Getting Help

- **Poe API Documentation**: [OpenAI Compatible API docs](https://creator.poe.com/docs/external-applications/openai-compatible-api)
- **Support**: Contact [developers@poe.com](https://creator.poe.com/docs/external-applications/)
- **Community**: Join discussion on [discord](https://discord.com/invite/joinpoe)

---

## Benefits of Using Poe API

- **Single API Key**: Access hundreds of models with one key
- **Cost Effective**: Use existing Poe subscription points
- **Model Variety**: Switch between different providers and models
- **Up-to-date Models**: Access the latest models as they're released
- **Reliable Infrastructure**: Built for scale and performance


