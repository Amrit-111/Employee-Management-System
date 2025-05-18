#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Step-1 : Plan the Data Storage



employees = {101:{'name':'Satya',
                  'age': 27,
                  'department':'HR',
                  'salary':50000}, 
             
             
             102:{'name':'Trump',
                  'age':34,
                  'department':'Revenue',
                 'salary': 35000}}


# In[ ]:


employees.update({103:{'name':'Riya',
                'age':24,
                'department':'Sales',
                'salary':39000},
             
             104:{'name':'Eera',
                 'age':21,
                 'department':'Finance',
                 'salary':44000}})


# In[3]:


for emp_id,info in employees.items():
    print(f"{emp_id}:{info}")


# In[4]:


# step-3 : Add Employee Functionality 


def add_employee():
    try:
        emp_id = int(input("Enter Employee ID: "))
        if emp_id in employees:
            print("Employee ID already exists!\n")
            return
        name = input("Name: ")
        age = int(input("Age: "))
        dept = input("Department: ")
        salary = int(input("Salary: "))
        
        employees[emp_id] = {
            'name': name, 
            'age': age, 
            'department': dept, 
            'salary': salary 
        }
        print("✅ Employee added Successfully!\n")
    except ValueError:
        print("❌ Invalid Input! Please enter correct data types.\n")


# In[8]:


# step -4 :  View All Employees


def view_employees():
    if not employees:
        print("🚫 No employees available.\n")
        return

  
    print("📋 Employee Details:\n")
    print(f"{'ID':<6}{'Name':<18}{'Age':<6}{'Department':<18}{'Salary':<10}")
    print("-" * 50)

   
    for emp_id, info in employees.items():
        print(f"{emp_id:<6}"
              f"{info['name']:<15}"
              f"{info['age']:<6}"
              f"{info['department']:<15}"
              f"{info['salary']:<10}")
    print() 


# In[5]:


# Step 5 : Search for an Employee by ID


def search_employee():
    try:
        emp_id = int(input("Enter Employee ID to Search: "))
        if emp_id in employees:
            info = employees[emp_id]
            print(f"\n🔍 Employee found:\nID: {emp_id}")
            print(f"Name: {info['name']}")
            print(f"Age: {info['age']}")
            print(f"Department: {info['department']}")
            print(f"Salary: {info['salary']}\n")
        else:
            print("❌ Employee not found.\n")
    except ValueError:
        print("❌ Invalid Input. Please enter a valid Employee ID (number).\n")


# In[ ]:


# Last Step : Menu System and Exit Option


def main_menu():
    while True:
        print("====== Employee Managemt System ======")
        print("1. Add Employee")
        print("2. View All Employee")
        print("3. Search for Employee")
        print("4. Exit")
        choice = input("Choose an option (1-4): ")
        
        if choice == "1":
            add_employee()
        elif choice == "2":
            view_employees()
        elif choice == "3":
            search_employee()
        elif choice == "4":
            print(" 🙏 Thank you for using the Employee Management System!")
            
        else:
            print(" ❌ Invalid choice! Please select from 1 to 4.\n")
            
            
main_menu()


# In[ ]:




