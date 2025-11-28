class Tree:
  def __init__(self, root = None):
    self.root = root

  def get_element_by_id(self, id):
    # Depth-first traversal using a stack
    if self.root is None:
      return None
    
    stack = [self.root]
    
    while stack:
      node = stack.pop()
      
      if node.get('id') == id:
        return node
      
      # Add children to stack in reverse order to maintain left-to-right traversal
      if 'children' in node and node['children']:
        for child in reversed(node['children']):
          stack.append(child)
    
    return None
