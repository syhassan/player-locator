#!usr/bin/python3
import numpy as np
import os

# Simple Kalman Filter Implemented

# Initial State x
x_u = np.matrix([[30.00],
               [50.00],
               [0.00],
               [0.00]])

# Initial Measurement z
z = [[30], 
     [50]]
     
# Velocity at t-1
vx_prev = 0
vy_prev = 0
            
# Sampling time t is 0.05
t = 0.05

u = [[],[]]

# State Transition Matrix A
A = np.matrix([[1, 0, t, 0],
               [0, 1, 0, t],
               [0, 0, 1, 0],
               [0, 0, 0, 1]])

B = np.matrix([[(t**2)/2, 0],
                [0, (t**2)/2],
                [t, 0],
                [0, t]])

# Measurement Mapping Matrix H
H = np.matrix([[1, 0, 0, 0],
               [0, 1, 0, 0]])

# Variance of uniform ly distributed noise calculated by (1/12)(b-a)^2
sig = 0.03

# Process Noise Covariance Matrix Q
Q = np.matrix([[0.5, 0, 0, 0],
               [0, 0.5, 0, 0],
               [0, 0, 0.5, 0],
               [0, 0, 0, 0.5]])
               
# Sensor Noise Covariance Matrix R
R = np.matrix([[sig, 0],
               [0, sig]])

# Initial Covriance Matrix P
P_u = np.matrix([[0.00000001, 0, 0, 0],
               [0, 0.00000001, 0, 0],
               [0, 0, 0.00000001, 0],
               [0, 0, 0, 0.00000001]])

if __name__ == "__main__":
    
    # Exit execution if predicted positions from multilaterion file does not exist.
    if os.path.exists("data/predicted_positions.txt"):
        print("Predictions file found.")
    else:
        print("Predictions file not found.")
        quit()
           
    # Check for existing files from previous run to replace
    if os.path.exists("data/filtered.txt"):
        print("Replacing old filtered state file.")
        os.remove("data/filtered.txt")
    else:
        print("Writing to new filtered file.")
    
    # Write to file
    filtered = open("data/filtered.txt", "a")
    
    # Read from file
    predicted = open("data/predicted_positions.txt", "r")
    signals = predicted.readlines()

    try:
        # Iterate for as many entries in generated data
        for i in range(len(signals)):
            
            str_buff = signals[i].split(",")
            str_buff.pop()
            position = [float(i) for i in str_buff]
            z = [[float(position[0])],[float(position[1])]]
            
            # Predict
            vx = (float(z[0][0]) - float(x_u[0]))/t
            vy = (float(z[1][0]) - float(x_u[1]))/t
            
            x_u[0] = z[0]
            x_u[1] = z[1]
            x_u[2] = vx
            x_u[3] = vy    
            
            u = [[(vx - vx_prev)/t], [(vy - vy_prev)/t]]
            
            x_p = np.matmul(A, x_u) + np.matmul(B, u)

            P_p = np.matmul(np.matmul(A, P_u), A.T) + Q

            vx_prev = vx
            vy_prev = vy
            
            # Update
            K = np.matmul(np.matmul(P_p, H.T), np.linalg.inv(np.matmul(H, np.matmul(P_p, H.T)) + R))
            x_u = x_p + np.matmul(K, (z - np.matmul(H, x_p)))
            
            I = np.eye(H.shape[1])
            
            P_u = (I - (K*H)) * P_p
            
            # Write state to file
            for i in range(4):
                filtered.write(str(float(x_u[i]))+',')
            filtered.write('\n')

    finally:
        predicted.close()
        filtered.close()
        print("\nFiles closed!\n")
