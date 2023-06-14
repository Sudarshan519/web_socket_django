# import json
# from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync,sync_to_async
@sync_to_async
def createMessage(message):
    chat=Chat.objects.create(message=message) 
    print(chat.message)
    chat.save()
    count=Chat.objects.count()
    # all=Chat.objects.all()
    # for chat in all:
    #     print(chat.message)
    print(count)
    return


@sync_to_async
def allUsers():
    chats=Chat.objects.all()[:10]
    for chat in chats:
        print(chat.message)
    return chats
# class ChatConsumer(WebsocketConsumer):
#     def connect(self):
#         self.room_group_name = 'test'

#         async_to_sync(self.channel_layer.group_add)(
#             self.room_group_name,
#             self.channel_name
#         )

#         self.accept()
   
#     # async def disconnect(self, close_code):
#     #     pass

#     def receive(self, text_data):
#         text_data_json = json.loads(text_data)
#         message = text_data_json['message']

#         async_to_sync(self.channel_layer.group_send)(
#             self.room_group_name,
#             {
#                 'type':'chat_message',
#                 'message':message
#             }
#         )

    
#     def chat_message(self, event):
#         message = event['message']

#         self.send(text_data=json.dumps({
#             'type':'chat',
#             'message':message
#         }))


# chat/consumers.py
# import json

# from asgiref.sync import async_to_sync
# from channels.generic.websocket import WebsocketConsumer
# class ChatConsumer(WebsocketConsumer):
#     def connect(self):
#         self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
#         self.room_group_name = f"chat_{self.room_name}"

#         # Join room group
#         async_to_sync(self.channel_layer.group_add)(
#             self.room_group_name, self.channel_name
#         )

#         self.accept()

#     def disconnect(self, close_code):
#         # Leave room group
#         async_to_sync(self.channel_layer.group_discard)(
#             self.room_group_name, self.channel_name
#         )

#     # Receive message from WebSocket
#     def receive(self, text_data):
#         text_data_json = json.loads(text_data)
#         message = text_data_json["message"]

#         # Send message to room group
#         async_to_sync(self.channel_layer.group_send)(
#             self.room_group_name, {"type": "chat.message", "message": message}
#         )

#     # Receive message from room group
#     def chat_message(self, event):
#         message = event["message"]

#         # Send message to WebSocket
#         self.send(text_data=json.dumps({"message": message}))


# chat/consumers.py
import json

from channels.generic.websocket import AsyncWebsocketConsumer
from .models import Chat

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"chat_{self.room_name}"
        
        
        # chats =sync_to_async(Chat.objects.all)()
        # for chat in chats:
        #     print(chat.message)
        # Join room group
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)

        await self.accept()
        users=await allUsers() 
        for chat in users:
            print(chat.message)
            await self.channel_layer.group_send(
            self.room_group_name, {"type": "chat.message", "message": chat.message}
        )

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        
        message = text_data_json["message"] 
        await createMessage(message=message)
        allUsers()
        # await sync_to_async(Chat.objects.create(message=message))
        # # print(chat.message)
        # # (Chat.objects.create(message=message).save())()
        # users = sync_to_async(Chat.objects.all)()
        # for user in users:
        #     print(user)
        # chat.save()
        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name, {"type": "chat.message", "message": message,}
        )
        

    # Receive message from room group
    async def chat_message(self, event):
        allUsers()
        message = event["message"]

        # Send message to WebSocket
        await self.send(text_data=json.dumps({  'type':'chat',"message": message}))