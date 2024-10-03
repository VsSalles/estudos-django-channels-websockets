import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import async_to_sync

class TesteConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_group_name = self.scope['url_route']['kwargs']['nome']
        
        await self.channel_layer.group_add(self.room_group_name, self.channel_name) 
        
        await self.accept()
    
    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)
    
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        
        #envia as mensagens no grupo
        await self.channel_layer.group_send(self.room_group_name, {'type': 'chat_message', 'message': message})
        
    #ouve as mensagens no grupo
    async def chat_message(self, event):
        message = event['message']
        #envia as mensagens no websocket
        await self.send(text_data=json.dumps({'message': message}))