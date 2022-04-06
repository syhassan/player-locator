#!usr/bin/python3
import matplotlib.pyplot as plt
import numpy as np
import os

t = 0.05

if __name__ == "__main__":

    # Check if all data files exist
    if os.path.exists("../data/predicted_positions.txt"):
        print("Predictions file found.")
    else:
        print("Predictions file not found.")
        quit()
   
    if os.path.exists("../data/trilaterated_positions.txt"):
        print("trilaterated_positions file found.")
    else:
        print("trilaterated_positions file not found.")
        quit()
        
    if os.path.exists("../data/filtered.txt"):
        print("Filtered values file found.")
    else:
        print("Filtered values file not found.")
        quit()

    if os.path.exists("../data/positions.txt"):
        print("True positions file found.")
    else:
        print("True positions file not found.")
        quit()
        
    # Read from files
    filtered = open("../data/filtered.txt", "r")
    filtered_values = filtered.readlines()
    
    predicted = open("../data/predicted_positions.txt", "r")
    predicted_values = predicted.readlines()
    
    trilaterated = open("../data/trilaterated_positions.txt", "r")
    trilaterated_values = trilaterated.readlines()
        
    ground_truth = open("../data/positions.txt", "r")
    true_positions = ground_truth.readlines()
            
    filtx = [0 for i in range(len(filtered_values))]
    predx = [0 for i in range(len(filtered_values))]
    trilx = [0 for i in range(len(filtered_values))]
    posix = [0 for i in range(len(filtered_values))]
    
    filty = [0 for i in range(len(filtered_values))]
    predy = [0 for i in range(len(filtered_values))]
    posiy = [0 for i in range(len(filtered_values))]
    trily = [0 for i in range(len(filtered_values))]
    
    time  = [0 for i in range(len(filtered_values))]
    
    try:
        
        # All files should be the same length so length of any would work to iterate over    
        for i in range(len(filtered_values)):
        
            str_buff = filtered_values[i].split(",")
            str_buff.pop()
            fil_buff = [float(i) for i in str_buff]
            filtx[i] = [float(fil_buff[0])]
            filty[i] = [float(fil_buff[1])]
            
            str_buff = predicted_values[i].split(",")
            str_buff.pop()
            pre_buff = [float(i) for i in str_buff]
            predx[i] = [float(pre_buff[0])]
            predy[i] = [float(pre_buff[1])]
            
            str_buff = trilaterated_values[i].split(",")
            str_buff.pop()
            tri_buff = [float(i) for i in str_buff]
            trilx[i] = [float(tri_buff[0])]
            trily[i] = [float(tri_buff[1])]
            
            str_buff = true_positions[i].split(",")
            str_buff.pop()
            pos_buff = [float(i) for i in str_buff]
            posix[i] = [float(pos_buff[0])]
            posiy[i] = [float(pos_buff[1])]
            
            time[i] = t*(i+1)
        
        # Make figures for y and x axis coordinates separately
        fig_1 = plt.figure(1)
        plt.plot(time, filtx, label = "Filtered Values")
        plt.plot(time, predx, label = "Predicted Values", linestyle='dashed')
        plt.plot(time, trilx, label = "Averaged Trilaterated Values", linestyle='dashed')
        plt.plot(time, posix, label = "True Values")
        
        plt.legend()
        plt.grid()
        
        plt.title("Player X Position")
        plt.xlabel("Time")
        plt.ylabel("X coordinate position")
        
        fig_2 = plt.figure(2)
        
        plt.plot(time, filty, label = "Filtered Values")
        plt.plot(time, trily, label = "Averaged Trilaterated Values", linestyle='dashed')
        plt.plot(time, predy, label = "Predicted Values", linestyle='dashed')
        plt.plot(time, posiy, label = "True Values")
        
        plt.legend()
        plt.grid()
        
        plt.title("Player Y Position")
        plt.xlabel("Time")
        plt.ylabel("Y coordinate position")
        
        plt.show()
        
    finally:
        predicted.close()
        filtered.close()
        ground_truth.close()
        print("\nFiles closed!\n")
