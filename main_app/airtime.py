import africastalking
from django.conf import settings

africastalking.initialize(settings.username, settings.api_key)
airtime = africastalking.Airtime

phone_number = "+256705876748"
amount = 300
currency_code = "UGX"

try:
    response = airtime.send(phone_number=phone_number, amount=amount, currency_code=currency_code)
    print(response)
except Exception as e:
    print(f"Encountered an error while sending airtime. More error details below\n {e}")