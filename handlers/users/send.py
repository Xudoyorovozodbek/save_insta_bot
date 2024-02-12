from aiogram import types
from loader import dp, bot
from aiogram.dispatcher.filters import Text
from insta import instadownloader
@dp.message_handler(Text(startswith='https://www.instagram.com/'))
async def send_media(massage:types.Message):
    link=massage.text
    data=instadownloader(link=link)
    if data =='Bad':
        await massage.answer('Bu Url manzil orqali hech narsa topilmadi !')
    else:
        if data['type']=='image':
            await massage.answer_photo(photo=data['media'])
        elif data['type']== 'video':
            await massage.answer_video(video=data['media'])
        elif data['type']=='carousel':
            for i in data['media']:
                await massage.answer_document(document=i)
        else:
            await massage.answer('Bu Url manzil orqali hech narsa topilmadi !')
