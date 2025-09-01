SELECT 
  ROUND(
    SUM(CASE WHEN customer_pref_delivery_date = first_order_date THEN 1 ELSE 0 END) * 100.0
    / COUNT(DISTINCT customer_id), 2
  ) AS immediate_percentage
FROM (
    SELECT 
      customer_id,
      MIN(order_date) AS first_order_date,
      MIN(customer_pref_delivery_date) AS customer_pref_delivery_date
    FROM delivery
    GROUP BY customer_id
) t;
