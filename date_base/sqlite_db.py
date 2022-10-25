import sqlite3 as sq

def sql_start():
    global base, cur
    base = sq.connect('marsian_sketch.db')
    cur = base.cursor()
    if base:
        print('Date base connected Ok!')
    base.execute('CREATE TABLE IF NOT EXISTS menu(notification TEXT, time TEXT)')
    base.commit()

async def sql_add_command(state):
    async with state.proxy() as date:
        cur.execute('INSERT INTO menu VALUES (?, ?)', tuple(date.values()))
        base.commit()








