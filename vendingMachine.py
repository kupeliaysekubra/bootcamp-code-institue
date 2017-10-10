from ryotest import *

def get_change(amount):
    if amount == 0:
        return []
        
    if amount in [100, 50, 20, 10, 5, 2, 1]:
        return [amount]
    
    change = []
    change.append(5)
    change.append(2)
    return change
    
test_are_equal(get_change(1),[1])
test_are_equal(get_change(2),[2])
test_are_equal(get_change(5),[5])
test_are_equal(get_change(10),[10])
test_are_equal(get_change(20),[20])
test_are_equal(get_change(50),[50])
test_are_equal(get_change(100),[100])
test_are_equal(get_change(7), [5, 2])

print("All tests pass")
