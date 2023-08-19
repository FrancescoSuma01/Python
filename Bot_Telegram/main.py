from typing import Final
from telegram import Update, InputFile
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from glob import glob
from random import choice

TOKEN: Final = 'xxxxxxxxxxxxxxx'

BOT_USERNAME: Final = 'bulldogFrencieBot'


#Commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Ciao! Digita 'frencie' o 'english' per una foto o un testo casuale per una sorpresa!")
    
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Digita 'frencie' o 'english' per avere una foto, altrimenti digita una qualsiasi cosa per avere una sorpresa!")
    
async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Questo è un comando personalizzato")
    

#Responses
async def handle_response(text: str, update: Update) -> None:
    
    processed: str = text.lower()
    
    if 'frencie' in processed:
        immagine = choice(glob("Frencie/*.jpg"))
        await update.message.reply_photo(photo=open(immagine, 'rb'))
    elif 'english' in processed:
        immagine = choice(glob("English/*.jpg"))
        await update.message.reply_photo(photo=open(immagine, 'rb'))
    else:
        await update.message.reply_video(video=open('Fart.mp4', 'rb'))
   
        
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text = update.message.text
    
    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME,'').strip()
            await handle_response(new_text, update)
        else:
            return
    else:
        await handle_response(text, update)


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')
    

if __name__ == '__main__':
    
    print('starting bot...')
    
    app = Application.builder().token(TOKEN).build()
    
    #Commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))
    
    #Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))
    
    #Error
    app.add_error_handler(error)
    
    #Polls the bot
    print('Polling...')
    app.run_polling(poll_interval=3)