#Data 
revenue = [14574.49, 7606.46, 8611.41, 9175.41, 8058.65, 8105.44, 11496.28, 9766.09, 10305.32, 14379.96, 10713.97, 15433.50]
expenses = [12051.82, 5695.07, 12319.20, 12089.72, 8658.57, 840.20, 3285.73, 5821.12, 6976.93, 16618.61, 10054.37, 3803.96]

#Calculating Profits (revenue - expenses)
profit = list([])    #Make a variable called profit which is an empty list. 

for i in range(0, len(revenue)):   #Do work while in the range of the length of the list.
    profit.append(revenue[i] - expenses[i])  #.append function adds whatever the result into the list
    
print(profit)

#Calculate Tax As 30% Of Profit And Round To 2 Decimal Points (profit x 30%)
tax = [round(i * 0.3, 2) for i in profit] 
print(tax)

#Calculate Profit Remaining After Tax Is Deducted
profit_after_tax = list([])  #Again, creating an empty list

for i in range(0, len(profit)):
    profit_after_tax.append(profit[i] - tax[i])
print(profit_after_tax)
    
#Calculate The Profit Margin As Profit After Tax Over Revenue
#Round To 2 Decimal Points, Then Multiply By 100 To Get %
profit_margin = list([])

for i in range(0, len(profit_after_tax)):
    profit_margin.append(profit_after_tax[i] / revenue[i])
    
profit_margin = [round((i*100), 2) for i in profit_margin]
print(profit_margin)

#Calculate The Mean Profit After Tax For The 12 Months
#Profit after tax mean
mean_pat = sum(profit_after_tax) / len(profit_after_tax)
print(mean_pat)

#Find The Months With Above-Mean Profit After Tax
#Finding a good month
good_month = list([])
for i in range(0, len(profit)):
    good_month.append(profit_after_tax[i] > mean_pat)
print(good_month)

#Bad Months Are The Opposite Of Good Months!
bad_month = list([])
for i in range(0, len(profit)):
    bad_month.append(profit_after_tax[i] < mean_pat)
print(bad_month)

#The Best Month Is Where Profit After Tax Was Equal To The Maximum
best_month = list([])
for i in range(0, len(profit)):
    best_month.append(profit_after_tax[i] == max(profit_after_tax))
print(best_month)

#The Worst Month Is Where Profit After Tax Was Equal To The Minimum
worst_month = list([])
for i in range(0, len(profit)):
    worst_month.append(profit_after_tax[i] == min(profit_after_tax))
print(worst_month)

#Convert All Calculations To Units Of One Thousand Dollars
revenue_1000 = [round(i/1000, 2) for i in revenue]
expenses_1000 = [round(i/1000, 2) for i in expenses]
profit_1000 = [round(i/1000, 2) for i in profit]
profit_after_tax_1000 = [round(i/1000, 2) for i in profit_after_tax]

revenue_1000 = [int(i) for i in revenue_1000]
expenses_1000 = [int(i) for i in expenses_1000]
profit_1000 = [int(i) for i in profit_1000]
profit_after_tax_1000 = [int(i) for i in profit_after_tax_1000]

### Print Results ###
print ("Revenue :") 
print (revenue_1000)
print ("Expenses :") 
print (expenses_1000)
print ("Profit :")
print(profit_1000)
print ("Profit after tax :")
print (profit_after_tax_1000)
print ("Profit margin :")
print (profit_margin)
print ("Good months :")
print (good_month)
print ("Bad months :")
print (bad_month)
print ("Best month :")
print (best_month)
print ("Worst month :")
print (worst_month)
