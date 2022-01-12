import requests
import json

# Checks if the item is available for delivery, pickup, or shipping. Returns true if it is
def product_available(url, headers):
    try:
        response = requests.get(url, headers=headers)
    except requests.exceptions.RequestException as e:  # This is the correct syntax
        raise SystemExit(e)
    
    response_formatted = json.loads(response.content.decode('utf-8-sig').encode('utf-8'))

    response_info = response_formatted['responseInfos'][0]
    delivery = response_info['deliveryEligible']
    pickup = response_info['pickupEligible']
    shipping = response_info['shippingEligible']

    return delivery or pickup or shipping
