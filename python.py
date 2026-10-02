import math

# =====================================================================
# MATHEMATICAL CALCULATIONS IN PYTHON
# =====================================================================
# This script performs various mathematical calculations in English,
# including basic arithmetic, algebra, geometry, and descriptive statistics.
# Detailed inline comments are provided for every step.
# =====================================================================

# ---------------------------------------------------------------------
# SECTION 1: BASIC ARITHMETIC OPERATIONS
# ---------------------------------------------------------------------

# Define initial numbers for basic operations
number_a = 25
number_b = 4

# Perform addition: combines two values together
sum_result = number_a + number_b

# Perform subtraction: calculates the difference between two values
difference = number_a - number_b

# Perform multiplication: calculates the product of two values
product = number_a * number_b

# Perform standard division: yields a floating-point (decimal) result
quotient = number_a / number_b

# Perform floor division: divides and rounds down to the nearest integer
integer_quotient = number_a // number_b

# Perform modulo operation: calculates the remainder left after division
remainder = number_a % number_b

# Print results of basic arithmetic operations
print("=== 1. Basic Arithmetic Operations ===")
print(f"Addition ({number_a} + {number_b}): {sum_result}")
print(f"Subtraction ({number_a} - {number_b}): {difference}")
print(f"Multiplication ({number_a} * {number_b}): {product}")
print(f"Division ({number_a} / {number_b}): {quotient}")
print(f"Floor Division ({number_a} // {number_b}): {integer_quotient}")
print(f"Remainder/Modulo ({number_a} % {number_b}): {remainder}")
print()


# ---------------------------------------------------------------------
# SECTION 2: ADVANCED MATH & ALGEBRA
# ---------------------------------------------------------------------

# Exponentiation: calculates number_a raised to the power of number_b (25^4)
power_result = number_a ** number_b

# Square Root: calculates the non-negative square root using math.sqrt()
square_root_a = math.sqrt(number_a)

# Natural Logarithm: calculates log base e of a number
log_natural = math.log(number_a)

# Common Logarithm: calculates log base 10 of a number
log_base10 = math.log10(number_a)

# Print results of advanced algebraic operations
print("=== 2. Advanced Math Operations ===")
print(f"Exponentiation ({number_a} ^ {number_b}): {power_result}")
print(f"Square Root of {number_a}: {square_root_a}")
print(f"Natural Logarithm of {number_a}: {log_natural:.4f}")
print(f"Base-10 Logarithm of {number_a}: {log_base10:.4f}")
print()


# ---------------------------------------------------------------------
# SECTION 3: GEOMETRY CALCULATIONS
# ---------------------------------------------------------------------

# Define radius for circle calculations
radius = 7.0

# Calculate Circle Area using formula: Area = pi * r^2
circle_area = math.pi * (radius ** 2)

# Calculate Circle Circumference using formula: Circumference = 2 * pi * r
circle_circumference = 2 * math.pi * radius

# Define dimensions for a right-angled triangle
base = 10.0
height = 5.0

# Calculate Triangle Area using formula: Area = 0.5 * base * height
triangle_area = 0.5 * base * height

# Calculate Hypotenuse using the Pythagorean theorem: c = sqrt(a^2 + b^2)
hypotenuse = math.hypot(base, height)

# Print results of geometric calculations
print("=== 3. Geometry Calculations ===")
print(f"Circle Radius: {radius}")
print(f"Circle Area: {circle_area:.2f}")
print(f"Circle Circumference: {circle_circumference:.2f}")
print(f"Triangle Base: {base}, Height: {height}")
print(f"Triangle Area: {triangle_area:.2f}")
print(f"Triangle Hypotenuse: {hypotenuse:.2f}")
print()


# ---------------------------------------------------------------------
# SECTION 4: DESCRIPTIVE STATISTICS
# ---------------------------------------------------------------------

# Define a list of numerical sample scores
dataset = [85, 90, 78, 92, 88, 76, 95]

# Calculate total sum of all items in the dataset
data_sum = sum(dataset)

# Count total number of elements in the list
data_count = len(dataset)

# Calculate Mean (Average): Total Sum divided by Total Count
mean = data_sum / data_count

# Calculate Variance: Average of the squared differences from the Mean
variance = sum((x - mean) ** 2 for x in dataset) / data_count

# Calculate Standard Deviation: Square root of Variance
std_deviation = math.sqrt(variance)

# Print results of statistical calculations
print("=== 4. Statistical Calculations ===")
print(f"Dataset: {dataset}")
print(f"Total Sum: {data_sum}")
print(f"Total Count: {data_count}")
print(f"Mean (Average): {mean:.2f}")
print(f"Variance: {variance:.2f}")
print(f"Standard Deviation: {std_deviation:.2f}")