const express = require('express');
const { MongoClient } = require('mongodb');
const axios = require('axios');
const { generateHint, generateSolution } = require('./utils/gemini_api.js');
require('dotenv').config();

const app = express();

// External API URL
LEETCODE_PROBLEMS_URL = process.env.LEETCODE_PROBLEMS_URL;

const port = 3000;

// MongoDB connection details
const mongoURI = process.env.MONGODB_URI;
const dbName = process.env.DB_NAME;
const questionCollectionName = process.env.QUESTION_COLLECTION;
const userCollectionName = process.env.USERS_COLLECTION;

// Connect to MongoDB
MongoClient.connect(mongoURI)
  .then((client) => {
    console.log('Connected to MongoDB');
    const db = client.db(dbName);
    const questionCollection = db.collection(questionCollectionName);
    const userCollection = db.collection(userCollectionName);

    app.get('/fetch-and-upload', async (req, res) => {
      try {
        // Delete existing records
        await questionCollection.deleteMany({});

        // Fetch data from the external API
        const response = await axios.get(LEETCODE_PROBLEMS_URL);
        const data = response.data;

        // Upload data to MongoDB
        const result = await questionCollection.insertMany(
          data.stat_status_pairs
        );

        res.status(201).json({
          message: `${result.insertedCount} documents inserted into MongoDB`,
        });
      } catch (error) {
        console.error(
          'Error fetching data from external API or uploading to MongoDB:'
        );
        res.status(500).json({ message: 'Internal Server Error' });
      }
    });

    app.get('/leetcode-problem', async (req, res) => {
      try {
        documents = await questionCollection.find({}).toArray();
        res.json(documents);
      } catch (error) {
        console.error('Error fetching data from MongoDB:');
        res.status(500).json({ message: 'Internal Server Error' });
      }
    });

    app.get('/random-problem', async (req, res) => {
      try {
        const { premium, premium_only, difficulty, username } = req.query;

        if (!username) {
          return res.status(400).json({
            message: 'No user',
          });
        }

        console.log(premium, premium_only, difficulty);

        let userFromDb = await userCollection.findOne({
          username,
        });

        if (!userFromDb) {
          userFromDb = await userCollection.insertOne({
            username,
            created_at: new Date(),
            asked: 0,
            solved: 0,
          });
        }

        await userCollection.updateOne(
          { username },
          {
            $set: {
              asked: userFromDb.asked + 1,
              created_at: new Date(),
            },
          }
        );

        let pipeline;

        let filterCriteria = {
          paid_only: false,
        };

        if (premium === 'true') {
          filterCriteria = {};
        }

        if (premium_only === 'true') {
          // Filter criteria
          filterCriteria = {
            paid_only: true,
          };
        }

        if (difficulty === 'easy') {
          filterCriteria = {
            ...filterCriteria,
            'difficulty.level': 1,
          };
        } else if (difficulty === 'medium') {
          filterCriteria = {
            ...filterCriteria,
            'difficulty.level': 2,
          };
        } else if (difficulty === 'hard') {
          filterCriteria = {
            ...filterCriteria,
            'difficulty.level': 3,
          };
        } else if (difficulty === 'easy_medium') {
          filterCriteria = {
            ...filterCriteria,
            'difficulty.level': { $in: [1, 2] },
          };
        } else if (difficulty === 'easy_hard') {
          filterCriteria = {
            ...filterCriteria,
            'difficulty.level': { $in: [1, 3] },
          };
        } else if (difficulty === 'medium_hard') {
          filterCriteria = {
            ...filterCriteria,
            'difficulty.level': { $in: [2, 3] },
          };
        }

        pipeline = [
          { $match: filterCriteria }, // Match documents based on filter criteria
          { $sample: { size: 1 } }, // Randomly select one document
        ];

        // Perform aggregation to get one random element
        const randomQuestion = await questionCollection
          .aggregate(pipeline)
          .toArray();

        res.status(200).json(randomQuestion[0]);
      } catch (error) {
        console.error('Error fetching data from MongoDB:', error);
        res.status(500).json({ message: 'Internal Server Error' });
      }
    });

    app.get('/fetch-filtered', async (req, res) => {
      try {
        // Filter criteria
        const filterCriteria = {
          'stat.is_new_question': false,
        };

        // Find documents matching the filter criteria
        const documents = await questionCollection
          .find(filterCriteria)
          .toArray();
        res.send(documents);
      } catch (error) {
        console.error('Error fetching data from MongoDB:', error);
        res.status(500).json({ message: 'Internal Server Error' });
      }
    });

    app.get('/get-hint', async (req, res) => {
      try {
        const slug = req.query.slug;
        if (!slug) {
          return res.status(404).json({
            message: 'Please provide a slug',
          });
        }

        const filterCriteria = {
          'stat.question__title_slug': slug,
        };

        // Find documents matching the slug
        const document = await questionCollection.findOne(filterCriteria);

        if (!document) {
          return res.status(404).json({
            message: 'Slug not found',
          });
        }

        const url = `https://leetcode.com/problems/${slug}/description`;

        const result = await generateHint(url);
        console.log('Result: ', result);

        res.status(200).json({
          title: document.stat.question__title,
          slug,
          result,
        });
      } catch (error) {
        console.error('Error fetching data from MongoDB:', error);
        res.status(500).json({ message: 'Internal Server Error' });
      }
    });

    app.get('/get-solution', async (req, res) => {
      try {
        const { slug, language } = req.query;
        if (!slug) {
          return res.status(404).json({
            message: 'Please provide a slug',
          });
        }

        const filterCriteria = {
          'stat.question__title_slug': slug,
        };

        // Find documents matching the slug
        const document = await questionCollection.findOne(filterCriteria);

        if (!document) {
          return res.status(404).json({
            message: 'Slug not found',
          });
        }

        const url = `https://leetcode.com/problems/${slug}/description`;

        const result = await generateSolution(url, language);
        console.log('Result: ', result);

        res.status(200).json({
          title: document.stat.question__title,
          slug,
          result,
        });
      } catch (error) {
        console.error('Error fetching data from MongoDB:', error);
        res.status(500).json({ message: 'Internal Server Error' });
      }
    });

    app.get('/get-stats', async (req, res) => {
      try {
        const { username } = req.query;

        if (!username) {
          return res.status(400).json({
            message: 'No user',
          });
        }

        let userFromDb = await userCollection.findOne({
          username,
        });

        if (!userFromDb) {
          return res.status(404).json({
            message: 'No User Found',
          });
        }

        res.status(200).json(userFromDb);
      } catch (error) {
        console.error('Error fetching data from MongoDB:', error);
        res.status(500).json({ message: 'Internal Server Error' });
      }
    });

    app.get('/add-solved', async (req, res) => {
      try {
        const { username } = req.query;

        if (!username) {
          return res.status(400).json({
            message: 'No user',
          });
        }

        let userFromDb = await userCollection.findOne({
          username,
        });

        if (!userFromDb) {
          return res.status(404).json({
            message: 'No User Found',
          });
        }

        await userCollection.updateOne(
          { username },
          {
            $set: {
              solved: userFromDb.solved + 1,
              created_at: new Date(),
            },
          }
        );

        userFromDb = await userCollection.findOne({
          username,
        });

        res.status(200).json(userFromDb);
      } catch (error) {
        console.error('Error fetching data from MongoDB:', error);
        res.status(500).json({ message: 'Internal Server Error' });
      }
    });

    app.get('/get-users', async (req, res) => {
      try {
        let usersFromDb = await userCollection.find({}).toArray();

        if (!usersFromDb) {
          return res.status(404).json({
            message: 'No Users Found',
          });
        }

        res.status(200).json(usersFromDb);
      } catch (error) {
        console.error('Error fetching data from MongoDB:', error);
        res.status(500).json({ message: 'Internal Server Error' });
      }
    });

    app.listen(port, () => {
      console.log(`Server running on http://localhost:${port}`);
    });
  })
  .catch((error) => console.error('Error connecting to MongoDB:'));
