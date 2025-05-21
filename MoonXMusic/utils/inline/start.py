from pyrogram.types import InlineKeyboardButton

import config
from MoonXMusic import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"], url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text=_["S_B_2"], url=config.SUPPORT_CHAT),
        ],
        [
            InlineKeyboardButton(text="•𝐒ᴜʙsᴄʀɪʙᴇ 𝐓ᴏ 𝐊ɪsᴍɪss•",url=f"https://t.me/kismis2003"),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(text="˹⌯ 𝐒ᴜʙsᴄʀɪʙᴇ 𝐓ᴏ 𝐊ɪsᴍɪss ⌯",url=f"https://t.me/About_Sohini"),
        ],
        [
            InlineKeyboardButton(text=_["S_B_4"], callback_data="settings_back_helper"),
        ],
    ]
    return buttons
