import subprocess
from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from secrete import Token

bot = Bot(token=Token.bot_token)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


def run_sudo_command(command):
    full_command = f'echo {Token.sudo_password} | sudo -S {command}'
    process = subprocess.Popen(full_command, shell=True)
    process.wait()
    exit_code = process.returncode
    return exit_code


def status_sudo_command(command):
    full_command = f'echo {Token.sudo_password} | sudo -S {command}'
    process = subprocess.Popen(full_command, shell=True)
    process.wait()
    exit_code = process
    return exit_code
# exit_code = run_sudo_command('systemctl stop manager_bot')


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.reply("Привет! Отправь /run для запуска скрипта или /stop для его остановки или /status для проверки статуса приложения .")


@dp.message_handler(commands=['run'])
async def run_script(message: types.Message):
    start = 'systemctl start sanchos'
    # Запуск скрипта
    rezult = run_sudo_command(start)
    await message.reply(f"{rezult}")


@dp.message_handler(commands=['stop'])
async def stop_script(message: types.Message):
    stop = 'systemctl stop sanchos'
    # Остановка скрипта
    rezult = run_sudo_command(stop)
    await message.reply(f"{rezult}")


@dp.message_handler(commands=['status'])
async def status_script(message: types.Message):
    status = 'systemctl status sanchos'
    # Остановка скрипта
    rezult =status_sudo_command(status)
    await message.reply(f"{rezult}")





if __name__ == '__main__':
    # Запуск клиента Telethon
    # Запуск бота aiogram
    executor.start_polling(dp)
    # client.loop.run_until_complete(main())
    # client.loop.run_until_complete(get_dialodgs())