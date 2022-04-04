# player-locator

## Running

First `range_generator.py` simulates the random movement of a player on a field of size 100 x 60 m. The player has a sensor on which sends out signals to the four receivers at each corner of the field at 20 Hz. Then the distance of the player from each receiver is calculated as the output, and +/-30 cm of noise is added to it.

Then `processor.py` performs multilateration on the 4 distances given out by the previous python program and calculates the position of the player based on that, as well as the predicted velocities of the player.

Then `filter.py` performs a simple kalman filter on the predicted position values using the predicted velocities of the player.

Lastly, `plot.py` makes a plot of them to view and compare the filtered values, predicted values and ground truth.

# Results
The multilateration works as planned but the filter either overfits to the multilateration model or becomes noisy and overshoots predictions when the process noise covariance matrix Q from `filter.py` has small values.

![Alt text](figures/Figure_1.png?raw=true "X Axis Position")
![Alt text](figures/Figure_2.png?raw=true "Y Axis Position")
