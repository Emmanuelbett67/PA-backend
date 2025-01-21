from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ConversationHandler,
    MessageHandler,
    filters
)

from bot.handlers.habit_handlers import add_habit, save_habit, ADDING_HABIT
from bot.handlers.task_handlers import add_task, save_task, ADDING_TASK
from bot.handlers.workout_handlers import add_workout, save_workout, ADDING_WORKOUT


class TrackerBot:
    def __init__(self, token: str):
        self.token = token

    def run(self):
        app = Application.builder().token(self.token).build()

        # Conversation handler
        conv_handler = ConversationHandler(
            entry_points=[
                CallbackQueryHandler(add_habit, pattern="^add_habit$"),
                CallbackQueryHandler(add_task, pattern="^add_task$"),
                CallbackQueryHandler(add_workout, pattern="^add_workout$"),
            ],
            states={
                ADDING_HABIT: [MessageHandler(filters.TEXT & ~filters.COMMAND, save_habit)],
                ADDING_TASK: [MessageHandler(filters.TEXT & ~filters.COMMAND, save_task)],
                ADDING_WORKOUT: [MessageHandler(filters.TEXT & ~filters.COMMAND, save_workout)],
            },
            fallbacks=[],
        )

        app.add_handler(CommandHandler("start", self.start))
        app.add_handler(conv_handler)
        
        # Run bot
        app.run_polling()
