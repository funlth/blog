import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer, AsyncJsonWebsocketConsumer, AsyncWebsocketConsumer
import datetime
import time


class ChatConsumer(WebsocketConsumer):

    # 默认用户名：
    DEFAULT_USERNAME = '无名氏'

    # websocket建立连接时执行方法
    def connect(self):
        # 从url里获取聊天室名字，为每个房间建立一个频道组
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name


        # 将当前频道加入频道组
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,   # 房间标识
            self.channel_name  # 个人标识
        )

        # 接受所有websocket请求
        self.accept()



    # websocket断开时执行方法
    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

        # 获取用户名，如果未指定则使用默认用户名

    def get_username(self, text_data_json):
        if 'username' in text_data_json:
            # a = 0;
            # b = a+1;
            # while b>0:
            return text_data_json['username']
        else:
            return self.DEFAULT_USERNAME


    # 从websocket接收到消息时执行函数
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        username = self.get_username(text_data_json)

        # 发送消息到频道组，频道组调用chat_message方法
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'username':username,
                'message': message
            }
        )

    # 从频道组接收到消息后执行方法
    def chat_message(self, event):
        message = event['message']
        username = event['username']
        datetime_str = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # 格式化消息
        formatted_message = f'[{datetime_str}] {username}: {message}'

        # 通过websocket发送消息到客户端
        self.send(text_data=json.dumps({
            'message': formatted_message
        }))
