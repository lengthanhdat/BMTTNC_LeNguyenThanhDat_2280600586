import tornado.ioloop
import tornado.websocket

class WebSocketClient:
    def __init__(self, io_loop):
        self.connection = None  
        self.io_loop = io_loop
        
    def start(self):
        
        self.connect_and_read()
        
    def stop(self):
        
        self.io_loop.stop()
        
    def connect_and_read(self): 
        print("Đang cố gắng kết nối và đọc tin nhắn...")
        tornado.websocket.websocket_connect( 
            url=f"ws://localhost:8888/websocket/",
            callback=self.maybe_retry_connection,
            on_message_callback=self.on_message,
            ping_interval=10,
            ping_timeout=30,
        )
        
    def maybe_retry_connection(self, future) -> None: 
        try:
            self.connection = future.result()
            print("Đã kết nối thành công tới server!")

            self.connection.read_message(callback=self.on_message)
        except Exception as e: 
            print(f"Không thể kết nối lại, thử lại sau 3 giây... Lỗi: {e}")
            self.io_loop.call_later(3, self.connect_and_read) 

    def _disconnect(self): 
        if self.connection:
            print("Ngắt kết nối khỏi server.")
            self.connection.close()
            self.connection = None 
            
    def on_message(self, message):
        if message is None: 
            print("Server đã đóng kết nối. Đang cố gắng kết nối lại...")
            self._disconnect() 
            self.io_loop.call_later(1, self.connect_and_read) 
            return

        print(f"Nhận được từ server: {message}")

        if self.connection: 
            self.connection.read_message(callback=self.on_message)

def main():
    io_loop = tornado.ioloop.IOLoop.current()
    client = WebSocketClient(io_loop)
    io_loop.add_callback(client.start) 
    io_loop.start()

if __name__ == "__main__":
    main()