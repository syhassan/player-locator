# player-locator

## Running

First `range_generator.py` simulates the random movement of a player on a field of size 100 x 60 m. The player has a sensor on which sends out signals to the four receivers at each corner of the field at 20 Hz. Then the distance of the player from each receiver is calculated as the output, and +/-30 cm of noise is added to it.

Then `multilateration.py` performs multilateration on the 4 distances given out by the previous python program and calculates the position of the player based on that, as well as the predicted velocities of the player with a degree of redundancy, using all 4 distances. In lieu of that, `average_trilateration.py` performs trilateration from different triplet combinations of the four distances and takes the average of them.

Then `kalman_filter.py` performs a simple linear kalman filter on the predicted position values using the predicted velocities of the player, the results are not useful as the movement is not linear.

Apart from this,`polynomial_regression.py` performs a simple polynomial function fitting to average out outliers and give us a smoother function.

Lastly, `plot.py` makes a plot of them to view and compare the filtered values, predicted values from multilateration, averaged values from trileration and ground truth.

## Results
The multilateration works as planned but the filter either overfits to the multilateration model or becomes noisy and overshoots estimates when the process noise covariance matrix Q from `filter.py` has small values. This is because the estimates from the kalman filter are using velocity as an input, but the predicted velocities come from the noisy values. If there were a secondary source of velocity data from the sensor on the player, the two data sets would fuse to make a more reasonable estimation.

![](figures/Fig_1.png?raw=true "Player X-Axis Position")
![](figures/Fig_2.png?raw=true "Player Y-Axis Position")
![](figures/Fig_4.png?raw=true "Polynom Reg on X-Axis Position")
![](figures/Fig_4.png?raw=true "Polynom Ref on Y-Axis Position")
