import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.substitutions import Command
from launch_ros.actions import Node

# Función que el sistema de lanzamiento buscará
def generate_launch_description():

    ####### ENTRADAS DE DATOS #####
    urdf_file = 'robot.urdf'
    package_description = "hexapod_description"

    ###### FIN DE ENTRADAS DE DATOS #####
    print("Fetching URDF ==>")
    
    # Ruta correcta al archivo URDF en la carpeta 'src'
    robot_desc_path = os.path.join(get_package_share_directory(package_description),'hexapodv1',urdf_file)
        
    # Nodo de Robot State Publisher
    robot_state_publisher_node = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        name="robot_state_publisher_node",
        emulate_tty=True,
        parameters=[{'use_sim_time': True,
                     'robot_description': open(robot_desc_path).read()}],  # Leer directamente el archivo URDF
        output="screen"
    )

    # Crear y devolver el objeto de descripción de lanzamiento
    return LaunchDescription(
        [
            robot_state_publisher_node
        ]
    )