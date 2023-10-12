
def count_points_in_circle(R, x, y):
        import math
        count = 0
        for i in range(x - R, x + R + 1):
            for j in range(y - R, y + R + 1):
                if math.sqrt((i - x)**2 + (j - y)**2) <= R:
                    count += 1
        return count
