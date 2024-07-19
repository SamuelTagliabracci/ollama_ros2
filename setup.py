import os
from glob import glob
from setuptools import find_packages, setup

package_name = 'ollama_ros2'

setup(
    name=package_name,
    version='1.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Samuel Tagliabracci',
    maintainer_email='sam@cornelltech.ca',
    description='ROS2 = Ollama LLM',
    license='GNU GENERAL PUBLIC LICENSE',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'ollama_ros2 = ollama_ros2.ollama_ros2:main',
        ],
    },
)
