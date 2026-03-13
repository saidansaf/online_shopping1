from aiogram import F,Router
from aiogram.types import Message
from filters.adminfilter import RoleFilter
from aiogram.fsm.context import FSMContext
from states.add_product import AddProductState

router=Router()

@router.message(F.text=="Mahsulotlar qoshish",RoleFilter('admin'))
async def add_product(msg:Message,state:FSMContext):
    await msg.answer("Mahsulotni qo'shish uchun iltimos mahsulot nomini kiriting: ")
    await state.set_state(AddProductState.name)

@router.message(AddProductState.name)
async def add_product(msg:Message,state:FSMContext):
    await state.update_data(name=msg.text)
    await msg.answer("mahsulot narxini kiriting: ")
    await state.set_state(AddProductState.price)
    
@router.message(AddProductState.price)
async def add_product(msg:Message,state:FSMContext):
    await state.update_data(price=int(msg.text))
    await msg.answer("mahsulot description kiriting: ")
    await state.set_state(AddProductState.description)

@router.message(AddProductState.description)
async def add_product(msg:Message,state:FSMContext,db):
    await state.update_data(description=msg.text)

    data=await state.get_data()

    await db.add_product(data["name"],data["price"],data["description"])
    await msg.answer("Mahsulot muvaffaqiyatli qo'shildi")
    await state.clear()

