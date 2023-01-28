initial_stock= int(input('Please enter an initial stock level:'))
month=input('Please enter months to plan:')
months=int(month)
monthly_sales={}
for i in range(months):
    i=i+1
    sales_quantity=input(f'Please enter the planned sales quantity for month {i}:')
    monthly_sales[i]=sales_quantity # Creating a dictionary called monthly_sales
print(monthly_sales)
i=0
quantity_produced=0
for forecast_sale in monthly_sales.values():
    i=i+1
    forecast=int(forecast_sale)
    if initial_stock>forecast:
       print(f'Quantity of production for {i} is 0')
       initial_stock=initial_stock-forecast #Getting new inital stock
    else:
        quantity_produced = forecast-initial_stock # Getting produced quantity
        print(f'quantity produced for month {i} is {quantity_produced}')
        initial_stock=quantity_produced+initial_stock-forecast #Getting new initial stock after a month
        