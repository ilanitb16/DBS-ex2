# DBS-ex2
In this assignment, we design and query a SQL database for the fictional O’donald’s Burgers fast food chain. The task involves three parts: constructing and populating the database with tables and sample data, performing business analysis using advanced SQL queries, and modifying the database schema to support cost evaluation of meals. Each query is implemented in a separate Python script with embedded SQL and proper documentation.

# Part 1: Database Construction
## Questions 1,2:
Creating the database and tables inside of it. This is a screenshot of the tables it created, since no output is returned indicating success (only upon failure).
![image](https://github.com/user-attachments/assets/0f505c4e-a603-470a-b24a-cc91534e3c4f)
### Notes:
- Defining a FK the way we leared didn't work, so I used ``` FOREIGN KEY (meal_id) REFERENCES menu_meal(meal_id)``` at the end of each query.
- In q1, I stuck to the first format but used removed the line ```database="burgers"``` because upon creating the DB we don't have a name for it yet because it does not exist.

## Question 3:
Inserting rows into all 9 tables.
![image](https://github.com/user-attachments/assets/fa443653-2fb8-4df6-922b-37440bda8f8b)

# Part 2: - Advanced Data Analysis

## Question 4: Business Analysis- Meal Type By City
Your first analysis task is to create a report on how the popularity of the different meal types
(breakfast-morning, regular- all day) is distributed across the cities.
Write a query that will return a table of cities, and for each city- total of
1. breakfasts
2. regular meals
The cities should appear in an alphabetical order.

- Result: ```('MIA', Decimal('1'), Decimal('4')), ('NYC', Decimal('1'), Decimal('2')), ('SF', Decimal('4'), Decimal('1'))```  

## Question 5: : Business Analysis- Popular Meals

### Question 5_1:
- Result: ```('Omfast', 4), ('small Oburger Meal', 3), ('large Oburger Meal', 2), ('small Onuggets meal', 1), ('large Onuggets meal', 1), ('Opanfast', 1), ('Owaffast', 1), ('chicken Oburger meal', 0)```

### Question 5_2:
- Result: ``````

### Uestion 5_3:
- Result: ```('chicken Oburger meal',), ('small Onuggets meal',)```
  
## Question 6:
Alter the menu_meal table such that it will include an integer raw_cost column, which will store the accumulative cost of all items in the meal. Screenshot of the update:
![image](https://github.com/user-attachments/assets/f772b277-8ed4-4def-ac02-5eaaac67ba95)


