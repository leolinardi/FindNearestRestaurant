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

def find_closest_restaurant(x, y):
    """ Finds the 'closest' distance between the user's location to the 
        surrounding restaurants across neighbourhoods. """
    
    # finds all of the the x and y coords of surrounding restaurants from the 
    # user's location across the neighbourhoods
    coords = [] 
    for x_value in range((floor(x) - 1), (floor(x) + 2)):
        
        for y_value in range((floor(y) - 1), (floor(y) + 2)):
            coords.append((x_value, y_value))
            coords.append((x_value + 0.5, y_value + 0.5))
    
    # sets up the initial distance between the user to a restaurant
    closest_distance = hypot((x - coords[0][0]), (y - coords[0][1]))
    
    # finds the closest distance between the user and the surrounding 
    # restaurants
    for digit in coords:
        new_distance = hypot((x - digit[0]), (y - digit[1]))
        
        if new_distance < closest_distance:
            closest_distance = new_distance
    
    # store the coords of the equidistant closest restaurants in a list
    closest_restaurants = []
    for digit in coords:
        if hypot((x - digit[0]), (y - digit[1])) == closest_distance:
            closest_restaurants.append((digit[0], digit[1]))
    
    # changes the closest restaurants coordinates into their respective 
    # names
    resto_list = []
    for coord in closest_restaurants:
        x_value = floor(coord[0])
        y_value = floor(coord[1])
        
        # the case when the restaurant is located in the corner
        if str(int(coord[0]/0.5))[-1] in "02468":
            resto_list.append(find_my_neighbourhood(x_value, y_value) + "CR")
        
        # the case when the restaurant is located in the middle
        else:
            resto_list.append(find_my_neighbourhood(x_value, y_value) + "MR")
    
    return sorted(resto_list)

def find_closest_restaurant_on_path(list_of_stops):
    """ Finds the 'closest' distance between the user's path (a list consisting
        coordinates of the user's stop points) to the surrounding restaurants
        across neighbourhoods. """
    
    # finds all the surrounding closest restaurants based on the user's 
    # stop points
    resto_list_path = []
    for path in list_of_stops:
        resto_list_path.append(find_closest_restaurant(path[0], path[1]))    
    return resto_list_path    


if __name__ == '__main__':
    # Run the sample inputs.
    print(find_closest_restaurant(1.0, 1.0))
    print(find_closest_restaurant_on_path([[1.0, 1.0], [4.5, 4.0]]))