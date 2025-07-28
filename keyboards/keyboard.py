from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from utils.utils import load_channels


def get_channels_keyboard() -> InlineKeyboardMarkup:
    """
    Створює клавіатуру з кнопками для підписки на канали та перевірки підписки.
    """
    channels = load_channels()
    buttons = []

    for ch in channels:
        url = ch.get("url")
        name = ch.get("name", "Канал")
        if url:
            buttons.append([InlineKeyboardButton(text=name, url=url)])
        else:
            print(f"⚠️ Увага! У каналу '{name}' немає поля 'url'.")

    buttons.append(
        [InlineKeyboardButton(text="✅ Перевірити підписки", callback_data="check_subs")]
    )

    return InlineKeyboardMarkup(inline_keyboard=buttons)
