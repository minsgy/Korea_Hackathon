from users.models import User
from django.shortcuts import get_object_or_404

from twilio.rest import Client

import os
import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# root dir에서 twilio.json을 읽어 auth_token 값을 불러오는 함수
def get_twilio_key(setting):
    print(BASE_DIR)
    twilio_file = os.path.join(BASE_DIR, "twilio.json")

    with open(twilio_file) as file:
        twilio_key = json.loads(file.read())

        try:
            return twilio_key["auth_token"]
        except KeyError:
            error_msg = "Set the {} environment variable".format(setting)
            raise ImproperlyConfigured(error_msg)

accounts_id = 'AC7e395a1420bb05fded85b3d46a896b57'
auth_token = get_twilio_key("TWILIO_KEY")
twilio_sending_number = '+12065905325'

print(auth_token)

client = Client(accounts_id, auth_token)

'''
SMS 알림 서비스 함수
@params : 신청/수락 구분(str), 보내는 사람 id, 받는 사람 id

register :
신청자가 공모전에 팀원으로 참가하는 경우로써 [팀장(to_user_id)]이 [신청자(from_user_id)]에 대한 신청알림을 받음
confirm :
팀장이 신청자를 수락하는 경우로써 [신청자(to_user_id)]가 [팀장(from_user_id)]이 수락했다는 알림을 받음
'''
def sms_reminder(register_or_confirm, from_user_id, to_user_id):
    remind_text = '알림 메시지'

    from_user = get_object_or_404(User, pk=from_user_id)
    to_user = get_object_or_404(User, pk=to_user_id)

    # 신청자가 공모전에 신청 시 팀장에서 문자 전송
    if register_or_confirm == 'register':
        remind_text = from_user.name + '님께서 ' + to_user.name + '님의 공모전에 참가하고 싶어합니다.\n- 나를 표현하는 가장 쉬운 방법, ANASO'
    # 팀장이 신청자가 맘에 들어 신청자의 참여를 수락 시 신청자에게 문자 전송
    elif register_or_confirm == 'confirm':
        remind_text = from_user.name + '님께서 ' + to_user.name + '님의 공모전 참여 신청을 승인하셨습니다.\n- 나를 표현하는 가장 쉬운 방법, ANASO'
    else:
        return "Error : SMS 알림 서비스를 실행할 수 없습니다."

    send_to = '+82' + to_user.phone_number[1:] # 국가번호 포함한 번호로 convert

    message = client.messages.create(
        from_ = twilio_sending_number,
        body = remind_text,
        to = send_to
    )
