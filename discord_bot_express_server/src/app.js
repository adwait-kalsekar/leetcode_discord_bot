const express = require('express');

const app = express();

// External API URL
LEETCODE_PROBLEMS_URL = 'https://leetcode.com/api/problems/all';

// MongoDB Config
const dbName = process.env.DB_NAME;
const collectionName = process.env.COLLECTION_NAME;

// Route to fetch data from external API and upload to MongoDB
app.get('/fetch-and-upload', async (req, res) => {
  try {
    // Delete existing records
    await collection.deleteMany({});

    // Fetch data from the external API
    const response = await axios.get(LEETCODE_PROBLEMS_URL);
    const data = response.data;

    // Upload data to MongoDB
    const result = await collection.insertMany(data.stat_status_pairs);

    res.send(`${result.insertedCount} documents inserted into MongoDB`);
  } catch (error) {
    console.error(
      'Error fetching data from external API or uploading to MongoDB:'
    );
    res.status(500).send('Internal Server Error');
  }
});

module.exports = { app };
