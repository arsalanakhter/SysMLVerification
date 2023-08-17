import csv
import os
import matplotlib.pyplot as plt



from pprint import pprint

from ARGoSConfigurator import ensure_folder_exists

saveRow = []
saveCol = []

####Parameters to Extract

def readCSV(filename, *args):
    saveData = {}
    with open(filename, mode='r') as f:
        mycsv = csv.reader(f)
        mycsv = list(mycsv)
        for arg in args:
            saveRow = []
            saveCol = []
            for counter_row, row in enumerate(mycsv):  # Use enumerate to get both row index and row data
                for counter_column, row_item in enumerate(row):  # Use enumerate to get both column index and column data
                    if row_item.strip() == arg:
                        saveRow.append(counter_row)
                        saveCol.append(counter_column)

            saveData[arg] = [mycsv[x] for x in saveRow if x < len(mycsv)]  # Check if index is within valid range

    return saveData

def create_fcd_plot(data, filename_string):
    # Extract all the values of fraction of correct decisions
    # in the current data, and create a plot, with values on y axis.
    # store the figures in a separate folder
    folder_path = ensure_folder_exists('figs')

    data = data ['fractioncorrectdecisions']
    data_vals = [float(row[2]) for row in data]
    plt.plot(data_vals)
    plt.title('Consensus Performance')
    plt.xlabel('Index')
    plt.ylabel('FCD')
    
    # Save the plot to a file in the 'figs' directory
    plt.savefig("figs/{}.png".format(filename_string))
    print("Plot saved as 'figs/{}.png".format(filename_string))




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
                experiment_output_string =  "R{}-S{}-C{}".format(r,s,c).replace('.', '_')
                experiment_output_file = os.path.join(experiment_output_folder_path, experiment_output_string+'.csv')
                saveData = readCSV(experiment_output_file, 'range', 'speed', 'robots', 'fillratio', 'sensorprob', 'fractioncorrectdecisions')
                print("Data:")
                pprint(saveData)
                create_fcd_plot(saveData, experiment_output_string)
                # search_terms = list(saveData.keys())  # Convert dictionary keys to a list
                # print(search_terms)

                # for search_term in search_terms:
                #     if search_term == 'fractioncorrectdecisions':
                #         last10points = saveData[search_term][-10:]
                #         print(last10points)
                #         total_sum = 0   # Use a different variable name to avoid conflicts with the built-in sum function
                #         for point in last10points:
                #             total_sum += float(point[2])
                #         avg = total_sum/10
                #         print(avg)
                #     else:
                #         print(saveData[search_term][0])
                    
