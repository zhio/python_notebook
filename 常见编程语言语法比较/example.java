int[] array = new int[5];

array[0] = 2;
array[1] = 3;
array[2] = 1;
array[3] = 0;
array[4] = 2;

int[] array = {2,3,1,0,2};

//初始化可变数组
List<Integer> array = new ArrayList<>();
//向尾部添加元素
array.add(2);
array.add(3);
array.add(1);
array.add(0);
array.add(2);

class ListNode {
    int val;
    ListNode next;
    listNode(int x) {val = x;}
}

ListNode n1 = new ListNode(4);
ListNode n2 = new ListNode(5);
ListNode n3 = new ListNode(1);

n1.next = n2;
n2.next = n3;