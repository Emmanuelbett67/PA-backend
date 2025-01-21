from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes, ConversationHandler
from datetime import datetime

ADDING_TASK = 1

async def add_task(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Prompt the user to enter a new task."""
    await update.callback_query.edit_message_text(
        "Please enter your new task:"
    )
    return ADDING_TASK

async def save_task(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Save the task provided by the user."""
    user_id = str(update.message.from_user.id)
    task_text = update.message.text
    
    user_data = context.bot_data.setdefault(user_id, {"habits": [], "tasks": [], "workouts": []})
    user_data["tasks"].append({
        "text": task_text,
        "completed": False,
        "created_at": datetime.now().isoformat()
    })
    
    keyboard = [[InlineKeyboardButton("🏠 Back to Menu", callback_data="start")]]
    await update.message.reply_text(
        f"Task '{task_text}' added successfully!",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )
    return ConversationHandler.END
