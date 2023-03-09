import sys
import pygame
import time
import heapq as hq

def create_pygame_map(display_surface):
    # Define the colors
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)

    radius = 0
    clearance = 5
    offset = radius + clearance

    for x in range(display_surface.get_width()):
        for y in range(display_surface.get_height()):

         # Drawing Scaled Obstacles ie. with clearance

            # Equations for rectangle1 using half-plane method
            if (x >= 100-offset and x <= 150+offset) and (y >= 0-offset and y <= 100+offset):
                display_surface.set_at((x,y), GREEN)

            # Equations for rectangle2 using half-plane method
            if (x >= 100-offset and x <= 150+offset) and (y >= 150-offset and y <= 250+offset):
                display_surface.set_at((x,y), GREEN)

            # Equations for hexagon using half-plane method
            if (y-(0.58*x)-(-offset*(0.58**2 + 1)**0.5 -123.38))>= 0 and (y-(-0.57*x)-(offset*((-0.57)**2 + 1)**0.5 + 370.77))<= 0 and (y-(0.58*x)-(offset*(0.58**2 + 1)**0.5 + 24.62))<= 0 and (y-(-0.58*x)-(-offset*((-0.58)**2 + 1)**0.5 + 225.38))>= 0 and (x-235+offset) >= 0 and (x-365-offset) <= 0:
                display_surface.set_at((x,y), GREEN)

            # Equations for triangle using half-plane method
            if (y-(2*x)-(-offset*(2**2 + 1)**0.5 + (-895)))>= 0 and (y-(-2*x)-(offset*((-2)**2 + 1)**0.5 + (1145)))<= 0 and (x-460+offset) >= 0:
                display_surface.set_at((x,y), GREEN)

            # Equations for boundary using half-plane method
            if(x-offset) <= 0 or (x+offset) >= 600 or (y-offset) <= 0 or (y+offset) >= 250:
                display_surface.set_at((x,y), GREEN)

         # Drawing Unscaled Obstacles ie. without clearance

            # Equations for rectangle1 using half-plane method
            if (x >= 100 and x <= 150) and (y >= 0 and y <= 100):
                display_surface.set_at((x,y), RED)
            
            # Equations for rectangle2 using half-plane method
            if (x >= 100 and x <= 150) and (y >= 150 and y <= 250):
                display_surface.set_at((x,y), RED)

            # Equations for hexagon using half-plane method
            if (y-(0.58*x)-(-123.38))>= 0 and (y-(-0.57*x)-(370.77))<= 0 and (y-(0.58*x)-(24.62))<= 0 and (y-(-0.58*x)-(225.38))>= 0 and (x-235) >= 0 and (x-365) <= 0:
                display_surface.set_at((x,y), RED)

            # Equations for triangle using half-plane method
            if (y-(2*x)-(-895))>= 0 and (y-(-2*x)-(1145))<= 0 and (x-460) >= 0:
                display_surface.set_at((x,y), RED)

    pygame.display.update()

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

        if obstacle_map.get_at((start_x,pygame.Surface.get_height(obstacle_map)-1 - start_y))[0] == 1:
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

        if obstacle_map.get_at((goal_x,pygame.Surface.get_height(obstacle_map)-1 - goal_y))[0] == 1:
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
    
    if (obstacle_map.get_at((new_node[0],pygame.Surface.get_height(obstacle_map)-1 - new_node[1]))[0] == 1):
        return new_node
    else:
        return None
    
def ActionMoveDown(node, obstacle_map):
    new_node = []
    new_node.append(node[0])
    new_node.append(node[1] - 1)
    if (new_node[1] >= 0) and (obstacle_map.get_at((new_node[0],pygame.Surface.get_height(obstacle_map)-1 - new_node[1]))[0] == 1):
        return new_node
    else:
        return None
    
def ActionMoveLeft(node, obstacle_map):
    new_node = []
    new_node.append(node[0] - 1)
    new_node.append(node[1])
    if (new_node[0] >= 0) and (obstacle_map.get_at((new_node[0],pygame.Surface.get_height(obstacle_map)-1 - new_node[1]))[0] == 1):
        return new_node
    else:
        return None

def ActionMoveRight(node, obstacle_map):
    new_node = []
    new_node.append(node[0] + 1)
    new_node.append(node[1])
    if (new_node[0] < 600) and (obstacle_map.get_at((new_node[0],pygame.Surface.get_height(obstacle_map)-1 - new_node[1]))[0] == 1):
        return new_node
    else:
        return None

def ActionMoveUpLeft(node, obstacle_map):
    new_node = []
    new_node.append(node[0] - 1)
    new_node.append(node[1] + 1)
    if (new_node[0] >= 0) and (new_node[1] < 250) and (obstacle_map.get_at((new_node[0],pygame.Surface.get_height(obstacle_map)-1 - new_node[1]))[0] == 1):
        return new_node
    else:
        return None

def ActionMoveUpRight(node, obstacle_map):
    new_node = []
    new_node.append(node[0] + 1)
    new_node.append(node[1] + 1)
    if (new_node[0] < 600) and (new_node[1] < 250) and (obstacle_map.get_at((new_node[0],pygame.Surface.get_height(obstacle_map)-1 - new_node[1]))[0] == 1):
        return new_node
    else:
        return None
    
def ActionMoveDownLeft(node, obstacle_map):
    new_node = []
    new_node.append(node[0] - 1)
    new_node.append(node[1] - 1)
    if (new_node[0] >= 0) and (new_node[1] >= 0) and (obstacle_map.get_at((new_node[0],pygame.Surface.get_height(obstacle_map)-1 - new_node[1]))[0] == 1):
        return new_node
    else:
        return None
    
def ActionMoveDownRight(node, obstacle_map):
    new_node = []
    new_node.append(node[0] + 1)
    new_node.append(node[1] - 1)
    if (new_node[0] < 600) and (new_node[1] >= 0) and (obstacle_map.get_at((new_node[0],pygame.Surface.get_height(obstacle_map)-1 - new_node[1]))[0] == 1):
        return new_node
    else:
        return None

def CheckGoal(node, goal,start, obstacle_map,ClosedList,start_time):
    if node[0] == goal[0] and node[1] == goal[1]:
        print("\nGoal Reached")
        end_time = time.time()
        time_taken = round(end_time - start_time, 2)
        print("\nTime taken: ", time_taken, "seconds")
        Backtrack(start, node, ClosedList, obstacle_map)

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
        obstacle_map.set_at((key[0],key[1]),(255,255,255))
        pygame.display.update()
    while current_node != start:
        current_node = ClosedList[(current_node[0],current_node[1])][1]
        path.append(current_node)
    path.reverse()
    for i in range(len(path)):
        obstacle_map.set_at((path[i][0],path[i][1]),(0,0,255))
        pygame.display.update()

    obstacle_map.set_at((start[0],start[1]),(255,0,0))
    obstacle_map.set_at((goal[0],goal[1]),(0,255,0))
    pygame.display.update()

    print("\nPath length: ", len(path))

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
    clock = pygame.time.Clock()

    clock.tick(60)
    obstacle_map = pygame.display.set_mode((600, 250))
    pygame.display.set_caption("Dijkstra Planner")
    pygame.display.update()
    obstacle_map.fill((1,1,1))
    create_pygame_map(obstacle_map)
    start, goal = UserInput(obstacle_map)
    DijkstraPlanner(start, goal, obstacle_map)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
            elif event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

if __name__ == '__main__':
    main()
