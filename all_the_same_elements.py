'''
In this mission you should check if all elements in the given list are equal.
Input: List.
Output: Bool.
The idea for this mission was found on Python Tricks series by Dan Bader
Precondition: all elements of the input list are hashable
'''

from typing import List, Any


def all_the_same(elements: List[Any]) -> bool:
    # your code here
    same=True
    if len(elements)>1:
        for e in range(len(elements)-1):
            if elements[e]!=elements[e+1]:
                return False   
                break
    elif len(elements)==1 or len(elements)==0: 
        return True
    return same

all_the_same([10000,99999])    

if __name__ == '__main__':
    print("Example:")
    print(all_the_same([1, 1, 1]))
    
    # These "asserts" are used for self-checking and not for an auto-testing
    assert all_the_same([1, 1, 1]) == True
    assert all_the_same([1, 2, 1]) == False
    assert all_the_same(['a', 'a', 'a']) == True
    assert all_the_same([]) == True
    assert all_the_same([1]) == True
    print("Coding complete? Click 'Check' to earn cool rewards!")
    
