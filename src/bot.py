from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from src.instagram_downloader import download_instagram_reel
from src.pinterest_downloader import download_pinterest_pin
from src.config import TELEGRAM_BOT_TOKEN

def start(update, context):
        update.message.reply_text('Send me Instagram or Pinterest URLs to download content!')

        def handle_message(update, context):
                url = update.message.text
                    if "instagram.com" in url:
                                video_path = download_instagram_reel(url)
                                        if video_path:
                                                        context.bot.send_video(chat_id=update.message.chat_id, video=open(video_path, 'rb'))
                                                                else:
                                                                                update.message.reply_text('Failed to download Instagram reel.')
                                                                                    elif "pinterest.com" in url:
                                                                                                media_url = download_pinterest_pin(url)
                                                                                                        if media_url:
                                                                                                                        context.bot.send_photo(chat_id=update.message.chat_id, photo=media_url)
                                                                                                                                else:
                                                                                                                                                update.message.reply_text('Failed to download Pinterest pin.')
                                                                                                                                                    else:
                                                                                                                                                                update.message.reply_text('Unsupported URL!')

                                                                                                                                                                def main():
                                                                                                                                                                        updater = Updater(token=TELEGRAM_BOT_TOKEN, use_context=True)
                                                                                                                                                                            dp = updater.dispatcher

                                                                                                                                                                                dp.add_handler(CommandHandler('start', start))
                                                                                                                                                                                    dp.add_handler(MessageHandler(Filters.text, handle_message))

                                                                                                                                                                                        updater.start_polling()
                                                                                                                                                                                            updater.idle()

                                                                                                                                                                                            if __name__ == '__main__':
                                                                                                                                                                                                    main()

