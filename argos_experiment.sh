# In a seperate terminal, make this script executable before running it, by using the following command
# $ chmod +rx argos_experiment.sh
for R in 5 10
do
    for S in 7 9
    do
        for C in 4 7
        do
            ITERATION_STRING="R${R}-S0_${S}-C0_${C}.argos"
            echo $ITERATION_STRING 
            cd ~/Downloads/collective_perception/collective_perception_dynamic/
            ./build/src/run_dynamic_simulations -c /home/smerl2/Downloads/SysMLVerification/experiment_data/${ITERATION_STRING}
        done
    done
done
