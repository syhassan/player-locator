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
    if os.path.exists("../data/signals.txt"):
        print("Signals file found.")
    else:
        print("Signals file not found.")
        quit()
           
    # Check for existing files from previous run to replace
    if os.path.exists("../data/trilaterated_positions.txt"):
        print("Replacing old trilaterated_positions file.")
        os.remove("../data/trilaterated_positions.txt")
    else:
        print("Writing to new trilaterated_positions file.")

    
    # New files for predictions
    trilaterated_positions = open("../data/trilaterated_positions.txt", "a")
    
    # Read from file
    signal_file = open("../data/signals.txt", "r")
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
            
            A = 2
            B = 1
            C = 0
            
            x1 = ((c[A]-c[C])*(b[B]-b[A])+(b[A]-b[C])*(c[A]-c[B]))/((b[B]-b[A])*(a[C]-a[A])+(b[C]-b[A])*(a[A]-a[B]))
            y1 = (c[A]-c[B]+(a[A]-a[B])*x1)/(b[B]-b[A])
            
            A = 1
            B = 2
            C = 3
            
            x2 = ((c[A]-c[C])*(b[B]-b[A])+(b[A]-b[C])*(c[A]-c[B]))/((b[B]-b[A])*(a[C]-a[A])+(b[C]-b[A])*(a[A]-a[B]))
            y2 = (c[A]-c[B]+(a[A]-a[B])*x2)/(b[B]-b[A])
            
            A = 3
            B = 0
            C = 1
            
            x3 = ((c[A]-c[C])*(b[B]-b[A])+(b[A]-b[C])*(c[A]-c[B]))/((b[B]-b[A])*(a[C]-a[A])+(b[C]-b[A])*(a[A]-a[B]))
            y3 = (c[A]-c[B]+(a[A]-a[B])*x3)/(b[B]-b[A])
            
            A = 0
            B = 2
            C = 3
            
            x4 = ((c[A]-c[C])*(b[B]-b[A])+(b[A]-b[C])*(c[A]-c[B]))/((b[B]-b[A])*(a[C]-a[A])+(b[C]-b[A])*(a[A]-a[B]))
            y4 = (c[A]-c[B]+(a[A]-a[B])*x4)/(b[B]-b[A])

            # Write data to files
            trilaterated_positions.write(str(((x3+x4)/2))+','+str(((y1+y4)/2))+',\n')
            
    finally:
        signal_file.close()
        trilaterated_positions.close()
        print("\nFiles closed!\n")
