from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import handlers

app = ApplicationBuilder().token('8729780473:AAFX7mpEkzjhtrDwyp8iyN2oqukXDKHNanI').build()

app.add_handler(handlers.start_command)
app.add_handler(handlers.get_help_command)
app.add_handler(handlers.joke_command)

app.run_polling()