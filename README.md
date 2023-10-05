# Device Inventory and Monitoring System

The **Device Inventory and Monitoring System** is a Django-based project designed to efficiently control and monitor devices in a warehouse, such as scanners and mobile printers. The primary goal of this project is to provide real-time inventory management and monitoring of the devices while automatically recording all changes in a dedicated Google Spreadsheet for analysis and reporting.

## Features

- **Device Registration:** Administrators can add new devices to the warehouse, providing their unique identifiers, models, costs, and other necessary information, along with their initial state.

- **Monitoring:** The system offers a user-friendly interface for displaying the status of each device in real-time. It can include information on availability, battery status (for mobile printers), potential issues, and more.

- **Inventory Management:** Users can conduct inventory checks using the system, marking which devices are present in the warehouse and which have been deployed or retired.

- **Change Log:** All device-related changes, such as additions, removals, or state modifications, are automatically recorded in a dedicated Google Spreadsheet. This allows for the creation of reports and tracking the history of changes.

- **Authorization and Access:** Different levels of access are provided for various users, with administrators having enhanced rights to manage the system, while regular users can view device information.


## Installation via GitHub

To install the Devices Tracker, you need to follow the below steps:

1. Install PostgresSQL and create a database
2. Clone the repository using `git clone https://github.com/MrYuriy/devices-tracker/tree/deploy`
3. Navigate to the repository directory using `cd devices-tracker`
4. Create a virtual environment using `python -m venv venv`
5. Activate the virtual environment on Linux/macOS using `source venv/bin/activate` or on Windows using `venv\Scripts\activate`
6. Install the required dependencies using `pip install -r requirements.txt`
7. Set environment variables like in .env_sample. Create .env file in your project's directory: 
   ```SQL
   echo. >.env
   ```
8. Create own creds.json file and SPREADSHEET_ID variable
9. Apply migrations to the database using `python manage.py migrate`
10. Start the server using `python manage.py runserver`

