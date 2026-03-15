from telegram.ext import CommandHandler
import jokey

async def start(update, context):
    await update.message.reply_text("Hello USER, Wanna Listen A Joke ?")
async def get_help(update, context):
    await update.message.reply_text("I Can Crack Jokes. Type /joke To Listen One")
async def joke(update, context):
    await update.message.reply_text(jokey.get_joke())

start_command = CommandHandler("start", start)
get_help_command = CommandHandler("help", get_help)
joke_command = CommandHandler("joke", joke)