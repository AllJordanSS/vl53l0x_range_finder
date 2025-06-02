import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    # Obtém o caminho para o diretório share do pacote range_finder
    package_dir = get_package_share_directory('range_finder')

    # Caminho para o arquivo YAML de configuração
    params_file = os.path.join(package_dir, 'settings', 'setting.yaml')

    return LaunchDescription([
        Node(
            package='range_finder',
            executable='range_finder_node',
            name='range_finder_node',
            output='screen',
            parameters=[params_file],  # Carrega os parâmetros do arquivo YAML
        )
    ])