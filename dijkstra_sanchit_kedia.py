import cv2
import numpy as np
import math
import pygame
import time

def create_cv_map(base_map):
    # Draw obstacles
    base_map = cv2.rectangle(base_map,(100,0),(150,100),(0,0,255),-1)
    base_map = cv2.rectangle(base_map,(100,150),(150,250),(0,0,255),-1)
    base_map = cv2.fillPoly(base_map,[np.array([[460,25],[460,225],[510,125]], np.int32)],(0,0,255))
    base_map = cv2.fillPoly(base_map,[np.array([[300,50],[235,87],[235,162],[300,200],[365,163],[365,88]], np.int32)],(0,0,255))
    obstacle_map = cv2.rectangle(base_map,(0,0),(600,250),(0,0,255),5)


    return obstacle_map

def create_pygame_map():
    import pygame
    pygame.init()
    # Create the display surface object
    display_surface = pygame.display.set_mode((600, 250))
    pygame.display.set_caption
    # Define the colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)
    YELLOW = (255, 255, 0)
    # Draw obstacles
    pygame.draw.rect(display_surface, GREEN, (95,0,60,105)) # For Clearance
    pygame.draw.rect(display_surface, RED, (100,0,50,100))
    pygame.draw.rect(display_surface, GREEN, (95,145,60,105)) # For Clearance
    pygame.draw.rect(display_surface, RED, (100,150,50,100))
    pygame.draw.polygon(display_surface, GREEN, [(455,20),(455,230),(515,125)]) # For Clearance
    pygame.draw.polygon(display_surface, RED, [(460,25),(460,225),(510,125)])
    pygame.draw.polygon(display_surface, GREEN, [(300,45),(231,85),(231,165),(300,205),(369,165),(369,85)]) # For Clearance
    pygame.draw.polygon(display_surface, RED, [(300,50),(235,87),(235,162),(300,200),(365,163),(365,88)])
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

def user_input(obstacle_map):

    start = []
    goal = []
    
    while True:
        start_x = int(input("Enter the x coordinate of the start point: "))
        while start_x < 0 or start_x > 600:
            print("Invalid input. Please enter a value between 0 and 600.")
            start_x = int(input("Enter the x coordinate of the start point: "))
        
        start_y = int(input("Enter the y coordinate of the start point: "))
        while start_y < 0 or start_y > 250:
            print("Invalid input. Please enter a value between 0 and 250.")
            start_y = int(input("Enter the y coordinate of the start point: "))

        if obstacle_map[obstacle_map.shape[0]-1 - start_y][start_x][0] == 1:
            break
        print("The start point is inside an obstacle. Please enter a valid start point.")

    start.append(start_x)
    start.append(start_y)
    
    while True:
        goal_x = int(input("Enter the x coordinate of the goal point: "))
        while (goal_x < 0 or goal_x > 600):
            print("Invalid input. Please enter a value between 0 and 600.")
            goal_x = int(input("Enter the x coordinate of the goal point: "))
        
        goal_y = int(input("Enter the y coordinate of the goal point: "))
        while goal_y < 0 or goal_y > 250:
            print("Invalid input. Please enter a value between 0 and 250.")
            goal_y = int(input("Enter the y coordinate of the goal point: "))

        if obstacle_map[obstacle_map.shape[0]-1 - goal_y][goal_x][0] == 1:
            break
        print("The goal point is inside an obstacle. Please enter a valid goal point.")
    
    goal.append(goal_x)
    goal.append(goal_y)

    obstacle_map = cv2.circle(obstacle_map, (start_x, start_y), 1, (255,255,255), -1)
    obstacle_map = cv2.circle(obstacle_map, (goal_x, goal_y), 1, (255,255,255), -1)

    return start, goal

def ActionMoveUp():


    return

def main():
    obstacle_map = np.ones((250,600,3), dtype=np.uint8)
    obstacle_map = create_cv_map(obstacle_map)
    
    start, goal = user_input(obstacle_map)
    print(start, goal)
    # create_pygame_map()

    cv2.imshow("Map", obstacle_map)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()




