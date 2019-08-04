def sum_of_a_beach(beach):
    return beach.lower().replace('sun','*').replace('sand','*').replace('fish','*').replace('water','*').count('*')

'''
Beaches are filled with sand, water, fish, and sun. Given a string,
 calculate how many times the words "Sand", "Water", "Fish", and "Sun"
 appear without overlapping (regardless of the case).
 
Examples

sum_of_a_beach("WAtErSlIde")                    ==>  1
sum_of_a_beach("GolDeNSanDyWateRyBeaChSuNN")    ==>  3
sum_of_a_beach("gOfIshsunesunFiSh")             ==>  4
sum_of_a_beach("cItYTowNcARShoW")               ==>  0
'''