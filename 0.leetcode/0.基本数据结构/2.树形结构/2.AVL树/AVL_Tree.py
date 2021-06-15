class Node():
    def __init__(self, val, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent
        self.balance = 0

    def isLeftChild(self):
        return True if self.parent and self.parent.left == self else False

    def isRightChild(self):
        return True if self.parent and self.parent.right == self else False

    def isRoot(self):
        return True if self.parent is None else False


class AVLTREE():
    def __init__(self):
        self.root = None
        self.size = 0

    def insert(self, val):
        """
        插入一个节点
        """

        def _insert(node, val):
            if val <= node.val:
                if node.left:
                    _insert(node.left, val)
                else:
                    node.left = Node(val, parent=node)
                    self._update_balance_insert(node.left)
            else:
                if node.right:
                    _insert(node.right, val)
                else:
                    node.right = Node(val, parent=node)
                    self._update_balance_insert(node.right)

        if not self.root:
            self.root = Node(val)
        else:
            _insert(self.root, val)
        self.size += 1

    def _update_balance_insert(self, root):
        """
        插入时候的更新balance
        """
        if root.balance > 1 or root.balance < -1:
            self._rebalance(root)
            return
        if root.parent is not None:
            if root.isLeftChild():
                root.parent.balance += 1
            else:
                root.parent.balance -= 1
            if root.parent.balance != 0:
                self._update_balance_insert(root.parent)

    def _rebalance(self, root):
        '''
        平衡重置函数
        '''
        # 1.LR / LL
        if root.balance > 1:
            if root.left.balance < 0:
                # LR 会多出这一步
                self._rotate_left(root.left)
            root = self._rotate_right(root)
        # 2.RR / RL
        elif root.balance < -1:
            if root.right.balance > 0:
                # RL会多出这一步
                self._rotate_right(root.right)
            root = self._rotate_left(root)
        return root

    def _rotate_left(self, root):
        """
        左旋
        """
        new_root = root.right
        # 1.处理new_root 双向指针
        if new_root.left:
            new_root.left.parent = root
        root.right = new_root.left

        # 2.解决new_root 的父双向指针
        if root.isRoot():
            self.root = new_root
        elif root.isLeftChild():
            root.parent.left = new_root
        else:
            root.parent.right = new_root
        new_root.parent = root.parent

        # 3.原root的双向指针
        root.parent = new_root
        new_root.left = root

        # 4.处理平衡因子问题
        root.balance = root.balance + 1 - min(0, new_root.balance)
        new_root.balance = new_root.balance + 1 + max(0, root.balance)

        return new_root

    def _rotate_right(self, root):
        """
        右旋
        """
        new_root = root.left
        # 1.处理new_root 双向指针
        if new_root.right:
            new_root.right.parent = root
        root.left = new_root.right

        # 2.解决new_root 的父双向指针
        if root.isRoot():
            self.root = new_root
        elif root.isLeftChild():
            root.parent.left = new_root
        else:
            root.parent.right = new_root
        new_root.parent = root.parent

        # 3.原root的双向指针
        root.parent = new_root
        new_root.right = root

        # 4.处理平衡因子问题
        root.balance = root.balance - 1 - max(0, new_root.balance)
        new_root.balance = new_root.balance - 1 + min(0, root.balance)

        return new_root

    def _get(self, val, node):
        if not node:
            return None
        elif val == node.val:
            return node
        elif val < node.val:
            return self._get(val, node.left)
        else:
            return self._get(val, node.right)

    def delete(self, val):
        """
        删除某节点
        """
        if self.size > 1:
            node2delete = self._get(val, self.root)
            if node2delete:
                self._delete(node2delete)
                self.size -= 1
            else:
                raise KeyError("Error,key not in tree")
        elif self.size == 1 and self.root.val == val:
            self.root = None
            self.size -= 1
        else:
            raise KeyError("Error,key not in tree")

    def _update_balance_delete(self, root):
        """
        删除节点后的平衡函数
        """
        if root:
            if root.balance > 1 or root.balance < -1:
                print('balance:{}'.format(root.val))

                root = self._rebalance(root)
                print('new_root: {}'.format(root.val))

            if root and root.balance == 0 and root.parent is not None:
                print("enter:{}".format(root.val))
                if root.isLeftChild():
                    root.parent.balance -= 1
                else:
                    root.parent.balance += 1
                if root.balance == 0:
                    self._update_balance_delete(root.parent)

    def _delete(self, node):
        """
        删除 辅助函数
        """

        def set_parent(node, child):
            if node.parent is not None:
                if node.isLeftChild():
                    node.parent.left = child
                    node.parent.balance -= 1
                else:
                    node.parent.right = child
                    node.parent.balance += 1
                return node.parent
            else:
                self.root = child
                return None

        # 选择左边，然后左子节点的右节点作为右子节点的左节点
        if node.left and node.right:
            sub_node = node.left
            while sub_node.right:
                sub_node = sub_node.right
            node.val = sub_node.val
            self._delete(sub_node)
            return
            # 选择左节点
        elif node.left:
            node.left.parent = node.parent
            parent = set_parent(node, node.left)
        # 选择右节点
        elif node.right:
            node.right.parent = node.parent
            parent = set_parent(node, node.right)
        # 无子节点，直接删除
        else:
            parent = set_parent(node, None)
        print("Parent to rebalance:{}".format(parent.val))
        if parent and parent.balance == 0 or (parent.balance > 1 or parent.balance < -1):
            self._update_balance_delete(parent)

    def show(self):
        if not self.root:
            return
        stack = [[self.root, 0]]
        level = []
        while stack:
            tempt = []
            for i in range(len(stack)):
                cur, id = stack.pop(0)
                tempt.append(('{}:{}'.format(cur.val, cur.balance), id))
                if cur.left:
                    stack.append([cur.left, id * 2])
                if cur.right:
                    stack.append([cur.right, id * 2 + 1])
            level.append(tempt)
        n = len(level)
        result = [['_____'] * (2 ** n - 1) for _ in range(n)]
        for i in range(n):
            for nodei in level[i]:
                indexi = int(2 ** (n - i) * (nodei[1] + 0.5) - 1)
                result[i][indexi] = str(nodei[0])
        result = [''.join(item) for item in result]
        for linei in result:
            print(linei)


if __name__ == '__main__':
    avl = AVLTREE()
    for ai in range(4100):
        avl.insert(ai)
    avl.show()

    print("***********")
    for i in range(10, 4096):
        avl.delete(i)
    avl.delete(4099)
    avl.show()
