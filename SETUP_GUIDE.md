# AI Chat Application - Complete Setup Guide

## Overview
This guide explains how to set up and configure the demo-ai-chat application from scratch. This is a web-based chatbot that uses OpenAI's ChatGPT with security checks through Cisco AI Defense.

---

## Table of Contents
1. [Project Architecture](#project-architecture)
2. [Configuration Files Explained](#configuration-files-explained)
3. [Step-by-Step Setup](#step-by-step-setup)
4. [How Everything Works Together](#how-everything-works-together)
5. [Troubleshooting](#troubleshooting)

---

## Project Architecture

### What This App Does
```
User (Browser) 
    ↓
    → Beautiful Chat UI (HTML/CSS/JavaScript)
    ↓
Express Server (Node.js)
    ↓
    → Cisco AI Defense (Security Check)
    ↓
    → OpenAI ChatGPT (AI Response Generation)
    ↓
Response back to User
```

### Project Structure
```
demo-ai-chat/
├── index.js                 # Main server file
├── package.json             # Project dependencies
├── .env                     # Environment variables (API keys)
├── public/
│   └── index.html          # Chat UI interface
├── node_modules/           # Installed packages
└── README.md               # Project documentation
```

---

## Configuration Files Explained

### 1. **package.json** - Project Metadata & Dependencies
**Location:** `/workspaces/demo-ai-chat/demo-ai-chat/package.json`

**What it does:**
- Defines project name, version, and description
- Lists all required libraries (dependencies)
- Defines scripts to run the application

**Key dependencies explained:**
```json
{
  "dependencies": {
    "express": "^5.1.0",        // Web server framework
    "axios": "^1.13.2",         // HTTP client for API calls
    "dotenv": "^17.2.3",        // Loads environment variables
    "openai": "^6.9.1"          // OpenAI API client
  },
  "scripts": {
    "start": "node index.js"    // Command to start the app
  }
}
```

**Why it matters:**
- Without dependencies listed here, the app won't have the libraries it needs
- `npm install` reads this file and downloads all required packages

---

### 2. **.env** - Sensitive Configuration (API Keys)
**Location:** `/workspaces/demo-ai-chat/demo-ai-chat/.env`

**What it does:**
- Stores sensitive information (API keys, endpoints)
- Never committed to Git (for security)
- Loaded at application startup

**Structure:**
```env
OPENAI_API_KEY=sk-proj-xxxxxx...
CISCO_AI_DEFENSE_ENDPOINT=https://us-west.ciscoaidefense.com/api/v1/inspect
CISCO_API_KEY=485a4380d4af...
```

**Each variable explained:**

| Variable | Purpose | Example |
|----------|---------|---------|
| `OPENAI_API_KEY` | Authentication token for OpenAI API | `sk-proj-...` (from platform.openai.com) |
| `CISCO_AI_DEFENSE_ENDPOINT` | URL to Cisco's security service | `https://us-west.ciscoaidefense.com/api/v1/inspect` |
| `CISCO_API_KEY` | Authentication for Cisco service | `485a4380d4af...` (from Cisco console) |

**Security note:**
- Never share these keys
- Never commit `.env` to version control
- `.gitignore` prevents accidental commits

---

### 3. **index.js** - Main Application Code
**Location:** `/workspaces/demo-ai-chat/demo-ai-chat/index.js`

**What it does:**
- Sets up the Express web server
- Defines API endpoints
- Handles request/response flow

**Key sections:**

#### Imports & Setup
```javascript
require('dotenv').config();              // Load .env variables
const express = require('express');      // Web server
const axios = require('axios');          // HTTP requests
const { OpenAI } = require('openai');    // OpenAI API

const app = express();                   // Create app instance
app.use(express.json());                 // Parse JSON requests
```

#### Serve Chat UI
```javascript
app.use(express.static(path.join(__dirname, 'public')));

app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'index.html'));
});
```
- When user visits `/`, serves the chat interface

#### Chat Endpoint
```javascript
app.post('/chat', async (req, res) => {
  const userPrompt = req.body.prompt;    // Get user message
  
  // Step 1: Cisco inspection
  // Step 2: OpenAI response
});
```

#### Start Server
```javascript
app.listen(3000, () => console.log('Server running on port 3000'));
```
- Listens on port 3000 (local) or forwarded port (Codespaces)

---

### 4. **public/index.html** - Chat User Interface
**Location:** `/workspaces/demo-ai-chat/demo-ai-chat/public/index.html`

**What it does:**
- Provides the beautiful chat interface users see
- Sends/receives messages via JavaScript

**Key features:**
- Modern gradient design (purple theme)
- Real-time message display
- Typing indicator animation
- Error handling
- Responsive mobile design

**How it works:**
1. User types message and clicks Send
2. JavaScript sends POST request to `/chat` endpoint
3. Waits for response from server
4. Displays AI response in chat

---

## Step-by-Step Setup

### Step 0: Prerequisites
You need:
- GitHub Codespaces environment (already set up)
- Node.js installed (comes with Codespaces)
- OpenAI API key (free to create)
- Cisco AI Defense credentials (optional for testing)

### Step 1: Get OpenAI API Key

**What:** Authentication to access ChatGPT

**Steps:**
1. Go to https://platform.openai.com/api-keys
2. Sign in with your OpenAI account (create one if needed)
3. Click "Create new secret key"
4. Copy the key (starts with `sk-proj-`)
5. **Keep this safe** - never share it

**Why:** OpenAI needs to authenticate you and track your usage

---

### Step 2: Get Cisco AI Defense Credentials (Optional)

**What:** Security layer to scan prompts for harmful content

**Steps:**
1. Go to https://www.cisco.com/site/us/en/products/security/cloud-security/ai-defense/
2. Sign up for a trial account
3. Get your API endpoint and key from the console
4. Note the regional endpoint (e.g., `us-west`, `us-east`)

**Why:** Protects against malicious prompts before they reach OpenAI

---

### Step 3: Create .env File

**What:** File that stores your API keys securely

**Steps:**
1. Create a new file: `/workspaces/demo-ai-chat/demo-ai-chat/.env`
2. Add the following:

```env
OPENAI_API_KEY=sk-proj-your_key_here
CISCO_AI_DEFENSE_ENDPOINT=https://us-west.ciscoaidefense.com/api/v1/inspect
CISCO_API_KEY=your_cisco_key_here
```

3. Replace:
   - `sk-proj-your_key_here` with your actual OpenAI key
   - `your_cisco_key_here` with your Cisco key
   - Change `us-west` to your region if needed

**Why:** These variables are loaded by `dotenv` package and made available to the app

---

### Step 4: Install Dependencies

**What:** Download all required libraries

**Command:**
```bash
cd /workspaces/demo-ai-chat/demo-ai-chat
npm install
```

**What happens:**
- `npm` reads `package.json`
- Downloads each dependency and its sub-dependencies
- Creates `node_modules/` folder
- Creates `package-lock.json` (exact versions used)

**Why:** Your app needs libraries to run (Express, OpenAI SDK, etc.)

---

### Step 5: Start the Server

**Command:**
```bash
npm start
```

**What happens:**
- Runs `node index.js` (defined in package.json)
- Server starts listening on port 3000
- You see: "Server running on port 3000"

**Why:** The server needs to be running to accept requests from the browser

---

### Step 6: Access the App

**In GitHub Codespaces:**
1. Look for port 3000 in the "Ports" tab
2. Click the globe icon to open the forwarded URL
3. You'll see the chat interface

**Locally (if running on your machine):**
```
http://localhost:3000
```

---

## How Everything Works Together

### Complete Request Flow

```
1. USER ACTION
   └─ User types message in chat box
   └─ Clicks "Send" button
      ↓
2. BROWSER (JavaScript)
   └─ Sends POST request to /chat endpoint
   └─ Includes user prompt in request body
      ↓
3. EXPRESS SERVER (index.js)
   └─ Receives request on /chat endpoint
   └─ Extracts user prompt
      ↓
4. CISCO AI DEFENSE CHECK
   └─ Sends prompt to Cisco's API
   └─ Cisco analyzes for malicious content
   └─ Returns "approved" or "rejected"
   └─ If rejected: Return error to user
      ↓
5. OPENAI CHATGPT
   └─ Sends approved prompt to OpenAI
   └─ OpenAI generates AI response
   └─ Returns response text
      ↓
6. EXPRESS RETURNS RESPONSE
   └─ Formats response as JSON
   └─ Sends back to browser
      ↓
7. BROWSER DISPLAYS RESPONSE
   └─ JavaScript receives response
   └─ Displays AI message in chat
   └─ User sees the answer
```

### Request/Response Format

**User sends to `/chat` endpoint:**
```json
{
  "prompt": "What is machine learning?"
}
```

**Server checks with Cisco:**
```json
{
  "prompt": "What is machine learning?",
  "status": "approved"  // or "rejected"
}
```

**Server sends to OpenAI:**
```json
{
  "model": "gpt-4-turbo",
  "messages": [
    {
      "role": "user",
      "content": "What is machine learning?"
    }
  ]
}
```

**Server returns to browser:**
```json
{
  "reply": "Machine learning is a subset of artificial intelligence that enables systems to learn and improve from experience..."
}
```

---

## Configuration Decisions Made

### 1. Using Express.js
**Why:** 
- Simple and lightweight
- Perfect for REST APIs
- Large community support

### 2. Using OpenAI API
**Why:**
- State-of-the-art AI models (ChatGPT)
- Easy to integrate
- Reliable and scalable

### 3. Using Cisco AI Defense
**Why:**
- Enterprise-grade security
- Prevents harmful prompt injections
- Compliance with security policies

### 4. Using gpt-4-turbo Model
**Why:**
- Most advanced ChatGPT model
- Better at reasoning and complex tasks
- Falls back to gpt-3.5-turbo if unavailable

### 5. Port 3000
**Why:**
- Standard for Node.js development
- Easy to remember
- Doesn't conflict with system ports

---

## Enabling/Disabling Cisco Inspection

### To Enable (Mandatory Check)
The code currently has Cisco inspection enabled. All prompts must pass the security check before reaching OpenAI.

### To Disable (For Development Only)
If you don't have Cisco credentials yet, comment out the Cisco section in `index.js`:

```javascript
/*
try {
  const inspection = await axios.post(process.env.CISCO_AI_DEFENSE_ENDPOINT, {
    prompt: userPrompt
  }, ...);
  // ... rest of Cisco code
}
*/
```

Then prompts go directly to OpenAI without security check.

---

## Environment Variables Summary

| Variable | Required | Source | Purpose |
|----------|----------|--------|---------|
| `OPENAI_API_KEY` | Yes | OpenAI Platform | Access ChatGPT |
| `CISCO_AI_DEFENSE_ENDPOINT` | No (Optional) | Cisco Console | Security check URL |
| `CISCO_API_KEY` | No (Optional) | Cisco Console | Cisco authentication |

---

## Troubleshooting

### Issue: "Cannot GET /"
**Cause:** Server not running or wrong port
**Solution:** 
- Run `npm start`
- Check that it says "Server running on port 3000"
- Refresh browser

### Issue: "OpenAI request failed"
**Cause:** Invalid API key
**Solution:**
- Check your OpenAI API key in `.env`
- Verify it starts with `sk-proj-`
- Get a new key from platform.openai.com

### Issue: "Model gpt-4 does not exist"
**Cause:** Your account doesn't have access to gpt-4
**Solution:**
- Code automatically falls back to gpt-3.5-turbo
- This is normal - both work great

### Issue: "Cisco inspection failed"
**Cause:** Invalid Cisco credentials or no internet
**Solution:**
- Verify Cisco endpoint and key in `.env`
- Check your Cisco account is active
- Comment out Cisco section for development

### Issue: Port 3000 already in use
**Cause:** Another app is using the port
**Solution:**
- Kill the process: `lsof -ti:3000 | xargs kill -9`
- Or change port in `index.js`: `app.listen(3001, ...)`

---

## What's Next?

### To Improve the App:
1. **Add authentication** - Login/logout for users
2. **Store chat history** - Database to save conversations
3. **User profiles** - Different settings per user
4. **Streaming responses** - Real-time text as it's generated
5. **File uploads** - Users can chat about documents
6. **Rate limiting** - Prevent API abuse

### To Deploy:
1. **Use a hosting service** - Heroku, Railway, Vercel
2. **Add environment variables** - Store secrets on hosting platform
3. **Use HTTPS** - Encrypt all traffic
4. **Add monitoring** - Track errors and usage

---

## Key Takeaways

✅ **Configuration files tell the app:**
- How to run (package.json)
- Where to find secrets (.env)
- What services to use (index.js)

✅ **API keys are sensitive:**
- Never commit to Git
- Never share publicly
- Use .env files

✅ **The app follows a simple flow:**
- Request → Validate → Process → Response

✅ **Cisco + OpenAI = Secure AI:**
- Cisco checks for threats
- OpenAI generates responses
- User gets safe, intelligent answers

---

## Glossary

| Term | Meaning |
|------|---------|
| **API** | Application Programming Interface - way apps communicate |
| **Express** | Web server framework for Node.js |
| **Endpoint** | URL where server accepts requests (e.g., `/chat`) |
| **Authentication** | Proving who you are with credentials |
| **Payload** | Data sent in a request |
| **Response** | Data returned by server |
| **Environment Variable** | Configuration stored in .env file |
| **Dependency** | External library your app needs |
| **Port** | Virtual connection point (e.g., 3000) |
| **Localhost** | Your computer (127.0.0.1) |
| **Codespaces** | GitHub's cloud development environment |

---

## Support & Resources

- **OpenAI Docs:** https://platform.openai.com/docs
- **Express.js Docs:** https://expressjs.com
- **Cisco AI Defense:** https://www.cisco.com/site/us/en/products/security/cloud-security/ai-defense/
- **Node.js Docs:** https://nodejs.org/docs

