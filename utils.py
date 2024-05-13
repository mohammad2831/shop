from django.contrib.auth.mixins import UserPassesTestMixin
from kavenegar import *

def send_otp_code(phone_number, code):
    try:
        api = KavenegarAPI('62572B316B5464595767584E7A30645156626D7538426B68515963346436777A43657875314133683178493D')
        params = {
            'sender': '',#optional
            'receptor': phone_number,
            'message':f'your code {code}'
        } 
        response = api.sms_send(params)
        print(response)
    except APIException as e: 
        print(e)
    except HTTPException as e: 
        print(e)


class UserIsAdminMixin(UserPassesTestMixin):
    def test_func(self):
        return self.reques.user.is_autheticated and self.request.user.is_admin