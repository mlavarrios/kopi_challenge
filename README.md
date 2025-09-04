# Configuration Reference
First you need to copy the example configuration file, run:

```bash
cp application.ini.example application.ini
```

This will create a new `application.ini` file in the same directory, which you can then edit with your own settings.

---

## Supabase Section

**supabase_url**  
The URL of your Supabase project (e.g., `https://xyz.supabase.co`).  
Provided by Supabase when you create a project.

**supabase_key**  
The API key for accessing your Supabase services.
Also provided when creating a project.

**supabase_table**  
The name of the table in Supabase where you want to save the messages data.

---

## Gemini Section

**gemini_api_key**  
The API key for accessing the Gemini AI model (Google GenAI).  
Required for generating AI responses.