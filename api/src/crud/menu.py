from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.db.models.menu import Menu


async def create_menu(session: AsyncSession, menu_data: dict) -> Menu:
    """ Create or update a menu in the database."""
    menu_exists = await session.execute(
        select(Menu).where(Menu.id == menu_data["id"])
    )
    menu_exists = menu_exists.scalar_one_or_none()

    if menu_exists is not None:
        menu = menu_exists
        menu.sys_name = menu_data["sys_name"]
        menu.name = menu_data["name"]
        menu.price = menu_data["price"]
        menu.vat_rate = menu_data["vat_rate"]
    else:
        menu = Menu(**menu_data)

    session.add(menu)
    await session.commit()
    await session.refresh(menu)
    return menu

async def exists(session: AsyncSession, menu_id: int) -> bool:
    """ Check if a menu exists in the database. """
    result = await session.execute(select(Menu).where(Menu.id == menu_id))
    return result.scalar_one_or_none() is not None

async def get_all_menus(session: AsyncSession) -> list[Menu]:
    """ Retrieve all menus from the database. """
    result = await session.execute(select(Menu))
    return result.scalars().all()