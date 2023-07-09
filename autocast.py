import tgcrypto, asyncio
from pyrogram import Client
from pyrogram.enums import ChatType

API_ID = 27472480
API_HASH = "7235e9fd48210c3aa75d4463e6313522"
SESSION = "BQGjMmAAPFmT4fHGgBhWUva_ExExURjTeT1iyBMDvm7yTnDUBwVTSR9StTM2QaCDZI-sgb_6FnjaISmBe-j2t14LCr28noFKi__ZF08vXAwiBD6ojVfAREySr2F02q0xnO0-R5xYgjRRoycaoIUKbVQbunKdStI2ZQyrQcotEx-MggA8FwxIvE5Zp_xcrr4PGBXCVb6o7gbRWeGUzIM-yfDkhlavK9sMMi2M97rPPDjCkl5FNSxz-l6qVHjKJ1R_L00YmcXPZC2Eb0_ZkzwVAjZ2IPsWAN4PkV1TTg1LFsIotzlXrDX8gMZMAMoUYfXUo3y-AroZkaRuBePrXZehtA29DYfRAwAAAAF0TuZVAA"

client = Client('auto-cast', api_id=API_ID, api_hash=API_HASH, session_string=SESSION)

@client.on_message(filters.me & filters.command("forward"))
async def fast_forward(client, message):
   rep = message.reply_to_message
   if not rep:
     await message.reply("please reply to messages!")
     return l
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
      await h.edit("Done ✅")
   except Exception as eor:
      await message.reply(str(eor))

print("Client Started ✓")
client.run()
