# Example 1 - baby shower pool

# Write a class that represents a single bet/participant in the pool
class Bet:
    # constructor -> takes length and weight guesses
    def __init__(self, length, weight):
        self.length = length
        self.weight = weight
    
    def calculate_score(self):
        actual_length = 20
        actual_weight = 106
        # 5 points per inch off of actual length
        # difference = actual_length - self.length -> 20 - 18 = 2 (multiply by 2 to find out how many 0.5-inch units the guess if off)
        # what if the guess is higher than the actual? -> 20 - 22 = -2 -> need to use absolute value
        length_score = (abs(actual_length - self.length)*2)*5
        # print(length_score)
        # 5 points per oz off of actual weight -> similar strategy as calculating length score
        weight_score = abs(actual_weight - self.weight)*5
        # total = length_score + weight_score
        # return total
        return (length_score + weight_score)
# 16 oz in lb -> 7lb = 112oz
riley = Bet(22, 112)
# 20 - 18 = 2, 2 * 2 = 4, 4 * 5 = 20
# 106 - 112 = 6, 6 * 5 = 30
# total = 20 + 30 = 50
sanjana = Bet(27, 130)
marc = Bet(20, 116)
# print(riley.calculate_score())
# print(sanjana.calculate_score())
# print(marc.calculate_score())


# Example 2 - Processing file
# data.txt
class Processing: # define a class called Processing
    def __init__(self, filename):
        # what should our dictionary look like?
        # {'1001': {
        # 'first_name': 'Rachel',
        # 'last_name' : 'Green',
        # 'midterm_average': 71.0
        # },
        #  '1002': {
        # 'first_name': 'Ross',
        # 'last_name': 'Geller',
        # 'midterm_average': 95.0
        # }
        # }
        data_list = []
        with open(filename, 'r') as file:
            for line in file:
                data = line.split(',')
                data_list.append(data)
#        print(data_list)
        self.data_dict = {}
        for data in data_list[1:]:
            #print(data)
            self.data_dict[data[0]] = {
                'first_name':data[1],
                'last_name':data[2],
                'midterm_average':float(data[3])
            }
    
    def get_average(self):
#        print(self.data_dict)
        # return the average of midterm grades
        total = 0
        count = 0
        for d in self.data_dict:
            #print(self.data_dict[d]['midterm_average'])
            total += self.data_dict[d]['midterm_average']
            count += 1
        #print(total/count)
        return total/count
    
    def get_names(self):
        name_list = []
        for d in self.data_dict:
            name = self.data_dict[d]['first_name'] + self.data_dict[d]['last_name']
            name_list.append(name)
        #print(name_list)
        return name_list
    
    def add_student(self, sid, first_name, last_name, midterm_average):
        self.data_dict[sid] = {
            'first_name':first_name,
            'last_name': last_name,
            'midterm_average':midterm_average
        }
        #print(self.data_dict)
    


p = Processing('data.csv')
p.add_student('1007', 'Jane', 'Doe', 50.0)