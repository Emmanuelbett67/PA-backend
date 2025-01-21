from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes, ConversationHandler
from datetime import datetime

ADDING_WORKOUT = 2

async def add_workout(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Prompt the user to enter a workout."""
    await update.callback_query.edit_message_text(
        "Please enter your workout in this format:\nExercise, Weight, SetsxReps\nExample: Bench Press, 185, 5x5"
    )
    return ADDING_WORKOUT

async def save_workout(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Save the workout provided by the user."""
    user_id = str(update.message.from_user.id)
    try:
        exercise, weight, reps = [x.strip() for x in update.message.text.split(",")]
        
        user_data = context.bot_data.setdefault(user_id, {"habits": [], "tasks": [], "workouts": []})
        user_data["workouts"].append({
            "exercise": exercise,
            "weight": weight,
            "reps": reps,
            "created_at": datetime.now().isoformat()
        })
        
        keyboard = [[InlineKeyboardButton("🏠 Back to Menu", callback_data="start")]]
        await update.message.reply_text(
            "Workout logged successfully!",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
    except ValueError:
        await update.message.reply_text(
            "Invalid format! Please use: Exercise, Weight, SetsxReps"
        )
        return ADDING_WORKOUT
    
    return ConversationHandler.END
