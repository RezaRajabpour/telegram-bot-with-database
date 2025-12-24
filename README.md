# Telegram Bot User Management

A Python project for managing Telegram bot users using SQLite.  
This bot stores basic user information when users interact with the `/start` command.

## Getting Started

This project is compatible with Python 3.x and uses SQLite as the database.

### Prerequisites

- Python 3.x
- SQLite3 (comes with Python by default)
- python-telegram-bot (v20+)


## Project Structure


bot.py                # Main bot file  
bot_data.db           # SQLite database (created automatically)  
README.md             # Project documentation  


## Classes and Functions

### Core Functions

- `init_db`  
  Initializes the SQLite database and creates the required table if it does not exist.

- `store_user`  
  Stores a Telegram user in the database if they are not already registered.

### Bot Commands

- `/start`  
  Registers the user in the database and confirms membership status.

- `/help`  
  Displays a simple help message.

- Text Messages  
  Echoes received text messages back to the user.


## Usage

Run the bot using:

```bash
python bot.py
```

When a user sends `/start`, their Telegram ID, first name, username, and join time are saved in the database.

## Notes

- The database is created automatically on first run.
- Duplicate users are prevented using a unique constraint on the Telegram user ID.
- This project is suitable for small bots and educational purposes.
- The code can be extended to include statistics, admin features, or advanced user management.
