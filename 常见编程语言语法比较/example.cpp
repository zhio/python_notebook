//数组

int array[5];

array[0] = 2;
array[1] = 3;
array[2] = 1;
array[3] = 0;
array[4] = 2;

int array[] = {2,3,1,0,2};

//初始化可变数组

vector<int> array;

array.push_back(2);
array.push_back(3);
array.push_back(1);
array.push_back(0);
array.push_back(2);

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};