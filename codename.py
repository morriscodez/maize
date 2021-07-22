import csv

#README
# This component is designed to dynamically parse csv files
# It takes two inputs:
# The first input (input_file) is the csv file that needs to be parsed
# The second input (parser_map) is the csv file that contains the instructions for how to parse the first file
# The function returns a brand new, parsed version of the input file (first file)

# Function to parse a csv file using another csv file as a map and then return the output as a new, separate, parsed csv file
def codename_parser(input_file, parser_map):

    #file to be parsed
    with open(input_file, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)

        # check input file in terminal
        for line in csv_reader:
            print("input_file line:", line)

    #file that instructs how the above file is to be parsed
    with open(parser_map, 'r') as map:
        map_reader = csv.reader(map)

        mapped_object_dict = {}

        #check monster map in terminal
        for line in map_reader:
            print("monster_map line:", line)
            mapped_object_dict[line[0]] = line[1]
            
        print("map check of Forest Ghost:", mapped_object_dict["Forest Ghost"])
                        
            


#Run the function, check how it is working
codename_parser('one.csv', 'monster_map.csv')



# with open('one.csv', 'r') as csv_file:
#         csv_reader = csv.reader(csv_file)

# print("csv_reader:", csv_reader)

# with open ('monster_map.csv', 'r') as map:
#     map_reader = csv.reader(map)

#     mapped_object_dict = {}

#     for line in map_reader:
#         print(line)
#         mapped_object_dict[line[0]] = line[1]
        
#     print("map:", mapped_object_dict["Forest Ghost"])    
            
            
            
            
            # for line in csv_reader:
                
            #     lineToStr = ','.join([str(elem) for elem in line])
                
            #     if "Bigfoot" in lineToStr:
            #         print(lineToStr.replace("Bigfoot", "FuzzyHuman"))
                
            #     elif "Lake Monster" in lineToStr:
            #         print(lineToStr.replace("Lake Monster", "GoodSwimmer"))

            #     elif "Forest Ghost" in lineToStr:
            #         print(lineToStr.replace("Forest Ghost", "TransparentCamper"))

            #     elif "Talking Cactus" in lineToStr:
            #         print(lineToStr.replace("Talking Cactus", "DesertBuddy"))

            #     elif "Ice Dragon" in lineToStr:
            #         print(lineToStr.replace("Ice Dragon", "ColdBird"))

            #     else :
            #         print(lineToStr)

                




            
            
            
            