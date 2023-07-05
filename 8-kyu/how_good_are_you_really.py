def better_than_average(class_points, your_points):
    # Your code here
    sum = 0; tot = len(class_points)
    for i in class_points: sum += i
    avg = sum/tot
    if your_points > avg :
        return True
    return False

# class_point = [2, 3]
# your_point = 5
# print(better_than_average(class_point, your_point))


def test_better_than_average():
    # Test case 1: Your points are better than the average
    class_points = [2, 3]
    your_points = 5
    assert better_than_average(class_points, your_points) == True

    # Test case 2: Your points are equal to the average
    class_points = [100, 40, 34, 57, 29, 72, 57, 88]
    your_points = 75
    assert better_than_average(class_points, your_points) == True

    # Test case 3: Your points are worse than the average
    class_points = [41, 75, 72, 56, 80, 82, 81, 33]
    your_points = 50
    assert better_than_average(class_points, your_points) == False

test_better_than_average()