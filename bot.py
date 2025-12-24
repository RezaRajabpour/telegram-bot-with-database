import sqlite3
from datetime import datetime
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

db_conn = None

def init_db():
    global db_conn
    if db_conn is None:
        db_conn = sqlite3.connect('bot_data.db', check_same_thread=False)
        db_conn.row_factory = sqlite3.Row
        cursor = db_conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS user_info (
                record_id INTEGER PRIMARY KEY,
                user_number INTEGER UNIQUE,
                user_first_name TEXT,
                user_username TEXT,
                added_on TEXT
            )
        ''')
        db_conn.commit()

def store_user(uid, fname, uname):
    init_db()
    cursor = db_conn.cursor()
    
    cursor.execute(
        'SELECT user_number FROM user_info WHERE user_number = :user_id',
        {'user_id': uid}
    )
    
    if cursor.fetchone():
        return False
    
    current_time = datetime.now().strftime("%d-%m-%Y %H:%M")
    cursor.execute(
        '''INSERT INTO user_info 
           (user_number, user_first_name, user_username, added_on) 
           VALUES (:id, :name, :username, :time)''',
        {'id': uid, 'name': fname, 'username': uname, 'time': current_time}
    )
    
    db_conn.commit()
    return True

async def cmd_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    sender = update.effective_user
    stored = store_user(sender.id, sender.first_name, sender.username)
    
    if stored:
        reply_msg = "عضویت انجام شد."
    else:
        reply_msg = "شما عضو هستید."
    
    await update.message.reply_text(reply_msg)

async def cmd_help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("راهنما: /start")

async def text_response(update: Update, context: ContextTypes.DEFAULT_TYPE):
    input_text = update.message.text
    await update.message.reply_text(input_text)

def start_bot():
    init_db()
    bot = Application.builder().token("8208856815:AAFF2xeo57cNQL1quT9mtTSEImP3pawLpzs").build()
    
    bot.add_handler(CommandHandler("start", cmd_start))
    bot.add_handler(CommandHandler("help", cmd_help))
    bot.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, text_response))
    
    bot.run_polling()

if __name__ == "__main__":
    start_bot()