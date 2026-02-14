import random
import sys

chromosomes=[]

#initial_chromosomes

text = "HELLO WORLD"

survival_rate=5

hello_world_ascii_values = []

mutation_rate=0.7



for s in text:
    hello_world_ascii_values.append(ord(s))

initial_no=100

allowed_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def score(chromosome):
    fitness=0
    for i in range(11):
        
        if(chromosome.string_data[i] == text[i]):
            fitness+=1
            
    return fitness

#STEP01
class chromosome:
    def __init__(self,string_data):
        self.string_data=string_data
        self.fitness=0
        
for i in range(initial_no):
        
    chrom=[]
        
    for j in range(11):
        if(j==5):
            chrom.append(" ")
        else:
            random_char = random.choice(allowed_chars)
            chrom.append(random_char)
        
    c = chromosome(chrom)
    chromosomes.append(c)
            
best_chromosome=chromosomes[0]

#STEP02
def fitness_check(chromosomes):
        
    list=[]
    for c in chromosomes:    
        c.fitness=score(c)
        list.append(c)
    list.sort(key= lambda c: c.fitness , reverse=True)
        
    return list

    
#STEP03    
def survival(list,survival_rate):
    count=survival_rate
    new_list=[]
    for i in range(count):
        new_list.append(list[i])
    return new_list

def mutation(chromosome_list):
            
    for c in chromosome_list:        
        for i in range(11):
            if i==5:
                continue
            else:
                random_float=random.random()
                if(random_float<=0.5 and random_float>=0.2):
                    random_str=random.choice(allowed_chars)
                    c.string_data[i]=random_str
                    
                    
def crossover(parent1,parent2):
    new_list=[]
    random_number= random.randint(0,10)
    
    for i in range(11):
        
        if(i<=random_number):
            charNow=parent1.string_data[i]
        else:
            charNow=parent2.string_data[i]
            
        new_list.append(charNow)
                
    return chromosome(new_list)
            

def printer(chromosome):
    str=""
    for s in chromosome.string_data:
        str+=s
    return str
    

generationCount=0

while(True):
    
    
    fitted_chromosomes=fitness_check(chromosomes)
    
    surviving_chromosomes=survival(fitted_chromosomes,survival_rate)
    
    best_chromosome = surviving_chromosomes[0]
    
    chromosome_index=0
    
    while(len(surviving_chromosomes) < initial_no):
        new_chromosome=crossover(surviving_chromosomes[chromosome_index] , surviving_chromosomes[chromosome_index+1])
        surviving_chromosomes.append(new_chromosome)
        chromosome_index+=1
    
    mutation(surviving_chromosomes[1:])
    
    generationCount+=1
    
    if(best_chromosome.fitness == 11):
        print(f"Generation {generationCount} : Best '{printer(best_chromosome)}' (Fitness: {best_chromosome.fitness}/11)")
        break
    else:
        print(f"Generation {generationCount} : Best '{printer(best_chromosome)}' (Fitness: {best_chromosome.fitness}/11)")
        
    chromosomes=surviving_chromosomes
    
    
    
#IF WE INCREASE/DECREASE THE MUTATION RATE 
    #-> decrease= the probability of the best_chromosome changing decreases because the letters are barely changing
    #-> increase= the letters change too much and we take far more generations

#HOW DOES THE POPULATION SIZE AFFECT THE CONVERGENCE SPEED?
    #-> takes more generations if increased and less generations if decreased

#WHAT IF I REMOVE ELITISM?
    #->the algorithm will forget my best_chromosome
    
#ARE SOME STRINGS HARDER TO EVOLVE?
    #-> takes more generation as the string increases