import sys
import random
import csv 

size = 100
if len(sys.argv) > 1:
    try:
        size = int(sys.argv[1])
    except ValueError:
        print("Incorrect value")
        sys.exit()

#gender: -1 = male, 0 = female, 1 = other
#age: 1-100
#criminal: 1 = criminal, 0 = not
#family: 1 = has, 0 = doesn't
#rich: 1 = rich, 0 = average, -1 = poor
#important: 1 = important job, 0 = unimportant
#species: 0 = human, -1 = cat, 1 = dog
#count = -1 = 2, 0 = 1, 1 = 3
#evil = 1 = evil, 0 = not
#story = text describing data
#result: 1 = person one dead, 0 = person two dead

#Are they gonna die soon ?
def decisionTree(positive = "broken", negative = "broken", num = 0, middle = "empty",):
    if middle == "empty":
        if num == 1:
            return positive
        else: 
            return negative
    if middle != "empty":
        if num == 1:
            return positive
        elif num == -1:
            return negative
        else:
            return middle
    

def makeStory(container = 0):
    if container == 0:
        return
    
    for i in container:
        pointer = 0
        story = ""
        for j in range(2):
            gender = decisionTree("other", "male", i[pointer + 0], "female")
            age = i[pointer + 1]
            criminal = decisionTree("criminal", "", i[pointer + 2])
            family = decisionTree("with", "without", i[pointer + 3])
            rich = decisionTree("rich", "poor", i[pointer + 4], "")
            important = decisionTree("important", "", i[pointer + 5])
            species = decisionTree("dog", "cat", i[pointer + 6], "human")
            count = decisionTree("3", "2", i[pointer + 7], "1")
            evil = decisionTree("evil", "", i[pointer + 8])
            pointer += 9
            
            story += "On one side, there are {count} {age} year old {gender} {criminal} {rich} {important} {evil} {species} that is {family} family \n".format(count = count, age = age, gender = gender, criminal = criminal, rich = rich, important = important, evil = evil, species = species, family = family)
        i.append(story)
    
    
    

def genData(container = 0):
    
    if container == 0:
        return
    
    for i in range(2):
        gender = random.randrange(1, 101)
        age = random.randrange(1, 101)
        criminal = random.randrange(1, 101)
        family = random.randrange(1, 101)
        rich = random.randrange(1, 101)
        important = random.randrange(1, 101)
        species = random.randrange(1, 101)
        count = random.randrange(1, 101)
        evil = random.randrange(1, 101)
        
        #Make that thing down there a method 
        
        if family >= 80:
            family = 0
        else:
            family = 1
        
        if gender <= 40:
            gender = -1
        elif gender >= 60:
            gender = 0
        else:
            gender = 1
        
        if count <= 30:
            count = -1
        elif count >= 70:
            count = 1
        else:
            count = 0
        
        if species <= 15:
            species = -1
        elif species >= 85:
            species = 1
        else:
            species = 0
        
        if criminal >= 80:
            criminal = 1
        else:
            criminal = 0
            
        if rich <= 20:
            rich = -1
        elif rich >= 90:
            rich = 1
        else:
            rich = 0
            
        if important >= 80:
            important = 1
        else:
            important = 0
        
        if evil <= 20:
            evil = 1
        else:
            evil = 0
            
        binaryFeatures = (criminal, rich, important, species, evil)
        
        for i in binaryFeatures:
            if i != 0:
                break
            if i == binaryFeatures[-1]:
                binaryFeatures = list(binaryFeatures)
                binaryFeatures[random.randrange(0, len(binaryFeatures))] = 1
        
        # if all(i == 0 for i in binaryFeatures):
        #     binaryFeatures = list(binaryFeatures)
        #     binaryFeatures[random.randrange(0, len(binaryFeatures))] = 1
            
        container.extend([gender, age, criminal, family, rich, important, species, count, evil])
    

fields = ["gender1", "age1", "criminal1", "family1", "rich1", "important1", "species1", "count1", "evil1", 
          "gender2", "age2", "criminal2", "family2", "rich2", "important2", "species2", "count2", "evil2",
          "story", "result"]

rows = [[]]

for i in range(size):
    genData(rows[i])
    rows.append([])
rows.pop(-1)

makeStory(rows)    
    
print(rows)
print(len(rows))
    
# name of csv file 
filename = "TrolleySamples.csv"
    
# writing to csv file 
with open(filename, 'w') as csvfile: 
    # creating a csv writer object 
    csvwriter = csv.writer(csvfile) 
        
    # writing the fields 
    csvwriter.writerow(fields) 
        
    # writing the data rows 
    csvwriter.writerows(rows)