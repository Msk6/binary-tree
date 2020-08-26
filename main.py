class Node:
    def __init__(self, name):
        self.name = name
        self.right = None
        self.left = None

    def get_name(self):
        return self.name

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right
    
    def set_name(self, name):
        self.name = name

    def set_left(self, left):
        self.left = left
    
    def set_right(self, right):
        self.right = right

class BinaryTree:
    def __init__(self):
        self.root = None
    
    def get_root(self):
        return self.root

    def set_root(self, root):
        self.root = root

    def add_child(self, name):
        current_node = self.get_root()
        while len(name):
            current_name = name.pop()
            # To check empty Tree
            if current_node:
                if current_node.get_name() == current_name:
                    # Check existing of next name
                    if current_node.get_right():
                        if current_node.get_right().get_name() == name[len(name)-1]:
                            # Go to right
                            current_node = current_node.get_right()
                        elif  current_node.get_left():
                            if current_node.get_left().get_name() == name[len(name)-1]:
                                # Go to left
                                current_node = current_node.get_left()

                elif current_node.get_right() == None:
                    # Add to right 
                    child = Node(current_name)
                    current_node.set_right(child)
                    print (f" Added {current_name} to {current_node.get_name()} to the right")
                    current_node = current_node.get_right()
                    #print (f" Added {current_name} to {current_node.get_name()}")


                elif current_node.get_left() == None:
                    # Add to left 
                    child = Node(current_name)
                    current_node.set_left(child)
                    print (f" Added {current_name} to {current_node.get_name()} to the left")
                    current_node = current_node.get_left()

                else:
                    print (f" There is no {current_name} and can not add more childs") 
                    return
            
            else:
                father = Node(current_name)
                self.set_root(father)
                current_node = self.get_root()

    def traverse(self, node):
        current_node = node
        #print(current_node.get_name())
        if current_node.get_right():
            print(current_node.get_name())
            self.traverse(current_node.get_right())
            if current_node.get_left():
                print(current_node.get_name())
                self.traverse(current_node.get_left())
        else:
            return
        return


    
                
    
family_tree = BinaryTree()
full_name = input("Enter your full name (Enter done to exit): ") 
while full_name != "done":
    full_name = full_name.split()
    family_tree.add_child(full_name)
    full_name = input("Enter your full name (Enter done to exit): ") 

family_tree.traverse(family_tree.get_root())


'''    def travarse(self, name):
        node = self.get_root()
        if node.get_right():
            while node.get_right():
                if node.get_right():
                    if node.get_right().get_name() == name:
                        node = node.get_right()
                        if node.get_right() == None:
                            child = Node(name)
                            node.get_right().get_left
                        elif node.get_left() == None:


                    elif node.get_left().get_name() == name:
                        node = node.get_left()
                    else:
                        return "Sorry the sequential not correct"
                    #else:
                    #    child = Node(name)
                    #    node.get_right().set_right(child)
                    
                elif node.get_left():
                    if node.get_left().get_name() == name:
                        node = node.get_left()
                    else: 
                        child = Node(name)
                        node.set_left(child)

            
            return "There is no father"
        
        else:
            child = Node(name)
            node.set_right(child)'''


'''    def travarse(self, name):
        current_node = self.get_root()
        #parent_node= self.get_root()
        #if node.get_right():
        while len(name):
            current_name = name.pop()
            #if current_node.get_right():
            if current_node.get_name() == current_name:
            #if node.get_right() != None
                if current_node.get_right().get_name() == name[len(name)-1]:
                    node = node.get_right()
                else:
                    node = node.get_left()
                    #else:
                    #    child = Node(current_name)
                    #    current_node.set_right(child)
                        
            elif current_node.get_right() == None:
                child = Node(current_name)
                current_node.set_right(child)

            elif current_node.get_left() == None:
                child = Node(current_name)
                current_node.set_left(child)

            else:
                print (f" {current_name} is exceesed")'''
                    
                    

                        #else:
                        #    child = Node(name)
                        #    node.set_right(child)
                        #if node.get_right() == None:
                        #    child = Node(name)
                        #    node.get_right().get_left
                        #elif node.get_left() == None:


                    #elif node.get_left().get_name() == name:
                    #    node = node.get_left()
                    #else:
                    #    return "Sorry the sequential not correct"
                    #else:
                    #    child = Node(name)
                    #    node.get_right().set_right(child)
                    
                #elif node.get_left():
                #    if node.get_left().get_name() == name:
                #        node = node.get_left()
                #    else: 
                #        child = Node(name)
                #        node.set_left(child)

            
            
        
                #else:
                #    child = Node(name)
                #    node.set_right(child)

                #return "There is no father"

                #def add_child(self, name):
    #    if self.root:
    #        pass 
    #        # Travarse then add child
    #    else:
    #        self.set_root(Node(name))
            
                


            
        




    