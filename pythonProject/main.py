import asyncio
import config
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
import logging
import random
from keybords import KeyboardButton

#Включаем логгирование
logging.basicConfig(level=logging.INFO)

#Создаем обьект бота
bot=Bot(token=config.token)

#Диспетчер
dp = Dispatcher()

#Реакция на команду /start

@dp.message(Command('start'))
async def cmd_start(message: types.Message):
    name = message.chat.first_name
    print(message.chat)
    await message.answer(f'Привет, {name} , у нас есть все необходимое для сборки мощного компьютера', Reply_Markup = KeyboardButton)

#Реакция команды стоп
@dp.message(Command('stop'))
async def cmd_stop(message: types.message):
    name = message.chat.first_name
    await message.answer(f'до встречи, {name}, заходи к нам ещё, мы рады помогать заинтересованным людям.')

#Хэндлер на сообщения
#@dp.message(F.text)
async def msg_echo(message: types.Message):
    msg_user = message.text
    await message.answer(f'уточните, вы хотите {msg_user}')

#Хэндлер сообщений 2
@dp.message(F.text)
async def msg_echo(message: types.Message):
    msg_user = message.text
    if 'Привет' in msg_user:
        await message.answer(f'Привет, что Вас интересует?')


    elif 'Материнская плата' in msg_user:
        await message.answer('Замечательно, у нас есть производители Asus, Gigabite, MSI, Maxsun, ASRock')
    elif 'Процессор' in msg_user:
        await message.answer('В нашем ассортименте имеется intel, Amd')
    elif 'Блок питания' in msg_user:
        await  message.answer('Все зависит от мощности и под какие цели подбирается данный девайс!?, я переведу Вас на оператора для уточнения параметров')
    elif 'Оперативная память' in msg_user:
        await message.answer('Производителей и параметров много, я переведу Вас на оператора')
    elif 'Системный блок' in msg_user:
        await message.answer('На данный момент, мы не успели собрать хороший аппарат для удовлетворения ваших ожиданий, Вы можете написать мне я передам запрос оператору он с Вами свяжется.')
    elif 'Корпус' in msg_user:
        await message.answer('Лучше посетите наш сайт "https://cyberHub.com/001", это ссылка на страницу с корпусами.')
    elif 'Жесткий диск' in msg_user:
        await message.answer('Я уточню? HDD или SSD?')
    elif 'Hdd' in msg_user:
        await message.answer('У нас есть двух типоразмеров 3,5" и 2,5"')
    elif 'Ssd' in msg_user:
        await message.answer('PCI-Ex4, SATA, NvMe')
    elif 'Видеокарта' in msg_user:
        await message.answer('Nvidia, AMD, Вас какаой производитель интересует?')

    elif '' in msg_user:
        await message.answer('Посетите наш сайт "https://cuberhub.com"')

    else:
        await message.answer('Я тебя не понимаю, перефразируй')



async def main():
    await dp.start_polling(bot)

#Попробуем примотать кнопки
from aiogram import types
button_1 = types.KeyboardButton(text='нформация')
button_2 = types.KeyboardButton(text='информация')


if  __name__ == '__main__':
    asyncio.run(main())
