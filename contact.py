# Contact Management System

contacts = []

def add_contact():
    print("\nAdding a new contact:")
    name = input("Enter name: ")
    phone_number = input("Enter phone number: ")
    email = input("Enter email address: ")
    address = input("Enter address: ")
    
    contacts.append({
        'name': name,
        'phone_number': phone_number,
        'email': email,
        'address': address
    })
    print("Contact added successfully!")

def view_contact_list():
    print("\nViewing all contacts:")
    if not contacts:
        print("No contacts found.")
    else:
        for index, contact in enumerate(contacts):
            print(f"{index + 1}. Name: {contact['name']}, Phone: {contact['phone_number']}, Email: {contact['email']}, Address: {contact['address']}")

def search_contact():
    query = input("\nEnter name or phone number to search: ")
    search_results = []
    for contact in contacts:
        if query.lower() in contact['name'].lower() or query in contact['phone_number']:
            search_results.append(contact)
    
    if not search_results:
        print("No matching contacts found.")
    else:
        print(f"\nSearch results for '{query}':")
        for result in search_results:
            print(f"Name: {result['name']}, Phone: {result['phone_number']}, Email: {result['email']}, Address: {result['address']}")

def update_contact():
    view_contact_list()
    if not contacts:
        return
    
    try:
        index = int(input("\nEnter the index of the contact to update: ")) - 1
        if 0 <= index < len(contacts):
            contact = contacts[index]
            print(f"\nUpdating contact: {contact['name']}")
            print("Leave input blank if you don't want to change a field.")
            
            new_name = input(f"Enter new name ({contact['name']}): ").strip() or contact['name']
            new_phone = input(f"Enter new phone number ({contact['phone_number']}): ").strip() or contact['phone_number']
            new_email = input(f"Enter new email ({contact['email']}): ").strip() or contact['email']
            new_address = input(f"Enter new address ({contact['address']}): ").strip() or contact['address']
            
            contacts[index] = {
                'name': new_name,
                'phone_number': new_phone,
                'email': new_email,
                'address': new_address
            }
            print("Contact updated successfully!")
        else:
            print("Invalid index.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def delete_contact():
    view_contact_list()
    if not contacts:
        return
    
    try:
        index = int(input("\nEnter the index of the contact to delete: ")) - 1
        if 0 <= index < len(contacts):
            del contacts[index]
            print("Contact deleted successfully!")
        else:
            print("Invalid index.")
    except ValueError:
        print("Invalid input. Please enter a number.")

# Main menu loop
while True:
    print("\n===== Contact Management System =====")
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")
    
    choice = input("\nEnter your choice (1-6): ")
    
    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contact_list()
    elif choice == '3':
        search_contact()
    elif choice == '4':
        update_contact()
    elif choice == '5':
        delete_contact()
    elif choice == '6':
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 6.")
