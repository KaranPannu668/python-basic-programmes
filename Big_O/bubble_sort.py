def bubble_sort(data: list) -> None:
    """Sorts a list in place."""
    n = len(data)
    comparison_count = 1

    for i in range(n-1):
        for j in range(n-1-i):
            comparison_count += 1
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
        
        print(f"End of pass {i}. `data` is now {data}")
    print(f"comparison_count is {comparison_count}")


numbers = [3,4,6,5,23,2,5,7]
bubble_sort(numbers)
print(f"Sorted list: {numbers}")