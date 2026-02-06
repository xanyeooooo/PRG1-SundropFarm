#Xander Yeo Kai Kiat CSF03
#PRG1 Assignment

#Additional Features : Limited Capacity for Seed Bag, High Score Board

# Game variables
game_vars = {
    'day': 1,
    'energy': 10,
    'money': 20,
    'bag': {'LET': 0, 'POT': 0, 'CAU': 0},}


seed_list = ['LET', 'POT', 'CAU']
seeds = {
    'LET': {'name': 'Lettuce',
            'price': 2,
            'growth_time': 2,
            'crop_price': 3
            },

    'POT': {'name': 'Potato',
            'price': 3,
            'growth_time': 3,
            'crop_price': 6
            },

    'CAU': {'name': 'Cauliflower',
            'price': 5,
            'growth_time': 6,
            'crop_price': 14
            },
}

farm = [ [[None, None, None], [None, None, None], [None, None, None], [None, None, None], [None, None, None]],
         [[None, None, None], [None, None, None], [None, None, None], [None, None, None], [None, None, None]],
         [[None, None, None], [None, None, None], ['HSE', 'X', None], [None, None, None], [None, None, None]],
         [[None, None, None], [None, None, None], [None, None, None], [None, None, None], [None, None, None]],
         [[None, None, None], [None, None, None], [None, None, None], [None, None, None], [None, None, None]] ]


#-----------------------------------------------------------------------
# in_town(game_vars)
#
#    Shows the menu of Albatross Town and returns the player's choice
#    Players can
#      1) Visit the shop to buy seeds
#      2) Visit the farm to plant seeds and harvest crops
#      3) End the day, resetting Energy to 10 and allowing crops to grow
#
#      9) Save the game to file
#      0) Exit the game (without saving)
#-----------------------------------------------------------------------
def in_town(game_vars):
    show_stats(game_vars) #shows the stats of the player

    #prints menu
    #-----------------------------------------------------------------------
    print('You are in Albatross Town')
    print('-------------------------')
    print('1) Visit Shop')
    print('2) Visit Farm')
    print('3) End Day')
    print()
    print('9) Save Game')
    print('0) Exit Game')
    print('-------------------------')

    try:
        choice = int(input('Your choice? '))
    except ValueError:
        print('Invalid choice. Try again.')
        in_town(game_vars)
    #-----------------------------------------------------------------------

    #input validations
    #-----------------------------------------------------------------------
    if choice == 1: #visit shop
        print("Welcome to Pierce's Seed Shop!")
        in_shop(game_vars)

        
    elif choice == 2: #visit farm
        in_farm(game_vars, farm)
    
    elif choice == 3: #end day
        end_day(game_vars,seed_list,seeds,farm)

    elif choice == 9: #save game
        save_game(game_vars, farm)
        
    
    elif choice == 0: #exit game
        print('Goodbye!')

    else:
        print('Invalid choice. Try again.')
        in_town(game_vars)
    #-----------------------------------------------------------------------

    

#----------------------------------------------------------------------
# in_shop(game_vars)
#
#    Shows the menu of the seed shop, and allows players to buy seeds
#    Seeds can be bought if player has enough money
#    Ends when player selects to leave the shop
#----------------------------------------------------------------------
def in_shop(game_vars):
    
    show_stats(game_vars)

    
    print('What do you wish to buy?')
    # Print table header
    print(f"{'Seed':<15}{'Price':<10}{'Growth Time':<15}{'Crop Price':<10}")
    index = 1
    print('-' * 50)  # Print a separator line


    

    for seed_code in seed_list:
        seed_info = seeds[seed_code]
        print(f"{index}) {seed_info['name']:<15}{seed_info['price']:<10}{seed_info['growth_time']:<15}{seed_info['crop_price']:<10}")
        index +=1 

    print()

    print('0) Leave')
    print('-' * 50)

    try:
        choice = int(input('Your choice? '))
    except ValueError:
        print('Invalid choice. Try again.')
        in_shop(game_vars)


    if choice == 0: #player choose to leave the seed shop
        in_town(game_vars)

    elif 1 <= choice <= len(seed_list): #total 3 different seeds only

        #seed_list = ['LET', 'POT', 'CAU']

        seed_code = seed_list[choice - 1] #get the seed code from the seed_list
        #eg. if user enters 1, which is LET, it is index 0 in the seed_list 
        seed_info = seeds[seed_code] #find price, growth time of the specific seed
        #eg. seeds[0] = seeds[LET] = info of lettuce seed

        #Show balance
        print('You have ${}' .format(game_vars['money']))

        #ADDITIONAL FEATURE - LIMITED CAPACITY FOR SEED BAG
        
        max_bag_capacity = 10 #maximum capacity of the bag
        total_seeds_in_bag = sum(game_vars['bag'].values()) #sums up the total number of seeds in the bag
        has_reached_max_capacity = False

        # Prompt user for quantity
        try:
            quantity = int(input(f"How many do you wish to buy? "))
            if quantity < 0: #if user enters negative number
                print('You cannot buy a negative quantity of seeds.')
                in_shop(game_vars)
                
        except ValueError:
            print('Invalid choice. Try again.')
            in_shop(game_vars)

        if quantity + total_seeds_in_bag > max_bag_capacity: #if total seeds in bag + quantity exceeds max capacity
            print('You can only carry up to 10 seeds at a time.')
            has_reached_max_capacity = True
            
        
        # Calculate total price
        total_price = seed_info['price'] * quantity
        
        # Check if the user has enough money
        if has_reached_max_capacity == False: #if bag has not reached max capacity
            if total_price <= game_vars['money']: #if player has enough money
                # Update game_vars
                game_vars['money'] -= total_price #minus the total price from money
                game_vars['bag'][seed_code] += quantity #add the quantity of seeds to the bag
                
                print(f"You bought {quantity} {seed_info['name']} seeds.")
        
            elif total_price > game_vars['money']: #if player has not enough money
                print("You can't afford that!")
    else:
        print('Invalid choice. Try again.')
    
    in_shop(game_vars) #return to shop
# ----------------------------------------------------------------------
# draw_farm(farm, farmer_row, farmer_col)

#    Draws the farm
#    Each space on the farm has 3 rows:
#      TOP ROW:
#        - If a seed is planted there, shows the crop's abbreviation
#        - If it is the house at (2,2), shows 'HSE'
#        - Blank otherwise
#      MIDDLE ROW:
#        - If the player is there, shows X
#        - Blank otherwise
#      BOTTOM ROW:
#        - If a seed is planted there, shows the number of turns before
#          it can be harvested
#        - Blank otherwise
# ----------------------------------------------------------------------

farmer_row = ''
farmer_col = ''

def draw_farm(farm, farmer_row, farmer_col):

    #making functions

    def printrowseparator():
        print('+-----+-----+-----+-----+-----+',end='')
        print()

    def printrowcontent(farmer_row):
        for subrow in range(3): #prints 3 rows
            print('|',end='') #prints 3 straight lines at each level
            for col in row: 
                if col[subrow] == 'X':
                    print(f'  X  ', end='|') 
                elif col[subrow] is not None: #if is lettuce / potato / hse etc.
                    print(f' {col[subrow]} ', end='|')
                else: #else print empty space
                    print('     ', end='|')
            print()

    #printing the table
    printrowseparator() #prints the separator after every 3 rows, before going to the next
    # 3 rows

    
    for row in farm:
        printrowcontent(row)
        printrowseparator()

#----------------------------------------------------------------------
# in_farm(game_vars, farm))
#
#    Handles the actions on the farm. Player starts at (2,2), at the
#      farmhouse.
#
#    Possible actions:
#    W, A, S, D - Moves the player
#      - Will show error message if attempting to move off the edge
#      - If move is successful, Energy is reduced by 1
#
#    P - Plant a crop
#      - Option will only appear if on an empty space
#      - Shows error message if there are no seeds in the bag
#      - If successful, Energy is reduced by 1
#
#    H - Harvests a crop
#      - Option will only appear if crop can be harvested, i.e., turns
#        left to grow is 0
#      - Option shows the money gained after harvesting
#      - If successful, Energy is reduced by 1
#
#    R - Return to town
#      - Does not cost energy
#----------------------------------------------------------------------
def in_farm(game_vars, farm):
    def get_position(farm,farmer_row,farmer_col): #used to keep track of the row and column indices 
        for row_num, row in enumerate(farm):#row_num = index of the row, row = the row itself
            for col_num, col in enumerate(row):
                if col[1]=="X":
                    return row_num, col_num #return the row ad column number

    #Move back player to house
    for row in farm:
        for col in row:
            if col[1] == 'X': #clears the current player position
                col[1] = None
                
    farm[2][2][1] = 'X' #sets the player position at the house

    while True:
        print()
        row_num, col_num = get_position(farm,farmer_row,farmer_col) #gets the x and y coords of player
        draw_farm(farm,farmer_col,farmer_row)
        print()

        
        print(f"Energy: {game_vars['energy']}")
        print('[WASD] Move')

        #Checking if player can plant a seed
        if farm[row_num][col_num][0] is None and sum(game_vars['bag'].values()) != 0: #if farm plot is empty and there is seeds in the bag
            print('P)lant seed')

        #Checking a seeds ability to be harvested
        if farm[row_num][col_num][2] is not None: #if crop growth time is not None
            growth_time = int(farm[row_num][col_num][2]) #convert growth time to integer
        else:
            growth_time = None 

        if growth_time == 0 and farm[row_num][col_num][0] is not None and farm[row_num][col_num][0] != 'HSE': 
            #if crop growth time = 0, and if there is a crop planted, and if current location is not HSE
            crop_code = farm[row_num][col_num][0] 
            crop_name = seeds[crop_code]['name']
            crop_price = seeds[crop_code]['crop_price']
            print(f'H)arvest {crop_name} for ${crop_price}')
        
        print('R)eturn to Town')
        move = input('Your choice? ').upper()


        if move == 'R': #return to town
            in_town(game_vars)

        #WASD movements    
        #----------------------------------------------------------------------------------------------------------------------------------------------
        if game_vars['energy'] > 0: #if player has energy, move
            if move == "W" and row_num > 0: # Move Up
                farm[row_num][col_num][1] = None #clears the current position
                farm[row_num-1][col_num][1] = 'X' #shifts up
                game_vars['energy'] -= 1 
                
            elif move == "S" and row_num < len(farm) - 1:  # Move Down
                farm[row_num][col_num][1] = None
                farm[row_num+1][col_num][1] = 'X'
                game_vars['energy'] -= 1 
                

            elif move == "A" and col_num > 0:  # Move Left if col_num is not at the most left
                farm[row_num][col_num][1] = None
                farm[row_num][col_num-1][1] = 'X'
                game_vars['energy'] -= 1 
                

            elif move == "D" and col_num < len(farm[0]) - 1:  # Move Right
                farm[row_num][col_num][1] = None
                farm[row_num][col_num+1][1] = 'X'
                game_vars['energy'] -= 1 
            
            #only if player moves, then energy will be subtracted, placing energy-1 here will minus energy even though if player does not move 
            #eg. trying to go right if player is already at top right -> cannot move

        else: #if player no energy
            print("You're too tired. You should get back to town.")
            game_vars['energy'] = game_vars['energy']
        #----------------------------------------------------------------------------------------------------------------------------------------------
        
        #Planting of seeds
        #----------------------------------------------------------------------------------------------------------------------------------------------
        seeds_code = {'Lettuce': 'LET', 'Potato': 'POT', 'Cauliflower': 'CAU'}

        if move == 'P':

            has_seeds = False #initially no seeds

            for seed_count in game_vars['bag'].values(): #iterates over each item in the bag
                if seed_count > 0: #if any item count is more than 0 , has_seeds = True
                    has_seeds = True
                    break

            if farm[row_num][col_num][0] is None and not has_seeds:#if farm plot is empty and no seeds in bag
                print("You can't plant here as you have no seeds.")
                game_vars['energy'] = game_vars['energy']

            elif farm[row_num][col_num][0] is None and has_seeds: #if farm plot is empty and has seeds
                index = 1
                seed = {}
                displayed_seeds = [] #list to keep track of seeds that are displayed in the table
                #when the user makes a choice, they will input a number which corresponds to the seed they want to plant
                

                #Prints table 
                print('What do you wish to plant?' )
                print('------------------------------------------------------------')
                print(f"    {'Seed':<18}{'Days to Grow':<15}{'Crop Price':14}{'Available'}")
                print('------------------------------------------------------------')

                for seed, seed_details in game_vars['bag'].items(): #seed -> key, seed_details -> value, item= key-value pair
                    count = game_vars['bag'].get(seed,0) #retrieves the quantity of a specific seed, get retrieves the value of the key, if key is not present, it returns 0
                    if count > 0 : #if there are seeds in the bag
                        seed_details = seeds[seed] #retrieves the seed info from the seeds dictionary,
                        growth_time = seed_details['growth_time']
                        crop_price = seed_details['crop_price']
                        print(f"{index:}) {seed_details['name']:<18} {growth_time:^12} {crop_price:^14}     {count:^1}")  # Debugging line: Check if values are printed correctly
                        print()
                        displayed_seeds.append(seed) #adds the seed to the displayed_seeds list
                        index += 1

                print('0) Leave')
                print('------------------------------------------------------------')


                try:
                    choice = int(input('Your choice? '))
                except ValueError:
                    print('Invalid choice. Try again.') 
                    continue


                if choice == 0: #if player chooses to leave
                    break
                elif 1<=choice<= len(displayed_seeds): #if player chooses to plant a seed
                    # gets the key from the dictionary, convert it to a list and get the index of the choice
                    chosen_seed = displayed_seeds[choice-1]
                    #this list helps to map back this number to the correct seed. eg. user chooses 1, use displayed_seeds[0] to get the seed they chose

                    if game_vars['bag'][chosen_seed] > 0:
                        # Place the seed in the farm and minus quantity of seed by 1
                        farm[row_num][col_num][0] = chosen_seed
                        farm[row_num][col_num][2] = f"{seeds[chosen_seed]['growth_time']:^3}"
                        #decreases quantity of chosen seed (LET / POT etc.) by 1
                        game_vars['bag'][chosen_seed] -= 1 
                        game_vars['energy'] -= 1
                    else:
                        print(f"You don't have any {seeds[chosen_seed]['name']} seeds.")
                else:
                    print('Invalid choice. Try again.')
        #----------------------------------------------------------------------------------------------------------------------------------------------

        #Harvesting of seeds
        #----------------------------------------------------------------------------------------------------------------------------------------------  
        elif move == 'H':
            if growth_time == 0:
                if game_vars['energy'] > 0: #if player has energy
                    crop = farm[row_num][col_num][0] #gets the crop code
                    crop_price = seeds[crop]['crop_price'] #gets the crop price
                    game_vars['money'] += crop_price #adds money gained from harvesting to wallet
                    farm[row_num][col_num][0] = None #remove crop name
                    farm[row_num][col_num][2] = None #remove crop time
                    game_vars['energy'] -= 1 
                    print(f"You harvest the {seeds[crop]['name']} and sold it for ${crop_price}!")
                    print(f'You now have ${game_vars["money"]}!')


                else: #if player no energy
                    print("You're too tired. You should get back to town.")
                    game_vars['energy'] = game_vars['energy']
            else:
                print("This crop is not ready to harvest yet.")
        #----------------------------------------------------------------------------------------------------------------------------------------------

        elif move not in ['P','H','R','W','A','S','D']: #if player enters invalid input
            print('Invalid direction. Try again.') #if input is not P / H / R / WASD

#----------------------------------------------------------------------
# show_stats(game_vars)
#
#    Displays the following statistics:
#      - Day
#      - Energy
#      - Money
#      - Contents of Seed Bag
#----------------------------------------------------------------------
def show_stats(game_vars):

    day = game_vars["day"]
    energy = game_vars["energy"]
    money = game_vars["money"]
    print("+--------------------------------------------------+")
    print("| Day {:<2}            Energy: {:<3}      Money: ${:<4}  |".format(day, energy,  money))
    
    
    if sum(game_vars['bag'].values()) == 0: #adds up all the values (seeds) in the bag, if 0 = no seeds
        print('| You have no seeds.                               |')
        print("+--------------------------------------------------+")
        print()

    else: #if have seeds:
        print(f"| Your seeds:{' ':38}|")
        
        if 'LET' in game_vars['bag'] and game_vars['bag']['LET'] != 0: #if there are lettuce seeds
            print(f"|{' ':2}Lettuce: {' ':10}{game_vars['bag']['LET']:9}{' ':20}|")   
        if 'POT' in game_vars['bag'] and game_vars['bag']['POT'] != 0: #if there are potato seeds
            print(f"|{' ':2}Potato: {' ':10}{game_vars['bag']['POT']:10}{' ':20}|")   
        if 'CAU' in game_vars['bag'] and game_vars['bag']['CAU'] != 0: #if there are cauliflower seeds
            print("|{0:2}Cauliflower: {1:10}{2:5}{3:20}|".format(" ", "", game_vars['bag']['CAU'], " "))
        print("+--------------------------------------------------+")

#----------------------------------------------------------------------
# end_day(game_vars)
#
#    Ends the day
#      - The day number increases by 1
#      - Energy is reset to 10
#      - Every planted crop has their growth time reduced by 1, to a
#        minimum of 0
#----------------------------------------------------------------------

def end_day(game_vars, seed_list, seeds, farm):
    # Increase the day by 1
    game_vars['day'] += 1
    
    # Reset energy to 10
    game_vars['energy'] = 10
    
    # Decrease the crop growth time by 1 for each crop in the farm
    for row in farm:
        for crop in row:
            if crop[2] is not None: #if crop growth time is not None
                crop[2] = int(crop[2])
                if crop[2] > 0:  # Ensure crop growth time doesnt go below 0
                    crop[2] -= 1
                crop[2] = f'{crop[2]:^3}'

    #Move back player to house
    for row in farm:
        for col in row:
            if col[1] == 'X':
                col[1] = None
                
    farm[2][2][1] = 'X'
            
    #If next day is Day 21
    if game_vars['day'] == 21:
        if game_vars['money'] >= 100:
            print(f"You have ${game_vars['money']} after 20 days.")
            profit = game_vars['money'] - 100
            print(f'You paid off your debt of $100 and made a profit of ${profit}.')
            print('You win!')

            #Prompt for player name 
            player_name = input('Enter your name: ')

            with open('scoreboard.txt' , 'a') as scoreboard:
                scoreboard.write(f'{player_name},{profit}\n')

        else:
            print('You lose!')
        
        exit()

    in_town(game_vars)
#----------------------------------------------------------------------
# save_game(game_vars, farm)
#
#    Saves the game into the file "savegame.txt"
#----------------------------------------------------------------------
def save_game(game_vars, farm):
    with open('savegame.txt', 'w') as file:
        #Writing game_vars to savegame.txt
        file.write(f"Day: {game_vars['day']}\n")
        file.write(f"Energy: {game_vars['energy']}\n")
        file.write(f"Money: {game_vars['money']}\n")
        file.write(f"Bag: {game_vars['bag']}\n")
        
        # Write farm to the file
        file.write("Farm:\n") #writes the farm heading
        for row in farm:
            file.write('\t'.join(str(cell) for cell in row) + '\n')
            #each cell is converted to a string and joined by a tab, then written to the file
            # \n : ensures that the next row is written on a new line
    
    print("Game saved.")
    exit()

#----------------------------------------------------------------------
# load_game(game_vars, farm)
#
#    Loads the saved game by reading the file "savegame.txt"
#----------------------------------------------------------------------
def load_game(game_vars, farm):
    #Initialise empty game_vars dictionary and farm list
    game_vars = {}
    farm = []

    with open('savegame.txt', 'r') as file:
        lines = file.readlines()
        
        # Load game variables
        game_vars['day'] = int(lines[0].split(': ')[1].strip()) #line 0 = Day : x, splitting and stripping, 
        #index 0 = Day, index 1 = x, where x is the days
        game_vars['energy'] = int(lines[1].split(': ')[1].strip())
        game_vars['money'] = int(lines[2].split(': ')[1].strip())
        
        # Load  bag data
        bag_data_str = lines[3].split('Bag: ')[1].strip() #4th line of the file, where the bag data is stored
        bag_data_str = bag_data_str.strip('{}') #remove the curly brackets 
        bag_data_items = bag_data_str.split(', ') #split to get the individual key-pair
        bag_data = {} #create a dictionary to store the key-value pairs
        for item in bag_data_items: #iterate over the items in the bag_data_items
            key, value = item.split(': ') #split the key and value
            bag_data[key.strip("'")] = int(value)  #removes the single quotes from the key string
            #eg. if key is "'LET'" it will be converted to "LET", convert the value string to an integer

            #assigns the integer value to the dictionary with the key
            #eg. if "LET" = 10 -> bag_data['LET'] = 10
        game_vars['bag'] = bag_data  #assigns the bag_data dictionary to the game_vars dictionary


        # Load farm data

        # Find the index of the start of the farm data (data of farm is one line below the farm heading)
        farm_start_index = lines.index("Farm:\n") + 1 

        for line in lines[farm_start_index:]: #iterates over each line starting from the farm_start_index
            row = [] 
            cells = line.strip().split('\t') #strip any whitespace and split the line by tabs
            for cell in cells: #iterates over each cell in the current row
                cell = cell.strip('[]') #removes square brackets
                if cell == 'None': #check if cell contains None, if true, append None to the row list
                    row.append(None) 
                else:
                    row.append(cell.strip("'").split(',')) #else remove the single quotes, split it by comma, 
                #and append to row list

                #eg. cell is " 'HSE, X'" -> remove single quotes -> "HSE, X" -> split by comma -> ['HSE', 'X']
                farm.append(row)

    print('Game loaded')
    in_town(game_vars)
    
    return game_vars, farm

#----------------------------------------------------------------------
#   ADDITIONAL FEATURES : HIGH SCORE BOARD
#----------------------------------------------------------------------
def show_high_scores():
    scores = []
    with open('scoreboard.txt', 'r') as scoreboard:
        for line in scoreboard:
            player_name, score = line.strip().split(',')
            scores.append((player_name,int(score)))
    
    def custom_sort(score):
        return score[1] #sorts by the second element in the tuple (score)

    scores.sort(key=custom_sort,reverse=True) #sorts the scores list in descending order 
    #according to the score returned in custom_sort

    print('High Scores: ')
    for name,score in scores[:5]: #first 5 elements of the list
        print(f'{name} : ${score}')
#----------------------------------------------------------------------
#    Main Game Loop
#----------------------------------------------------------------------
def main_loop(game_vars):
    print("----------------------------------------------------------")
    print("Welcome to Sundrop Farm!")
    print()
    print("You took out a loan to buy a small farm in Albatross Town.")
    print("You have 30 days to pay off your debt of $100.")
    print("You might even be able to make a little profit.")
    print("How successful will you be?")
    print("----------------------------------------------------------")

    # Write your main game loop here

    print('1) Start a new game')
    print('2) Show high scores')
    print('3) Load your saved game')
    print()
    print('0) Exit Game')

    try:
        choice = int(input('Your choice? '))
    except ValueError:
        print('Invalid choice. Try again.')
        main_loop(game_vars)

    print()

    if choice == 1:
        in_town(game_vars)

    elif choice == 2:
        show_high_scores()

    elif choice == 3:
        load_game(game_vars,farm)


    elif choice == 0:
        print('Goodbye!')

    else:
        print('Invalid choice. Try again.')
        main_loop(game_vars)

main_loop(game_vars)
