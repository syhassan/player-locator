#!usr/bin/python3

import os

c = [0, 0, 0, 0]
b = [0, 0, 0, 0]
a = [0, 0, 0, 0]
vel = [0, 0]

sensor = [[0]*2 for i in range(4)]
sensor[0][0]   = 00.00    # Left Bottom Sensor
sensor[0][0]   = 00.00
sensor[1][0]   = 60.00    # Right Bottom Sensor
sensor[1][1]   = 00.00
sensor[2][0]   = 00.00    # Left Top Sensor
sensor[2][1]   = 100.00
sensor[3][0]   = 60.00    # Right Top Sensor
sensor[3][1]   = 100.00

x_old = 30.00
y_old = 50.00

if __name__ == "__main__":
    
    # Exit execution if signals file does not exist.
    if os.path.exists("data/signals.txt"):
        print("Signals file found.")
    else:
        print("Signals file not found.")
        quit()
           
    # Check for existing files from previous run to replace
    if os.path.exists("data/predicted_positions.txt"):
        print("Replacing old predicted_positions file.")
        os.remove("data/predicted_positions.txt")
    else:
        print("Writing to new predicted_positions file.")
    
    if os.path.exists("data/predicted_velocities.txt"):
        print("Replacing old predicted_velocities file.")
        os.remove("data/predicted_velocities.txt")
    else:
        print("Writing to new predicted_velocities file.")
    
    # New files for predictions
    predicted_pos = open("data/predicted_positions.txt", "a")
    predicted_vel = open("data/predicted_velocities.txt", "a")
    
    # Read from file
    signal_file = open("data/signals.txt", "r")
    signals = signal_file.readlines()
    
    try:
    
        # Iterate for as many entries in generated data
        for i in range(len(signals)):
        
            # Separate data in txt file by comma and remove newline char, then convert to float
            str_buff = signals[i].split(",")
            str_buff.pop()
            signal = [float(i) for i in str_buff]
            
            # Calculate coordinates for each collection of readings
            for i in range(4):
                c[i] = ((signal[i])**2) - (sensor[i][0]**2) - (sensor[i][1]**2)
                b[i] = 2*sensor[i][1]
                a[i] = 2*sensor[i][0]
            
            x = ((c[0]-c[3])*(b[2]-b[1])-(b[3]-b[0])*(c[1]-c[2]))/((b[2]-b[1])*(a[3]-a[0])+(b[3]-b[0])*(a[1]-a[2]))
            y = (c[1]-c[2]+(a[1]-a[2])*x)/(b[2]-b[1])
            
            # Calculate velocity on x and y axis compared to old reading
            vel[0] = (x - x_old) / 0.05
            vel[1] = (y - y_old) / 0.05
            
            # Write data to files
            predicted_pos.write(str(x)+','+str(y)+',\n')
            predicted_vel.write(str(vel[0])+','+str(vel[1])+',\n')
            
            # Configure new reading as old for next iteration
            x_old = x
            y_old = y
    
    finally:
        signal_file.close()
        predicted_pos.close()
        predicted_vel.close()
        print("done")
