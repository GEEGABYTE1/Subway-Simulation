import time
from double_ll import DoubleLinkedList


class Solution:
    
    def gameplay(self):
        running = True
        subway = DoubleLinkedList()
        while running:
            time.sleep(0.1)
            print("You have three options")
            time.sleep(0.1)
            print('1: /view - You can view the next subway stations')
            print('2: /del -  Delete traveled subway stations')
            print('3: /add - Add a new subway station \n') 
            time.sleep(0.2)

            prompt = input()

            if prompt == '/view':
                if subway.head_node == None and subway.tail_node == None:
                    print('Your list is empty! ')
                print(subway.stringify_list())
            
            elif prompt == '/del':
                print(subway.stringify_list())
                print("-"*24)
                subway_station = input('Please type the station you would like to delete: ')

                result = subway.remove_by_value(subway_station)

                if result == None:
                    print("That station does not seem to be documented")
                    print("-"*24)
                else:
                    print(result)
                    print("-"*24)
            
            elif prompt == '/add':
                new_subway = input('Please type a new subway station you would like to add: ')
                
                mini_prompt = True 
                while mini_prompt:
                    view = input("Have you already visited this station before or is this an upcoming destination? (Type either \"upcoming desintation\" if you still have to visit the station or \"already visited\" if already visited): ")

                    if view == "already visited":
                        subway.add_to_head(new_subway)
                        print("-"*24)
                        break

                    elif view == "upcoming destination":
                        subway.add_to_tail(new_subway)
                        print("-"*24)
                        break 
                    else:
                        print('That command does not seem to be valid')
                        print("-"*24)
            
            elif prompt =='/quit':
                break
            
            else:
                print("That command is not valid")


game = Solution()

print(game.gameplay())
                    








