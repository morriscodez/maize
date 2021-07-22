import csv

#README
# This component is designed to dynamically parse csv files
# It takes two inputs:
# The first input (input_file) is the csv file that needs to be parsed
# The second input (parser_map) is the csv file that contains the instructions for how to parse the first file
# The function returns a brand new, parsed version of the input file (first file)
#! Two solutions must be added to make module more dynamic:
#! First, the index position is hardcoded, but ideally I would target column names
#! Second, the final csv writer is hard codes the new output .csv file name, so I need to find a way to make the naming of that file dynamic

# Function to parse a csv file using another csv file as a map and then return the output as a new, separate, parsed csv file
def codename_parser(input_file, parser_map):

    #file that handles instructions for parsing the input file
    with open(parser_map, 'r') as map:
        map_reader = csv.reader(map)

        # Establish empty dictionairy to contain key, value pairs from the parser map file
        mapped_object_dict = {}

        #Add key value pairs to the dictionairy looping through the map file line by line
        for line in map_reader:
            mapped_object_dict[line[0]] = line[1]

        #file to be parsed
        with open(input_file, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            
            # Establish empty list to contain each line of the csv file as it's own list nested inside the parsed_file_list
            parsed_file_list = []
            
            # check input file in terminal
            for line in csv_reader:
                
                # Check the input file to see if the current string at index position 2 is contained within the mapped_object_dictionairy as part of a key-value pair. If the string is a key inside that dictionairy, replace that string with the corresponding value in the key-value pair
                if line[2] in mapped_object_dict:
                    line[2] = mapped_object_dict[line[2]]
                    
                # Add the newly parsed line to the parsed_file_list
                parsed_file_list.append(line)

            # Write the new csv file using the parsed information contained in parsed_file_list
            with open('parsed.csv', 'w') as output:
                output_writer = csv.writer(output, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)

                for row in parsed_file_list:
                    output_writer.writerow(row)


#Run the function, check how it is working
codename_parser('one.csv', 'monster_map.csv')