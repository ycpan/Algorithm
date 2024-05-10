# 二叉树最长宽度
## 解题
```python
class Node():
    def __init__(self,):
        self.left = None
        self.right = None
    def 


def get_longest_layer(node):
    res_tmp = []
    res = []
    tmp = 0
    count = 0
    node_1 = []
    node_2 = []
    node_1.append(node)
    while(node_1 or node_2):
        res_tmp = []
        for n in node_1:
            if n:
                res_tmp.append(n.value())
                tmp += 1
                if n.left != None:
                    node_2.append(n.left)
                if n.right !=None:
                    node_2.append(n.right)
        node_1 = []
        if tmp >= count:
            res = res_tmp
            count = tmp
        res_tmp = []
        for n in node_2:
            if n:
                res_tmp.append(n.value())
                tmp += 1
                if n.left != None:
                    node_1.append(n.left)
                if n.right !=None:
                    node_1.append(n.right)

        node_2 = []
        if tmp >= count:
            res = res_tmp
            count = tmp
    return res,count
```


