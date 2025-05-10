# DBS-ex2
In this assignment, we design and query a SQL database for the fictional O’donald’s Burgers fast food chain. The task involves three parts: constructing and populating the database with tables and sample data, performing business analysis using advanced SQL queries, and modifying the database schema to support cost evaluation of meals. Each query is implemented in a separate Python script with embedded SQL and proper documentation.

## Questions 1,2:
Creating the database and tables inside of it. This is a screenshot of the tables it created, since no output is returned indicating success (only upon failure).
![image](https://github.com/user-attachments/assets/0f505c4e-a603-470a-b24a-cc91534e3c4f)
### Notes:
- Defining a FK the way we leared didn't work, so I used ``` FOREIGN KEY (meal_id) REFERENCES menu_meal(meal_id)``` at the end of each query.
- In q1, I stuck to the first format but used removed the line ```database="burgers"``` because upon creating the DB we don't have a name for it yet because it does not exist.

# Question 3:
Inserting rows into all 9 tables.
![image](https://github.com/user-attachments/assets/fa443653-2fb8-4df6-922b-37440bda8f8b)

