import sys
input = sys.stdin.readline

def Preorder(answer, node):
    answer.append(node)
    left, right = tree[node]
    
    if left != '.':
        Preorder(answer, left)
    if right != '.':
        Preorder(answer, right)
    return
    
def Inorder(answer, node):
    left, right = tree[node]
    
    if left != '.':
        Inorder(answer, left)
    answer.append(node)
    if right != '.':
        Inorder(answer, right)
    return

    
def Postorder(answer, node):
    left, right = tree[node]
    
    if left != '.':
        Postorder(answer, left)
    if right != '.':
        Postorder(answer, right)
    answer.append(node)
    return
    
n = int(input())
tree = {}

preorder_answer = []
inorder_answer = []
postorder_answer = []

for _ in range(n):
    node, left, right = input().split()
    tree[node] = (left, right)
    
Preorder(preorder_answer, 'A')
Inorder(inorder_answer, 'A')
Postorder(postorder_answer, 'A')

print(''.join(preorder_answer))
print(''.join(inorder_answer))
print(''.join(postorder_answer))