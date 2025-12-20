import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():
    # 1. 패키지 경로 설정
    gazebo_package = FindPackageShare('indy_gazebo')
    
    # 2. 월드 파일 경로 설정 (test.world)
    # indy_gazebo/worlds/test.world 파일이 실제로 존재하는지 확인하세요.
    world_file_name = 'test.world'
    world_path = os.path.join(
        get_package_share_directory('indy_gazebo'), 
        'worlds', 
        world_file_name
    )

    # 3. Gazebo 서버 및 클라이언트 실행 (World 인자 전달)
    # Gazebo nodes
    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            [os.path.join(get_package_share_directory('gazebo_ros'), 'launch', 'gazebo.launch.py')]
        ),
        launch_arguments={
            'world': world_path,
            'verbose': 'true'  # 이 줄을 추가하여 상세 로그를 켭니다.
        }.items(),
    )
    
    return LaunchDescription([
        gazebo
    ])