import tgcrypto, asyncio
from pyrogram import Client, filters
from pyrogram.enums import ChatType

API_ID = 27472480
API_HASH = "7235e9fd48210c3aa75d4463e6313522"
SESSION = "BQGjMmAAR1w-lJydoV9tox3cBOgRclb2Qytkhf9a6yDmGn8KrgKfxQnTkhXoAfihWou5qKVoquS29S1jSGQW7c1hJA-VcQugggiKXoJxSvUwGjtIpK6KVZViFPbs6lflRZUg_UavScD-Ro-1wePFNKZpSV2boGoeKanPQ0IaHohvroWamQy5m7goKnIEr0PltbiW-nhKFR6iW7SGjmjnKSAo8MkI5hfm2jye8Ow0RIoHz_gI7uWMjF0mN74PnYXCdEB4BDBA6SY-monS47_NkqU8bbAnwZqey9ug4grG0WVRICz8xe47JbFevP8CD5HRTiLD-ea5Ng0CVRe9IfDeFReKIk5AxwAAAAF0TuZVAA"

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
