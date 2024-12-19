import telebot
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
import os
from dotenv import load_dotenv
from media_downloader import download_twitter_video, download_ig_media, download_linkedin_media, download_pinterest_video, download_tiktok_audio, download_tiktok_video, download_facebook_video, download_youtube_video

load_dotenv()

API_KEY = os.getenv("API_KEY")

bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=["start"])
def start_bot(message):
    chat_id = message.chat.id

    sm_keyboard = InlineKeyboardMarkup()

    twitter_key = InlineKeyboardButton("X (Twitter)", callback_data="twitter_key")
    ig_key = InlineKeyboardButton("Instagram", callback_data="ig_key")
    linkedin_key = InlineKeyboardButton("LinkedIn", callback_data="linkedin_key")
    tiktok_video_key = InlineKeyboardButton("TikTok Video", callback_data="tiktok_vid_key")
    tiktok_audio_key = InlineKeyboardButton("TikTok Audio", callback_data="tiktok_audio_key")
    facebook_key = InlineKeyboardButton("Facebook", callback_data="fb_key")
    pinterest_key = InlineKeyboardButton("Pinterest", callback_data="pinterest_key")
    youtube_key = InlineKeyboardButton("YouTube", callback_data="youtube_key")
    
    sm_keyboard.add(youtube_key, twitter_key, ig_key, tiktok_video_key, linkedin_key, facebook_key, pinterest_key)

    bot.send_message(chat_id, "*\u23ecWhich download do you want to do?*", parse_mode="Markdown", reply_markup=sm_keyboard)


@bot.callback_query_handler(func=lambda call: call.data in ["twitter_key", "ig_key", "linkedin_key", "tiktok_vid_key", "tiktok_audio_key", "fb_key", "pinterest_key", "youtube_key"])
def twitter_button(call: CallbackQuery):
    chat_id = call.message.chat.id
    if call.data == "twitter_key":
        bot.send_message(chat_id, "Input link of X (twitter) video")

        bot.register_next_step_handler(call.message, twitter_processing_link)

    elif call.data == "ig_key":
        bot.send_message(chat_id, "Input link of instagram video")

        bot.register_next_step_handler(call.message, ig_processing_link)

    elif call.data == "linkedin_key":
        bot.send_message(chat_id, "Input link of linkedin video")

        bot.register_next_step_handler(call.message, linkedin_processing_link)

    elif call.data == "tiktok_vid_key":
        bot.send_message(chat_id, "Input link of tiktok video")

        bot.register_next_step_handler(call.message, tiktok_vid_processing_link)

    elif call.data == "tiktok_audio_key":
        bot.send_message(chat_id, "Input link of tiktok video")

        bot.register_next_step_handler(call.message, tiktok_audio_processing_link)

    elif call.data == "fb_key":
        bot.send_message(chat_id, "Input link of facebook video")

        bot.register_next_step_handler(call.message, fb_processing_link)

    elif call.data == "pinterest_key":
        bot.send_message(chat_id, "Input link of pinterest video")

        bot.register_next_step_handler(call.message, pinterest_processing_link)
    
    elif call.data == "youtube_key":
        bot.send_message(chat_id, "Input link of youtube video")

        bot.register_next_step_handler(call.message, youtube_processing_link)

   
    bot.answer_callback_query(call.id)



def twitter_processing_link(message):
    chat_id = message.chat.id
    twitter_link = message.text
    bot.send_message(chat_id, "\U0001f504*Processing your video ...*\nTakes less than a minute", parse_mode="Markdown")
    try:
        download_link = download_twitter_video(twitter_link)
        bot.send_message(chat_id, download_link)
    except:
        bot.send_message(chat_id, "Invalid link format. Try again")
        start_bot(message)


def ig_processing_link(message):
    chat_id = message.chat.id
    ig_link = message.text
    bot.send_message(chat_id, "\U0001f504*Processing your video ...*\nTakes less than a minute", parse_mode="Markdown")
    try:
        download_link = download_ig_media(ig_link)
        bot.send_message(chat_id, download_link)
    except:
        bot.send_message(chat_id, "Invalid link format. Try again")
        start_bot(message)


def linkedin_processing_link(message):
    chat_id = message.chat.id
    linkedin_link = message.text
    bot.send_message(chat_id, "\U0001f504*Processing your video ...*\nTakes less than a minute", parse_mode="Markdown")
    try:
        download_link = download_linkedin_media(linkedin_link)
        bot.send_message(chat_id, download_link)
    except:
        bot.send_message(chat_id, "Invalid link format. Try again")
        start_bot(message)

def tiktok_audio_processing_link(message):
    chat_id = message.chat.id
    tiktok_audio_link = message.text
    bot.send_message(chat_id, "\U0001f504*Processing your video ...*\nTakes less than a minute", parse_mode="Markdown")
    try:
        download_link = download_tiktok_audio(tiktok_audio_link)
        bot.send_message(chat_id, download_link)
    except:
        bot.send_message(chat_id, "Invalid link format. Try again")
        start_bot(message)


def tiktok_vid_processing_link(message):
    chat_id = message.chat.id
    tiktok_vid_link = message.text
    bot.send_message(chat_id, "\U0001f504*Processing your video ...*\nTakes less than a minute", parse_mode="Markdown")
    try:
        download_link = download_tiktok_video(tiktok_vid_link)
        bot.send_message(chat_id, download_link)
    except:
        bot.send_message(chat_id, "Invalid link format. Try again")
        start_bot(message)


def fb_processing_link(message):
    chat_id = message.chat.id
    facebook_link = message.text
    bot.send_message(chat_id, "\U0001f504*Processing your video ...*\nTakes less than a minute", parse_mode="Markdown")
    try:
        download_link = download_facebook_video(facebook_link)
        bot.send_message(chat_id, download_link)
    except:
        bot.send_message(chat_id, "Invalid link format. Try again")
        start_bot(message)


def pinterest_processing_link(message):
    chat_id = message.chat.id
    pinterest_link = message.text
    bot.send_message(chat_id, "\U0001f504*Processing your video ...*\nTakes less than a minute", parse_mode="Markdown")
    try:
        download_link = download_pinterest_video(pinterest_link)
        bot.send_message(chat_id, download_link)
    except:
        bot.send_message(chat_id, "Invalid link format. Try again")
        start_bot(message)


def youtube_processing_link(message):
    chat_id = message.chat.id
    youtube_link = message.text
    bot.send_message(chat_id, "\U0001f504*Processing your video ...*\nTakes less than a minute", parse_mode="Markdown")
    try:
        download_link = download_youtube_video(youtube_link)
        bot.send_message(chat_id, download_link)
    except:
        bot.send_message(chat_id, "Invalid link format. Try again")
        start_bot(message)






if __name__ == "__main__":
    bot.infinity_polling()