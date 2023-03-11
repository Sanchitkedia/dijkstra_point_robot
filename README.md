# Project 8 Puzzle Solve using BFS

The project is to implement the Dijkstra algorithm for path planning of a point robot.
The project is a part of the course ENPM661 - Planning for Autonomous Robots at the University of Maryland, College Park.
The vizualization of the project is done using pygame and OpenCV.
The project is implemented in Python 3.8.10

## Contributor

- Sanchit Kedia  UID:119159620

## Installation

The project uses the following libraries:

1. numpy
2. pygame
3. OpenCV
4. time
5. heapq
6. sys
7. vidmaker

## Usage

### The project with vizualization in pygame can be run using the following command

```sh
python3 dijkstra_sanchit_kedia_pygame.py -h # Use this command to get help for the command line arguments
python3 dijkstra_sanchit_kedia_pygame.py # Use this command to run the project with vizualization in pygame wihout saving the video
python3 dijkstra_sanchit_kedia_pygame.py --save_video # Use this command to run the project with vizualization in pygame and save the video
```

### The project with vizualization in OpenCV can be run using the following command

```sh
python3 dijkstra_sanchit_kedia.py -h # Use this command to get help for the command line arguments
python3 dijkstra_sanchit_kedia.py # Use this command to run the project with vizualization in OpenCV
python3 dijkstra_sanchit_kedia.py --save_video # Use this command to run the project with vizualization in OpenCV and save the video
```

## Output

- Test case 1
  - START NODE: (19,19)
  - GOAL NODE: (440,125)

- Test case 2
  - START NODE: (19,231)
  - GOAL NODE: (125,125)

- Test case 3 [Goal node not reachable]
  - START NODE: (50,125)
  - GOAL NODE: (572,220)

### Video of vizualization of Task 1 in pygame

https://user-images.githubusercontent.com/61658557/224482895-b837eec6-2420-47a9-9e7c-16198ab95040.mp4

### Video of vizualization of Task 2 in OpenCV

https://user-images.githubusercontent.com/61658557/224203222-dec8b470-60ef-4b8b-990f-7db4e0c79649.mp4

### Terminal output for Task 3 [Goal node not reachable]

![Screenshot from 2023-03-09 20-41-30](https://user-images.githubusercontent.com/61658557/224203252-86d2d541-46e7-43ce-a85e-462ab17f34e9.png)
