# Identify the parameters to be changed in ARGoS

from lxml import etree
import os
import shutil

def copy_file(source, destination):
    """
    Copy a source file to a destination location.
    
    Args:
    - source (str): Path to the source file.
    - destination (str): Path where the source file should be copied to.
    """
    shutil.copy2(source, destination)
    print(f"File '{source}' copied to '{destination}'!")

# Example usage:
# copy_file("path_to_source_file.txt", "path_to_destination_directory_or_file")


def modify_argos_attribute(file_name, tag, attrib, val):
    parser = etree.XMLParser(remove_blank_text=True)
    tree = etree.parse(file_name, parser)
    root = tree.getroot()
    for element in root.iter(tag=tag):
        print(element.tag)
        print(element.attrib)
        element.set(attrib, val)
        print(element.attrib)
        with open(file_name, 'wb') as f:
            tree.write(f, pretty_print=True)
        break


def argos_configurator():
    file_name = ""  # Add filename here
    # Map: Map1

    # Length / Width of the Map: 8x7 something

    # Number of robots: 3
    # ARGoS parameters : entity quantity="11", under arena configuration
    no_of_robots = 3
    modify_argos_attribute(file_name, 'entity', 'quantity', str(no_of_robots))
    # Swarm Density: 10
    # We need to use a script to generate these parameters, which is
    # given by the collective perception library
    swarm_density = 10
    # Number of robots to shut off: 1 ARGoS parameters :
    # <robot_disabling amount="5" sim_clock_time="51" />
    no_of_robots_to_shutoff = 1
    modify_argos_attribute(file_name, 'robot_disabling', 'amount',
                           str(no_of_robots_to_shutoff))
    # Time of the total simulation: 5 minutes (300 seconds)
    # ARGoS parameters : <experiment length="100"
    time_of_simulation = 300
    modify_argos_attribute(file_name, 'experiment', 'length',
                           str(time_of_simulation))
    # Time of robot shut down: 2.5-minute mark (150 seconds) ARGoS
    # parameters : <robot_disabling amount="5" sim_clock_time="51" />
    time_of_robot_shutdown = 150
    modify_argos_attribute(file_name, 'robot_disabling', 'sim_Write results file to current directoryclock_time',
                           str(time_of_robot_shutdown))
    # Area on fire: 80%
    # ARGoS parameters = fill_ratio_range
    area_on_fire = 0.8
    modify_argos_attribute(file_name, 'fill_ratio_range', 'min', str(area_on_fire))
    modify_argos_attribute(file_name, 'fill_ratio_range', 'max', str(area_on_fire))
    modify_argos_attribute(file_name, 'fill_ratio_range', 'steps', str(1))
    # Robot sensors accuracy: 95%
    # <sensor_probability_range min="0.525" max="0.975" steps="2" />
    # Evenly spaced experiments within the range.
    robot_sensor_accuracy = 0.95
    modify_argos_attribute(file_name, 'sensor_probability_range', 'min',
                           str(robot_sensor_accuracy))
    modify_argos_attribute(file_name, 'sensor_probability_range', 'max',
                           str(robot_sensor_accuracy))
    modify_argos_attribute(file_name, 'sensor_probability_range', 'steps',
                           str(2))


def ensure_folder_exists(folder_name):
    """
    Ensure that a certain folder exists in the current working directory.
    Args:
    folder_name: Name of the folder

    returns: folder absolute path
        
    """
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
        print(f"Folder '{folder_name}' created!")
        return os.path.abspath(folder_name)
    else:
        print(f"Folder '{folder_name}' already exists!")
        return os.path.abspath(folder_name)

def copy_file(source, destination):
    """
    Copy a source file to a destination location.
    
    Args:
    - source (str): Path to the source file.
    - destination (str): Path where the source file should be copied to.
    """
    shutil.copy2(source, destination)
    print(f"File '{source}' copied to '{destination}'!")


if __name__ == '__main__':
    experiment_data_folder_name = "experiment_data"
    experiment_output_folder_name = "experiment_output"
    # Ensure that the experiment data folder exists
    experiment_data_folder_path = ensure_folder_exists(experiment_data_folder_name)
    experiment_output_folder_path = ensure_folder_exists(experiment_output_folder_name)
    # Identify the parameters to be changed
    no_of_robots = [5,10]
    sensor_accuracy = [0.7, 0.9]
    communication_range = [0.4, 0.7]
    # In the experiment_data folder, create experiment files containing
    # one experiment per combination for $2_k$ factorial designs
    # First, copy the model argos file, with the name of the experiment 
    # where the name is in terms of the experiment parameters
    # Then, modify the attributes to be modified

    for r in no_of_robots:
        for s in sensor_accuracy:
            for c in communication_range:
                src_file = "src/kheperaiv_5_tiled.argos"
                experiment_file_string =  "R{}-S{}-C{}".format(r,s,c).replace('.', '_')
                experiment_file = os.path.join(experiment_data_folder_name, experiment_file_string+'.argos')
                copy_file(src_file, experiment_file)
                # Modify number of robots in this file
                modify_argos_attribute(experiment_file, 'entity', 'quantity', str(r))
                # Modify sensor accuracy in this file
                modify_argos_attribute(experiment_file, 'sensor_probability_range', 'min', str(s))
                modify_argos_attribute(experiment_file, 'sensor_probability_range', 'max', str(s))
                modify_argos_attribute(experiment_file, 'sensor_probability_range', 'steps', str(-2))
                # Modify communication range
                modify_argos_attribute(experiment_file, 'kheperaiv', 'rab_range', str(c))

                # Modify the results file parameter
                modify_argos_attribute(experiment_file, 'param', 'csv_path', 
                                       os.path.join(experiment_output_folder_path, experiment_file_string+'.csv'))
