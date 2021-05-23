from double_ll import DoubleLinkedList

subway = DoubleLinkedList()
subway.add_to_head("Times Square")
subway.add_to_head("Grand Central")
subway.add_to_head("Central Park")
subway.add_to_tail("Penn Station")
subway.add_to_tail("Wall Street")
subway.add_to_tail("Brooklyn Bridge")
subway.remove_head()
subway.remove_tail()
subway.remove_by_value("Times Square")

print(subway.stringify_list())