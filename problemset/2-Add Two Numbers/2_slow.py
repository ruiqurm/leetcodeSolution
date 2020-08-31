class ListNode:
    '''
    链表
    '''
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
import array

def to_array(ln:ListNode)->array.array:
    
    l = []
    while(ln.next!=None):
        l.append(ln.val)
        ln = ln.next
    l.append(ln.val)
    l.append(0)
    arr = array.array('i',l)
    return arr
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1 = to_array(l1)
        l2 = to_array(l2)
        len1,len2 = len(l1),len(l2)
        if len1 < len2:
            l1,l2 = l2,l1
        for index,value in enumerate(l2):
            tmp,l1[index] = divmod(value + l1[index],10)
            if(index!=len(l1)-1):
                l1[index+1] += tmp
        l = now=last = ListNode(val=0)
        for index,value in enumerate(l1[:-1]):
            if (l1[index]>=10):
                now.val = l1[index]-10
                l1[index+1]+=1
            else:
                now.val = l1[index]
            now.next = ListNode(val=0)
            last = now
            now = now.next
        if(l1[index+1]!=0):
            now.val = l1[index+1]
        else:
            last.next = None
        return l
            
            
#l = ListNode(val=9,next=ListNode(val=9))
ll = ListNode(val=1)
l =  ListNode(val=9,next =ListNode(val=9,next = ListNode(val=9,next=ListNode(val=9,next=ListNode(val=9,next=None)))))
#ll = ListNode(val=5,next=ListNode(val=6,next=ListNode(val=4,next=None)))
d = Solution().addTwoNumbers(l,ll)