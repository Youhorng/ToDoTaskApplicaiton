# Import necessary libraries
import streamlit as st

# Define a Node class for the linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Define a LinkedList class
class LinkedList:
    def __init__(self):
        self.head = None

    def add_task(self, task):
        new_node = Node(task)
        new_node.next = self.head
        self.head = new_node

    def remove_task(self, task):
        current = self.head
        previous = None

        while current is not None:
            if current.data == task:
                if previous is not None:
                    previous.next = current.next
                else:
                    self.head = current.next
                break
            previous = current
            current = current.next

    def display_tasks(self):
        tasks = []
        current = self.head

        while current is not None:
            tasks.append(current.data)
            current = current.next

        return tasks[::-1]

# Define a session state class to store the linked list
class _SessionState:
    def __init__(self):
        self._task_list = LinkedList()

    def get_task_list(self):
        return self._task_list

def get_session_state():
    if not hasattr(st, '_session_state'): # Check if the session state has been set
        st._session_state = _SessionState() # If not, set the session state
    return st._session_state

# Create a Streamlit app
def main():
    st.title("To-Do List App with Linked List")

    # Get the session state
    session_state = get_session_state()

    # Get the linked list from the session state
    tasks_list = session_state.get_task_list()

    # Sidebar for adding tasks
    task_input = st.sidebar.text_input("Add Task:")
    if st.sidebar.button("Add"):
        if task_input:
            tasks_list.add_task(task_input)

    # Sidebar for removing tasks
    task_to_remove = st.sidebar.text_input("Remove Task:")
    if st.sidebar.button("Remove"):
        if task_to_remove:
            tasks_list.remove_task(task_to_remove)

    # Sidebar for viewing tasks
    if st.sidebar.button("View Tasks"):
        # Main content to display tasks
        st.write("## Your To-Do List:")
        tasks = tasks_list.display_tasks()

        if not tasks:
            st.write("No tasks yet. Add some tasks using the sidebar!")

        for i, task in enumerate(tasks, start=1):
            st.write(f"{i}. {task}")

if __name__ == "__main__":
    main()