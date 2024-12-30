import asyncio
from bitmoro import Bitmoro

# async def main():
#     # Replace with your actual API token
#     token="PpvGm90RbURBQlOziA4A-19b51a33ff3306d3eab2895ef6ba979a5cd7f5ce20baaac469b1070b8286"

#     # Instantiate the Bitmoro client
#     client = Bitmoro(token)

#     # # Send a bulk message
#     # bulk_response = await client.send_bulk_message(
#     #     message="ranodm DAHKSB ljsahA random",
#     #     numbers=["9869363132"],
#     # )
#     # print("Bulk message response:", bulk_response)

#     # Send a dynamic message
#     # dynamic_response = await client.send_dynamic_message(
#     #     message="Hello, ${name}!",
#     #     contacts=[
#     #         {"number": "9869363132", "name": "ramu"},
#     #         # {"number": "9862937055"}
#     #     ],
#     #     sender_id="BIT_MORE",
#     #     scheduled_date=int(time.time())+60,  # Optional
#     #     default_value={"name": "User"},
#     #     # callback_url=None  # Optional
#     # )
#     # print("Dynamic message response:", dynamic_response)

#     # OTP Manager example
#     otp_manager = await client.get_otp_manager()

#     # Generate OTP for a phone number
#     phone_number = "9869363132"
#     otp = otp_manager.generate_otp(phone_number)
#     print(f"Generated OTP for {phone_number}: {otp}")

#     # Send OTP via SMS
#     otp_send_response = await otp_manager.send_otp(
#         phone_number=phone_number,
#         message_template="Your OTP is:"+otp,  # Optional prefix or message template
#         # sender_id="YourSenderID"
#     )
#     print("OTP send response:", otp_send_response)
    
    

#     # # Verify OTP (example of how to verify OTP after user enters it)
#     # entered_otp = otp  # For example, let's say the user entered the OTP correctly
#     # otp_verification_response = otp_manager.verify_otp(phone_number, entered_otp)
#     # if otp_verification_response:
#     #     print(f"OTP for {phone_number} verified successfully.")
#     # else:
#     #     print(f"OTP verification failed for {phone_number}.")

# # Run the main async function
# asyncio.run(main())


# async def getUserInput():
#     data = input("otp")


async def get_user_input():
    return input("Enter the OTP you received: ")

async def main():
    token = "PpvGm90RbURBQlOziA4A-19b51a33ff3306d3eab2895ef6ba979a5cd7f5ce20baaac469b1070b8286"
    client = Bitmoro(token)
    otp_manager = await client.get_otp_manager()
    phone_number = "9869363132"
    otp = otp_manager.generate_otp(phone_number)
    print(f"Generated OTP for {phone_number}: {otp}")
    otp_send_response = await otp_manager.send_otp(
        phone_number=phone_number,
        message_template="Your OTP is:" + otp,
    )
    print("OTP send response:", otp_send_response)
    entered_otp = await get_user_input()
    otp_verification_response = otp_manager.verify_otp(phone_number, entered_otp)
    if otp_verification_response:
        print(f"OTP for {phone_number} verified successfully.")
    else:
        print(f"OTP verification failed for {phone_number}.")

asyncio.run(main())
