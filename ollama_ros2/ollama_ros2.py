# gpt_ros2/gpt_ros2/gpt_client.py

#ros2 pkg create --build-type ament_python ollama_ros2 --dependencies rclpy
#pip install requests
#pip install ollama

import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import ollama

class gptClient(Node):
    def __init__(self):
        super().__init__('gpt_client')
        self.publisher_ = self.create_publisher(String, '/gpt/response', 10)
        self.subscription = self.create_subscription(
            String,
            '/gpt/prompt',
            self.prompt_callback,
            10
        )

#        self.model="llama3"
#        self.model="wizardlm-uncensored"
        self.model="dolphin-phi"

        self.system="You are a T100 Terminator. Do not use any emoties."

        self.stream=False

        self.gpt_client = ollama.Client(host='http://localhost:11434')
        self.get_logger().info(f'GPT Client Online')

    def prompt_callback(self, msg):
        if msg.data != "":
          prompt = msg.data
          response = self.gpt_client.chat(model=self.model, messages=[
            {
              'role': 'system',
              'content': self.system,
            },
            {
              'role': 'user',
              'content': prompt,
            },
          ], stream = self.stream)

        if response and self.stream == False:
            response_msg = String()
            response_msg.data = response['message']['content']
            self.publisher_.publish(response_msg)
            self.get_logger().info(f'Published response: {response}')
        else:
            self.get_logger().error('Failed to get response from gpt API')

def main(args=None):
    rclpy.init(args=args)
    gpt_client = gptClient()
    rclpy.spin(gpt_client)
    gpt_client.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
