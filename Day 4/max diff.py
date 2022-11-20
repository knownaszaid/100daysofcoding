"""Problem
Chef prepared two dishes yesterday. Chef had assigned the tastiness T1 and T2 to the first and to the second dish respectively. The tastiness of the dishes can be any integer between 0 and N (both inclusive).
Unfortunately, Chef has forgotten the values of T1 and T2 that he had assigned to the dishes. However, he remembers the sum of the tastiness of both the dishes - denoted by SS.

Chef wonders, what can be the maximum possible absolute difference between the tastiness of the two dishes. Can you help the Chef in finding the maximum absolute difference?

Input Format
The first line of input contains a single integer T, denoting the number of test cases. The description of the T testcases follows.
The first and only line of each test case contains two space-separated integers N, S, denoting the maximum tastiness and the sum of tastiness of the two dishes, respectively.
Output Format
For each testcase, output a single line containing the maximum absolute difference between the tastiness of the two dishes.

 
Input:
3
3 1
4 4
2 3
Output :
1
4
1
Explanation:
Test Case 1: The possible pairs of {T1,T2} are {0,1}and{1,0}.Difference in both the cases is 1, hence the maximum possible absolute difference is 1.
Test Case 2: The possible pairs of {T1,T2} are {0,4},{1,3},{2, 2},{3, 1}and {4,0}. The maximum possible absolute difference is 4.
Test Case 3: The possible pairs of {T1,T2} are {1,2}and{2,1}.Difference in both the cases is 1, hence the maximum possible absolute difference is 1.

"""






for i in range(int(input())):
    n,s=map(int,input().split())
    if(s<=n):
        print(s)
    elif((2*n-s)>0):
        print(2*n-s)
    else:
        print(s-2*n)
