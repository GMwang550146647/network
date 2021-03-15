from fundamentals.tree import TreeNode, Tree


class BSTTree():
    @staticmethod
    def isValidBST(root):
        """
        98.mid_验证二叉搜索树.py
        判断是否合法二叉树（中序遍历，必须是递增序列！）
        """

        def mid_recur(root):
            nonlocal recorder
            if root:
                if not mid_recur(root.left):
                    return False
                if recorder is not None and root.val <= recorder:
                    return False
                else:
                    recorder = root.val
                if not mid_recur(root.right):
                    return False
                return True
            else:
                return True

        recorder = None
        return mid_recur(root)

    @staticmethod
    def isSameTree(p, q):
        """
        100.easy_相同的树.py
        判断两个树是否完全一样
        """

        def recur(p, q):
            if p is None and q is None:
                return True
            if p is None or q is None:
                return False
            if p.val == q.val:
                return recur(p.left, q.left) and recur(p.right, q.right)
            else:
                return False

        return recur(p, q)

    @staticmethod
    def searchBST(root, val):
        """
        700.easy_二叉搜索树中的搜索.py
        在二叉树中搜索某个值 ，若不存在返回None
        """

        def search(root, val):
            if root:
                if val == root.val:
                    return root
                elif val > root.val:
                    return search(root.right, val)
                else:
                    return search(root.left, val)
            else:
                return None

        return search(root, val)

    @staticmethod
    def insertIntoBST(root, val):
        """
        701.mid_二叉搜索树中的插入操作.py
        根节点处插入值
        """

        def insert(root, val):
            if not root:
                return TreeNode(val)
            if root.val == val:
                return root
            if val < root.val:
                root.left = insert(root.left, val)
            else:
                root.right = insert(root.right, val)
            return root

        return insert(root, val)

    @staticmethod
    def deleteNode(root, key):
        """
        450.mid_删除二叉搜索树中的节点.py
        删除某个节点
        """
        def get_min_node(root):
            while root.left:
                root = root.left
            return root

        def delete(root, key):
            # 0.函数目的是返回该root 删除key 后的根节点
            if root is None:
                return None
            # 1.大的往右走
            if key > root.val:
                root.right = delete(root.right, key)
            # 2.小的往左走
            elif key < root.val:
                root.left = delete(root.left, key)
            # 3.相等的时候就要删除了
            else:
                # 3.1.若只有单边节点的，直接顶替上来
                if root.right is None:
                    return root.left
                elif root.left is None:
                    return root.right

                # 3.2.若有双边节点，返回右节点的最小节点（或者左节点的最大节点)
                else:
                    root.val = get_min_node(root.right).val
                    root.right = delete(root.right, root.val)
            return root

        return delete(root, key)
