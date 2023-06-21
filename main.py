import subprocess
from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from secrete import Token

TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
bot = Bot(token=Token.bot_token)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


def run_sudo_command(command):
    full_command = f'echo {Token.sudo_password} | sudo -S {command}'
    process = subprocess.Popen(full_command, shell=True)
    process.wait()
    exit_code = process.returncode
    return exit_code
exit_code = run_sudo_command('systemctl stop manager_bot')
print(f"Код завершения: {exit_code}")

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.reply("Привет! Отправь /run для запуска скрипта или /stop для его остановки.")

@dp.message_handler(commands=['run'])
async def run_script(message: types.Message):
    # Запуск скрипта
    subprocess.Popen(["python3", "~/home/sanchos_bot/sanchos/main.py"])
    await message.reply("Скрипт запущен.")

@dp.message_handler(commands=['stop'])
async def stop_script(message: types.Message):
    # Остановка скрипта
    subprocess.call(["pkill", "-f", "~/home/sanchos_bot/sanchos/main.py"])
    await message.reply("Скрипт остановлен.")

def run_sudo_command(command, password):
    full_command = f'echo {password} | sudo -S {command}'
    process = subprocess.Popen(full_command, shell=True)
    process.wait()
    exit_code = process.returncode
    return exit_code

password = "Ваш_пароль"
exit_code = run_sudo_command('systemctl stop manager_bot', password)
print(f"Код завершения: {exit_code}")

if __name__ == '__main__':
    # Запуск клиента Telethon
    # Запуск бота aiogram
    executor.start_polling(dp)
    # client.loop.run_until_complete(main())
    # client.loop.run_until_complete(get_dialodgs())