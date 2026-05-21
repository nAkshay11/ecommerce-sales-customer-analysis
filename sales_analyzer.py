import pandas as pd

# Load dataset
data = pd.read_csv('ecommerce_sales_data.csv')

# Create total sales column
data['total_sales'] = data['quantity'] * data['price']

# Total revenue
total_revenue = data['total_sales'].sum()

# Average sales
average_sales = data['total_sales'].mean()

# Top selling products
top_products = data.groupby('product')['total_sales'].sum().sort_values(ascending=False)

# City-wise sales
city_sales = data.groupby('city')['total_sales'].sum()

# Payment method analysis
payment_analysis = data['payment_method'].value_counts()

# Print outputs
print("Total Revenue:", total_revenue)
print("Average Sales:", average_sales)

print("\nTop Products:")
print(top_products)

print("\nCity Wise Sales:")
print(city_sales)

print("\nPayment Method Analysis:")
print(payment_analysis)

# Save processed data
data.to_csv('processed_sales_data.csv', index=False)

print("\nProcessed file saved successfully.")