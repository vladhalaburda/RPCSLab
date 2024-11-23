import math

def cartesian_distance_2d(x1, y1, x2, y2):
    """Обчислення відстані у 2D декартовій системі."""
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def cartesian_distance_3d(x1, y1, z1, x2, y2, z2):
    """Обчислення відстані у 3D декартовій системі."""
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)

def polar_distance_2d(r1, theta1, r2, theta2):
    """Обчислення відстані між точками у полярній системі координат (2D)."""
    return math.sqrt(r1**2 + r2**2 - 2 * r1 * r2 * math.cos(theta2 - theta1))

def spherical_distance_3d_direct(r1, theta1, phi1, r2, theta2, phi2):
    """Пряма відстань у 3D сферичній системі координат."""
    x1 = r1 * math.sin(phi1) * math.cos(theta1)
    y1 = r1 * math.sin(phi1) * math.sin(theta1)
    z1 = r1 * math.cos(phi1)
    x2 = r2 * math.sin(phi2) * math.cos(theta2)
    y2 = r2 * math.sin(phi2) * math.sin(theta2)
    z2 = r2 * math.cos(phi2)
    return cartesian_distance_3d(x1, y1, z1, x2, y2, z2)

def spherical_distance_on_surface(r, theta1, phi1, theta2, phi2):
    """Велика колова відстань між точками по поверхні сфери."""
    central_angle = math.acos(
        math.sin(phi1) * math.sin(phi2) +
        math.cos(phi1) * math.cos(phi2) * math.cos(theta2 - theta1)
    )
    return r * central_angle

if __name__ == "__main__":
    # Точки для тестування
    point1_polar = (2, math.pi / 6)  # (r, theta) у 2D
    point2_polar = (3, math.pi / 3)  # (r, theta) у 2D

    point1_spherical = (4, math.pi / 4, math.pi / 6)  # (r, theta, phi) у 3D
    point2_spherical = (5, math.pi / 3, math.pi / 4)  # (r, theta, phi) у 3D

    print("Відстань у полярній системі (2D):")
    r1, theta1 = point1_polar
    r2, theta2 = point2_polar
    polar_dist = polar_distance_2d(r1, theta1, r2, theta2)
    print(f"Відстань між точками: {polar_dist:.3f}")

    print("\nВідстань у сферичній системі (3D):")
    r1, theta1, phi1 = point1_spherical
    r2, theta2, phi2 = point2_spherical

    # Пряма відстань
    direct_dist = spherical_distance_3d_direct(r1, theta1, phi1, r2, theta2, phi2)
    print(f"Пряма відстань: {direct_dist:.3f}")

    # Велика колова відстань
    surface_dist = spherical_distance_on_surface(r1, theta1, phi1, theta2, phi2)
    print(f"Велика колова відстань: {surface_dist:.3f}")
