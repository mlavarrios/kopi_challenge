# Kopi API

### This is an API for debating with an AI chatbot, created as a challenge for Kavak Kopiloto.
Feel free trying to prove your most wild, controversial point, Kopi will answer with facts why you are wrong.

## Endpoint `/chat`

Request
```
{
    "conversation_id": "text" | null,
    "message": "text"
}
```
Response
```
{
    "conversation_id": "text",
    // history of the 5 most recent messages on both sides. most recent message last
    "message": [
        {
            "role": "user",
            "message": "text"
        },
        {
            "role": "bot",
            "message": "text"
        }
    ]
}
```

## Requirements

- Docker Desktop (or Docker Engine)
- Node.js (for local supabase instance)
- API key for Gemini (no local LLM hosting)

## Quick Start

1. **Clone the repository**
   ```bash
   git clone https://github.com/mlavarrios/kopi_challenge.git
   cd kopi
   ```
2. **Copy and edit configuration**
   ```bash
   cp src/application.ini.example src/application.ini
   # Edit src/application.ini with your settings, check Configuration Reference for the required values
   ```
3. **Check software requirements and install dependencies**
   ```bash
   make install
   # This checks for Docker and Node.js
   ```
4. **Start the service**
   ```bash
   make run
   ```
5. **Run tests**
   ```bash
   make test
   # The containers must be up, so be sure to run 'make run' before running tests
   ```

## Configuration Reference

These are the values required in your `src/application.ini`

### Supabase Section

**supabase_url**  
The URL of your Supabase project. (When using Docker Desktop `http://host.docker.internal:54321`, if you have problems with other Docker engines try changing it to `http://localhost:54321`)

**supabase_key**  
The API key for accessing your Supabase services.
Already in the `src/application.ini.example`, but if it changes, it is displayed when doing `make run` in the value `service_role key:`

---

### Gemini Section

**gemini_api_key**  
The API key for accessing the Gemini AI model (Google GenAI).  
Required for generating AI responses.
- If you need an API key, message me and I will share it with you, can't upload it here.