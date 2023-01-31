# Identify the parameters to be changed in ARGoS

import xml.etree.ElementTree as ET
import os


def modify_argos_attribute(tag, attrib, val):
    file_name = 'src/kheperaiv_5_tiled.argos'
    tree = ET.parse(file_name)
    root = tree.getroot()
    for element in root.iter(tag=tag):
        print(element.tag)
        print(element.attrib)
        element.set(attrib, val)
        print(element.attrib)
        with open(file_name, 'wb') as f:
            tree.write(f)
        break


def argos_configurator():
    # Map: Map1

    # Length / Width of the Map: 8x7 something

    # Number of robots: 3
    # ARGoS parameters : entity quantity="11", under arena configuration
    no_of_robots = 3
    modify_argos_attribute('entity', 'quantity', str(no_of_robots))
    # Swarm Density: 10
    # We need to use a script to generate these parameters, which is
    # given by the collective perception library
    swarm_density = 10
    # Number of robots to shut off: 1 ARGoS parameters :
    # <robot_disabling amount="5" sim_clock_time="51" />
    no_of_robots_to_shutoff = 1
    modify_argos_attribute('robot_disabling', 'amount',
                           str(no_of_robots_to_shutoff))
    # Time of the total simulation: 5 minutes (300 seconds)
    # ARGoS parameters : <experiment length="100"
    time_of_simulation = 300
    modify_argos_attribute('experiment', 'length',
                           str(time_of_simulation))
    # Time of robot shut down: 2.5-minute mark (150 seconds) ARGoS
    # parameters : <robot_disabling amount="5" sim_clock_time="51" />
    time_of_robot_shutdown = 150
    modify_argos_attribute('robot_disabling', 'sim_clock_time',
                           str(time_of_robot_shutdown))
    # Area on fire: 80%
    # ARGoS parameters = fill_ratio_range
    area_on_fire = 0.8
    modify_argos_attribute('fill_ratio_range', 'min', str(area_on_fire))
    modify_argos_attribute('fill_ratio_range', 'max', str(area_on_fire))
    modify_argos_attribute('fill_ratio_range', 'steps', str(1))
    # Robot sensors accuracy: 95%
    # <sensor_probability_range min="0.525" max="0.975" steps="2" />
    # Evenly spaced experiments within the range.
    robot_sensor_accuracy = 0.95
    modify_argos_attribute('sensor_probability_range', 'min',
                           str(robot_sensor_accuracy))
    modify_argos_attribute('sensor_probability_range', 'max',
                           str(robot_sensor_accuracy))
    modify_argos_attribute('sensor_probability_range', 'steps',
                           str(2))
    # Write results file to current directory
    # <param num_bins="5" write_period="50"
    # csv_path="/home/khaiyichin/test.csv" />
    modify_argos_attribute('param', 'csv_path',
                           os.getcwd()+'/test.csv')


if __name__ == '__main__':
    argos_configurator()
