import discord
import asyncio
import os
import requests
import random
from datetime import datetime, timedelta
import time

# Define intents
intents = discord.Intents.default()
intents.message_content = True  # Enable member intents

# Create your Discord bot client with intents
client = discord.Client(intents=intents)

# LeetCode API endpoint for getting random problems
EXPRESS_URL = 'http://127.0.0.1:3000/'

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!hello') or message.content.startswith('!hey'):
        await message.channel.send(f'Hello {message.author}!')

    if message.content.startswith('!help'):
        await message.channel.send(embed=get_help())

    if message.content.startswith('!hint'):
        commands = message.content.split()
        print(commands)

        if len(commands) > 1:
            problem_slug = commands[1]
            embed, result = get_hint(problem_slug)
            await message.channel.send(embed=embed)
            await message.channel.send(result)
        else:
            await message.channel.send(f'Please put a valid slug value')

    if message.content.startswith('!solution'):
        commands = message.content.split()
        language = 'python'
        print(commands)

        if len(commands) > 1:
            problem_slug = commands[1]
            if len(commands) > 2:
                language = commands[2]

            embed, result = get_solution(problem_slug, language)
            await message.channel.send(embed=embed)
            await message.channel.send(result)
        else:
            await message.channel.send(f'Please put a valid slug value')

    if message.content.startswith('!leetcode'):
        commands = message.content.split()
        print(commands)

        premium = False
        premium_only = False
        difficulty = 'all'

        if 'premium_only' in commands:
            premium_only = True

        elif 'premium' in commands:
            premium = True

        if 'easy' in commands and 'medium' in commands and 'hard' in commands:
            difficulty = 'all'
        elif 'easy' in commands and 'medium' in commands:
            difficulty = 'easy_medium'
        elif 'easy' in commands and 'hard' in commands:
            difficulty = 'easy_hard'
        elif 'medium' in commands and 'hard' in commands:
            difficulty = 'medium_hard'
        elif 'easy' in commands:
            difficulty = 'easy'
        elif 'medium' in commands:
            difficulty = 'medium'
        elif 'hard' in commands:
            difficulty = 'hard'
        
        # Fetch random problem from LeetCode API
        problem = get_random_leetcode_problem(user=message.author, premium=premium, premium_only=premium_only, difficulty=difficulty)
        # Sending the problem information to the channel
        await message.channel.send(embed=problem)

    if message.content.startswith('!stats'):
        await message.channel.send(embed=get_stats(message.author))

    if message.content.startswith('!solved'):
        await message.channel.send("Added to your solved questions\n")
        await message.channel.send(embed=add_solved(message.author))


def get_help():
    embed = discord.Embed(
            title="Welcome to AD's discord bot",
            description="This bot gives you random leet code problems based on your preference",
            color=discord.Color.green()
        )
    help_text = '''
        !help: show this menu 
        \n!hello: get hello response from the bot 
    '''

    help_text_leetcode = '''
        \n!leetcode: get random leetcode problem (free)
        \n!leetcode premium: get random leetcode problem (free + premium)
        \n!leetcode premium_only: get random leetcode problem (only premium)
    '''

    help_text_leetcode_difficulty = '''
        \n!leetcode easy (optional - premium | premium_only): get random leetcode problem (easy difficulty)
        \n!leetcode medium (optional - premium | premium_only): get random leetcode problem (medium difficulty)
        \n!leetcode hard (optional - premium | premium_only): get random leetcode problem (hard difficulty)
        \n!leetcode easy_medium (optional - premium | premium_only): get random leetcode problem (easy or medium difficulty)
        \n!leetcode easy_hard (optional - premium | premium_only): get random leetcode problem (easy or hard difficulty)
        \n!leetcode medium_hard (optional - premium | premium_only): get random leetcode problem (medium or hard difficulty)
    '''

    embed.add_field(name="Help Menu", value=help_text, inline=False)
    embed.add_field(name="LeetCode Menu", value=help_text_leetcode, inline=False)
    embed.add_field(name="LeetCode Menu Based on Difficulty", value=help_text_leetcode_difficulty, inline=False)
    return embed

def get_random_leetcode_problem(user, premium=False, premium_only=False, difficulty='all'):
    random_leetcode_url = EXPRESS_URL + 'random-problem'
    if premium == True:
        random_leetcode_url = random_leetcode_url + '?premium=true'
    elif premium_only == True:
        random_leetcode_url = random_leetcode_url + '?premium_only=true'
    else:
        random_leetcode_url = random_leetcode_url + '?premium=false&premium_only=false'

    if difficulty == 'all':
        random_leetcode_url = random_leetcode_url + '&difficulty=all'
    elif difficulty == 'easy':
        random_leetcode_url = random_leetcode_url + '&difficulty=easy'
    elif difficulty == 'medium':
        random_leetcode_url = random_leetcode_url + '&difficulty=medium'
    elif difficulty == 'hard':
        random_leetcode_url = random_leetcode_url + '&difficulty=hard'
    elif difficulty == 'easy_medium':
        random_leetcode_url = random_leetcode_url + '&difficulty=easy_medium'
    elif difficulty == 'easy_hard':
        random_leetcode_url = random_leetcode_url + '&difficulty=easy_hard'
    elif difficulty == 'medial_hard':
        random_leetcode_url = random_leetcode_url + '&difficulty=medium_hard'

    random_leetcode_url = random_leetcode_url + f'&username={user}'

    response = requests.get(random_leetcode_url)

    if response.status_code == 200:
        data = response.json()
        random_problem = data
        # random_problem = random.choice(all_problems)
        
        # Extracting relevant information
        problem_title = random_problem['stat']['question__title']
        problem_difficulty = random_problem['difficulty']['level']
        problem_ispremium = random_problem["paid_only"]
        problem_slug = random_problem['stat']['question__title_slug']
        problem_url = f"https://leetcode.com/problems/{problem_slug}/"

        # Creating an embed to send a formatted message to Discord
        embed = discord.Embed(
            title=f"Random LeetCode Problem ({'Easy' if problem_difficulty == 1 else ('Medium' if problem_difficulty == 2 else 'Hard')})",
            description=problem_title,
            color=random.randint(0, 0xFFFFFF)
        )
        embed.add_field(name="Problem URL", value=problem_url, inline=False)
        embed.add_field(name="Problem Slug", value=problem_slug, inline=False)
        embed.add_field(name="Premium", value=problem_ispremium, inline=False)
        return embed
    else:
        return discord.Embed(
            title="Error",
            description="Failed to fetch random LeetCode problem. Please try again later.",
            color=discord.Color.red()
        )
    
def get_hint(slug):
    if slug == '':
        return discord.Embed(
            title="Error",
            description="Please Provide a Valid Slug.",
            color=discord.Color.red()
        )

    hint_url = EXPRESS_URL + 'get-hint?slug=' + slug
    response = requests.get(hint_url)

    if response.status_code == 200:
        data = response.json()
        # random_problem = random.choice(all_problems)
        
        # Extracting relevant information
        problem_title = data['title']
        problem_slug = data['slug']
        problem_url = f"https://leetcode.com/problems/{problem_slug}/"
        result = data['result']

        # Creating an embed to send a formatted message to Discord
        embed = discord.Embed(
            title=f"Problem Hint",
            description=problem_title,
            color=discord.Color.green()
        )
        embed.add_field(name="Problem URL", value=problem_url, inline=False)
        embed.add_field(name="Problem Slug", value=problem_slug, inline=False)
        return embed, result
    else:
        return discord.Embed(
            title="Error",
            description="Failed to fetch Hint. Please try again later.",
            color=discord.Color.red()
        )

def get_solution(slug, language='python'):
    if slug == '':
        return discord.Embed(
            title="Error",
            description="Please Provide a Valid Slug.",
            color=discord.Color.red()
        )

    solution_url = EXPRESS_URL + 'get-solution?slug=' + slug + '&language=' + language
    response = requests.get(solution_url)

    if response.status_code == 200:
        data = response.json()
        # random_problem = random.choice(all_problems)
        
        # Extracting relevant information
        problem_title = data['title']
        problem_slug = data['slug']
        problem_url = f"https://leetcode.com/problems/{problem_slug}/"
        result = data['result']

        # Creating an embed to send a formatted message to Discord
        embed = discord.Embed(
            title=f"Problem Code Solution",
            description=problem_title,
            color=discord.Color.green()
        )
        embed.add_field(name="Problem URL", value=problem_url, inline=False)
        embed.add_field(name="Problem Slug", value=problem_slug, inline=False)
        return embed, result
    else:
        return discord.Embed(
            title="Error",
            description="Failed to fetch Hint. Please try again later.",
            color=discord.Color.red()
        )

def get_stats(user):
    stats_url = EXPRESS_URL + 'get-stats?username=' + str(user)
    response = requests.get(stats_url)

    if response.status_code == 200:
        data = response.json()
        # random_problem = random.choice(all_problems)
        
        # Extracting relevant information
        questions_asked = data['asked']
        questions_solved = data['solved']
        updated_at = data['created_at']

        # Creating an embed to send a formatted message to Discord
        embed = discord.Embed(
            title=f"{user}",
            description="User Stats: ",
            color=discord.Color.blue()
        )
        embed.add_field(name="Questions Asked: ", value=questions_asked, inline=False)
        embed.add_field(name="Questions Solved: ", value=questions_solved, inline=False)
        embed.add_field(name="Updated At: ", value=updated_at, inline=False)
        return embed
    else:
        return discord.Embed(
            title="Error",
            description="Failed to fetch Hint. Please try again later.",
            color=discord.Color.red()
        )

def add_solved(user):
    solved_url = EXPRESS_URL + 'add-solved?username=' + str(user)
    response = requests.get(solved_url)

    if response.status_code == 200:
        data = response.json()
        # random_problem = random.choice(all_problems)
        
        # Extracting relevant information
        questions_asked = data['asked']
        questions_solved = data['solved']

        # Creating an embed to send a formatted message to Discord
        embed = discord.Embed(
            title=f"{user}",
            description="User Stats: ",
            color=discord.Color.blue()
        )
        embed.add_field(name="Questions Asked: ", value=questions_asked, inline=False)
        embed.add_field(name="Questions Solved: ", value=questions_solved, inline=False)
        return embed
    else:
        return discord.Embed(
            title="Error",
            description="Failed to fetch Hint. Please try again later.",
            color=discord.Color.red()
        )

def get_users():
    get_user_url = EXPRESS_URL + 'get-users'
    response = requests.get(get_user_url)

    if response.status_code == 200:
        data = response.json()
        
        return data
        
    else:
        return None

async def send_reminder():
  await client.wait_until_ready()

  while not client.is_closed():  # Continue running until the bot is closed
    print('Executing scheduled job...')

    users_list = get_users()

    for user in users_list:
        print(user)

  # for user in users_list:
  #   date_string = user['created_at']
  #   date_time_object = datetime.strptime(date_string, "%Y-%m-%dT%H:%M:%S.%fZ")

  #   current_time = datetime.utcnow()
  #   time_difference = current_time - date_time_object

  #   # twenty_four_hours = timedelta(days=1)

  #   # for Testing only
  #   five_minutes = timedelta(minutes=5)

  #   if time_difference > five_minutes:
  #     return True
  #   else: 
  #     return False

client.run('MTIxMTAwNTIzMjgwOTY0ODEzOA.G-TRTg.oLLGEAclPvSbnimwJz6r6Pmer-m4CBp8zsTtBw')


