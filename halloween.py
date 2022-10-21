import random
import math

class House:
    def __init__(self):
        
        self.rating = random.randint(1, 10)
        self.passed = False

    def streetPath(self, n):
        return ""
    
    def getPass(self):
        return self.passed

    def passing(self):
        self.passed = True

    def getRating(self):
        return self.rating

        
def path(n, x, y):
    nums = []

        #x-axis
    if x >= 1 and not(n[x-1][y].getPass()):
        nums.append(n[x-1][y].getRating())
    else:
        nums.append(-1)
    
    if x <= 3 and not(n[x+1][y].getPass()):
        nums.append(n[x+1][y].getRating())
    else:
        nums.append(-1)

        #y-axis
    if y >= 1 and not(n[x][y-1].getPass()):
        nums.append(n[x][y-1].getRating())
    else:
        nums.append(-1)

    if y <= 3 and not(n[x][y+1].getPass()):
        nums.append(n[x][y+1].getRating())
    else:
        nums.append(-1)
        

    m = max(nums)
    if m == -1:
        return [0, -1, -1]
    
    i = nums.index(m)
    if i == 0:
        return [m, x+1, y]
    elif i ==1:
        return [m, x-1, y]
    elif i ==2:
        return [m, x, y+1]
    elif i ==3:
        return [m, x, y-1]

    


def main():
    m = 5 # num rows
    n = 5 # num cols
    houses = []
    starting_i = 0
    starting_j = 0
    max_house_rating = 1
    house_rating_sum = 0.

    for i in range(m):
        house_row = []
        for j in range(n):
            new_house = House()
            house_row.append(new_house)
            # find the best house (so far)
            if (new_house.rating > max_house_rating):
                starting_i = i
                starting_j = j
                max_house_rating = new_house.rating
                house_rating_sum += new_house.rating

        houses.append(house_row)

    avg_house_rating = house_rating_sum / (m*n)

    num_visits = int(input("choose a number between 1-25"))
    num_visits = max(1, num_visits)
    num_visits = min(25, num_visits)


    # start from the best house
    # then given the next houses

    num_visited = 0
    cur_i = starting_i
    cur_j = starting_j
    path = []
    while (num_visited < num_visits):
        cur_house = houses[cur_i][cur_j]
        path.append(cur_house.rating)
        cur_house.passing()

        # left, right, up, down
        possible_dirs = [True, True, True, True]
        possible_next_pos = [(cur_i, cur_j-1),
                             (cur_i, cur_j+1),
                             (cur_i-1, cur_j),
                             (cur_i+1, cur_j)]
        
        if cur_i == 0:
            possible_dirs[2] = False
        if cur_i == m-1:
            possible_dirs[3] = False
        if cur_j == 0:
            possible_dirs[0] = False
        if cur_j == n-1:
            possible_dirs[1] = False

        # choose best house among next possible
        next_best_house_rating = 1
        for ii in range(4):
            next_i, next_j = possible_next_pos[ii]
            if (possible_dirs[ii]):
                next_house = houses[next_i][next_j]
                if (not next_house.passed): # if have not visited
                    if (next_house.rating > next_best_house_rating):
                        cur_i = next_i
                        cur_j = next_j
                        next_best_house_rating = next_house.rating
        num_visited += 1
        # find the next i,j to go to
       

    # check if path is ideal
    avg_path_rating = sum(path) / len(path)

    if avg_path_rating >= avg_house_rating:
        print("pass", avg_path_rating)
    else:
        print("not pass")
    
    
    house = []

    houseB = 0
    for i in range(5):
        
        houseNum = []
        streetNum = []
        
        for a in range(5):
            houseNum.append(House())
            
            houseB = houseB + houseNum[a].getRating()
            
            streetNum.append(houseNum[a].getRating())
            
        house.append(houseNum)
        print(streetNum)

    
    
    x = int(input("which house in x-axis?"))
    
    y = int(input("which house in y-axis?"))
    
    n = int(input("How many houses?"))


    street = [x, y]
    sums = 0
    house[street[0]][street[1]].passing()
    s  = int(house[street[0]][street[1]].getRating())
    sums = sums + s
    
    
    for k in range (n-1):
        p = path(house, street[0], street[1])
        sums = sums + int(p[0])
        
        street = [int(p[1]), int(p[2])]
        house[street[0]][street[1]].passing()
        
    
    print ("\nAverage houses val:" + str(sums/n))

    print ("all houses val: " + str(houseB/25))
        
        



if __name__ == "__main__":
    main()
