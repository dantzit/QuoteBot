require('dotenv').config();
const express = require('express');
const OpenAI = require('openai');

const app = express();
const port = process.env.PORT || 3000;

// Initialize OpenAI client
const openai = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY,
});

// Middleware to parse JSON bodies
app.use(express.json());

// Health check endpoint
app.get('/', (req, res) => {
  res.json({ status: 'ok', message: 'QuoteBot API is running' });
});

// OpenAI API endpoint
app.post('/api/chat', async (req, res) => {
  try {
    const { message, model = 'gpt-4o-mini' } = req.body;

    if (!message) {
      return res.status(400).json({ error: 'Message is required' });
    }

    // Load your nightly thoughts as examples
    const fs = require('fs');
    const path = require('path');
    const data = JSON.parse(fs.readFileSync(path.join(__dirname, 'combined_transcriptions.json')));

    const examples = Object.values(data).slice(0, 10).join('\n\n');

    // Call OpenAI API
    const completion = await openai.chat.completions.create({
      model,
      messages: [
        { role: 'system', content: 'You are a calm and inspiring assistant that writes short, reflective nightly thoughts. Each response should feel personal, wise, and written in a minimalist, human tone.' },
        { role: 'user', content: `Here are example nightly thoughts:\n\n${examples}\n\nNow, write one new nightly thought inspired by these.` },
      ],
    });

    const response = completion.choices[0].message.content;

    res.json({
      success: true,
      response,
      model,
    });
  } catch (error) {
    console.error('Error calling OpenAI API:', error);
    res.status(500).json({ error: error.message });
  }
});


app.listen(port, () => {
  console.log(`QuoteBot server listening on port ${port}`);
});
