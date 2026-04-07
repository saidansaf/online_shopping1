from aiogram import F,Router
from aiogram.types import Message

router=Router()

@router.message(F.text=="Profile")
async def profile(msg:Message,db):
    tg_id=msg.from_user.id
    data = await db.profile(tg_id)
    await msg.answer(
    f"Sizning malumotlaringiz:\n"
    f"Ismingiz: {data['name']}\n"
    f"Familyangiz: {data['surename']}\n"
    f"Yoshingiz: {data['age']}\n"
    f"Telefon raqamingiz: {data['phone_number']}\n"
    f"Mansabingiz: {data['role']}"
)