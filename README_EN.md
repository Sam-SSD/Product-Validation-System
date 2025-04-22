![product_validation_system_banner2](https://github.com/user-attachments/assets/c8f3e51e-288e-4556-8aff-53e6285b231f)

# 🛒 Product Validation System

## 📌 Project Description

This project was developed as part of **Module 1 – Week 1 of the training program**. The main goal is to build an application that **calculates the total cost of a purchase** in a store, properly validating user input and applying discounts when applicable.

---

## 🎯 Features

- Prompts the user for the following data:
  - Product name
  - Unit price (positive number)
  - Quantity of products (positive number)
  - Discount percentage (between 0 and 100)
- Validates that all inputs are within the allowed range.
- Calculates:
  - Total cost before any discount
  - Final cost with discount applied (if applicable)
- Displays the result with two decimal places in a readable format.

---

## 🧠 Logic Implemented

- Two specific functions were implemented to validate numerical input:
  - `validar_numero_positivo(num)`
  - `validar_descuento(num)`
- The main logic calculates the total by **multiplying the price by the quantity**, then **applying the discount** if greater than 0.
- The result is shown in currency format (two decimals), along with the product name.

---

## ✅ Validations Performed

The following test scenarios were covered:

1. Product with no discount  
2. Product with 100% discount  
3. Discount out of range (rejected)  
4. Invalid input using letters or symbols (rejected)  
5. Quantity or price equal to zero  

All cases were handled correctly with no runtime errors.

---

## 📁 Code Structure

- Code is organized into reusable functions
- Main module includes clear comments for easy understanding
- User interaction messages are simple and informative

---

## 🧩 Technical Justification

Specific functions were used to separate responsibilities and ensure **modularity**, making the code easier to maintain and extend. Additionally:

- `float()` was used instead of `int()` to support decimal values for prices and quantities, which is more realistic in retail contexts.
- Error handling was implemented using `try/except` to manage invalid inputs and prevent execution errors.
- Output formatting with **two decimal places** improves readability and user experience.

These decisions enhance the **clarity, scalability, and quality** of the code, following good development practices.

---

## 🚀 Future Improvements

Potential enhancements for future versions:

- Implement a graphical user interface (GUI) using Tkinter or PyQt
- Allow multiple product entries in a single session and display the total sum
- Save purchase history to an external file (CSV or JSON)
- Validate that product names are not empty or follow a specific format
- Localize the currency format (e.g., thousands separator or local currency symbol)

---

## 💻 Execution Instructions

1. Make sure you have Python installed on your system (recommended version: Python 3.8 or higher).
2. Clone the repository from GitHub using the following command:

   ```bash
   git clone https://github.com/Sam-SSD/Product-Validation-System.git
   ```

3. Navigate to the project directory:

   ```bash
   cd Products-Validation-System
   ```

4. Run the main script with the following command:

   ```bash
   python validacion_de_productos.py
   ```

5. Follow the on-screen instructions to input the required data.
