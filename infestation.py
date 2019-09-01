from math import hypot, floor
GRIDBOURNE = [["A1", "B1", "C1", "D1", "E1", "F1", "G1", "H1", "I1", "J1"],
              ["A2", "B2", "C2", "D2", "E2", "F2", "G2", "H2", "I2", "J2"],                    
              ["A3", "B3", "C3", "D3", "E3", "F3", "G3", "H3", "I3", "J3"],                        
              ["A4", "B4", "C4", "D4", "E4", "F4", "G4", "H4", "I4", "J4"],                        
              ["A5", "B5", "C5", "D5", "E5", "F5", "G5", "H5", "I5", "J5"],                       
              ["A6", "B6", "C6", "D6", "E6", "F6", "G6", "H6", "I6", "J6"],                       
              ["A7", "B7", "C7", "D7", "E7", "F7", "G7", "H7", "I7", "J7"],                       
              ["A8", "B8", "C8", "D8", "E8", "F8", "G8", "H8", "I8", "J8"],
              ["A9", "B9", "C9", "D9", "E9", "F9", "G9", "H9", "I9", "J9"],                        
              ["A10", "B10", "C10", "D10", "E10", "F10", "G10", "H10", 
               "I10", "J10"]]

def find_my_neighbourhood(x, y):
    """ Change coordinates into the respective neighbourhood name. """
    return str(GRIDBOURNE[floor(x)][floor(y)]) 

def find_restaurants_to_shut(distance, list_of_epicentres):
    """ Finds the restaurants across neighbourhoods to be 'shut down', based on
        the list of epicentres where the rat infestation is, which is strictly
        less than 'distance' away from the infestation epicentres. """
    
    # stores all the restaurant names to be shut at all epicentres
    list_to_shut = []
    
    # finds the restaurants to shut around the coordinates of the epicentres
    # based on the distance from the epicentres
    for coord in list_of_epicentres:
        
        # stores the restaurant names to be shut at 1 epicentre
        resto_at_point = []
        
        # iterates over all x-coordinates in the whole grid/Gridbourne city
        for x in range(0, 10):
            
            # iterates over all y-coordinates in the whole grid/Gridbourne city
            for y in range(0, 10):
                
                # the case when the restaurant is located in the corner
                if hypot((x - coord[0]), (y - coord[1])) < distance:
                    resto_at_point.append(find_my_neighbourhood(x, y) + "CR")
                                
                # the case when the restaurant is located in the middle            
                if hypot(((x + 0.5) - coord[0]), ((y + 0.5) - coord[1])) \
                   < distance:
                    resto_at_point.append(find_my_neighbourhood(x, y) + "MR")
        
        list_to_shut.append(sorted(resto_at_point))
    
    return list_to_shut


if __name__ == '__main__':
    # Run the sample inputs.
    print(find_restaurants_to_shut(1.0, [[3.0, 3.0]]))
    print(find_restaurants_to_shut(0.4, [[1.0, 1.0], [2.0, 2.0]]))