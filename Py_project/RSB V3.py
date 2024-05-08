"""
Restraunt billing system, created by Ruhan Saad Dave and Rushil Vishwakarma.
This python program helps to create order,view order, edit order, edit menu and see total profit.
All the code used in this program belong to their rightful owner which is us, and we own all of them, the usage of these are only for educational and entertainment purpose 😉
The program is little long,but it covers all the useful functions needed in a restaurant billing system.
"""

#If you found an error or bug, please report it
#value of all items
category=["Pizza","Burger","Fries","Pasta","Garlic Bread","Juice","Icecream","Bevarages"]
items=[["Simple_cheese_pizza","Mix_veg_pizza","Chicken_pizza","Paneer_pizza","Speacial_pizza"],["Veg_cutlet_burger","Chicken_burger","Egg_burger","Paneer Burger","Fish burger","Special Burger"],["Plain Salted fries","Cheesy fries","Mix sauce fries","Pizza Flavoured fries","Speacial fries"],["Classic Pasta","Cheese Pasta","Mix sauce pasta","Chicken pasta","Paneer pasta","Speacial pasta"],["Simple garlic bread","Cheesy garlic bread","Mix sauce Garlic-Bread","Speacial garlic-Bread"],["Apple juice","Mango juice","Banana juice","Strawberry juice","Orange juice","Watermelon juice","Pineapple juice"],["Vanilla icecream","Butter scotch icecream","Chocolate icecream","Dry fruit icecream","Strawberry icecream","Dark chocolate icecream","Coconut icecream"],["Water (small Bottle; Fazleri 1l)","Water (Large Bottle; Fazleri 2l)","Coffee","Tea","FazbearCola"]]
price=[[50,10,150,150,200],[50,100,50,100,100,150,150],[30,50,50,70,70],[50,60,60,80,80,100],[30,40,40,50],[20,20,20,30,30,40,40],[20,30,50,50,30,60,70],[10,20,30,30,20]]
#single bill details
bill_item=[]
bill_quantity=[]
bill_price=[]
bill_total=[]
bill_sum=0
bill_discount=0
bill_gst=0
bill_final=0
#all bill items
order_item_list=[]
order_quantity_list=[]
order_price_list=[]
order_total_list=[]
order_sum_list=[]
order_gst_list=[]
order_discount_list=[]
order_final_list=[]
#total earning (in admin option)
gst_percent=5
discount=0
cash=0
card=0
online_payment=0
gst=0
total_discount=0
total_income=0
total_bill=0
password="123456"
#Full name of the customer
name = input("Enter your full name: ")
print("\n"*3)
#Actual program starts now
print("*" * 30)
print("\tWelcome to")
print("Freddy Fazbear's Restaurant!")
print("PLACE YOUR ORDER HERE")
print("*" * 30)
print("\n" * 3)
print("*How to use - To proceed further, type the number listed before the product/category name and press Enter.")
print("*Tip - To avoid errors, make sure you Only use Alphabets or Numbers given in choice.")
print("\n"*3)
#taking main function
program=1
while program==1:#to see if user want to stop the program
	print("-*-"*8)
	print("Hi",name,"..How may I help you?")
	print("1 → Place order")#line 70
	print("2 → View Placed order")#202
	print("3 → Edit order / Export Bill (in text format)")#line 217
	print("4 → Admin")#line695
	print("5 → Exit")#line1123
	main_choice=input("Choose option: ")
	if main_choice.isdigit()==False:
		print("ERROR!")
		print("Please enter a number!")
		exit=input("Press ENTER to continue")#this to make sure the user reads the message to prevent confusion
		print("\n"*3)
	else:
		main_choice=int(main_choice)		
		if main_choice==1:  #creating new order
			create_new=1
			bill_item=[]
			bill_price=[]
			bill_quantity=[]		
			bill_total=[]
			bill_sum=0
			bill_gst=bill_sum * gst_percent*0.01
			bill_discount=(bill_sum+bill_gst)*discount*0.01
			bill_final=bill_sum+bill_gst-bill_discount
			while create_new==1:#to see if user want to stop adding items or not
				print("-*-"*8)
				print("Please select category : )") #print all categories
				for sino in range(0,len(category)):
					print(sino+1,"→",category[sino])
				print("other option_ Exit")
				category_choice=input("Choose option: ")
				if category_choice.isdigit()==False:
					print("ERROR!")
					print("Please enter a number!")
					exit=input("Press ENTER to continue")#this is to make sure the user reads this message to prevent confusion
					print("\n")
				else:
					category_choice=int(category_choice)
					category_choice-=1
					if category_choice not in range(0,len(category)): #checking for exit option
						print("-*-"*8)
						print("Are you sure you want to exit?")
						print("All changes won't be saved!")
						print("y→yes")
						print("n→no")
						print("other option→no")
						confirm=input("Please select:-")
						if confirm=="y":
							print("You chose to stop creating order and exit")
							create_new=0
							exit=input("Press ENTER to continue")#this to make sure the user reads the message to prevent confusion
						else:
							print("Exiting order canceled")
							exit=input("Press ENTER to continue")#this to make sure the user reads the message to prevent confusion
					else:
						print("-*-"*8)
						print("Please select item :)") #print all item of selected category
						for sino1 in range(0,len(items[category_choice])):
							print(sino1+1,"→",items[category_choice][sino1])
						print("Other number_Exit to main menu")
						item_choice=input("Enter your choice : ")
						if item_choice.isdigit()==False:
							print("ERROR!")
							print("Please enter a number!")
							exit=input("Press ENTER to continue")#this to make sure the user reads the message to prevent confusion
							print("\n")
						else:
							item_choice=int(item_choice)
							item_choice-=1
							if item_choice not in range(0,len(items[category_choice])):
								print("-*-"*8)
								print("Are you sure you want to exit?")
								print("All changes won't be saved!")
								print("y→yes")
								print("n→no")
								print("other option→no")
								confirm=input("Please select:-")
								if confirm=="y":
									print("You chose to stop creating order and exit")
									exit=input("Press ENTER to continue")#this to make sure the user reads the message to prevent confusion
									create_new=0
								else:
									print("Exiting order canceled!")
									exit=input("Press ENTER to continue")#this to make sure the user reads the message to prevent confusion
							else:
								if items[category_choice][item_choice] in bill_item:
									print("This item is already existing in your order!")
									print("If you want to change quantity you can go to edit_order at MAIN MENU!")
									exit=input("Press ENTER to continue")#This is done so user can read this message instead of getting confused
									print("\n"*3)
								else:
									bill_item.append(items[category_choice][item_choice])
									bill_price.append(price[category_choice][item_choice])
									print("-*-"*8)
									print("How much",items[category_choice][item_choice],"do you want? (just enter a number of box you want; Standard single box is Half Kg)")
									print("*For fries, Garlic Bread- It is medium size pack Quantity")
									temp_quant=input("Enter quantity: ") #temp_quant is temporary storage of value of quantity
									if temp_quant.isdigit()==False:
										print("ERROR!")
										print("Please enter a number!")
										exit=input("Press ENTER to continue")#this to make sure the user reads the message to prevent confusion
										print("\n")
										bill_item.pop()
										bill_price.pop()
									else:
										temp_quant=int(temp_quant)
										bill_quantity.append(temp_quant)
										temp_total=temp_quant * price[category_choice][item_choice]
										bill_total.append(temp_total)
										bill_sum+=temp_total
										bill_gst=bill_sum * gst_percent * 0.01
										bill_discount=(bill_sum+bill_gst)*discount*0.01
										bill_final=bill_sum+bill_gst-bill_discount
										print("-*-"*8)
										print("Bill items is \n",bill_item)
										print("Quantity of items is \n",bill_quantity)
										exit=input("Press ENTER to continue")#this to make sure the user reads the messageto prevent confusion
										print("-*-"*8)
										print("Item added")
										print("Add more items?")
										print("y → yes ")
										print("n → no ")
										print("other option → no")
										add_more_item=input("Enter your choice: ")
										if add_more_item== "y":
											create_new=1
										else:
											create_new=0
											order_item_list.append(bill_item)
											order_price_list.append(bill_price)
											order_quantity_list.append(bill_quantity)
											order_total_list.append(bill_total)
											order_sum_list.append(bill_sum)
											order_gst_list.append(bill_gst)
											order_discount_list.append(bill_discount)
											order_final_list.append(bill_final)
											bill_item=[]
											bill_price=[]
											bill_quantity=[]		
											bill_total=[]
											bill_sum=0
											bill_gst=bill_sum * gst_percent*0.01
											bill_discount=(bill_sum+bill_gst)*discount*0.01
											bill_final=bill_sum+bill_gst-bill_discount	
											print("Order Placed successfully!")
											exit=input("Press ENTER to continue")#this to make sure the user reads the messageto prevent confusion
		elif main_choice==2:
			print("-*-"*8)
			print("order list are as follows")
			for sino2 in range(0,len(order_item_list)): # print number of orders
				print("Order_",sino2+1) #print all items of each order
				print("|      Item                 |      Quantity      |       price       |        Total      |")	
				for sino3 in range(0,len(order_item_list[sino2])):
					print(sino3+1,"→",order_item_list[sino2][sino3],"___",order_quantity_list[sino2][sino3],"___",order_price_list[sino2][sino3],"___",order_total_list[sino2][sino3])
				print("Total = ₹",order_sum_list[sino2])
				print("Tax = ₹",order_gst_list[sino2])
				print("Discount = ₹",order_discount_list[sino2])
				print("Total with GST = ₹",order_final_list[sino2])
				print("-*-"*8)
				print("\n" * 2)
			exit=input("Press 'ENTER' to return to main menu") # for easy exiting main choice 2				
		elif main_choice==3:
			edit_new=1
			while edit_new==1:
				print("\n" * 2)
				print("-*-"*8)
				print("Select the order you want to edit/Export Bill of - ")
				for order_no in range (0,len(order_item_list)): #print all order with total
					print(order_no+1,"→order",order_no+1)
					print("Total=",order_final_list[order_no])
					print("Total items=",len(order_item_list[order_no]))
				print("other option→ Exit to main menu")
				edit_order=input("Which order do you want to edit? Please select: ")
				if edit_order.isdigit()==False:
					print("ERROR!")
					print("Please enter a number!")
					exit=input("Press ENTER to continue")#this to make sure the user reads the message to prevent confusion
					print("\n")
				else:
					edit_order=int(edit_order)
					print("-*-"*8)
					edit_order-=1
					if edit_order not in range (0,len(order_item_list)): #checking for exit option
						print("Are you sure you want to exit to main menu?")
						print("y_yes")
						print("n_no")
						print("other option_no")
						confirm=input("Enter your choice:-")
						if confirm=="y":
							edit_new=0
						else:
							print("You chose not to exit to main menu")
							exit=input("Press ENTER to continue")#this to make sure the user reads the message to prevent confusion
					else: #printing all items in order to edit
						print("Order no : #",edit_order)
						print("-*-"*8)
						print("|     Item                 |      Quantity      |       price       |        Total      |")
						for sino4 in range(0,len(order_item_list[edit_order])): 
							print(sino4+1,"→",order_item_list[edit_order][sino4],"___",order_quantity_list[edit_order][sino4],"___",order_price_list[edit_order][sino4],"___",order_total_list[edit_order][sino4])
						print("Total = ₹",order_sum_list[edit_order])
						print("Tax = ₹",order_gst_list[edit_order])
						print("Discount = ₹")
						print("Total (GST Included) = ₹",order_final_list[edit_order])
						print("-*-"*8)
						print("\nWhat would you like to do?") #asking for edit function
						print("1 → Add more item")#line275
						print("2 → Delete item")#line 381
						print("3 → Edit item")#line 441
						print("4 → Delete order")#line 503
						print("5 → Export bill")#line527
						print("other option → Exit")
						edit_choice=input("Select item")
						if edit_choice.isdigit()==False:
							print("ERROR!")
							print("Please enter a number!")		
							exit=input("Press ENTER to continue")#this to make sure the user reads the message to prevent confusion
							print("\n"*3)
						else:
							edit_choice=int(edit_choice)				
							if edit_choice==1: #add new items on existing order
								temp_quant=0				
								temp_total=0
								bill_sum=0
								bill_gst=0
								bill_discount=0
								bill_final=0
								edit_new_add=1
								while edit_new_add==1:
									print("-*-"*8)
									print("Please select a category :)") #print all category
									for sino in range(0,len(category)):
										print(sino+1,"→",category[sino])
									print("other option → Exit")
									category_choice=input("Select item -")
									if category_choice.isdigit()==False:
										print("ERROR!")
										print("Please enter a number!")
										exit=input("Press ENTER to continue")#this to make sure the user reads the message to prevent confusion
										print("\n"*3)
									else:
										category_choice=int(category_choice)
										category_choice-=1
										if category_choice not in range(0,len(category)): #checking for exit option
											print("Are you sure you want to exit?")
											print("y_yes")
											print("n_no")
											print("other option_no")
											confirm=input("Enter your choice:-")
											if confirm=="y":
												print("You chose to exit adding new item ")
												exit=input("Press ENTER to continue")#this to make sure the user reads the message to prevent confusion
												edit_new_add=0
											else:
												print("You chose not to exit adding new item")
										else:
											print("-*-"*8)
											print("Please select an item :)") #print all item of selected category
											for sino1 in range(0,len(items[category_choice])):
												print(sino1+1,"→",items[category_choice][sino1])
											print("other option→ Exit to main menu")
											item_choice=input("Choose option:")
											if item_choice.isdigit()==False:
												print("ERROR!")
												print("Please enter a number!")
												exit=input("Press ENTER to continue")#this to make sure the user reads the message to prevent confusion
											else:
												item_choice=int(item_choice)
												item_choice-=1
												if item_choice not in range(0,len(items[category_choice])):
													print("Are you sure you want to exit?")
													print("y_yes")
													print("n_no")
													print("other option_no")
													confirm=input("Enter your choice:-")
													if confirm=="y":
														print("You chose to exit adding item to order")
														exit=input("Press ENTER to continue")#this to make sure the user reads the message to prevent confusion
														edit_new_add=0
													else:
														print("You chose not to exit")
														edit_new_add=1
												else:
													if items[category_choice][item_choice] in order_item_list[edit_order]:
														print("This item already exists in your order!")
														exit=input("Press ENTER to continue")#this to make sure the user reads the message to prevent confusion
													else:
														order_item_list[edit_order].append(items[category_choice][item_choice])
														order_price_list[edit_order].append(price[category_choice][item_choice])
														print("-*-"*8)
														print("How much ",items[category_choice][item_choice],"do you want?")
														temp_quant=input("Enter the quantity? : ")
														if temp_quant.isdigit()==False:
															print("ERROR!")
															print("Please enter a number!")
															order_item_list[edit_order].pop()
															order_price_list[edit_order].pop()
															exit=input("Press ENTER to continue")#this to make sure the user reads the message to prevent confusion
															print("\n"*3)
														else:
															temp_quant=int(temp_quant)
															order_quantity_list[edit_order].append(temp_quant)
															temp_total=temp_quant * price[category_choice][item_choice]
															order_total_list[edit_order].append(temp_total)
															bill_sum=order_sum_list[edit_order]
															bill_sum+=temp_total
															bill_gst=bill_sum * gst_percent*0.01
															bill_discount=(bill_sum+bill_gst)*discount*0.01
															bill_final=bill_sum+bill_gst-bill_discount
															order_sum_list[edit_order]=bill_sum
															order_gst_list[edit_order]=bill_gst
															order_discount_list[edit_order]=bill_discount
															order_final_list[edit_order]=bill_final
															print("-*-"*8)
															print("Bill items is \n ",order_item_list[edit_order])
															print("Quantity of items is \n ",order_quantity_list[edit_order])
															exit=input("Press ENTER to continue")#this to make sure the user reads the message to prevent confusion
															print("-*-"*8)		
															print("Add more?")
															print("y → yes ")
															print("n → no ")
															exit_choice=input("Select item") #checking if user wants something else too
															if exit_choice =="y":
																edit_new_add=1
															else:
																edit_new_add=0
							elif edit_choice==2:
								#delete item function
								print("Are you sure you want to delete item from order?")
								print("y_yes")
								print("n_no")
								print("other option_no")
								confirm=input("Enter your choice:-")#This is done to prevent user from accidentally deleting item
								if confirm=="y":
									edit_delete=1
									while edit_delete==1:
										print("-*-"*8)
										for sino1 in range(0,len(order_item_list[edit_order])):
											print(sino1+1,"→",order_item_list[edit_order][sino1])
										print("Other option_exit")
										print("Which item to delete?")
										delete_choice=input("Select item to delete: ")
										if delete_choice.isdigit()==False:
											print("ERROR!")
											print("Please enter a number!")
											exit=input("Press ENTER to continue")#this to make sure the user reads the message to prevent confusion
											print("\n")
										else:
											delete_choice=int(delete_choice)
											delete_choice-=1
											if delete_choice not in range(0,len(order_item_list[edit_order])):
												print("Are you sure you want to exit delete item?")
												print("y_yes")
												print("n_no")
												print("other option_no")
												confirm=input("Enter your choice:-")
												if confirm=="y":
													print("You chose to exit delete item")
													edit_delete=0
													print("\n")
												else:
													print("You chose not to exit delete item")
													edit_delete=1
											else:
												bill_sum=order_sum_list[edit_order]
												bill_sum-=order_total_list[edit_order][delete_choice]
												bill_gst=bill_sum * gst_percent *0.01
												bill_discount=(bill_sum+bill_gst)*discount*0.01
												bill_final=bill_sum+bill_gst-bill_discount
												order_sum_list[edit_order]=bill_sum
												order_gst_list[edit_order]=bill_gst
												order_discount_list[edit_order]=bill_discount
												order_final_list[edit_order]=bill_final
												order_item_list[edit_order].pop(delete_choice)
												order_price_list[edit_order].pop(delete_choice)
												order_quantity_list[edit_order].pop(delete_choice)
												order_total_list[edit_order].pop(delete_choice)
												print("Item Deleted Successfully")#delete function complete
												print("-*-"*8)
												print("Bill items is \n ",order_item_list[edit_order])
												print("Quantity of items is \n ",order_quantity_list[edit_order])
												exit=input("Press ENTER to continue")#this to make sure the user reads the message to prevent confusion
												edit_delete=0
									else:
										print("You chose not to delete item from order!")
										print("\n")
							elif edit_choice==3:
								#edit order starts,only changes quantity of item in the order
								quantity_edit=1#this is for looping the edit quantity function till user is satisfied
								while quantity_edit==1:
									print("-*-"*8)
									for sino1 in range(0,len(order_item_list[edit_order])):
										print(sino1+1,"→",order_item_list[edit_order][sino1])
									print("other option_exit")
									print("Which item quantity to edit?")		
									edit_quantity=input("Enter your choice:- ")
									if edit_quantity.isdigit()==False:
										print("ERROR!")
										print("Please enter a number!")
										exit=input("Press ENTER to continue")#this to make sure the user reads the message to prevent confusion
										print("\n")
									else:
										edit_quantity=int(edit_quantity)
										edit_quantity-=1
										if edit_quantity not in range(0,len(order_item_list[edit_order])):
											print("Are you sure you want to exit edit quantity?")
											print("y_yes")
											print("n_no")
											print("other option_no")
											confirm=input("Enter your choice:-")
											if confirm=="y":
												print("You chose to exit edit quantity")
												quantity_edit=0
												print("\n")
											else:
												print("You chose not to exit edit quantity")
										else:
											print("Original quantity of ",order_item_list[edit_order][edit_quantity],"=",order_quantity_list[edit_order][edit_quantity])
											new_quantity=input("Enter new quantity:- ")
											if new_quantity.isdigit()==False:
												print("ERROR!")
												print("Please enter a number!")
												exit=input("Press ENTER to continue")#this to make sure the user reads the message to prevent confusion
												print("\n"*3)
											else:
												new_quantity=int(new_quantity)
												bill_sum=order_sum_list[edit_order]
												bill_sum-=order_total_list[edit_order][edit_quantity]#deletes the old total to add the new total
												order_quantity_list[edit_order][edit_quantity]=new_quantity
												order_total_list[edit_order][edit_quantity]=order_price_list[edit_order][edit_quantity] * order_quantity_list[edit_order][edit_quantity]
												print("New quantity=",order_quantity_list[edit_order][edit_quantity])
												bill_sum+=order_total_list[edit_order][edit_quantity]
												bill_gst=bill_sum * gst_percent*0.01
												bill_discount=(bill_sum+bill_gst)*discount*0.01
												bill_final=bill_sum+bill_gst
												order_sum_list[edit_order]=bill_sum
												order_gst_list[edit_order]=bill_gst
												order_discount_list[edit_order]=bill_discount
												order_final_list[edit_order]=bill_final
												bill_sum=0
												bill_gst=0
												bill_discount=0
												bill_final=0
												print("Edited Quantity successfully!")
												print("-*-"*8)
												print("Bill items is \n ",order_item_list[edit_order])
												print("Quantity of items is \n ",order_quantity_list[edit_order])
												exit=input("Press ENTER to continue")#this to make sure the user reads the message to prevent confusion					
							elif edit_choice==4:
								#check if user want to delete the whole order
								print("-*-"*8)
								for sino1 in range(0,len(order_item_list[edit_order])):
									print(sino1+1,"→",order_item_list[edit_order][sino1])
								print("Are your sure you want to delete this order?")
								print("y → yes")
								print("n → no")
								print("other option_no")
								delete_order=input("Select: ")
								if delete_order=="y":
									order_item_list.pop(edit_order)
									order_price_list.pop(edit_order)
									order_quantity_list.pop(edit_order)
									order_total_list.pop(edit_order)
									order_sum_list.pop(edit_order)
									order_gst_list.pop(edit_order)
									order_discount_list.pop(edit_order)
									order_final_list.pop(edit_order)
									print("Order Deleted successfully")
									exit=input("Press ENTER to continue")#this to make sure the user reads the message to prevent confusion
								else:
									print("Order deletion canceled!")
									exit=input("Press ENTER to continue")#this to make sure the user reads the message to prevent confusion
							elif edit_choice==5:
								#converting the order into bill to add income in final income available in admin function in main menu
								print("-*-"*8)
								print("Order total = ₹",order_final_list[edit_order])
								print("Please select payment method:)")
								print("1 → Cash")#line544
								print("2 → Card")#line596
								print("3 → Online payment")#line637
								print("other number → Exit")
								pay_choice=input("Select: ")
								if pay_choice.isdigit()==False:
									print("ERROR!")
									print("Please enter a number!")
									exit=input("Press ENTER to continue")#this to make sure the user reads the message to prevent confusion
									print("\n"*3)
								else:
									pay_choice=int(pay_choice)
									if pay_choice==1:
										print("Total Bill = ₹",order_final_list[edit_order])
										total_money=order_final_list[edit_order]
										cash_pay=input("Enter customer given cash amount:- ")
										if cash_pay.isdigit()==False:
											print("ERROR!")
											print("Please enter a number!")
											exit=input("Press ENTER to continue")#this to make sure the user reads the message to prevent confusion
											print("\n"*3)
										else:
											cash_pay=int(cash_pay)
											change=cash_pay-total_money
											print("Change = ₹",change)
											cash+=total_money
											total_income+=total_money
											total_bill+=1
											gst+=order_gst_list[edit_order]
											total_discount+=order_discount_list[edit_order]
											#following code is for printing bill,
											print("Exporting your bill. Hold on!")
											print("\n" * 3)
											print("*" * 30)
											print("Freddy fazbear's Resaurant")
											print("Name:",name)
											print("--INVOICE--")
											print("*" * 30)
											for sino4 in range(0,len(order_item_list[edit_order])):
												print(sino4+1,"→",order_item_list[edit_order][sino4],"\t",order_quantity_list[edit_order][sino4],"\t",order_price_list[edit_order][sino4],"\t",order_total_list[edit_order][sino4])
											print("Total = ₹",order_sum_list[edit_order])
											print("Tax  = ₹",order_gst_list[edit_order])
											print("Discount = ₹",order_discount_list[edit_order])
											print("Total with gst=",order_final_list[edit_order])
											print("*" * 30)
											print("Cash taken = ₹",cash_pay)
											print("Change = ₹",change)
											print("*" * 30)
											print("Thank you for chosing freddy fazbear's Restaurant!")
											print("See you soon!")#bill printing complete
											#following is to remove the record of the order as the money is taken
											print("\n"*5)
											print("Bill exported successfully!")
											exit=input("Press ENTER to continue")#this to make sure the user reads the message to prevent confusion
											print("\n"*3)
											order_item_list.pop(edit_order)
											order_price_list.pop(edit_order)
											order_quantity_list.pop(edit_order)
											order_total_list.pop(edit_order)
											order_sum_list.pop(edit_order)
											order_gst_list.pop(edit_order)
											order_discount_list.pop(edit_order)
											order_final_list.pop(edit_order)
											edit_new=0
									elif pay_choice==2:
										print("Order total = ₹",order_final_list[edit_order])
										total_money=order_final_list[edit_order]
										total_bill+=1
										card+=total_money
										total_income+=total_money
										gst+=order_gst_list[edit_order]
										total_discount+=order_discount_list[edit_order]
										#following code is for printing bill
										print("Exporting Bill.. Hold on!")
										print("\n" * 3)
										print("*" * 30)
										print("Freddy fazbear's Restaurant")
										print("Name:",name)
										print("--INVOICE--")
										print("*" * 30)
										for sino4 in range(0,len(order_item_list[edit_order])):
											print(sino4+1,"→",order_item_list[edit_order][sino4],"\t",order_quantity_list[edit_order][sino4],"\t",order_price_list[edit_order][sino4],"\t",order_total_list[edit_order][sino4])
										print("Total = ",order_sum_list[edit_order])
										print("Tax = ₹",order_gst_list[edit_order])
										print("Discount = ₹",order_discount_list[edit_order])
										print("Total + GST = ",order_final_list[edit_order])
										print("*" * 30)
										print("Card payment = ₹",total_money)
										print("*" * 30)
										print("Thank you for chosing Freddy fazbear's Restaurant!")
										print("See you soon again!")#bill printing completed
										#this is to remove the record of the order as it turned into bill
										print("\n"*5)
										print("Bill exported successfully!")
										exit=input("Press ENTER to continue")#this to make sure the user reads the message to prevent confusion
										print("\n"*3)
										order_item_list.pop(edit_order)
										order_price_list.pop(edit_order)
										order_quantity_list.pop(edit_order)
										order_total_list.pop(edit_order)
										order_sum_list.pop(edit_order)
										order_gst_list.pop(edit_order)
										order_discount_list.pop(edit_order)
										order_final_list.pop(edit_order)
										edit_new=0
									elif pay_choice==3:
										print("Order total = ₹",order_final_list[edit_order])
										total_money=order_final_list[edit_order]
										total_bill+=1
										online_payment+=total_money
										total_income+=total_money
										gst+=order_gst_list[edit_order]
										total_discount+=order_discount_list[edit_order]
										#following code is for printing bill,
										print("Exporting Bill.. Hold on!")
										print("\n" * 3)
										print("*" * 30)
										print("Freddy fazbear's Restaurant")
										print("Name:",name)
										print("--INVOICE--")
										print("*" * 30)
										for sino4 in range(0,len(order_item_list[edit_order])):
											print(sino4+1,"→",order_item_list[edit_order][sino4],"\t",order_quantity_list[edit_order][sino4],"\t",order_price_list[edit_order][sino4],"\t",order_total_list[edit_order][sino4])
										print("Total = ₹",order_sum_list[edit_order])
										print("Tax = ₹",order_gst_list[edit_order])
										print("Discount = ₹",order_discount_list[edit_order])
										print("Total with gst = ₹",order_final_list[edit_order])
										print("*" * 30)
										print("Online payment = ₹",total_money)
										print("*" * 30)
										print("Thank you for chosing Freddy fazbear's Restaurant!")
										print("Hoping to see you soon again!")#bill printing completed
										#this is to remove the record of the order as it turned into bill
										print("\n"*5)
										print("Bill exported successfully!")
										exit=input("Press ENTER to continue")#this to make sure the user reads the message to prevent confusion
										print("\n"*3)
										order_item_list.pop(edit_order)
										order_price_list.pop(edit_order)
										order_quantity_list.pop(edit_order)
										order_total_list.pop(edit_order)
										order_sum_list.pop(edit_order)
										order_gst_list.pop(edit_order)
										order_discount_list.pop(edit_order)
										order_final_list.pop(edit_order)
										edit_new=0
									else:
										print("Bill has not been Exported ⚠️.")#this comes when user select othe option of payment choice
										exit=input("Press ENTER to continue")#this to make sure the user reads the message to prevent confusion
							else:
								print("Are you sure you want to exit edit order?")
								print("y_yes")
								print("n_no")
								print("other option_no")
								confirm=input("Enter your choice:-")
								if confirm=="y":
									print("You chose to exit edit order!")
									exit=input("Press ENTER to continue")#this to make sure the user reads the message to prevent confusion
									print("\n"*3)
									edit_new=0 #This is to stop the loop of editing order
								else:
									print("You chose not to exit edit order")
									print("\n")
		elif main_choice==4:
			print("-*-"*8)
			print("Please enter admin password to access admin function")
			print("(Default password is 123456)")
			enter_pass=input("Enter the password:-")
			if enter_pass!=password:
				print("Wrong password, please try again")
			else:
				print("Welcome to the Admin Panel")
				admin=1 #this is for looping the admin function till the user want to exit loop
				while admin==1:
					print("-*-"*8)
					print("How may i help you?")
					print("1 → View today's income")#line723
					print("2 → Change category")#line736
					print("3 → Change item")#line846
					print("4 → Change Tax amount")#line1042
					print("5 → Change Discount Price")#line1066
					print("6 → Change password")#line1090
					print("Other option_exit")
					admin_choice=input("Enter your choice")
					if admin_choice.isdigit()==False:
						print("ERROR!")
						print("Please enter a number!")
						exit=input("Press ENTER to continue")#this to make sure the user reads the message to prevent confusion
						print("\n"*3)
					else:
						admin_choice=int(admin_choice)
						if admin_choice==1: #shows the income details
							print("-*-"*8)
							print("Today's income details are as follows:-")
							print("Total CASH payment = ₹",cash)
							print("Total CARD payment = ₹",card)
							print("Total Online payment = ₹",online_payment)
							print("Total Tax = ₹",gst)
							print("Total discount given = ₹",total_discount)
							print("Total income = ₹",total_income)
							print("Total bills exported =",total_bill)
							print("-*-"*8)
							print("\n"*3)
							exit=input("Press ENTER to return") #to return back to admin menu
						elif admin_choice==2:
							print("-*-"*8)
							print("(All changes done will be temporary stored)") #this is because the program cant link to a file
							for sino in range(0,len(category)):
								print(sino+1,"→",category[sino]) #this prints all the category available
							print("How would you like to change the category?")
							print("1 → Add category")#line735
							print("2 → Delete category")#line750
							print("3 → Edit category name")#line784
							print("Other option → Return to admin menu")
							change_choice=input("Enter your choice:- ")
							if change_choice.isdigit()==False:
								print("ERROR!")
								print("please enter a number!")
								exit=input("Press ENTER to continue")#this to make sure the user reads the message to prevent confusio
								print("\n"*3)
							else:
								change_choice=int(change_choice)
								if change_choice==1:
									print("-*-"*8)
									new_category=input("Please enter new category name:-") #takes the name of the category to be added
									if new_category in category:
										print("This category already exited!")
										exit=input("Press ENTER to continue")#this to make sure the user reads the message to prevent confusio
									else:
										category.append(new_category)
										items.append([])
										price.append([])
										print(new_category,"is successfully add!")
										print("Category list is as follow:-")
										print(category)
										exit=input("Press ENTER to continue")#this to make sure the user reads the message to prevent confusio
										print("\n" *3)
								elif change_choice==2:
									print("-*-"*8)
									print("Deleting the category will delete all the items and their price as well")
									print("Are you sure you want to delete category?")#this is to prevent accident deleting category
									print("y → yes ")
									print("n → no ")
									print("other option→no")
									confirm=input("Enter your choice:-")
									if confirm=="y":
										print("-*-"*8)
										print("Which category to delete?")
										delete_category=input("Enter your choice:- ")#takes the category to be deleted
										if delete_category.isdigit()==False:
											print("ERROR!")
											print("Please enter a number!")
											exit=input("Press ENTER to continue")#this to make sure the user reads the message to prevent confusio
											print("\n"*3)
										else:
											delete_category=int(delete_category)
											delete_category-=1
											if delete_category not in range(0,len(category)):
												print("Invalid number entered,please try again later!")
												exit=input("Press ENTER to continue")#this to make sure the user reads the message to prevent confusio
											else:	
												category.pop(delete_category)
												items.pop(delete_category)
												price.pop(delete_category)
												print("Category successfully deleted!")
												print("Category list is now as follow:-")
												print(category)
												exit=input("Press ENTER to continue")#this to make sure the user reads the message to prevent confusio
												print("\n" * 3)
									else:
										print("You chose to not delete the category") 
								elif change_choice==3:
									print("-*-"*8)
									print("Are you sure you want to edit category?")
									print("y → yes ")
									print("n → no ")
									print("other option→no")
									choice=input("Enter your choice:-")#this is to prevent accidentally editting category
									if choice=="y":
										print("-*-"*8)
										print("Which category to edit?")
										edit_category=input("Enter your choice:-")
										if edit_category.isdigit()==False:
											print("ERROR!")
											print("Please enter a number!")
											exit=input("Press ENTER to continue")#this to make sure the user reads the message to prevent confusio
											print("\n")
										else:
											edit_category=int(edit_category)
											edit_category-=1
											if edit_category not in range(0,len(category)):
												print("Invalid number entered, please try again later!")
												exit=input("Press ENTER to continue")#this to make sure the user reads the message to prevent confusio
												print("\n"*3)
											else:
												print("Original category name is",category[edit_category])
												edit_name=input("Enter new category name:-") #takes the new name of the category
												if edit_name in category:
													print("This category name already exists!")
													exit=input("Press ENTER to continue")#this to make sure the user reads the message to prevent confusio
												else:
													category[edit_category]=edit_name
													print("New category name is now",edit_name)
													print("Category name changed successfully!")
													print("-*-"*8)
													print("New category list is",category)
													exit=input("Press ENTER to continue")#this to make sure the user reads the message to prevent confusio
													print("\n" * 3)
									else:
										print("You chose not to edit category name")
										exit=input("Press ENTER to continue")#this to make sure the user reads the message to prevent confusion
								else:
									print("Category change is done successfully!")
									print("\n" * 3)
						elif admin_choice==3:
							print("-*-"*8)
							print("(All changes will be temporarily stored)")
							print("Category are as follows:-")
							#following lines print the categories with all their items in it
							for sino in range(0,len(category)):
								print(sino+1,"→",category[sino])
								print("Items of this category are as follows:-")
								for sino1 in range(0,len(items[sino])):
									print("\t",sino1+1,"→",items[sino][sino1])
								print("Item of which category would you like to edit?")#takes the category to change item easily
								change_item=input("Enter your choice:-")
								if change_item.isdigit()==False:
									print("ERROR!")
									print("Please enter a number!")
									exit=input("Press ENTER to continue")#this to make sure the user reads the message to prevent confusio
									print("\n")
								else:
									change_item=int(change_item)
									change_item-=1
									if change_item not in range(0,len(category)):
										print("Invalid number entered, please try again later")
										exit=input("Press ENTER to continue")#this to make sure the user reads the message to prevent confusio
										print("\n"*3)
									else:
										print("-*-"*8)
										print("How would you like to change the items?")
										print("1→Add")#line867
										print("2→Delete")#line895
										print("3→Edit item name")#line930
										print("4→Edit item price")#line972
										print("other option_Return to admin menu")
										change_choice=input("Enter your choice:-")
										if change_choice.isdigit()==False:
											print("ERROR!")
											print("Please enter a number!")
											exit=input("Press ENTER to continue")#this to make sure the user reads the message to prevent confusio
											print("\n"*3)
										else:
											change_choice=int(change_choice)
											if change_choice==1:
												print("-*-"*8)
												new_item=input("Please enter name of new item:-")#this adds a new item
												if new_item in items[change_item]:
													print("This item name already exists!")
													exit=input("Press ENTER to continue")#this to make sure the user reads the message to prevent confusio
												else:
													items[change_item].append(new_item)
													print("New item",new_item,"successfully created!")
													print("New item list of category",category[change_item],"are as follows")
													print(items[change_item])
													exit=input("Press ENTER to continue")#this to make sure the user reads the message to prevent confusio
													print("What is the price of",new_item,"?")#this adds the price of the new item
													new_price=input("Enter your choice:-")
													if new_price.isdigit()==False:
														print("ERROR!")
														print("Please enter a number!")
														print("To prevent error the new item entered will be deleted!")
														items[change_item].pop()
														exit=input("Press ENTER to continue")#this to make sure the user reads the message to prevent confusio
														print("\n"*3)
													else:
														new_price=int(new_price)
														price[change_item].append(new_price)
														print("Price of new item",new_item,"is",new_price)
														print("New item successfully added!")
														exit=input("Press ENTER to continue")#this to make sure the user reads the message to prevent confusio
														print("\n" * 3)
											elif change_choice==2:
												print("-*-"*8)
												print("Are you sure you want to delete item?")#this is to prevent accident delete of items
												print("y→yes")
												print("n→no")
												print("other option→no")
												confirm=input("Enter your choice:-")
												if confirm=="y":
													print("-*-"*8)
													print("Which item would you like to delete?")
													for sino in range(0,len(items[change_item])):
														print(sino+1,"→",items[change_item][sino])
													delete_item=input("Enter your choice:-")
													if delete_item.isdigit()==False:
														print("ERROR!")
														print("Please enter a number!")
														exit=input("Press ENTER to continue")#this to make sure the user reads the message to prevent confusio
														print("\n"*3)
													else:
														delete_item=int(delete_item)
														delete_item-=1
														if delete_item not in range(0,len(items[change_item])):
															print("Invalid number entered, please try again later!")
															exit=input("Press ENTER to continue")#this to make sure the user reads the message to prevent confusio
														else:
															items[change_item].pop(delete_item)
															price[change_item].pop(delete_item)
															print("Item successfully deleted!")
															print("New list of items in category",category[change_item],"are as follow:-")
															print(items[change_item])
															exit=input("Press ENTER to continue")#this to make sure the user reads the message to prevent confusion
															print("\n" * 3)
												else:
													print("No items are deleted")	
													exit=input("Press ENTER to continue")#this to make sure the user reads the message to prevent confusion					
											elif change_choice==3:
												print("-*-"*8)
												print("Are you sure you want to edit item name?")#this is to prevent accident editing of items
												print("y→yes")
												print("n→no")
												print("other option→no")
												confirm=input("Enter your choice:-")
												if confirm=="y":
													print("-*-"*8)
													print("Which item would you like to edit?")
													for sino in range(0,len(items[change_item])):
														print(sino+1,"→",items[change_item][sino])
													edit_name=input("Enter your choice:-")
													if edit_name.isdigit()==False:
														print("ERROR!")
														print("Please enter a number!")
														exit=input("Press ENTER to continue")#this to make sure the user reads the message to prevent confusio
														print("\n"*3)
													else:
														edit_name=int(edit_name)
														edit_name-=1
														if edit_name not in range(0,len(items[change_item])):
															print("Invalid number entered, please try again later!")
															exit=input("Press ENTER to continue")#this to make sure the user reads the message to prevent confusion
															print("\n"*3)
														else:
															print("Original item name:-",items[change_item][edit_name])
															new_name=input("Please enter new name")
															if new_name in items[change_item]:
																print("This item name already exists!")
																exit=input("Press ENTER to continue")#this to make sure the user reads the message to prevent confusion
																print("\n"*3)
															else:
																items[change_item][edit_name]=new_name
																print("Item name successfully changed to",new_name)
																print("New list of items of category",category[change_item],"are as follow:-")
																print(item[change_item])
																exit=input("Press ENTER to continue")#this to make sure the user reads the message to prevent confusion
																print("\n" * 3)
												else:
													print("No items are edited")
													exit=input("Press ENTER to continue")#this to make sure the user reads the message to prevent confusion					
											elif change_choice==4:
												print("-*-"*8)
												print("Are you sure you want to edit item price?")#this is to prevent accident editing of item price
												print("y → yes ")
												print("n → no ")
												print("other option → no ")
												confirm=input("Enter your choice:- ")
												if confirm=="y":
													print("-*-"*8)
													print("Which item price would you like to edit?")
													print("SI.no\titem\tprice")
													for sino in range(0,len(items[change_item])):
														print(sino+1,"→",items[change_item][sino],"\t",price[change_item][sino])
													edit_name=input("Enter your choice:-")
													if edit_name.isdigit()==False:
														print("ERROR!")
														print("Please enter a number!")
														exit=input("Press ENTER to continue")#this to make sure the user reads the message to prevent confusion
														print("\n"*3)
													else:
														edit_name=int(edit_name)
														edit_name-=1
														if edit_name not in range(0,len(items[change_item])):
															print("Invalid number entered, please try again later!")
															exit=input("Press ENTER to continue")#this to make sure the user reads the message to prevent confusion
															print("\n"*3)
														else:
															print("Original item price of",items[change_item][edit_name],"is:-",price[change_item][edit_name])
															new_price=input("Please enter new price")
															if new_price.isdigit()==False:
																print("ERROR!")
																print("Please enter a number!")
																exit=input("Press ENTER to continue")#this to make sure the user reads the message to prevent confusio
																print("\n"*3)
															else:
																new_price=int(new_price)
																price[change_item][edit_name]=new_price
																print("Item price successfully changed to",new_price)
																print("New list of items of category",category[change_item],"with their price are as follow:- ")
																print("SI.no\titem\tprice")
																for sino in range(0,len(items[change_item])):
																	print(sino+1,"→",items[change_item][sino],"\t",price[change_item][sino])
																exit=input("Press ENTER to continue")#this to make sure the user reads the message to prevent confusion
																print("\n" * 3)	
												else:
													print("You chose to not edit item price")
													exit=input("Press ENTER to continue")#this to make sure the user reads the message to prevent confusion
											else:
												print("Item change is done successfully!")
												exit=input("Press ENTER to continue")#this to make sure the user reads the message to prevent confusion
						elif admin_choice==4:
							print("-*-"*8)
							print("Are you sure you want to change tax?")#this is to prevent accident changing tax				
							print("y → yes ")
							print("n → no ")
							print("other option → no")
							confirm=input("Enter your choice:-")
							if confirm=="y":
								print("-*-"*8)
								print("Original tax% is",gst_percent,"%")
								new_gst=input("Please enter new tax% in numbers:-")
								if new_gst.isdigit()==False:
									print("ERROR!")
									print("Please enter a number!")
									exit=input("Press ENTER to continue")#this to make sure the user reads the message to prevent confusion
									print("\n"*3)
								else:
									new_gst=int(new_gst)
									gst_percent=new_gst
									print("Tax% changed successfully!")
									exit=input("Press ENTER to continue")#this to make sure the user reads the message to prevent confusion
									print("\n" * 3)
							else:
								print("Tax not changed")
								exit=input("Press ENTER to continue")#this to make sure the user reads the message to prevent confusion
						elif admin_choice==5:
							print("-*-"*8)
							print("Are you sure you want to change discount?")#this is to prevent accident changing discount				
							print("y → yes ")
							print("n → no ")
							print("other option_no")
							confirm=input("Enter your choice:-")
							if confirm=="y":
								print("-*-"*8)
								print("Original discount is",discount,"%")
								new_discount=input("Please enter new discount in numbers:-")
								if new_discount.isdigit()==False:
									print("ERROR!")
									print("Please enter a number!")
									exit=input("Press ENTER to continue")#this to make sure the user reads the message to prevent confusion
									print("\n"*3)
								else:
									new_discount=int(new_discount)
									discount=new_discount
									print("Discount changed successfully!")
									exit=input("Press ENTER to continue")#this to make sure the user reads the message to prevent confusion
									print("\n" * 3)
							else:
								print("Discount not changed")
						elif admin_choice==6:
							print("-*-"*8)
							print("Are you sure you want to change password?")#this is to prevent accident changing password
							print("y → yes ")
							print("n → no ")
							print("other option→no")
							confirm=input("Enter your choice:-")
							if confirm=="y":
								print("-*-"*8)
								print("Please enter old password")
								print("(Default password =123456)")
								old_pass=input("Enter old password:-")
								if old_pass==password:
									print("You are allowed to change password")				
									new_pass=input("Please enter new password:-")
									confirm_pass=input("Please confirm new password:-")
									if confirm_pass==new_pass:
										print("Password successfully changed!")
										password=new_pass
										print("Do not share the password with anyone to keep your data safe")
										print("\n" *3)
									else:
										print("Sorry, your confirm password is incorrect!")
										exit=input("Press ENTER to continue")#this to make sure the user reads the message to prevent confusion
										print("\n"*3)
								else:
									print("Incorrect password")
									exit=input("Press ENTER to continue")#this to make sure the user reads the message to prevent confusion
									print("\n" *3)
							else:
								print("Password is not changed!")
						else:
							admin=0
		elif main_choice==5:
			print("-*-"*8)
			print("Are you sure you want to exit program?")
			print("All the changes wont be saved!")
			print("y→yes")
			print("n→no")
			print("other option→no")
			confirm=input("Enter your choice:-")
			if confirm=="y":
				print("-*-"*8)
				print("Exiting program")
				print("Thank you for using our program and welcome back soon!")
				print("Good bye!")
				program=0
			else:
				print("You chose not to exit program!")	
		else:
			print("Please enter one of the following number:-") # this is to tell user what input to put at main menu
			print("1,2,3,4,5")
			exit=input("Press ENTER to continue")#this to make sure the user reads the message to prevent confusio
			print("\n" * 3)
	#The code of the program is over