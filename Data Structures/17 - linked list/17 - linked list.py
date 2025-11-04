""""Implementation of a singly linked list in Python."""
class Node:
    """A class representing a node in a linked list."""
    def __init__(self, data):
        """
        Initialize a new node with data.
        
        Args:
            data: The data to store in the node.
        """
        # Store the given data in the node
        self.data = data  
        # Initialize the next pointer to None, indicating no next node yet
        self.next = None  

class LinkedList:
    """A class representing a singly linked list."""
    def __init__(self):
        """
        Initialize the linked list.
        The head of the list is set to None, indicating that the list is initially empty.
        """
        # The head of the linked list, initially set to None
        self.head = None  

    def add_to_beginning(self, data):
        """
        Add a new node with the specified data at the beginning of the linked list.
        
        Args:
            data: The data to store in the new node.
        """
        # Create a new node with the provided data
        new_node = Node(data)  
        # Set the new node's next pointer to the current head
        new_node.next = self.head  
        # Update the head of the linked list to be the new node
        self.head = new_node  

    def add_to_end(self, data):
        """
        Add a new node with the specified data at the end of the linked list.
        
        Args:
            data: The data to store in the new node.
        """
        # Create a new node with the provided data
        new_node = Node(data)  
        # Check if the linked list is currently empty
        if not self.head:  
            # If empty, make the new node the head of the list
            self.head = new_node  
            # Exit the function since the node has been added
            return  

        last_node = self.head
        # Start from the head to find the last node in the list  
        # Traverse the list until the last node is found
        # Continue until we reach a node with no next node
        while last_node.next:  
            # Move to the next node
            last_node = last_node.next  
        # Set the last node's next pointer to the new node
        last_node.next = new_node  

    def add_at_position(self, data, position):
        """
        Add a new node with the specified data at a specific position in the linked list.
        
        Args:
            data: The data to store in the new node.
            position: The position where the new node should be added (0-indexed).
        """
        # If the position is 0, add the node at the beginning
        if position == 0:  
            # Call the method to add at the beginning
            self.add_to_beginning(data)  
            return  
        # Create a new node with the provided data
        new_node = Node(data)  
        # Start from the head to find the correct position
        current_node = self.head  
        # Initialize an index to keep track of the current position
        current_index = 0  

        # Traverse the list to find the position to insert the new node
          # Stop when we reach the desired position
        while current_node and current_index < position - 1:
            # Move to the next node
            current_node = current_node.next  
            # Increment the index
            current_index += 1  
        # If we reached the end of the list before the position        
        if current_node is None:  
              # Inform the user that the position is invalid
            print("Position out of bounds.")
            return  

        # Insert the new node at the specified position
        # Set the new node's next to the current node's next
        new_node.next = current_node.next  
        # Update the current node's next to point to the new node
        current_node.next = new_node  

    def display(self):
        """
        Print the elements of the linked list.
        Traverse the list and print the data in each node.
        """
        # Start from the head of the list
        current_node = self.head  
        # Continue until we reach the end of the list
        while current_node:  
            # Print the data in the current node
            print(current_node.data, end=' -> ')  
             # Move to the next node
            current_node = current_node.next 
        # Indicate the end of the list
        print("None")  

# Example usage of the LinkedList class
if __name__ == "__main__":
    ll = LinkedList()  
    ll.add_to_end(1)  
    ll.add_to_end(2)  
    ll.add_to_beginning(0)
    ll.add_at_position(1.5,1)
    ll.display()










