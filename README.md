# QuoteBot

A simple backend API for making calls to OpenAI's GPT models (GPT-4o-mini).

## Setup

1. Clone the repository
2. Install dependencies:
   ```bash
   npm install
   ```
3. Create a `.env` file based on `.env.example`:
   ```bash
   cp .env.example .env
   ```
4. Add your OpenAI API key to the `.env` file:
   ```
   OPENAI_API_KEY=your_actual_api_key_here
   ```

## Running the Server

Start the server with:
```bash
npm start
```

The server will run on `http://localhost:3000` by default.

## API Endpoints

### Health Check
- **GET** `/`
- Returns server status

### Chat with GPT
- **POST** `/api/chat`
- **Body**:
  ```json
  {
    "message": "Your message here",
    "model": "gpt-4o-mini"
  }
  ```
- **Response**:
  ```json
  {
    "success": true,
    "response": "AI response here",
    "model": "gpt-4o-mini"
  }
  ```

## Example Usage

Using curl:
```bash
curl -X POST http://localhost:3000/api/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "Tell me a quote about coding"}'
```

## Environment Variables

- `OPENAI_API_KEY` - Your OpenAI API key (required)
- `PORT` - Server port (default: 3000)