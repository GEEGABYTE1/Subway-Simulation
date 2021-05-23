# Subway Station Tracker 🔂
Keep track of subway stations easily 🚅

Built using Bidirectional Linked List

# Commands

- `/view` - View the next subway stations on the list
- `/del` - Delete traveled subway stations 
- `/add` - Add a new subway station to the list
- `/quit` - Quit the program

*Note: Any other command will not work as the program will decline it.

# Extras

- `/del`: If the list is empty, and the user tries to delete a certain "station", the program will return that the list itself is empty.
- `/view`: If the list is empty, instead of returning the list itself, the software will return `Your list is empty!` 
- When trying to add a new a subway station to the list, the program will prompt if you have *already visited* the station or if it is an *upcoming destination*. Based on the result it will either add to the head node (if the station was already visited) or add to the tail node (if the stations is an upcoming destination). This process is under a while loop hence, you would have to type either `upcoming destination` or `already visited` when prompted for the program to add the new station to the list. It will not take any other command under this process otherwise, the while loop will keep running.

- All Commands have been listed in the program as well. 

Time complexity: O(N) 

Made in Python 🐍
