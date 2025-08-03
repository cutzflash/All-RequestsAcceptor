import logging, asyncio

from os import environ
from pyrogram import Client, filters
from pyrogram.errors import FloodWait

logging.basicConfig(level=logging.ERROR)
       
SESSION = environ.get("SESSION", "BQG0uSsAhIhul2UcSgWjLXpjVFOwLdZgpuRce212MELzHHA54TXlbYpdjLi1WcBPzm7fS3DusOM73JIuOMT3sjq47O90N9iehnBzNfKdWTxvhWv98PZ_TBahlz1FnlN6azPVD_YNr2KqSH1t_GodlBiVJ1fnAYLcrBtaBIjpiv-yK0F5nlvhsMfQkVB0QI4MUHfEvl0C1E5TZYl_4_O-r8i-04hId4wyd6Kkc1NoKs_uMhokcFjdNs5Uxx_aYUtigC_IFaXFgtwOzO0O5EVt6x_2I-9GBjQ6xj6cqbeUsONGwPwc3EY2VtqfidRRWVExsMsH0ucV43wcg_u1tSpPCwQ6kGLUrwAAAAGvnh-HAA")        
User = Client(name="AcceptUser", session_string=SESSION)


@User.on_message(filters.command(["run", "approve"], [".", "/"]))                     
async def approve(client, message):
    Id = message.chat.id
    await message.delete(True)
 
    try:
       while True: # create loop is better techniq to accept within seconds 💀
           try:
               await client.approve_all_chat_join_requests(Id)         
           except FloodWait as t:
               asyncio.sleep(t.value)
               await client.approve_all_chat_join_requests(Id) 
           except Exception as e:
               logging.error(str(e))
    except FloodWait as s:
        asyncio.sleep(s.value)
        while True:
           try:
               await client.approve_all_chat_join_requests(Id)         
           except FloodWait as t:
               asyncio.sleep(t.value)
               await client.approve_all_chat_join_requests(Id) 
           except Exception as e:
               logging.error(str(e))

    msg = await client.send_message(Id, "**Task Completed** ✓ **Approved Pending All Join Request**")
    await msg.delete()


logging.info("Bot Started....")
User.run()







