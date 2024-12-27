from telethon import TelegramClient

# Введення власних API_ID та API_HASH
API_ID = ''  # Свій API_ID!
API_HASH = ''  # Свій API_HASH!


# Створення клієнта
client = TelegramClient('simple_session', API_ID, API_HASH)

async def get_members_by_link(chat_link):
    #Отримати список учасників групи за посиланням
    chat = await client.get_entity(chat_link)
    participants = await client.get_participants(chat)

    print(f"Учасники групи {chat.title}:")
    for user in participants:
        print(f"{user.first_name or 'Немає імені'} {user.last_name or ''} (@{user.username or 'немає'})")

async def send_message_to_user():
    #Відправити повідомлення користувачу за юзернеймом
    username = input("Юзернейм отримувача: ")
    message = input("Текст повідомлення: ")
    await client.send_message(username, message)
    print(f"Повідомлення успішно надіслано до {username}!")

async def main():
    chat_link = input("Посилання на групу: ")
    await get_members_by_link(chat_link)
    await send_message_to_user()

# Запуск програми
if __name__ == '__main__':
    client.start()
    client.loop.run_until_complete(main())
    client.disconnect()
