# Smart Traffic Light

## Overview
This project aims to develop a smart traffic light system that incorporates a dataset for detecting people in wheelchairs. Additionally, we implement the logic in ROS to demonstrate how the traffic light would function.

## Wheelchair Detection

We have developed a dataset for detecting people in wheelchairs. You can watch a demonstration of the detection in action in [this video](https://www.youtube.com/watch?v=CJRx00M8mIw).

To access the dataset, please visit [this link](https://universe.roboflow.com/serviciosocialworkspace/wheel-chair-detector-sample/browse?queryText=&pageSize=50&startingIndex=0&browseQuery=true).

## ROS Traffic Light Logic

To run the ROS code, follow these steps:

1. Clone this repository into your ROS workspace because it's a ROS package.

   ```bash
   git clone https://github.com/andrea2702/SmartTrafficLight
   
2. Run the semaforo.py script to start the traffic light logic.
```bash
rosrun semafoto semaforo.py
```

3. Run the send_signal.py script to simulate the detection of people. The script accepts inputs ranging from 1 to 4:
1: Many pedestrians
2: Person in wheelchair
3: Some pedestrians
Any other input: Few pedestrians
```bash
rosrun semaforo send_signal.py
```

## Demo
[![Demo del Proyecto](http://img.youtube.com/vi/16Uw4eZmJN4/0.jpg)](https://www.youtube.com/watch?v=16Uw4eZmJN4)

