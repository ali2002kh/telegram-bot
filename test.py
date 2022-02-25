from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters

watingForAdding = False 
watingForDeleting = False
todoList = []

updater = Updater('5143681979:AAFrZRwJYbyabEI0FZ9d-wsJjSdJeh9sVB4',
                  use_context=True)

def start(update: Update, context: CallbackContext):
    update.message.reply_text("سلاملکم\n/add\n/delete\n/list")
    
def add(update: Update, context: CallbackContext):
    update.message.reply_text("چیو میخوای اضافه کنی ؟")
    global watingForAdding
    watingForAdding = True

def delete(update: Update, context: CallbackContext):
    update.message.reply_text("چیو میخوای پاک کنی ؟")   
    global watingForDeleting
    watingForDeleting = True 
    
def getTask(update: Update, context: CallbackContext):
    global watingForAdding,watingForDeleting
    if watingForAdding:
        task = update.message.text
        update.message.reply_text(" " + task + " اضافه شد ")
        todoList.append(task)
        watingForAdding = False  
    elif watingForDeleting:
        task = update.message.text
        try:
            todoList.remove(task)
            update.message.reply_text(" " + task + " پاک شد ")
        except:
            update.message.reply_text(" " + task + " یافت نشد ")
        watingForDeleting = False  
  
def getList(update: Update, context: CallbackContext):
    text = ""
    for task in todoList:
        text += task + "\n"
    try:
        update.message.reply_text(text)
    except:
        update.message.reply_text("بیکاری")
    
    
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('add', add))
updater.dispatcher.add_handler(CommandHandler('delete', delete))
updater.dispatcher.add_handler(CommandHandler('list', getList))
updater.dispatcher.add_handler(MessageHandler(Filters.text, getTask))
updater.start_polling()
updater.idle()