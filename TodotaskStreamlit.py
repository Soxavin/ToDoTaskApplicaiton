# NOTE: IGNORE ERRORS IN TERMINAL WHEN RUNNING THE CODE, JUST TYPE: streamlit run TodotaskStreamlit.py

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

    # Modified add_task function
    def add_task(self, task):
        new_node = Node(task)

        if self.head is None:
            self.head = new_node
        else:
            last_node = self.head
            while last_node.next:
                last_node = last_node.next
            last_node.next = new_node

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

        return tasks

# Create or get the linked list from session state
def get_linked_list():
    if 'linked_list' not in st.session_state:
        st.session_state.linked_list = LinkedList()
    return st.session_state.linked_list

# Create a Streamlit app
def main():
    st.title("To-Do List App with Linked List")

    # Initialize a linked list
    tasks_list = get_linked_list()

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

    # Main content to display tasks
    st.write("## Your To-Do List:")
    tasks = tasks_list.display_tasks()

    if not tasks:
        st.write("No tasks yet. Add some tasks using the sidebar!")

    for i, task in enumerate(tasks, start=1):
        st.write(f"{i}. {task}")

if __name__ == "__main__":
    main()