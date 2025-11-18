# demo-ai-chat

A secure AI chat application that integrates OpenAI's GPT-4 with Cisco AI Defense for prompt inspection and content safety.

## Overview

This project demonstrates a production-ready chatbot API built with Node.js and Express that:
- Accepts user prompts via a REST API
- Inspects prompts using Cisco AI Defense for security and compliance
- Processes approved prompts through OpenAI's GPT-4 model
- Returns AI-generated responses in JSON format

## Features

- **Secure Prompt Inspection**: All user prompts are validated through Cisco AI Defense before processing
- **GPT-4 Integration**: Leverages OpenAI's advanced language model for intelligent responses
- **REST API**: Simple HTTP endpoints for easy integration
- **Error Handling**: Comprehensive error handling and logging for debugging
- **Environment Configuration**: Uses environment variables for sensitive credentials

## Architecture

The application consists of:
1. **Express Server**: RESTful API server running on port 3000
2. **OpenAI Integration**: Direct integration with OpenAI API for chat completions
3. **Cisco AI Defense**: Security layer for prompt validation
4. **Middleware**: JSON parsing and request handling

## Installation

1. Clone the repository:
```bash
git clone https://github.com/NikhilBedi-cuda/demo-ai-chat.git
cd demo-ai-chat
```

2. Install dependencies:
```bash
npm install
```

3. Configure environment variables by creating a `.env` file:
```
OPENAI_API_KEY=your_openai_api_key
CISCO_API_KEY=your_cisco_api_key
CISCO_AI_DEFENSE_ENDPOINT=https://your_cisco_endpoint
```

## API Endpoints

### GET /
Health check endpoint that returns the server status.

**Response:**
```json
{
  "message": "AI Chat API is running"
}
```

### POST /chat
Submit a prompt and receive an AI-generated response.

**Request Body:**
```json
{
  "prompt": "Your question or prompt here"
}
```

**Success Response (200):**
```json
{
  "reply": "AI-generated response text"
}
```

**Error Response (400):**
```json
{
  "error": "Prompt rejected by Cisco AI Defense"
}
```

**Error Response (500):**
```json
{
  "error": "OpenAI request failed",
  "details": "Error message details"
}
```

## Usage Example

Using curl:
```bash
curl -X POST http://localhost:3000/chat \
  -H "Content-Type: application/json" \
  -d '{"prompt": "What is machine learning?"}'
```

Using JavaScript/Node.js:
```javascript
const response = await fetch('http://localhost:3000/chat', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ prompt: 'Your question here' })
});
const data = await response.json();
console.log(data.reply);
```

## Security Considerations

- All prompts are validated through Cisco AI Defense before reaching the AI model
- API keys are stored in environment variables and never committed to version control
- Sensitive information is not logged
- Proper error handling prevents information leakage in error responses

## Dependencies

- **express**: Web framework for Node.js
- **axios**: HTTP client for API requests
- **openai**: Official OpenAI Node.js SDK
- **dotenv**: Environment variable management

## Running the Application

1. Start the server:
```bash
npm start
```

2. The server will output:
```
Server running on port 3000
```

3. Test the root endpoint:
```bash
curl http://localhost:3000/
```

## Error Handling

The application implements comprehensive error handling:
- Cisco AI Defense inspection failures return 500 status with details
- Rejected prompts return 400 status with rejection reason
- OpenAI API failures return 500 status with error information

## Contributing

Contributions are welcome! Please fork the repository and submit pull requests with improvements.

## License

This project is open source and available under the MIT License.

## Support

For issues, questions, or feature requests, please open an issue on GitHub.