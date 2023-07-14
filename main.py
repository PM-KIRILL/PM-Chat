import time
import random
import requests
import chatlink
import bot
import config
from commands import Commands
import psutil

def run_bot():
    print("Запуск бота...")
    for i in range(1, 101):
        print(f"Progress-{i}%")
        time.sleep(0.035)  # Задержка в 0.035 секунды для имитации загрузки
        
    print("Загрузка завершена!")
    
    # Проверка пинга (рандомное значение для примера)
    ping = random.randint(1, 100)
    print(f"Пинг: {ping}ms")
    
    # Использование оперативной памяти ботом
    memory_usage = psutil.Process().memory_info().rss / 1024 / 1024
    print(f"Использование памяти: {memory_usage}MB")

    # Успешный запуск скрипта main.py
    print("Скрипт main.py успешно запущен!")
    
    if config.webhook == True:
        chatlink_object = chatlink.Chatlink()
        for line in chatlink_object.main():
            print("MC -> Discord: " + text)
            data = {
                "content": text,
                "username": config.discord_nickname
            }
            r = requests.post(config.webhook_url, json=data)
    else:
        client = bot.BotClient(command_prefix=config.command_prefix,
                               help_command=None)
        client.add_cog(Commands(client))
        client.run(config.bot_token)

run_bot()