import math

def polar_to_cartesian(r, theta):
    """Перетворення полярних координат у декартові."""
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    return x, y

def cartesian_to_polar(x, y):
    """Перетворення декартових координат у полярні."""
    r = math.sqrt(x**2 + y**2)
    theta = math.atan2(y, x)
    return r, theta

def spherical_to_cartesian(r, theta, phi):
    """Перетворення сферичних координат у декартові."""
    x = r * math.sin(phi) * math.cos(theta)
    y = r * math.sin(phi) * math.sin(theta)
    z = r * math.cos(phi)
    return x, y, z

def cartesian_to_spherical(x, y, z):
    """Перетворення декартових координат у сферичні."""
    r = math.sqrt(x**2 + y**2 + z**2)
    theta = math.atan2(y, x)
    phi = math.acos(z / r) if r != 0 else 0
    return r, theta, phi

def verify_2d_conversion(points_polar):
    """Перевірка перетворення між полярною та декартовою системами координат."""
    for r, theta in points_polar:
        x, y = polar_to_cartesian(r, theta)
        r_check, theta_check = cartesian_to_polar(x, y)
        print(f"Початкові полярні: ({r:.3f}, {theta:.3f}), "
              f"Після зворотного перетворення: ({r_check:.3f}, {theta_check:.3f})")

def verify_3d_conversion(points_spherical):
    """Перевірка перетворення між сферичною та декартовою системами координат."""
    for r, theta, phi in points_spherical:
        x, y, z = spherical_to_cartesian(r, theta, phi)
        r_check, theta_check, phi_check = cartesian_to_spherical(x, y, z)
        print(f"Початкові сферичні: ({r:.3f}, {theta:.3f}, {phi:.3f}), "
              f"Після зворотного перетворення: ({r_check:.3f}, {theta_check:.3f}, {phi_check:.3f})")

if __name__ == "__main__":
    # Приклади точок у полярній системі координат (r, theta)
    points_polar = [
        (1, math.pi / 4),
        (2, math.pi / 2),
        (3, math.pi),
    ]

    # Приклади точок у сферичній системі координат (r, theta, phi)
    points_spherical = [
        (1, math.pi / 4, math.pi / 6),
        (2, math.pi / 3, math.pi / 4),
        (3, math.pi / 2, math.pi / 3),
    ]

    print("2D Перетворення координат (Полярна ↔ Декартова):")
    verify_2d_conversion(points_polar)

    print("\n3D Перетворення координат (Сферична ↔ Декартова):")
    verify_3d_conversion(points_spherical)
