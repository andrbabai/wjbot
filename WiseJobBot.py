from aiogram import Bot, Dispatcher, executor, types, filters
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from config import TOKEN
from states import Form
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()
bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=storage) 

@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.answer("Привет! Давай заполним анкету. Как тебя зовут?")
    await Form.name.set()

@dp.message_handler(state=Form.name)
async def process_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await message.answer("Привет, {0}. Какой у тебя опыт программирования?".format(message.text))
    await Form.next()

@dp.message_handler(state=Form.experience)
async def process_experience(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['experience'] = message.text
    await state.finish()
    await message.answer("Спасибо, {0}. Мы обязательно учтём твои данные.".format(message.text))

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

    
    #async def cmd_handler(message: types.Message):
    #await message.answer('👋 Привет! Я WJ Бот.\n\nЯ помогаю компаниям и соискателям работы легко найти друг друга.\n\n🔎С поиском чего я могу тебе помочь?!', reply_markup=kb)

#@dp.message_handler()
#sync def echo(message: types.Message):
    #if message.text == '🧗Я ищу работу':
       # await start_poll(message)

#async def start_poll(message: types.Message):
   # options=["🔛Да, хорошо", "🔙Назад"]
    #await bot.send_poll(message.chat.id, "Чтобы понять каких работодателей вам представить нужно задать вам всего 5 вопросов, ок?", options)

#@dp.poll_answer_handler()
#async def handle_poll_answer(quiz_answer: "🔛Да, хорошо"):
    #if quiz_answer.option_ids[0] == 0: # если выбран первый вариант ответа
        #options=["Вы управляете процессами", "Вы управляете функциями", "Вы управляете людьми"]
        #await bot.send_poll(quiz_answer.user.id, "1. Какой тип управления вам больше всего подходит?", options)

#async def start_poll(message: types.Message):
    #options=["Вы управляете процессами", "Вы управляете функциями", "Вы управляете людьми"]
    #await bot.send_poll(message.chat.id, "1. Какой тип управления вам больше всего подходит?", options)

#@dp.message_handler(filters.Text(equals='Option 1'))
#async def cmd_handler(message: types.Message):
   # await message.answer ()

#@dp.message_handler()
#async def echo(message: types.Message):
    #await message.answer(message.text)
