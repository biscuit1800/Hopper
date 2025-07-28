from aiogram import Router, types, F
from aiogram.exceptions import TelegramForbiddenError, TelegramBadRequest
from utils.utils import load_data

router = Router()
user_invite_links = {}


@router.callback_query(F.data == "check_subs")
async def check_subscriptions(callback: types.CallbackQuery):
    bot = callback.bot
    user_id = callback.from_user.id

    data = load_data()
    channels = data.get("channels", [])
    target_channel = data.get("target_channel")

    if not target_channel:
        await callback.message.answer("⚠️ Цільовий канал не налаштований.")
        await callback.answer()
        return

    not_subscribed = []
    for ch in channels:
        chat_id = ch.get("chat_id")
        name = ch.get("name", "Канал")
        if not chat_id:
            not_subscribed.append(name)
            continue
        try:
            member = await bot.get_chat_member(chat_id=chat_id, user_id=user_id)
            if member.status not in ("member", "administrator", "creator"):
                not_subscribed.append(name)
        except (TelegramForbiddenError, TelegramBadRequest):
            not_subscribed.append(name)
        except Exception as e:
            print(f"Тимчасова помилка при перевірці {chat_id}: {e}")
            await callback.message.answer(
                "⚠️ Виникла тимчасова проблема з перевіркою підписки. Спробуйте ще раз пізніше."
            )
            await callback.answer()
            return

    if not_subscribed:
        await callback.message.answer(
            "❌ Ви ще не підписалися на:\n" + "\n".join(f"• {name}" for name in not_subscribed)
        )
        await callback.answer()
        return

    invite_link = user_invite_links.get(user_id)
    if not invite_link:
        try:
            invite = await bot.create_chat_invite_link(chat_id=target_channel, member_limit=1)
            invite_link = invite.invite_link
            user_invite_links[user_id] = invite_link
        except Exception as e:
            await callback.message.answer("⚠️ Не вдалося створити посилання на цільовий канал.")
            print(f"Помилка створення інвайту: {e}")
            await callback.answer()
            return

    await callback.message.answer(
        f"Дякуємо за підписку! Ось ваше персональне одноразове посилання:\n{invite_link}"
    )
    await callback.answer()
