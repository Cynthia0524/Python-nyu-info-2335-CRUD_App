# Product Manager Application

## Overview

**Target Users** Grocery owners or product managers

**Goal** Manage your product list

### Core Features
|             |**Description**                                 |
|-------------|:----------------------------------------------:|
|List         |Display a list of product identifiers and names.|
|Show         |Show information about a product.               |
|Create       |Add a new product.                              |
|Update       |Edit an existing product.                       |
|Destroy      |Delete an existing product.                     |



### User Friendly
1. You can choose exit or not after every operation.
2. You will get guides when you are choosing.
3. When you exit, your changes will be saved and reflected in your product list, the csv file.
4. Your changes before exit would be saved temporarily in python rather in the csv file.

   So you are free to change whatever you like until you are satisfied!

## Prerequisite
python3 installed
csv file saving product list

## Installation

Download the source code:

```shell
git clone https://github.com/Cynthia0524/Python-nyu-info-2335-CRUD_App.git
cd some/path/to/Python-nyu-info-2335-CRUD_App
```

Finally, download the [example `products.csv` file](https://raw.githubusercontent.com/prof-rossetti/nyu-info-2335-70-201706/master/projects/crud-app/products.csv) and save it as `data/products.csv` in the downloaded folder.

Or if you like, you could have your own csv file in the data folder, which should has the same format with the example csv file.

## Usage

### Go to the required folder in Terminal (Mac)
```shell
cd some/path/to/Python-nyu-info-2335-CRUD_App
```
### Run the python
```shell
python3 app/products_app.py
```
