from linked_list import LinkedList 

def merge_sort(linked_list):
    #sorts a linked list in asxending order 
    # -Recursively divide the linked list into sublists containing a single node
    # - Repeatedl merge the sublist to produce sorted sublists until one remains
    # Returns a sorted linked list
    
    if linked_list.size() == 1:
        return linked_list
    elif linked_list.head is None:
        return linked_list
    
    left_half , right_half = split(linked_list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)
    
    return merge(left, right)

def split(linked_list):
    #Divide the unsorted list at midpoint into sublists
    
    if linked_list == None or linked_list.head == None:
        left_half = linked_list 
        right_half = None
        
        return left_half, right_half
    else:
        size = linked_list.size() 
        mid = size // 2
        
        mid_node = linked_list.node_at_index(mid-1)
        
        left_half = linked_list 
        right_half = LinkedList()
        right_half.head = mid_node.next_node
        mid_node.next_node = None
        
        return left_half, right_half
    
def merge(left, right):
        #Merges two linked lists, sorting by data in nodes 
        #Return a new, merge list 
        
        #Create a new linked list that contains nodes from 
        # Merging left and right
        
    merged = LinkedList()
        # Add a fake head that is discarded later 
    merged.add(0)
        
        #Set current to the head of the linked list 
        
    current = merged.head 
        
        #obtain head nodes for left and right linked lists
    left_head = left.head 
    right_head = right.head 
        
        #iterate over left and right until we each the tail node of either
        
    while left_head or right_head:
            #if the head node of left is None, we're past the tail 
            #Add the node from right to merged linked list 
            
        if left_head is None:
            current.next_node = right_head 
                # Call next on right to set loop condition to False 
                
            right_head = right_head.next_node 
            #if the head node of right is None, we're past the tail 
            #Add the tail node from left to merged linked list 
            
        elif right_head is None:
            current.next_node = left_head 
                # Call next on left to set loop condition to False 
            left_head = left_head.next_node 
        else:
                # Not at either tail node 
                # Obtain node data to perform comparison operations
            left_data = left_head.data
            right_data = right_head.data  
                
            if left_data < right_data:
                current.next_node = left_head 
                    #Move left head to next node 
                left_head = left_head.next_node
                #if data on the left is grater than right, set current to right node 
            else:
                current.next_node = right_head 
                    #Move right head to next node 
                right_head = right_head.next_node 
        # Move current to next node
        current = current.next_node
#Discard fake head and set first ,erged node as head
    head = merged.head.next_node 
    merged.head = head

    return merged
l = LinkedList()
l.add(10)
l.add(2)
l.add(44)
l.add(15)
l.add(200)

print(l)
sorted_linked_list = merge_sort(l)
print(sorted_linked_list)
        
        
        
        