from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


# 👤 USERS LIST
def users_inline(users):
    keyboard = []

    for user in users:
        keyboard.append([
            InlineKeyboardButton(
                text=f"{user['name']} {user['surename']} ({user['role']})",
                callback_data=f"user_{user['id']}"
            )
        ])

    return InlineKeyboardMarkup(inline_keyboard=keyboard)


# 👤 USER ACTION
def user_action(user_id):
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="Admin",
                    callback_data=f"changeto_admin_{user_id}"
                ),
                InlineKeyboardButton(
                    text="User",
                    callback_data=f"changeto_user_{user_id}"
                )
            ]
        ]
    )


# 🛍 PRODUCT LIST
def product_inline(products):
    keyboard = []

    for product in products:
        keyboard.append([
            InlineKeyboardButton(
                text=f"{product['name']} ({product['price']} so'm)",
                callback_data=f"product_{product['id']}"
            )
        ])

    return InlineKeyboardMarkup(inline_keyboard=keyboard)


# 🛠 PRODUCT ACTION
def product_action(product_id):
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="✏️ Edit",
                    callback_data=f"edit_product_{product_id}"
                ),
                InlineKeyboardButton(
                    text="🗑 Delete",
                    callback_data=f"delete_product_{product_id}"
                )
            ]
        ]
    )


# 🛒 SAVAT (CART)
def savat_inline(products):
    keyboard = []

    for product in products:
        keyboard.append([
            InlineKeyboardButton(
                text=f"{product['name']} ({product['price']} so'm)",
                callback_data=f"view_{product['id']}"
            ),
            InlineKeyboardButton(
                text="❌",
                callback_data=f"remove_product_{product['id']}"
            )
        ])

    keyboard.append([
        InlineKeyboardButton(
            text="🛍 Buyurtma berish",
            callback_data="order"
        )
    ])

    return InlineKeyboardMarkup(inline_keyboard=keyboard)


# 💳 PAYMENT
def payment_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="💳 Karta orqali to'lov",
                    callback_data="pay_card"
                )
            ],
            [
                InlineKeyboardButton(
                    text="💵 Naqd to'lov",
                    callback_data="pay_cash"
                )
            ]
        ]
    )