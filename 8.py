# -------
#method 1:-
# -------
lst=[]
n = int(input("Enter number of elements : "))
for i in range(0, n):
    ele = int(input())
    lst.append(ele) 
print(lst)
#without using loop
#lst.reverse
#print(lst)
#using loop
lst2=[]
for i in range(n-1,-1,-1):
    lst2.append(int(lst[i]))
print(lst2)
# ------------
#method2:-
# -----------
original_list = [1, 2, 3, 4, 5]
print("List before reverse : ",original_list)
reversed_list = []
for i in original_list:
  reversed_list =[i]+ reversed_list
print("List after reverse : ", reversed_list)
