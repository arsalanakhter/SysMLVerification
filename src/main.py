import os

from ARGoSConfigurator import ensure_folder_exists, copy_file, modify_argos_attribute 



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
            modify_argos_attribute(experiment_file, 'sensor_probability_range', 'steps', str(1))
            # Modify communication range
            modify_argos_attribute(experiment_file, 'kheperaiv', 'rab_range', str(c))

            # Modify the results file parameter
            modify_argos_attribute(experiment_file, 'param', 'csv_path', 
                                    os.path.join(experiment_output_folder_path, experiment_file_string+'.csv'))
