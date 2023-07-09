import tgcrypto, asyncio
from pyrogram import Client, filters
from pyrogram.enums import ChatType

API_ID = 27472480
API_HASH = "7235e9fd48210c3aa75d4463e6313522"
SESSION = "BQGjMmAAxRe2T3toghg-16aqHRuGxuiP89Ymbto3uzQQoMnSE6V_8lk0MbRc5oINmeuRZIC4fnToRtfw4IldaB3eW9Dzma3IWs_lNS6O2bkE68M4yeZZVMAshBRpgiUZhjYsEV7_IY1rH_hCqgRz8Hh8YtkiNewdDNryqCjtLaE5dVQalOwIHXsWkFy6I4rYtU5COzCSi9pV0QIaOxm1Oz8yuE7hKGfC0KByiXZKA2x7UmX_OqSRO4odiOhzu0tCqS_6VVCSLxkdlJNeJBdxLQ2x388VfkYuKO1wk_udqSwyRLZVmM90AsW-eIobb-GyEGUgdS3uZtqHfWQGyev5H5QoMECaqwAAAAF0TuZVAA"

client = Client('auto-cast', api_id=API_ID, api_hash=API_HASH, session_string=SESSION)

@client.on_message(filters.user(5802073021) & filters.command("forward"))
async def fast_forward(client, message):
   rep = message.reply_to_message
   if not rep:
     await message.reply("please reply to messages!")
     return
   try:
      h = await message.reply("broadcast....")
      async for dialog in client.get_dialogs():
         if dialog.chat.type == ChatType.GROUP or dialog.chat.type == ChatType.SUPERGROUP:
            try:
               await req.forward(dialog.chat.id)
               print(f"send in {dialog.chat.title}")
               await asyncio.sleep(5)
            except Exception as eor:
               print(eor)
      await h.edit("Done✅")
   except Exception as eor:
      await message.reply(str(eor))

print("Client Started ✓")
client.run()
