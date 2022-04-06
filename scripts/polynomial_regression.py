#!usr/bin/python3
import numpy as np
import os
import matplotlib.pyplot as plt

if __name__ == "__main__":
    
    # Exit execution if predicted positions from multilateration file does not exist.
    if os.path.exists("../data/predicted_positions.txt"):
        print("predicted_positions file found.")
    else:
        print("predicted_positions file not found.")
        quit()
    
    # Read from file
    predicted = open("../data/predicted_positions.txt", "r")
    signals = predicted.readlines()

    try:

        x = []
        y = []
        time =  []
    
        # Iterate for as many entries in generated data
        for i in range(len(signals)):
        
            # Separate data into different lists to plot
            str_buff = signals[i].split(",")
            str_buff.pop()
            position = [float(i) for i in str_buff]
            x.append(float(position[0]))
            y.append(float(position[1]))
            time.append(0.05*(i+1))
        
        # Fit polynomials to each list
        modelx = np.poly1d(np.polyfit(time, x, 12))
        modely = np.poly1d(np.polyfit(time, y, 12))

        line = np.linspace(0.05, time[-1], 200)
        
        # Plot separate figures for each axis
        fig1 = plt.figure(1)
        plt.scatter(time, x)
        plt.plot(line, modelx(line))
        plt.title("Polynomial Regression On X Position")
        plt.xlabel("Time")
        plt.ylabel("X coordinate position")
        plt.grid()
        
        fig2 = plt.figure(2)
        plt.scatter(time, y)
        plt.plot(line, modely(line))
        plt.title("Polynomial Regression On Y Position")
        plt.xlabel("Time")
        plt.ylabel("Y coordinate position")
        plt.grid()
        
        plt.show() 

    finally:
        predicted.close()
        print("\nFiles closed!\n")
