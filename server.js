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

    if (!process.env.OPENAI_API_KEY) {
      return res.status(500).json({ error: 'OpenAI API key not configured' });
    }

    // Call OpenAI API
    const completion = await openai.chat.completions.create({
      model: model,
      messages: [{ role: 'user', content: message }],
    });

    const response = completion.choices[0].message.content;

    res.json({
      success: true,
      response: response,
      model: model,
    });
  } catch (error) {
    console.error('Error calling OpenAI API:', error);
    res.status(500).json({
      error: 'Failed to get response from OpenAI',
      details: error.message,
    });
  }
});

app.listen(port, () => {
  console.log(`QuoteBot server listening on port ${port}`);
});
