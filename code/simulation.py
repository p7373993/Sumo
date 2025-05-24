import traci
import sys,os

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def simulation():
    # Directory
    sumo_binary = "sumo-gui" # or sumo-gui
    sumocfg_dir = project_root+"/Net/test.sumocfg"
    route_dir = project_root+"/Net/rou.rou.xml"

    # Run SUMO
    sumo_cmd = [sumo_binary, "-c", sumocfg_dir, "-r", route_dir, "--junction-taz", "--no-warnings", "--random"]
    traci.start(sumo_cmd)

    # Set variables
    time = 0
    reroute_freq = 10
    
    # Running ...
    while traci.simulation.getMinExpectedNumber() > 0:
        traci.simulationStep()
        time += 1
        if time // reroute_freq == 0:
            for vid in traci.simulation.getDepartedIDList():
                traci.vehicle.rerouteTraveltime(vid)

        # Close SUMO
        if time > 300:
            traci.close()
            break
            
    return 0

