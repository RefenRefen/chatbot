import random

import db


def process(data):
    print(data)
    msg = data['msg'].lower()
    user = data['user'].lower()


    db.push_user_message(user, msg)
    combined_msg = db.get_user_last_messages(user)
    return combined_msg
    # return random.randint(1, 100)


def core(combined_msg):
    # decide accordingly
    return random.randint(1, 100)