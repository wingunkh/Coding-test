def preorder(v): # 전위 순회 : 루트 -> 왼쪽 자식 -> 오른쪽 자식
    if v != '.':
        print(v, end = '')
        preorder(tree[v][0])
        preorder(tree[v][1])

def inorder(v): # 중위 순회 : 왼쪽 자식 -> 루트 -> 오른쪽 자식
    if v != '.':
        inorder(tree[v][0])
        print(v, end = '')
        inorder(tree[v][1])

def postorder(v): # 후위 순회 : 왼쪽 자식 -> 오른쪽 자식 -> 루트
    if v != '.':
        postorder(tree[v][0])
        postorder(tree[v][1])
        print(v, end = '')

n = int(input())
tree = {}
        
for i in range(n):
    root, left, right = input().split()
    tree[root] = [left, right]

preorder('A')
print()
inorder('A')
print()
postorder('A')
