# Bitmoro Python Library

A Python library for sending messages and handling OTP (One-Time Password) operations using the **Bitmoro** API.

## Table of Contents
- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
  - [Initializing the Client](#initializing-the-client)
  - [Sending OTPs](#sending-otps)
  - [Sending Bulk Messages](#sending-bulk-messages)
  - [Sending Dynamic Messages](#sending-dynamic-messages)
- [Callback URL Response](#callback-url-response)
- [Dependencies](#dependencies)
- [Example](#example)
- [License](#license)

---

## Introduction
The **Bitmoro Python Library** provides a simple interface for:
1. Sending bulk SMS.
2. Sending dynamic personalized messages.
3. Managing OTP operations (generation, sending, and verification).

This library integrates seamlessly with the **Bitmoro API**, enabling efficient SMS services for your application.

## Installation
To install the library, use the following command:

```bash
pip install bitmoro
```

## Usage

### Initializing the Client
To begin, import the `Bitmoro` class and initialize it with your API token:

Follow the link to get API key. [API Docs](https://bitmoro.com/blog/api-integration-for-bulk-sms-service-with-bitmoro)

```python
from bitmoro.bitmoro import Bitmoro

token = "<YOUR_API_TOKEN>"
client = Bitmoro(token)
```

### Sending OTPs
You can generate, send, and verify OTPs as shown below:

#### Generating an OTP
```python
otp_manager = await client.get_otp_manager()
phone_number = "98XXXXXXXX"
otp = otp_manager.generate_otp(phone_number)
print(f"Generated OTP for {phone_number}: {otp}")
```

#### Sending an OTP
```python
otp_send_response = await otp_manager.send_otp(
    phone_number=phone_number,
    message_template=f"Your OTP is: {otp}"
)
print("OTP send response:", otp_send_response)
```

#### Verifying an OTP
```python
entered_otp = await get_user_input()  # Async function to get user input
otp_verification_response = otp_manager.verify_otp(phone_number, entered_otp)
if otp_verification_response:
    print("OTP verified successfully!")
else:
    print("OTP verification failed.")
```

### Sending Bulk Messages
To send bulk messages:
import time

```python
bulk_response = await client.send_bulk_message(
    message="Hello, this is a test message", #required
    numbers=["98XXXXXXXX"],  #required
    sender_id="BIT_MORE",  #optional
    scheduled_date=int(time.time()*1000) + 60*1000, #unix time stamp in millisecond of future date. Optional
    callback_url="https://your-callback-url.com/test" #optional
)
print("Bulk message response:", bulk_response)
```

### Sending High Priority Message

For high priority message, use the `send_high_priority_message` method:
These messages are sent with high priority and are delivered instantly unlike others.

```python
response = await client.send_high_priority_message(
    message_template="TEST!",
    phone_number="98xxxxxxxx",
    sender_id="joe_alert",
)
print("Message response:",response)
```

### Sending Dynamic Messages
For personalized messages, use the `send_dynamic_message` method:

```python
dynamic_response = await client.send_dynamic_message(
    message="Hello, ${name}!",  #required
    contacts=[
        {"number": "98XXXXXXXX", "name": "John"},
        {"number": "98XXXXXXXX"}
    ],   #required
    sender_id="BIT_MORE", #optional
    scheduled_date=int(time.time()*1000) + 60*1000,  #unix time stamp in millisecond of future date. Optional
    default_value={"name": "User"}, #optional
    callback_url= "https://your-callback-url.com/test" #optional
)
print("Dynamic message response:", dynamic_response)
```

## Callback URL Response
When a callback URL is provided, it receives a POST request containing the following information:

```json
{
  "messageId": "unique_message_id",
  "message": "Hello, this is a test message",
  "status": "sent",
  "report": [
    {
      "number": "98XXXXXXXX",
      "status": "success",
      "message": "Sent",
      "creditCount": 1
    }
  ],
  "senderId": "BIT_MORE",
  "deliveredDate": "2025-01-16T03:53:22.188Z",
  "refunded": 0
}
```

## Dependencies
This library requires Python 3.7+ and the `bitmoro` package. Install it using:

```bash
pip install bitmoro
```

## Example
Here is a complete example of sending an OTP and verifying it:

```python
import asyncio
from bitmoro import Bitmoro

async def main():
    token = "<YOUR_API_TOKEN>"
    client = Bitmoro(token)
    
    otp_manager = await client.get_otp_manager()
    phone_number = "98XXXXXXXX"
    otp = otp_manager.generate_otp(phone_number)
    print(f"Generated OTP for {phone_number}: {otp}")
    
    #Sending single message
    otp_send_response = await otp_manager.send_otp(
        phone_number=phone_number,
        message_template=f"Your OTP is: {otp}"
    )
    print("OTP send response:", otp_send_response)

    entered_otp = input("Enter the OTP you received: ")
    otp_verification_response = otp_manager.verify_otp(phone_number, entered_otp)
    if otp_verification_response:
        print("OTP verified successfully!")
    else:
        print("OTP verification failed.")

    #sending Bulk Message
    BULK MESSAGE 
    
    bulk_response = await client.send_bulk_message(
    message="ranodm ",
    numbers=["98XXXXXXXX"],
    callback_url="https://demo.requestcatcher.com/test",
    scheduledDate=int(time.time()*1000) + 60*1000,
    )
    print("Bulk message response:", bulk_response)
    
    # Send a dynamic message
    dynamic_response = await client.send_dynamic_message(
        message="Hello, ${name}!",
        contacts=[
            {"number": "98XXXXXXXX", "name": "ramu"},
            {"number": "98XXXXXXXX"}
        ],
        sender_id="BIT_MORE",
        scheduledDate=int(time.time()*1000) + 60*1000,  # Optional
        default_value={"name": "User"},
        # callback_url=None  # Optional
    )
    print("Dynamic message response:", dynamic_response)
    

asyncio.run(main())
```

## License
This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).