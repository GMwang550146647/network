class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Tree():

    def build_tree_from_list(self,tree_list,current_index=0):
        if len(tree_list)==0:
            return None
        if current_index>=len(tree_list):
            return None
        #防止该节点是None的时候
        if tree_list[current_index] is None:
            return None
        root=TreeNode(tree_list[current_index])
        root.left=self.build_tree_from_list(tree_list,current_index=current_index*2+1)
        root.right=self.build_tree_from_list(tree_list,current_index=current_index*2+2)
        return root

    def mid_recur_tree(self,root,depth=0):
        if root is None:
            return None
        self.mid_recur_tree(root.left,depth+1)
        print('\t'*depth+str(root.val))
        self.mid_recur_tree(root.right,depth+1)
