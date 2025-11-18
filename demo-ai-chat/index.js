require('dotenv').config();
const express = require('express');
const axios = require('axios');
const { OpenAI } = require('openai');

const app = express();
app.use(express.json());

const openai = new OpenAI({ apiKey: process.env.OPENAI_API_KEY });

app.post('/chat', async (req, res) => {
  const userPrompt = req.body.prompt;

  // Step 1: Inspect prompt with Cisco AI Defense
  try {
    const inspection = await axios.post(process.env.CISCO_AI_DEFENSE_ENDPOINT, {
      prompt: userPrompt
    }, {
      headers: { Authorization: `Bearer ${process.env.CISCO_API_KEY}` }
    });

    if (inspection.data.status !== 'approved') {
      return res.status(400).json({ error: 'Prompt rejected by Cisco AI Defense' });
    }
  } catch (error) {
    return res.status(500).json({ error: 'Cisco inspection failed', details: error.message });
  }

  // Step 2: Send prompt to OpenAI
  try {
    const response = await openai.chat.completions.create({
      model: 'gpt-4',
      messages: [{ role: 'user', content: userPrompt }]
    });
    res.json({ reply: response.choices[0].message.content });
  } catch (error) {
    res.status(500).json({ error: 'OpenAI request failed', details: error.message });
  }
});

app.listen(3000, () => console.log('Server running on port 3000'));
