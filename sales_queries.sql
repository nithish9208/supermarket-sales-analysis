-- Top 10 selling product categories
SELECT product_line, SUM(total) AS revenue
FROM supermarket_sales
GROUP BY product_line
ORDER BY revenue DESC
LIMIT 10;

-- Monthly sales trend per branch
SELECT branch, strftime('%Y-%m', date) AS month, SUM(total) AS revenue
FROM supermarket_sales
GROUP BY branch, month
ORDER BY month;

-- Average customer spending by gender
SELECT gender, AVG(total) AS avg_spending
FROM supermarket_sales
GROUP BY gender;

-- Gross income contribution per branch
SELECT branch, SUM(gross_income) AS total_income
FROM supermarket_sales
GROUP BY branch;
