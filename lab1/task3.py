import math
import random
import time

# Функції обчислення відстаней
def cartesian_distance_2d(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def cartesian_distance_3d(x1, y1, z1, x2, y2, z2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)

def polar_distance_2d(r1, theta1, r2, theta2):
    return math.sqrt(r1**2 + r2**2 - 2 * r1 * r2 * math.cos(theta2 - theta1))

def spherical_distance_on_surface(r, theta1, phi1, theta2, phi2):
    central_angle = math.acos(
        math.sin(phi1) * math.sin(phi2) +
        math.cos(phi1) * math.cos(phi2) * math.cos(theta2 - theta1)
    )
    return r * central_angle

# Генерація масивів координат
def generate_cartesian_points_2d(size):
    return [(random.uniform(-1000, 1000), random.uniform(-1000, 1000)) for _ in range(size)]

def generate_cartesian_points_3d(size):
    return [(random.uniform(-1000, 1000), random.uniform(-1000, 1000), random.uniform(-1000, 1000)) for _ in range(size)]

def generate_polar_points(size):
    return [(random.uniform(0, 1000), random.uniform(0, 2 * math.pi)) for _ in range(size)]

def generate_spherical_points(size):
    return [(random.uniform(0, 1000), random.uniform(0, 2 * math.pi), random.uniform(0, math.pi)) for _ in range(size)]

# Бенчмарки
def benchmark_cartesian_2d(points):
    start_time = time.time()
    for i in range(len(points) - 1):
        cartesian_distance_2d(*points[i], *points[i + 1])
    return time.time() - start_time

def benchmark_cartesian_3d(points):
    start_time = time.time()
    for i in range(len(points) - 1):
        cartesian_distance_3d(*points[i], *points[i + 1])
    return time.time() - start_time

def benchmark_polar(points):
    start_time = time.time()
    for i in range(len(points) - 1):
        polar_distance_2d(*points[i], *points[i + 1])
    return time.time() - start_time

def benchmark_spherical(points):
    start_time = time.time()
    for i in range(len(points) - 1):
        spherical_distance_on_surface(points[i][0], *points[i][1:], *points[i + 1][1:])
    return time.time() - start_time

if __name__ == "__main__":
    size = 50000  # Розмір масиву (рекомендується 10,000–100,000)
    print(f"Генерація масивів з {size} точок...")

    # Генерація точок
    cartesian_points_2d = generate_cartesian_points_2d(size)
    cartesian_points_3d = generate_cartesian_points_3d(size)
    polar_points = generate_polar_points(size)
    spherical_points = generate_spherical_points(size)

    print("Запуск бенчмарків...")

    # Виконання бенчмарків
    time_cartesian_2d = benchmark_cartesian_2d(cartesian_points_2d)
    time_cartesian_3d = benchmark_cartesian_3d(cartesian_points_3d)
    time_polar = benchmark_polar(polar_points)
    time_spherical = benchmark_spherical(spherical_points)

    # Виведення результатів
    print(f"2D Декартова система: {time_cartesian_2d:.3f} секунд")
    print(f"3D Декартова система: {time_cartesian_3d:.3f} секунд")
    print(f"2D Полярна система: {time_polar:.3f} секунд")
    print(f"3D Сферична система (велика колова відстань): {time_spherical:.3f} секунд")
