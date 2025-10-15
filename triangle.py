import math

def check_triangle(a, b, c):
    """
    Checks if three lengths form a valid triangle and determines its type.
    
    Args:
        a (float): Length of side a
        b (float): Length of side b.
        c (float): Length of side c.

    Returns:
        tuple: (side_type, angle_type)
    """
    
    # --- 1. VALIDITY CHECK (Triangle Inequality Theorem) ---
    if a + b <= c or a + c <= b or b + c <= a:
        return "Invalid", "N/A"

    # --- 2. SIDE TYPE CHECK ---
    side_type = ""
    if a == b and b == c:
        side_type = "Equilateral"
    elif a == b or b == c or a == c:
        side_type = "Isosceles"
    else:
        side_type = "Scalene"

    # --- 3. ANGLE TYPE CHECK (Pythagorean Theorem Extension) ---
    # Find the squares of the sides
    sides_squared = sorted([a**2, b**2, c**2])
    x, y, z = sides_squared[0], sides_squared[1], sides_squared[2] # x^2 + y^2 vs z^2

    angle_type = ""

    TOLERANCE = 1e-9 
    
    if abs(x + y - z) < TOLERANCE:
        # If a^2 + b^2 == c^2 (approx)
        angle_type = "Right"
    elif x + y < z:
        # If a^2 + b^2 < c^2
        angle_type = "Obtuse"
    else: # x + y > z
        # If a^2 + b^2 > c^2
        angle_type = "Acute"
        
    return side_type, angle_type

def main():
    
    try:
        print("Enter the lengths of the three sides of the triangle:")
        a = float(input("Side A: "))
        b = float(input("Side B: "))
        c = float(input("Side C: "))
        
        
        if a <= 0 or b <= 0 or c <= 0:
            print("Error: All side lengths must be positive.")
            return

        side_type, angle_type = check_triangle(a, b, c)

        if side_type == "Invalid":
            print("\nResult: The given side lengths CANNOT form a triangle.")
        else:
            print("\n--- Triangle Analysis ---")
            print(f"Side Classification: {side_type}")
            print(f"Angle Classification: {angle_type}")
            print("-------------------------")

    except ValueError:
        print("Invalid input. Please enter valid numbers for the side lengths.")

if __name__ == "__main__":
    main()
