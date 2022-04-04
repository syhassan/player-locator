#!usr/bin/python3

import time
import random as rd
import numpy as np
import os

sensor = [[0]*2 for i in range(4)]

sensor[0][0]   = 00.00    # Left Bottom Sensor
sensor[0][0]   = 00.00
sensor[1][0]   = 60.00    # Right Bottom Sensor
sensor[1][1]   = 00.00
sensor[2][0]   = 00.00    # Left Top Sensor
sensor[2][1]   = 100.00
sensor[3][0]   = 60.00    # Right Top Sensor
sensor[3][1]   = 100.00

player_pos  = [30.00, 50.00]    # Starting position of the player
x_limit     = 60.00             # Upper X axis limit to stay on field
y_limit     = 100.00            # Upper Y axis limit to stay on field
min_limit   = 00.00             # Lower X and Y axis limit

# Distance list from: lb, rb, lt, rt
dist        = [58.309519, 58.309519, 58.309519, 58.309519]
signal      = [58.309519, 58.309519, 58.309519, 58.309519]
pos_prev = [30.00, 50.00]

if __name__ == "__main__":
    
    # Check for existing files from previous run to replace
    if os.path.exists("data/signals.txt"):
        print("Replacing old signals file.")
        os.remove("data/signals.txt")
    else:
        print("Writing to new signals file.") 
    
    if os.path.exists("data/positions.txt"):
        print("Replacing old positions file.")
        os.remove("data/positions.txt")
    else:
        print("Writing to new positions file.") 
    
    if os.path.exists("data/velocities.txt"):
        print("Replacing old velocities file.")
        os.remove("data/velocities.txt")
    else:
        print("Writing to new velocities file.") 
    
    # Create new files for data
    signal_file = open("data/signals.txt", "a")
    positions_file = open("data/positions.txt", "a")
    velocities_file = open("data/velocities.txt", "a")
        
    try:
        while True:

            # Highest possible speed for a human is ~ 12.42 m/s and we get a signal at 20 Hz (0.05 s).
            # Maximum movement would be 0.05 * 12.42 = 0.621 m.
            
            # Add random input within possible range and ensure limits of field size
            for i in range(2):
                player_pos[i] += rd.uniform(-0.621, 0.621)
                player_pos[i] = np.clip(player_pos[i], min_limit, x_limit)
            
            # Calculate distance from each sensor
            for i in range(4):
                dist[i] = np.linalg.norm(np.asarray(player_pos) - np.asarray(sensor[i]))
            
            # Generate and add noise of +/-0.30 m
            for i in range(4):
                signal[i] = dist[i] + rd.uniform(-0.30, 0.30)

            # Round to 2 decimal place to match precision of noise, 30 cm
            signal_rounded = list(np.around(np.array(signal), 2))
            
            # Write data to files
            for signals in signal_rounded:
                signal_file.write(str(signals))
                signal_file.write(",")
            signal_file.write("\n")
            
            for pos in player_pos:
                positions_file.write(str(pos))
                positions_file.write(",")
            positions_file.write("\n")
            
            for i in range(2):
                pos_prev[i] = player_pos[i]
                
            # Keep frequency of 20 Hz
            time.sleep(0.05)
    
    finally:
        # Ensure the file is closed (only works with a single Ctrl-C)
        signal_file.close()
        positions_file.close()
        print("\nFiles closed!\n")
