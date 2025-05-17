from insertion_sort import insertion_sort_decreasing

def test_insertion_sort():
    # Test with a sample array
    arr = [5, 2, 4, 6, 1, 3]
    print(f"Original array: {arr}")
    sorted_arr = insertion_sort_decreasing(arr)
    print(f"Sorted array (decreasing): {sorted_arr}")
    
    # Verify the result
    expected = [6, 5, 4, 3, 2, 1]
    assert sorted_arr == expected, f"Expected {expected}, but got {sorted_arr}"
    print("Test passed!")

if __name__ == "__main__":
    test_insertion_sort()