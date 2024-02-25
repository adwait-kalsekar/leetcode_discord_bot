const OpenAI = require('openai');
const axios = require('axios');
require('dotenv').config();

const CHATGPT_PRO_API_KEY = process.env.CHATGPT_PRO_API_KEY;

// Replace 'your_api_key' with your actual OpenAI API key
const apiKey = process.env.CHATGPT_PRO_API_KEY;
const endpoint = 'https://api.openai.com/v1/engines/gpt-3.5-turbo/completions';

// Setup the request headers
const headers = {
  'Content-Type': 'application/json',
  Authorization: `Bearer ${apiKey}`,
};

async function generateText(slug) {
  const prompt = 'What does ' + slug + 'mean?';
  console.log('key: ', CHATGPT_PRO_API_KEY);

  // Setup the data to send
  const postData = {
    prompt: prompt,
    temperature: 0.5,
    max_tokens: 60,
    top_p: 1.0,
    frequency_penalty: 0.0,
    presence_penalty: 0.0,
  };

  // Make the POST request
  axios
    .post(endpoint, postData, { headers: headers })
    .then((response) => {
      console.log('Success:', response.data);
      return response.data;
    })
    .catch((error) => {
      console.error('Error:', error.response.data);
    });
}

module.exports = { generateText };
