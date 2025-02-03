from flask import Flask, jsonify, request
import math

app = Flask(__name__)

# Helper function to check if a number is prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# Helper function to check if a number is perfect
def is_perfect(n):
    if n < 2:
        return False
    divisors = [i for i in range(1, n) if n % i == 0]
    return sum(divisors) == n

# Helper function to check if a number is an Armstrong number
def is_armstrong(n):
    digits = [int(d) for d in str(abs(n))]  # Ignore negative sign for Armstrong check
    length = len(digits)
    return sum([d ** length for d in digits]) == abs(n)  # Use absolute value for Armstrong check

# Helper function to calculate the sum of digits
def sum_of_digits(n):
    return sum(int(d) for d in str(abs(n)))  # Ignore negative sign for sum of digits

# Helper function to get a fun fact (placeholder for now)
def get_fun_fact(n):
    return f"{n} is an interesting number!"

# API endpoint
@app.route('/api/classify-number', methods=['GET'])
def classify_number():
    number = request.args.get('number')

    # Check if the input is a valid number (integer or floating-point)
    try:
        number = float(number)  # Convert the string input to a float
    except (ValueError, TypeError):
        return jsonify({
            "number": number,
            "error": True,
            "message": "Invalid input. Please provide a valid number."
        }), 400

    # Determine properties (only for integers)
    properties = []
    if number == int(number):  # Check if the number is an integer
        number = int(number)  # Convert to integer for property checks
        if is_prime(number):
            properties.append("prime")
        if is_perfect(number):
            properties.append("perfect")
        if is_armstrong(number):
            properties.append("armstrong")
        if number % 2 == 0:
            properties.append("even")
        else:
            properties.append("odd")
    else:
        # If the number is floating-point, only include basic properties
        properties.append("floating-point")

    # Prepare response
    response = {
        "number": number,
        "is_prime": is_prime(number) if number == int(number) else False,
        "is_perfect": is_perfect(number) if number == int(number) else False,
        "properties": properties,
        "digit_sum": sum_of_digits(int(number)) if number == int(number) else None,
        "fun_fact": get_fun_fact(number)
    }

    return jsonify(response), 200

# Run the app
if __name__ == '__main__':
    app.run(debug=True)