import requests

print(
    "[!] Before entering your IP address, hold down the power button on your Nanoleaf product for 5-7 seconds. Once you see a flashing light, proceed with the script."
)

ipInput = input(
    "[?] Enter your Nanoleaf product IP address (can be found in the Nanoleaf app or through your router settings): "
)
try:
    req = requests.post(f"http://{ipInput}:16021/api/v1/new")

    if req.status_code == 200:
        print(
            f'[!] Succesfully generated authorzation token: {req.json()["auth_token"]}'
        )
        print("[!] Make sure to put this in your config.py file so the bot can run.")
    elif req.status_code == 403:
        print(
            "[!] Your product was not in pairing mode at the time of connection. Make sure to hold down the power button for 5-7 seconds, and try again."
        )
except Exception as e:
    print(
        "[!] Couldn't connect to your Nanoleaf product. Make sure you have the correct IP address."
    )

