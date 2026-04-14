import math

BLOCKS = [
    ["ALU", 5, 5],
    ["Cache", 7, 4],
    ["Control␣Unit", 4, 4],
    ["Register␣File", 6, 6],
    ["Decoder", 5, 3],
    ["Floating␣Unit", 5, 5]
]

ALPHA=1000
BETA = 2
GAMMA = 1

ind = [(9,3), (12 ,15), (13 ,16),
(1,13), (4,15), (9,6)]
class helper:

    def overlap_count(self, ind):
        overlap = 0
        
        for i in range(len(ind) - 1):
            
            left1 = ind[i][0]
            bottom1 = ind[i][1]
            right1 = left1 + BLOCKS[i][1]  
            top1 = bottom1 + BLOCKS[i][2] 

            for j in range(i + 1, len(ind)):
                
                left2 = ind[j][0]
                bottom2 = ind[j][1]
                right2 = left2 + BLOCKS[j][1]
                top2 = bottom2 + BLOCKS[j][2]
                
                if not (right1 <= left2 or 
                        left1 >= right2 or 
                        bottom1 >= top2 or 
                        top1 <= bottom2):
                    overlap += 1
                    
        return overlap

    def bounding_box(self,ind):
        x_min=math.inf
        x_max=-math.inf

        y_min=math.inf
        y_max=-math.inf

        for index in range(len(ind)):
        
            block = BLOCKS[index]
            x_min = min(ind[index][0] , x_min)
            x_max =max(( ind[index][0] + block[1]) , x_max )
            y_min = min(ind[index][1] , y_min )
            y_max = max(( ind[index][1] + block[2]) , y_max )


        return ((y_max-y_min)*(x_max-x_min))

    def fitness_value(self,overlap , wiring , area):
        return -(ALPHA*overlap +BETA*wiring + GAMMA*area)


    def compute_all(self,ind,wiring):
        overlaps = self.overlap_count(ind)
        boundary_box_area = self.bounding_box(ind)
        fitness = self.fitness_value(overlaps, wiring , boundary_box_area )

        return fitness , overlaps , boundary_box_area



    
    