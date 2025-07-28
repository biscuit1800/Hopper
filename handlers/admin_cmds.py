from aiogram import Router, types
from aiogram.filters import Command
from utils.utils import check_not_admin, load_data, save_data


router = Router()


@router.message(Command("admin"))
async def admin_panel(message: types.Message):
    if check_not_admin(message.from_user.id):
        return await message.answer("⛔ Доступ заборонений.")

    data = load_data()
    channels = data.get("channels", [])
    target = data.get("target_channel")

    text = "Поточні канали:\n"
    if channels:
        for ch in channels:
            name = ch.get("name", "Немає назви")
            url = ch.get("url", "URL не вказано")
            chat_id = ch.get("chat_id", "ID не вказано")
            text += f"• {name} — {url} — {chat_id}\n"
    else:
        text += "Список порожній."

    text += f"\nЦільовий канал: {target if target else 'Не налаштовано'}"
    text += (
        "\n\nДоступні команди:\n"
        "/add_channel <chat_id> <url> <name>\n"
        "/remove_channel <chat_id>\n"
        "/set_target <chat_id>"
    )

    await message.answer(text, disable_web_page_preview=True)


@router.message(Command("add_channel"))
async def add_channel(message: types.Message):
    if check_not_admin(message.from_user.id):
        return await message.answer("⛔ Доступ заборонений.")

    args = message.text.split(maxsplit=3)
    if len(args) != 4:
        return await message.answer("Використання: /add_channel <chat_id> <url> <name>")

    chat_id, url, name = args[1], args[2], args[3]
    data = load_data()

    try:
        member = await message.bot.get_chat_member(chat_id=chat_id, user_id=(await message.bot.me()).id)
        if member.status not in ("administrator", "creator"):
            await message.answer(f"⚠️ Бот не є адміністратором каналу {url}. Запросіть його як адміна для перевірки підписників.",
                                 disable_web_page_preview = True)
    except Exception as e:
        return await message.answer(f"Помилка доступу до каналу: {e}")

    if any(ch["chat_id"] == chat_id for ch in data["channels"]):
        return await message.answer("Такий канал вже є у списку.")

    data["channels"].append({"chat_id": chat_id, "url": url, "name": name})
    save_data(data)
    await message.answer(f"Канал додано:\n• {name} — {url} — {chat_id}", disable_web_page_preview=True)


@router.message(Command("remove_channel"))
async def remove_channel(message: types.Message):
    if check_not_admin(message.from_user.id):
        return await message.answer("⛔ Доступ заборонений.")

    args = message.text.split(maxsplit=1)
    if len(args) != 2:
        return await message.answer("Використання: /remove_channel <chat_id>")

    chat_id = args[1]
    data = load_data()
    new_channels = [ch for ch in data["channels"] if ch["chat_id"] != chat_id]

    if len(data["channels"]) == len(new_channels):
        return await message.answer("Канал не знайдено у списку.")

    data["channels"] = new_channels
    save_data(data)
    await message.answer(f"Канал {chat_id} видалено.")


@router.message(Command("set_target"))
async def set_target(message: types.Message):
    if check_not_admin(message.from_user.id):
        return await message.answer("⛔ Доступ заборонений.")

    args = message.text.split(maxsplit=1)
    if len(args) < 2:
        return await message.answer("Використання: /set_target <chat_id>")

    chat_id = args[1]
    data = load_data()
    data["target_channel"] = chat_id
    save_data(data)
    await message.answer(f"Цільовий канал встановлено: {chat_id}")
