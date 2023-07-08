import tgcrypto, time, asyncio
from pyrogram import Client, idle
from pyrogram.enums import ChatType

API_ID = 27472480
API_HASH = "7235e9fd48210c3aa75d4463e6313522"
SESSION = "BQGjMmAAPFmT4fHGgBhWUva_ExExURjTeT1iyBMDvm7yTnDUBwVTSR9StTM2QaCDZI-sgb_6FnjaISmBe-j2t14LCr28noFKi__ZF08vXAwiBD6ojVfAREySr2F02q0xnO0-R5xYgjRRoycaoIUKbVQbunKdStI2ZQyrQcotEx-MggA8FwxIvE5Zp_xcrr4PGBXCVb6o7gbRWeGUzIM-yfDkhlavK9sMMi2M97rPPDjCkl5FNSxz-l6qVHjKJ1R_L00YmcXPZC2Eb0_ZkzwVAjZ2IPsWAN4PkV1TTg1LFsIotzlXrDX8gMZMAMoUYfXUo3y-AroZkaRuBePrXZehtA29DYfRAwAAAAF0TuZVAA"

chatid = -1801325976
msgid = 2

client = Client('auto-cast', api_id=API_ID, api_hash=API_HASH, session_string=SESSION)
client.start()

while True:
   try:
      print("starting broadcast....")
      for dialog in client.get_dialogs():
         if dialog.chat.type == ChatType.GROUP or dialog.chat.type == ChatType.SUPERGROUP:
            try:
               client.forward_messages(dialog.chat.id, chatid, int(msgid))
               print(f"send in {dialog.chat.title}")
               time.sleep(10)
            except Exception as eor:
               print(eor)
      print("wait for 1hr")
      time.sleep(3600)
   except KeyboardInterrupt:
      client.stop()
