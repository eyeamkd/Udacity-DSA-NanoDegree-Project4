def get_minimum_platforms(arrival:list,departure:list):
    platforms_count = 0
    free_platforms = 0
    occupied_platforms = 0
    timings = merge_arrivals_departure(arrival, departure) 
    print("Timings are", timings)
    
    for i in timings:
        if i['type'] == 'arrival':
            if free_platforms > 0:
                free_platforms-=1 
                occupied_platforms+=1 
            else:
                platforms_count+=1 
        else:                 
            free_platforms+=1 
            occupied_platforms-=1 
    
    print("Minimum number of platforms required are ", platforms_count ) 
        
        
def merge_arrivals_departure(arrival:list, departure:list):
    result = []  
    arrival_pointer = 0 
    departure_pointer = 0 
    arrival.sort()
    departure.sort()
    while arrival_pointer <= len(arrival)-1 and departure_pointer <= len(departure)-1:
        if departure[departure_pointer]<=arrival[arrival_pointer]: 
            result.append({'type':'departure', 'time':departure[departure_pointer]})
            departure_pointer+=1 
        else: 
            result.append({'type':'arrival', 'time':arrival[arrival_pointer]})
            arrival_pointer+=1 
            
    if arrival_pointer < departure_pointer:
        while arrival_pointer <= len(arrival)-1:
            result.append({'type':'arrival', 'time': arrival[arrival_pointer]})
            arrival_pointer+=1 
    else:
        while departure_pointer <= len(departure)-1:
            result.append({'type':'departure', 'time': departure[departure_pointer]})
            departure_pointer+=1  
    #print(result)
    return result

arrival = [900,  940, 950,  1100, 1500, 1800]
departure = [910, 1200, 1120, 1130, 1900, 2000]  

arrival_1 = [200, 210, 300, 320, 350, 500]
departure_1 = [230, 340, 320, 430, 400, 520]

get_minimum_platforms(arrival_1, departure_1)
get_minimum_platforms(arrival, departure)
        