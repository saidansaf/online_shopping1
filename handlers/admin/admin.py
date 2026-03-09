from aiogram import F,Router
from aiogram.types import Message,CallbackQuery

from keyboards.reply import admin_panel
from keyboards.inline import users_inline,user_action
from filters.adminfilter import RoleFilter

router=Router()

@router.message(F.text=="Admin panel",RoleFilter('admin'))
async def admin(msg:Message):
    await msg.answer(text=f"Admin panelga xush kelibsiz: ",reply_markup=admin_panel())

@router.message(F.text=="Users",RoleFilter('admin'))
async def user(msg:Message,db):
    users= await db.get_users()
    await msg.answer("Foydalanuvchilar ro'yxati: ",reply_markup=users_inline(users))

@router.callback_query(F.data.startswith("user_"),RoleFilter('admin'))
async def user(call:CallbackQuery):
    user_id= int(call.data.split("_")[1]) #["user","16"]
    await call.message.answer("User rolini tanlang: ",reply_markup=user_action(user_id))
    await call.answer()

@router.callback_query(F.data.startswith("changeto_"),RoleFilter('admin'))
async def user(call:CallbackQuery,db): 
    _,role,user_id=call.data.split("_")
    user_id=int(user_id)
    await db.update_role(user_id,role)
    await call.message.answer("Role o'zgartirildi!")
    await call.answer()
