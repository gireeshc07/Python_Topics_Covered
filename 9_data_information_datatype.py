
# What is Data?

# Definition:
'''
-> Data is a collection of raw facts, numbers, symbols, or measurements that, by itself, doesn’t carry much meaning until it is processed or analyzed. 
-> It is unprocessed and unorganized. 
-> Data serves as the starting point for any kind of analysis, processing, or decision-making, providing the foundation for extracting information.
'''
# Key Characteristics of Data:
'''
-> It is unprocessed.
-> It may not have context.
-> It serves as input for generating insights.
'''
# Real-Life Example:
''' 
-> Imagine you’re running a café. You note down:  
   - 5 (number of coffees sold),  
   - 10:30 AM (time of sale),  
   - $15 (amount collected).  

These are individual pieces of raw data. Without context, they don’t tell you much.
'''
# What is Information?

# Definition:  
'''
-> Information is processed, organized, or interpreted data that is meaningful and useful for decision-making. 
-> It is the next step after data and provides context.
'''
# Key Characteristics of Information:
'''
-> It is processed and meaningful.
-> It provides insights and answers to specific questions.
-> It is actionable.
'''
# Real-Life Example:
'''
-> Continuing the café scenario, if you analyze the raw data:  
   - 5 coffees were sold at 10:30 AM for $15.

This analysis provides meaningful insights that can help you make business decisions, such as identifying peak sales times.
'''
# What is a Data Type?

# Definition:
'''
-> A data type classifies data based on its characteristics and specifies the kind of value a variable can hold, such as a number, text, or a collection of items. 
-> It determines how the data can be stored, processed, and manipulated in a program.
   - Storage: How much memory is allocated for the data.
   - Processing: What operations can be performed (e.g., arithmetic operations for numbers, string concatenation for text).
   - Manipulation: How the data can be changed or accessed (e.g., sorting a list, changing a string).
'''
# Key Characteristics of Data Types:
'''
-> They ensure data is handled correctly by programs.
-> They define the operations that can be performed on data.'''

# Types of Data and Examples:
'''
Integer    -->  Number of coffee cups sold in a day, e.g., 50.                         
String     -->  Coffee flavor name, e.g., "Espresso".                             
Float      -->  Revenue earned, e.g., 245.50 (decimal values).                   
Date/Time  -->  Timestamp of when an order was placed, e.g., 12-12-2024 10:15 AM. 
'''
# Real-Life Example of Data Types:
'''
-> Imagine you are filling out a form:

   Text/String         -->  Your Name: "Gireesh"
   Integer             -->  Your Age: 28 
   Float               -->  Your Height: 5.9 (decimal values)
   Boolean             -->  Do you have a driver's license?: Yes/No (True/False)
   File or Binary data -->  Your Photo: JPEG/PNG file
   Date/Time           -->  Timestamp of when the form was filled: 12-12-2024 10:15 AM.
'''
# Real-Life Analogy:
'''  
-> In the café example, you have:  
   1. 5 → This is a number (data type: integer).  
   2. 10:30 AM → This is text or a time string (data type: string).  
   3. $15 → This is a floating-point number because of the dollar value (data type: float). 
'''
# How They All Fit Together with Real-Life Scenarios:

# Scenario-1: Maintaining a sales record:  

# 1. Raw Data (Data):
'''
- Day: "Monday"  
- Coffees Sold: 50  
- Revenue: $150.25  

Here, 50, Monday, and $150.25 are data because they’re raw facts.  
'''
# 2. Information:
'''  
After processing the raw data, you determine:  
- "Monday is the busiest day, with an average sale of 50 coffees, generating $150.25 in revenue."  

This is information derived from the data.
'''
# 3. Data Types:
'''  
Each piece of data has a type that defines what it represents and how it can be used:  
- "Monday" → String: Represents text.  
- 50 → Integer: Represents a whole number.  
- $150.25 → Float: Represents a decimal number.
'''
# Examples in Python

# Storing Raw Data in Variables
day = "Monday"           # Data type: string
coffees_sold = 50        # Data type: integer
revenue = 150.25         # Data type: float

# Processing data into meaningful information
average_sale = revenue / coffees_sold
print(f"On {day}, the average revenue per coffee sold was ${average_sale:.2f}.")
# Output:  On Monday, the average revenue per coffee sold was $3.00.

# Scenario-2: Managing a Gym:

# 1. Raw Data (Data):
'''
   - Daily attendance numbers: 20, 25, 22, 30, 28.
   - Members' names: "John", "Sara", "Mike".
   - Weight measurements: 75.5, 62.3, 80.2.
'''
# 2. Data Types:
'''
   - 20, 25, 22: Integer (count of people).
   - "John", "Sara": String (names).
   - 75.5, 62.3: Float (weights).
'''

# 3. Information:
'''
   - "The average daily attendance at the gym is 25 people."
   - "Mike has lost 5 kg in the last month, indicating good progress."

Now you have actionable insights to make decisions, like planning gym capacity or tailoring fitness programs.
'''
# Examples in Python
# Storing Raw Data in Variables
attendance = [20, 25, 22, 30, 28]
members = ["John", "Sara", "Mike"]
weights = [75.5, 62.3, 80.2]

# Calculating average attendance
average_attendance = sum(attendance) / len(attendance)
print(f"The average daily attendance at the gym is {average_attendance} people.")
# Output: The average daily attendance at the gym is 25.0 people.

# Tracking weight loss for Mike
initial_weight = 85
mike_weight = weights[members.index("Mike")]
weight_loss = initial_weight - mike_weight
print(f"Mike has lost {weight_loss} kg in the last month, indicating good progress.")
# Output: Mike has lost 4.799999999999997 kg in the last month, indicating good progress.

# Key Points to Remember:
'''
-> Data is the foundation of everything. Without it, there’s no analysis or insights.  
-> Information is the value extracted from data, guiding decisions.  
-> Data Types ensure data is handled correctly in programming, enabling efficient processing.
'''
# Final Thought:
'''
-> Data is the raw material, information is the finished product, and data types are the tools that help us manage the raw material effectively in programming.
'''
