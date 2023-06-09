import json
from channels.generic.websocket import AsyncWebsocketConsumer


class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Join the "notification" group
        await self.channel_layer.group_add("notification", self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        # Leave the "notification" group
        await self.channel_layer.group_discard("notification", self.channel_name)

    async def notify_manager(self, event):
        # Send a notification to the manager
        await self.send(text_data=json.dumps({
            "type": "notification",
            "message": event["message"],
        }))
    async def notify_customer(self, event):
        # Send a notification to the manager
        await self.send(text_data=json.dumps({
            "type": "notification",
            "customer": event["customer"],
            "status":event["status"]
        }))
