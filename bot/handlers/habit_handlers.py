from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes, ConversationHandler
from datetime import datetime

ADDING_HABIT = 0

async def add_habit(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Prompt the user to enter a new habit."""
    await update.callback_query.edit_message_text(
        "Please enter your new habit:"
    )
    return ADDING_HABIT

async def save_habit(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Save the habit provided by the user."""
    user_id = str(update.message.from_user.id)
    habit_name = update.message.text
    
    user_data = context.bot_data.setdefault(user_id, {"habits": [], "tasks": [], "workouts": []})
    user_data["habits"].append({
        "name": habit_name,
        "streak": 0,
        "completed": False,
        "created_at": datetime.now().isoformat()
    })
    
    keyboard = [[InlineKeyboardButton("🏠 Back to Menu", callback_data="start")]]
    await update.message.reply_text(
        f"Habit '{habit_name}' added successfully!",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )
    return ConversationHandler.END
