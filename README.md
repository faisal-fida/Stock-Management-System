# Stock Management System

This is a simple Stock Management System built using Python and Tkinter. It allows users to manage stock items, including adding, updating, deleting, and exporting stock data to an Excel file.

## Features

- Add new stock items
- Update existing stock items
- Delete stock items
- Search for stock items
- Export stock data to an Excel file
- Generate random item IDs

## Requirements

- Python 3.x
- Tkinter
- pymysql
- numpy

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/stock-management-system.git
    cd stock-management-system
    ```

2. Install the required Python packages:
    ```sh
    pip install pymysql numpy
    ```

3. Ensure you have a MySQL database set up with the following details:
    - Host: `localhost`
    - User: `root`
    - Password: ``
    - Database: `stockmanagementsystem`

4. Create the `stocks` table in your MySQL database:
    ```sql
    CREATE TABLE `stocks` (
        `id` int(11) NOT NULL AUTO_INCREMENT,
        `item_id` varchar(255) NOT NULL,
        `name` varchar(255) NOT NULL,
        `price` decimal(10,2) NOT NULL,
        `quantity` int(11) NOT NULL,
        `category` varchar(255) NOT NULL,
        `date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
        PRIMARY KEY (`id`)
    );
    ```

## Usage

1. Run the application:
    ```sh
    python main.py
    ```

2. The application window will open, allowing you to manage stock items.

## Code Overview

### Main Functions

- `refreshTable()`: Refreshes the data displayed in the table.
- `setph(word, num)`: Sets the placeholder text for the form fields.
- `generateRand()`: Generates a random item ID.
- `save()`: Saves a new stock item to the database.
- `update()`: Updates an existing stock item in the database.
- `delete()`: Deletes a stock item from the database.
- `select()`: Selects a stock item from the table and fills the form fields with its data.
- `connection()`: Establishes a connection to the MySQL database.

### UI Components

- `window`: The main application window.
- `my_tree`: The treeview widget displaying the stock items.
- `placeholderArray`: An array of StringVar objects for form field placeholders.
- `frame`: The main frame containing all UI components.
- `manageFrame`: The frame containing the management buttons (Save, Update, Delete, etc.).
- `entriesFrame`: The frame containing the form fields for stock item details.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgements

- [Tkinter](https://docs.python.org/3/library/tkinter.html) - Python's standard GUI toolkit
- [pymysql](https://pypi.org/project/PyMySQL/) - A pure-Python MySQL client library
- [numpy](https://numpy.org/) - A fundamental package for scientific computing with Python

---

Feel free to contribute to this project by submitting issues or pull requests. Happy coding!
