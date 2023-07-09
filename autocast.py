import tgcrypto, asyncio
from pyrogram import Client, filters
from pyrogram.enums import ChatType

API_ID = 27472480
API_HASH = "7235e9fd48210c3aa75d4463e6313522"
SESSION = "BQGjMmAAlhiYia_kqQrJkLHNiqhqS0XtAS1CUoclegw30dYr4s7DSheLuW9zX3gZuJW76OLEZ7zveJdGuwoD8BJDaQXw6lFzlL7OJSSbRa6RiMKHq_1GpFRfh5x4vQdFJAnTuwADlw_YzQk-qdv99-y-8cniRMyGcRWaIwGoXaY_u6BIzJnZWJu0zW1AT_WAzU8umVJF1-RUncPEa2xOyg1U1DAY5ReF9sE6niAB4Of5Npu8cuuOpR_fiE1sH44hU-QClXm_g_SE-Cas3iNnEcw0_iENud6TEBn5K2-JzqqEksGgsVf9rPy-hCURuEfFVrsZW5V9EClmqVJEStBH6rYopEMJ-wAAAAF0TuZVAA"

client = Client('auto-cast', api_id=API_ID, api_hash=API_HASH, session_string=SESSION)

@client.on_message(filters.private & filters.all)
async def fast_forward(client, message):
   if message.from_user.id == 5802073021:
     try:
       h = await message.reply("broadcast....")
       async for dialog in client.get_dialogs():
          if dialog.chat.type == ChatType.GROUP or dialog.chat.type == ChatType.SUPERGROUP:
             try:
                await message.forward(dialog.chat.id)
                print(f"send in {dialog.chat.title}")
                await asyncio.sleep(5)
             except Exception as eor:
                print(eor)
       await h.edit("Done ✅")
     except Exception as eor:
      await message.reply(str(eor))

print("Client Started ✓")
client.run()
