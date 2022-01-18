# -*- coding: utf-8 -*-
"""LinkedList.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1GdOMWc7tMmoIptYIYIsymvb34kDwM9_J
"""

# Main Program
print("/10101200138")
print("Linked List.py")
print("")

def main(): 
    print("/10101200138")
    print("Linked List.py")
    print("")
    print("PROJEK UJIAN TENGAH SEMESTER IBDA 1012")
    print("Dibuat Oleh: Stefannus Christian")
    print("")

    # Linked List
    patient_list = LinkedList()

    # Print Header
    header()

    # Show Current List
    show(patient_list)

    print("")

    # Show Options
    option_gui()

    while True:
        user_option = input("Choose Your Option: ")
        print("")

        #Add Queue (Append)
        if user_option == '1':
          print("Your Option: "+user_option)
          print("You have choose option "+ user_option +" to add queue.")
          input_data = input_patient_data()
          
          if count(patient_list) < 14:
            append(patient_list, input_data)

            print("")

            # Print Header
            header()

            print("")
            print("List of Vaccine Recipient Patients")
            print("")

            # Show Patient List and Options

            show(patient_list)

            print("")
            print("===========================")
            print("Total Patient: ",count(patient_list))
            print("")

            option_gui()

          else:
            # Print Header
            header()

            print("")
            print("List of Vaccine Recipient Patients")
            print("")

            # Show Patient List and Options
            show(patient_list)

            print("")
            print("===========================")
            print("Total Patient: ",count(patient_list))
            print("Cannot add Queue! Queue is full.")
            
            print("")

            option_gui()

        # Pop List
        elif user_option == '2':
          print("You have choose option "+ user_option +" to remove the first patient.")

          pop(patient_list)

          print("")

          header()

          show(patient_list)

          print("")
          print("===========================")
          print("Total Patient: ",count(patient_list))
          print("")

          option_gui()

        elif user_option == '3':
          # Emergency Call (Remove)
          print("You have choose option "+ user_option +" which is to remove a patient of your choice.")

          patient_name = input("Which patient do you want to remove? ")
          print("")

          remove(patient_list,patient_name)
          print("")

          header()

          show(patient_list)

          print("")
          print("===========================")
          print("Total Patient: ",count(patient_list))
          print("")

          option_gui()

        elif user_option == '4':
          confirmation = input("Are you sure you want to leave (y/n)? ")
          confirmation.lower()

          while confirmation not in ["y","n"]:
            confirmation = input("Your input is invalid! Please enter (y --> yes) or (n --> no) ")

          if confirmation == "y":
            print("You left the program.")
            break

        else:
          print("Invalid Input!")
          print("Please enter a valid option! (1 / 2 / 3 / 4)")
          print("")

if __name__ == "__main__":

  # Class

  # Node
  class Node:
    def __init__ (self):
      self.data = None
      self.next = None

  # LinkedList
  class LinkedList:
    def __init__(self):
      self.head = None

  # Patient
  class Patient:
    def __init__(self):
      self.name = None
      self.age = None

  # Functions

  # Data input
  def input_patient_data():
    patient = Patient()

    print("Please enter patient name and age.")
    print("")

    patient.name = input("Patient Name: ")

    while True:
      try:
        patient.age = int(input("Patient Age: "))

        if patient.age >= 0:
          break

        else:
          print("")
          print("Invalid Input. Please enter an integer greater than 0!")
          print("")

      except ValueError:
        print("")
        print("Invalid Input. Please enter an integer greater than 0!")
        print("")

    return patient

  # Append Function

  def append(Linked_List, patient_data):
    if Linked_List.head == None:
      current = Node()
      current.data = patient_data
      Linked_List.head = current

    elif Linked_List.head is not None:
        current = Linked_List.head
        new_Data = Node()

        while current.next is not None:
          current = current.next 

        new_Data.data = patient_data
        current.next = new_Data

    return Linked_List  

  # Pop Function 

  def pop(Linked_List):
    if Linked_List.head is None:
      print("Cannot reduce queue because current queue is empty!")

    elif Linked_List.head.next is None:
      Linked_List.head = None

    else:
      Linked_List.head = Linked_List.head.next

  # Remove Function
  def remove(Linked_List, patient_name):

    current = Linked_List.head

    if current is None: 
      print("Current queue is empty!")

    elif current.data.name == patient_name:

      if current.next is None:
        Linked_List.head = None

      else:
        Linked_List.head = current.next

    else:
      found = True

      while current.next.data.name != patient_name:
        current = current.next

        if current.next is None:

          if current.data.name == patient_name:
            current.next = None

          found = False
          break

      if found is True:
        current.next = current.next.next
        
      else:
        print("Name not found")   



  # Count Function

  def count(Linked_List):
    if Linked_List.head is None:
      return 0

    elif Linked_List.head is not None:
      index = 1
      current = Linked_List.head

      while current.next is not None:
        current = current.next
        index = index + 1

      return index

  # Show Function

  def show(Linked_List):
    current = Linked_List.head

    if current is not None:
      number = 1

      print("===========================")
      print("No ","Name ","Age  ")
      print(number , current.data.name, current.data.age)

      while current.next is not None:
        current = current.next
        number = number + 1
        print(number, current.data.name, current.data.age)

    else:
        print("~ Queue is currently empty ~")

  # Header text

  def header():
    print("===========================")
    print("KrankenHause ScharfeSpitze")
    print("        Ilsestr 23.")
    print("        B-12051")
    print("===========================")
    print("") 

  # Option Text

  def option_gui():
    print("")
    print("Options: ")
    print("Option 1: Option (1) is to Add Queue. This option will add a patient to the queue.")
    print("Option 2: Option (2) is to Reduce Queue. This option will remove the first patient.")
    print("Option 3: Option (3) is Emergency Call. This option will search a patient name and remove it.")
    print("Option 4: Option (4) is to exit the program.")
    print("")

main()
