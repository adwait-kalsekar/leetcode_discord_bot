# Discord Bot Challenge

## Problem Statement:

To design a Discord Chat bot which gives random LeetCode Problems based on user tags.

## Real world application:

The Discord chat bot offers a practical and interactive platform for users to enhance their coding skills, collaborate with peers, and stay engaged in ongoing learning and professional development endeavors. Below are the few examples:

1.  **Learning and Skill Improvement:**
    Users, especially those preparing for technical interviews or coding competitions, can use the bot to practice solving coding problems regularly.

2.  **Community Engagement and Collaboration:**
    Discord servers dedicated to coding, programming, or tech communities can integrate this bot to engage members in collaborative learning and problem-solving activities. Users can share their solutions, discuss approaches, and help each other understand different problem-solving techniques.
3.  **Remote Learning and Education:**
    In educational settings such as coding bootcamps, online courses, or programming clubs, instructors can use the bot to assign practice problems tailored to the difficulties level. This promotes active learning and provides students with additional resources to reinforce their understanding of concepts.
4.  **Motivation and Gamification:**
    Incorporating features such as leaderboards, achievement badges, or progress tracking can add a gamified element to the bot, motivating users to engage more actively with coding challenges. Users can track their progress over time and compete with friends or fellow community members, fostering a sense of achievement and healthy competition.
5.  **Continuous Learning and Reinforcement:**
    Beyond interview preparation, the bot can serve as a tool for continuous learning and skill reinforcement for software developers and programmers. Users can use the bot regularly to stay sharp, explore new problem domains, and keep up with evolving industry trends and technologies.

## Features:

This bot has several features that helps to enhance the user experience. Below are the list of features and its descriptions:

1. **Help**- Show the list of features this bot has.
2. **Hello**- Get the hello response from the bot.

3. **LeetCode Menu**- - **_LeetCode_**- Retrieve the random LeetCode problem free. - **_LeetCode Premium_** -Retrieve random LeetCode problem (Free+ premium) - **_LeetCode Premium only_** - Retrieve random premium LeetCode problem.

4. **LeetCode Options based on difficulty**-  
    - **_LeetCode Easy_**- Retrieve random LeetCode problems with an easy difficulty level. - **_LeetCode Medium_**- Retrieve random LeetCode problems with an medium difficulty level.
5. **_LeetCode Hard_**-Retrieve random LeetCode problems with an hard difficulty level.
6. **Hint**- Give a hint on how to approach a problem and present the algorithm to solve it.
7. **Code Solution**- Retrieve a complete code solution for the problem.

#### NOTE:

Users can select multiple difficulty levels like (easy-medium, easy-hard, medium-hard). Additionally, this feature offers options for solving problems based on both premium and premium-only subscriptions.

## How I built it:

- Used the discord.py library to create a discord bot in python and connected it to discord using an API key
- Created an Express server to handle all the backend tasks
- Fetched all questions data from the leetcode URL and stored in MongoDB Collection
- Added discord bot commands to query the MongoDB database and get the required question url based on some optional filters
- Added Google Gemini API to allow people to ask for hints, explanations and solutions to the coding problems
- Finally, also get user stats to see how many problems the user generated and how many total problems the user has solved

## Challenges we ran into:

- Creating the discord bot, as it was the first time
- Open AI API keys, so had to switch to Google Gemini
- No leetcode api to get certain problems, so for every filter all the questions had to be fetched and filtered on the bot
- To solve this, created a separate backend and fetched all data at once and stored in DB, and fetched from DB as required
- Building a scheduler in Discord Bot

## Accomplishments that I'm proud of

- Completed the bot with lot of custom features and a backend

## What I learned

- Learned how to build a discord bot
- Learned to use Google Gemini API

## Built With:

Python, discord.py, Node.JS, Express, Google Gemini API, MongoDB
