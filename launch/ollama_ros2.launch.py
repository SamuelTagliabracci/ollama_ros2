from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='ollama_ros2',
            executable='ollama_ros2',
            name='ollama_node',
            output='screen'
        )
    ])
