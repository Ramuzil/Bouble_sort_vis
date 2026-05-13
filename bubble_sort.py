import random
import time

def bubble_sort(arr):
    """Bubble sort implementation"""
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def main():
    # Create array with 10,000 random values
    print("Generating 10,000 random values...")
    arr = [random.randint(1, 100000) for _ in range(10000)]
    
    # Create a copy for verification
    arr_copy = arr.copy()
    
    print(f"First 10 elements before sort: {arr[:10]}")
    
    # Sort and time it
    print("\nSorting with bubble sort...")
    start_time = time.time()
    sorted_arr = bubble_sort(arr)
    end_time = time.time()
    
    print(f"Sort completed in {end_time - start_time:.4f} seconds")
    print(f"First 10 elements after sort: {sorted_arr[:10]}")
    print(f"Last 10 elements after sort: {sorted_arr[-10:]}")
    
    # Verify correctness
    print("\nVerifying sort correctness...")
    
    # Test 1: Check if sorted
    is_sorted = all(sorted_arr[i] <= sorted_arr[i + 1] for i in range(len(sorted_arr) - 1))
    print(f"✓ Array is sorted: {is_sorted}")
    
    # Test 2: Check length unchanged
    length_match = len(sorted_arr) == len(arr_copy)
    print(f"✓ Length preserved: {length_match} ({len(sorted_arr)} elements)")
    
    # Test 3: Check same elements (using sorted comparison)
    same_elements = sorted(sorted_arr) == sorted(arr_copy)
    print(f"✓ All elements preserved: {same_elements}")
    
    # Test 4: Compare with Python's built-in sort
    python_sorted = sorted(arr_copy)
    matches_builtin = sorted_arr == python_sorted
    print(f"✓ Matches Python's sort: {matches_builtin}")
    
    if is_sorted and length_match and same_elements and matches_builtin:
        print("\n✅ All tests passed! Bubble sort works correctly.")
    else:
        print("\n❌ Some tests failed!")

if __name__ == "__main__":
    main()
