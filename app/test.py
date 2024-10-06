import asyncio
from user.db import db


async def do_insert():
    document = {'name': 'first',
                'email': 'test@demo.com', 'password': 'test123'}
    result = await db['user'].insert_one(document)
    print(result)
    print(result.inserted_id)


def insert():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(do_insert())


if __name__ == '__main__':
    insert()

