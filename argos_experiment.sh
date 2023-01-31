python3 src/ARGoSConfigurator.py
cp -f src/kheperaiv_5_tiled.argos ../collective_perception/collective_perception_dynamic/build/src/run_dynamic_simulations
cd ../collective_perception/collective_perception_dynamic/build/src
./run_dynamic_simulations -c argos/kheperaiv_5_tiled.argos