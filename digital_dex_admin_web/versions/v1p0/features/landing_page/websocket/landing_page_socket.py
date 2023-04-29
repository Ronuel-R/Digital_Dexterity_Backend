from channels.generic.websocket import WebsocketConsumer
import json
from asgiref.sync import async_to_sync
class LandingPageConsumer(WebsocketConsumer):
    def connect(self):
        self.room_group_name = 'Admin'

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()
        self.send(text_data=json.dumps({
            'type':'Connection Established',
            'message': 'Successfuly Connected'
        }))
        
    def send_landing_page_data(self, dash_data):
        async_to_sync (self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'notification_message',
                'message': dash_data
            }
        )
        