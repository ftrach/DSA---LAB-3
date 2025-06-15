# LAB 3 ANALYSIS AND REFLECTION



## PART B ANALYSIS





### FUNCTION 1

# THIS FUNCTION CALCULATES VALUE RAISED TO A POWER USING RECURSION

```python
def recursive_product(value, count):
    if count == 0:
        return 1  # BASE CASE: ANYTHING TO THE POWER OF 0 IS 1
    elif count == 1:
        return value  # BASE CASE: POWER OF 1 RETURNS THE VALUE ITSELF
    else:
        return value * recursive_product(value, count - 1)  # RECURSIVE CALL DECREASES COUNT
```

**ANALYSIS**:  
Let T(n) represent the time complexity.  
- BASE CASES: O(1) when count == 0 or 1  
- RECURSIVE CASE: T(n) = T(n-1) + O(1)  
This is a linear recursive function.  
**TIME COMPLEXITY: O(n)**





---

### FUNCTION 2

# THIS FUNCTION CHECKS IF A GIVEN STRING IS A PALINDROME USING RECURSION

```python
def recur_check_palindrome(txt, left, right):
    if left >= right:
        return True  # BASE CASE: REACHED MIDDLE OF STRING
    else:
        if txt[left] != txt[right]:
            return False  # CHARACTERS DON'T MATCH, NOT A PALINDROME
        else:
            return recur_check_palindrome(txt, left + 1, right - 1)  # RECURSIVE CHECK ON NEXT CHARACTERS

def is_palindrome(txt):
    return recur_check_palindrome(txt, 0, len(txt) - 1)  # WRAPPER FUNCTION TO START FROM EDGES
```

**ANALYSIS**:  
Let T(n) represent the time complexity, where n is the length of the string.  
- EACH CALL COMPARES TWO CHARACTERS AND MAKES ONE RECURSIVE CALL  
This is a linear recursive function.  
**TIME COMPLEXITY: O(n)**

---





### FUNCTION 3 (OPTIONAL CHALLENGE)

# THIS FUNCTION EFFICIENTLY CALCULATES EXPONENTIATION USING RECURSION AND DIVIDE-AND-CONQUER

```python
def power_recursive(value, number):
    if number == 0:
        return 1  # BASE CASE: ANY VALUE TO THE POWER OF 0 IS 1
    elif number == 1:
        return value  # BASE CASE: POWER OF 1 RETURNS THE VALUE
    else:
        half = number // 2
        result = power_recursive(value, half)  # RECURSIVE CALL ON HALF THE EXPONENT
        if number % 2 == 0:
            return result * result  # EVEN POWER: SQUARE THE HALF RESULT
        else:
            return value * result * result  # ODD POWER: MULTIPLY EXTRA VALUE ONCE
```

**ANALYSIS**:  
Let T(n) represent the time complexity.  
- EACH CALL DIVIDES THE PROBLEM IN HALF AND DOES CONSTANT WORK  
T(n) = T(n/2) + O(1)  
**TIME COMPLEXITY: O(log n)**

---





## PART C REFLECTION





### HOW TO APPROACH WRITING RECURSIVE FUNCTIONS  



1.  IDENTIFY THE BASE CASE  :  This is the simplest scenario that can be solved directly without further recursion. 

2.  DEFINE THE RECURSIVE CASE  :  Determine how the problem can be broken down into smaller subproblems.  

3.  MAKE PROGRESS TOWARD THE BASE CASE  :  Ensure each recursive call gets closer to the base case  .  

4.  COMBINE RESULTS  :  If needed, combine the results of recursive calls to solve the overall problem  . 

5.  TEST THE FUNCTION  :  Try a variety of inputs to make sure it behaves correctly, especially edge cases.



### HOW RECURSIVE ANALYSIS DIFFERS FROM NON-RECURSIVE ANALYSIS  



- Recursive functions are analyzed using recurrence relations to represent time complexity growth.  
- Base case and recursive cases are analyzed completely separately to determine the overall complexity.  
- Recursive analysis often involves specific techniques like tree expansion or the Master Theorem  .  
- Non-recursive analysis usually involves things such as counting loop iterations  .



### SIMILARITIES  



- Both approaches measure performance based on input size.  
- Both assess best, worst, and average case complexity depending on the problem at hand  !
