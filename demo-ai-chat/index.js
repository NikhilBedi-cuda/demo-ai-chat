require('dotenv').config();
const express = require('express');
const axios = require('axios');
const path = require('path');
const { OpenAI } = require('openai');

const app = express();
app.use(express.json());

// Serve static files from public directory
app.use(express.static(path.join(__dirname, 'public')));

const openai = new OpenAI({ apiKey: process.env.OPENAI_API_KEY });

// Validate configuration on startup
if (!process.env.OPENAI_API_KEY) {
  console.error('ERROR: OPENAI_API_KEY is not set in .env file');
}
if (!process.env.CISCO_AI_DEFENSE_ENDPOINT) {
  console.error('ERROR: CISCO_AI_DEFENSE_ENDPOINT is not set in .env file');
}
if (!process.env.CISCO_API_KEY) {
  console.error('ERROR: CISCO_API_KEY is not set in .env file');
}

app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

app.post('/chat', async (req, res) => {
  const userPrompt = req.body.prompt;

  // Step 1: Inspect prompt with Cisco AI Defense (MANDATORY)
  try {
    const inspection = await axios.post(process.env.CISCO_AI_DEFENSE_ENDPOINT, {
      prompt: userPrompt
    }, {
      headers: { Authorization: `Bearer ${process.env.CISCO_API_KEY}` },
      timeout: 5000
    });

    if (inspection.data.status !== 'approved') {
      return res.status(400).json({ error: 'Prompt rejected by Cisco AI Defense' });
    }
  } catch (error) {
    console.error('Cisco AI Defense inspection error:', error.message);
    return res.status(500).json({ error: 'Cisco inspection failed', details: error.message });
  }

  // Step 2: Send prompt to OpenAI (ChatGPT)
  try {
    const response = await openai.chat.completions.create({
      model: 'gpt-4-turbo',
      messages: [{ role: 'user', content: userPrompt }]
    });
    res.json({ reply: response.choices[0].message.content });
  } catch (error) {
    // Fallback to gpt-3.5-turbo if gpt-4-turbo is not available
    if (error.status === 404) {
      console.log('gpt-4-turbo not available, falling back to gpt-3.5-turbo');
      try {
        const response = await openai.chat.completions.create({
          model: 'gpt-3.5-turbo',
          messages: [{ role: 'user', content: userPrompt }]
        });
        res.json({ reply: response.choices[0].message.content });
      } catch (fallbackError) {
        console.error('OpenAI Error:', fallbackError.message);
        res.status(500).json({ 
          error: 'OpenAI request failed', 
          details: fallbackError.message
        });
      }
    } else {
      console.error('OpenAI Error:', error.message);
      console.error('Error Status:', error.status);
      console.error('Error Type:', error.type);
      res.status(500).json({ 
        error: 'OpenAI request failed', 
        details: error.message,
        type: error.type,
        status: error.status
      });
    }
  }
});

app.listen(3000, () => console.log('Server running on port 3000'));
