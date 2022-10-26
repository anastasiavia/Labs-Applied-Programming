from schemas import *
from manager import DBManager
import datetime


if __name__ == '__main__':
    #creation of db session
    db = DBManager()
    session = db.session()


    item = Item(
        iditem=2,
        name='notepad',
        amount=8,
        price=300,
        photoUrls="htttcar/skak.a/ahksk",
        status="available",
        category="uni stuff"
    )

    item1 = Item(
        iditem=3,
        name='pencil',
        amount=8,
        price=300,
        photoUrls="htttcar/skak.a/ahksk",
        status="available",
        category="uni stuff"
    )


    address = Address(
        idaddress=2,
        street="Korolenka",
        city="Lviv",
        house_number=1
    )

    address1 = Address(
        idaddress=3,
        street="Korolenka",
        city="Lviv",
        house_number=6
    )


    user = User(
        iduser=2,
        username='sashaa',
        firstname="Sasha",
        lastname="Kylie",
        email="sasha@gmail.com",
        password="1238220",
        phone="_380679547215",
        address_id=2
    )

    user1 = User(
        iduser=3,
        username='aniaa',
        firstname="Ania",
        lastname="Kylie",
        email="sasha@gmail.com",
        password="1238220",
        phone="_380679547215",
        address_id=3
    )


    order = Order(
        idorder=2,
        quantity=6,
        orderDate=datetime.date(2022, 5, 2),
        status="packed",
        payment_method="later",
        item_id=2,
        user_id=2,
    )

    order1 = Order(
        idorder=3,
        quantity=6,
        orderDate=datetime.date(2022, 6, 2),
        status="packed",
        payment_method="later",
        item_id=3,
        user_id=3,
    )


    order2 = Order(
        idorder=4,
        quantity=6,
        orderDate=datetime.date(2022, 6, 2),
        status="packed",
        payment_method="later",
        item_id=2,
        user_id=2,
    )

    session.add(item)
    session.add(item1)
    session.commit()

    session.add(address)
    session.add(address1)
    session.commit()

    session.add(user)
    session.add(user1)
    session.commit()

    session.add(order)
    session.add(order1)
    session.add(order2)
    session.commit()



    session.close()
