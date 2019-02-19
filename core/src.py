# 主要逻辑部分：
# 核心逻辑，代码放在这。
from conf import settings
from lib import common
import time

logger = common.get_logger(__name__)

current_user = {'user': None, 'login_time': None, 'timeout': int(settings.LOGIN_TIMEOUT)}


def auth(func):
    def wrapper(*args, **kwargs):
        if current_user['user']:
            interval = time.time() - current_user['login_time']
            if interval < current_user['timeout']:
                return func(*args, **kwargs)
        name = input('name>>: ')
        password = input('password>>: ')
        db = common.conn_db()
        print('---', db)
        if db.get(name):
            if password == db.get(name).get('password'):
                logger.info('登录成功')
                current_user['user'] = name
                current_user['login_time'] = time.time()
                return func(*args, **kwargs)
        else:
            logger.error('用户名不存在')

    return wrapper


@auth
def buy():
    print('buy...')


@auth
def run():
    print('''
购物
查看余额
转账
    ''')
    while True:
        choice = input('>>: ').strip()
        if not choice: continue
        if choice == '1':
            buy()
