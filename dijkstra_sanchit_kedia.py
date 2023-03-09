import cv2
import numpy as np
# import pygame
import time
import heapq as hq

def create_cv_map(base_map):
    # Draw obstacles

    # base_map = cv2.rectangle(base_map,(100,0),(150,100),(0,255,255),-1)
    # base_map = cv2.rectangle(base_map,(100,150),(150,250),(0,255,255),-1)
    # base_map = cv2.fillPoly(base_map,[np.array([[460,25],[460,225],[510,125]], np.int32)],(0,255,255))
    # base_map = cv2.fillPoly(base_map,[np.array([[300,50],[235,87],[235,162],[300,200],[365,163],[365,88]], np.int32)],(0,255,255))
    # obstacle_map = cv2.rectangle(base_map,(0,0),(600,250),(0,255,255),5)

    for x in range(base_map.shape[1]):
        for y in range(base_map.shape[0]):

            # Equations for rectangle1 using half-plane method
            if (x >= 100 and x <= 150) and (y >= 0 and y <= 100):
                base_map[y][x] = [0,0,255]
            
            # Equations for rectangle2 using half-plane method
            if (x >= 100 and x <= 150) and (y >= 150 and y <= 250):
                base_map[y][x] = [0,0,255]

            # Equations for hexagon using half-plane method
            if (y-(0.58*x)+123.38)>= 0 and (y-(-0.57*x)-370.77)<= 0 and (y-(0.58*x)-24.62)<= 0 and (y-(-0.58*x)-225.38)>= 0 and (x-235) >= 0 and (x-365) <= 0:
                base_map[y][x] = [0,0,255]

            # Equations for triangle using half-plane method
            if (y-(2*x)+895)>= 0 and (y+(2*x)-1145)<= 0 and (x-460) >= 0:
                base_map[y][x] = [0,0,255]

            if(x-5<=0) or (x-595>=0) or (y-5 <=0) or (y-245>=0):
                base_map[y][x] = [0,0,255]

    return base_map

# def create_pygame_map():
#     import pygame
#     pygame.init()
#     # Create the display surface object
#     display_surface = pygame.display.set_mode((600, 250))
#     pygame.display.set_caption
#     # Define the colors
#     BLACK = (0, 0, 0)
#     WHITE = (255, 255, 255)
#     GREEN = (0, 255, 0)
#     RED = (255, 0, 0)
#     BLUE = (0, 0, 255)
#     YELLOW = (255, 255, 0)
#     # Draw obstacles
#     pygame.draw.rect(display_surface, GREEN, (95,0,60,105)) # For Clearance
#     pygame.draw.rect(display_surface, RED, (100,0,50,100))
#     pygame.draw.rect(display_surface, GREEN, (95,5,60,105)) # For Clearance
#     pygame.draw.rect(display_surface, RED, (100,150,50,100))
#     pygame.draw.polygon(display_surface, GREEN, [(455,20),(455,230),(515,125)]) # For Clearance
#     pygame.draw.polygon(display_surface, RED, [(460,25),(460,225),(510,125)])
#     pygame.draw.polygon(display_surface, GREEN, [(300,45),(231,85),(231,165),(300,205),(369,165),(369,85)]) # For Clearance
#     pygame.draw.polygon(display_surface, RED, [(300,50),(235,87),(235,162),(300,200),(365,163),(365,88)])
#     pygame.display.update()

#     while True:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 exit()

def UserInput(obstacle_map):

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
    start.append(250-start_y)
    
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
    goal.append(250-goal_y)

    # obstacle_map = cv2.circle(obstacle_map, (start_x, start_y), 1, (255,255,255), -1)
    # obstacle_map = cv2.circle(obstacle_map, (goal_x, goal_y), 1, (255,255,255), -1)

    return start, goal

def ActionMoveUp(node, obstacle_map):
    new_node = []
    new_node.append(node[0])
    new_node.append(node[1] + 1)
    if (new_node[1] <= 250) and (obstacle_map[obstacle_map.shape[0]- new_node[1]][new_node[0]][0] == 1):
        return new_node
    else:
        return None
    
def ActionMoveDown(node, obstacle_map):
    new_node = []
    new_node.append(node[0])
    new_node.append(node[1] - 1)
    if (new_node[1] >= 0) and (obstacle_map[obstacle_map.shape[0] - new_node[1]][new_node[0]][0] == 1):
        return new_node
    else:
        return None
    
def ActionMoveLeft(node, obstacle_map):
    new_node = []
    new_node.append(node[0] - 1)
    new_node.append(node[1])
    if (new_node[0] >= 0) and (obstacle_map[obstacle_map.shape[0] - new_node[1]][new_node[0]][0] == 1):
        return new_node
    else:
        return None

def ActionMoveRight(node, obstacle_map):
    new_node = []
    new_node.append(node[0] + 1)
    new_node.append(node[1])
    if (new_node[0] < 600) and (obstacle_map[obstacle_map.shape[0] - new_node[1]][new_node[0]][0] == 1):
        return new_node
    else:
        return None

def ActionMoveUpLeft(node, obstacle_map):
    new_node = []
    new_node.append(node[0] - 1)
    new_node.append(node[1] + 1)
    if (new_node[0] >= 0) and (new_node[1] < 250) and (obstacle_map[obstacle_map.shape[0] - new_node[1]][new_node[0]][0] == 1):
        return new_node
    else:
        return None

def ActionMoveUpRight(node, obstacle_map):
    new_node = []
    new_node.append(node[0] + 1)
    new_node.append(node[1] + 1)
    if (new_node[0] < 600) and (new_node[1] < 250) and (obstacle_map[obstacle_map.shape[0] - new_node[1]][new_node[0]][0] == 1):
        return new_node
    else:
        return None
    
def ActionMoveDownLeft(node, obstacle_map):
    new_node = []
    new_node.append(node[0] - 1)
    new_node.append(node[1] - 1)
    if (new_node[0] >= 0) and (new_node[1] >= 0) and (obstacle_map[obstacle_map.shape[0] - new_node[1]][new_node[0]][0] == 1):
        return new_node
    else:
        return None
    
def ActionMoveDownRight(node, obstacle_map):
    new_node = []
    new_node.append(node[0] + 1)
    new_node.append(node[1] - 1)
    if (new_node[0] < 600) and (new_node[1] >= 0) and (obstacle_map[obstacle_map.shape[0] - new_node[1]][new_node[0]][0] == 1):
        return new_node
    else:
        return None

def CheckGoal(node, goal,start, obstacle_map,ClosedList,start_time):
    if node[0] == goal[0] and node[1] == goal[1]:
        print("\nGoal Reached")
        print("\nPath Length: ", len(ClosedList))
        end_time = time.time()
        print("\nTime taken: ", end_time - start_time, "seconds")
        obstacle_map = Backtrack(start, goal, ClosedList, obstacle_map)
    else:
        return False

def CheckNode(node_new,ClosedList,OpenList,current_cost,current_node,cost):
    node_new = tuple(node_new)
    if node_new not in ClosedList:
        found = True
        for node in OpenList:
            if node[2] == node_new:
                idx = OpenList.index(node)
                found = False
                if node[0] > current_cost + cost:
                    OpenList[idx][0] = current_cost + cost
                    OpenList[idx][1] = current_node[2]
                break
        if found:
            hq.heappush(OpenList, [current_cost + cost, current_node[2], node_new])

def Backtrack(start, goal, ClosedList, obstacle_map):
    path = []
    path.append(goal)
    current_node = goal
    for key in list(ClosedList.keys()):
        obstacle_map[key[1], key[0]] = (255,255,255)
        cv2.imshow("Exploration", obstacle_map)
        cv2.waitKey(1)
    while current_node != start:
        current_node = ClosedList[(current_node[0],current_node[1])][1]
        path.append(current_node)
    path.reverse()
    for i in range(len(path)):
        obstacle_map[path[i][1], path[i][0]] = (255,0,0)

    obstacle_map[start[1], start[0]] = (0,255,0)
    obstacle_map[goal[1], goal[0]] = (0,255,0)

    # show the image in the same window 
    cv2.imshow("Exploration", obstacle_map)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def DijkstraPlanner(start, goal, obstacle_map):

    OpenList = []
    ClosedList = {}
    node_start = [0.0, start, start]
    hq.heappush(OpenList, node_start)
    hq.heapify(OpenList)
    start_time = time.time()
    
    while (len(OpenList) > 0):
        current_node = hq.heappop(OpenList)
        ClosedList[(current_node[2][0],current_node[2][1])] =  current_node[0], current_node[1]
        current_cost = current_node[0]
        CheckGoal(current_node[2], goal, start, obstacle_map, ClosedList,start_time)
        
        new_node = ActionMoveUp(current_node[2],obstacle_map)
        if new_node is not None:
            CheckNode(new_node,ClosedList,OpenList,current_cost,current_node,1.0)
        
        new_node = ActionMoveDown(current_node[2],obstacle_map)
        if new_node is not None:
            CheckNode(new_node,ClosedList,OpenList,current_cost,current_node,1.0)

        new_node = ActionMoveLeft(current_node[2],obstacle_map)
        if new_node is not None:
            CheckNode(new_node,ClosedList,OpenList,current_cost,current_node,1.0)

        new_node = ActionMoveRight(current_node[2],obstacle_map)
        if new_node is not None:
            CheckNode(new_node,ClosedList,OpenList,current_cost,current_node,1.0)

        new_node = ActionMoveUpLeft(current_node[2],obstacle_map)
        if new_node is not None:
            CheckNode(new_node,ClosedList,OpenList,current_cost,current_node,1.4)

        new_node = ActionMoveUpRight(current_node[2],obstacle_map)
        if new_node is not None:
            CheckNode(new_node,ClosedList,OpenList,current_cost,current_node,1.4)

        new_node = ActionMoveDownLeft(current_node[2],obstacle_map)
        if new_node is not None:
            CheckNode(new_node,ClosedList,OpenList,current_cost,current_node,1.4)

        new_node = ActionMoveDownRight(current_node[2],obstacle_map)
        if new_node is not None:
            CheckNode(new_node,ClosedList,OpenList,current_cost,current_node,1.4)

def main():
    obstacle_map = np.ones((250,600,3), dtype=np.uint8)
    obstacle_map = create_cv_map(obstacle_map)
    start, goal = UserInput(obstacle_map)
    DijkstraPlanner(start, goal, obstacle_map)

if __name__ == '__main__':
    main()
