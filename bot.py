```python
import os
import asyncio
import logging

from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
)

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    raise RuntimeError("BOT_TOKEN is not set")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎵 NoeNoe Music Bot အလုပ်လုပ်နေပါပြီ!\n\n"
        "အသုံးပြုနိုင်သော command များ:\n"
        "/play - သီချင်းဖွင့်ရန်\n"
        "/pause - ခဏရပ်ရန်\n"
        "/resume - ပြန်ဖွင့်ရန်\n"
        "/skip - နောက်သီချင်းသို့\n"
        "/stop - ရပ်ရန်"
    )


async def play(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text(
            "🎵 သီချင်းနာမည်ထည့်ပါ။\n\n"
            "ဥပမာ - /play Shape of You"
        )
        return

    song = " ".join(context.args)

    await update.message.reply_text(
        f"🔎 သီချင်းရှာနေပါတယ်...\n\n🎵 {song}"
    )


async def pause(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("⏸️ Music ကို ခဏရပ်ထားပါတယ်။")


async def resume(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("▶️ Music ကို ပြန်ဖွင့်နေပါတယ်။")


async def skip(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("⏭️ နောက်သီချင်းသို့ ကျော်နေပါတယ်။")


async def stop(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("⏹️ Music ကို ရပ်လိုက်ပါပြီ။")


def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("play", play))
    app.add_handler(CommandHandler("pause", pause))
    app.add_handler(CommandHandler("resume", resume))
    app.add_handler(CommandHandler("skip", skip))
    app.add_handler(CommandHandler("stop", stop))

    print("🎵 NoeNoe Music Bot is running...")
    app.run_polling()


if __name__ == "__main__":
    main()
```
  
