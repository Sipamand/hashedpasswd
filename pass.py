import bcrypt
import time
import openpyxl

# Simulating request data (replace with actual data from aiohttp request)
request_data = {
    "username": "Sipamandla",
    "password": "s.F@3565%"
}

password = request_data["password"].encode("utf-8")
hashed = bcrypt.hashpw(password, bcrypt.gensalt())

print("Hashed Password:", hashed.decode('utf-8'))

if bcrypt.checkpw(password, hashed):
    print("Matched")
else:
    print("Did not match")
    
    start = time.time()
    hashed_rounds = bcrypt.hashpw(password, bcrypt.gensalt(rounds=14))
    end = time.time()
    time_taken = end - start
    print("Time taken for 14 rounds:", time_taken)

    # Open or create a spreadsheet
    file_path = 'password_info.xlsx'
    try:
        wb = openpyxl.load_workbook(file_path)
    except FileNotFoundError:
        wb = openpyxl.Workbook()

    # Select the active sheet (first sheet by default)
    sheet = wb.active

    # Add data to the spreadsheet
    row_data = [request_data["username"], hashed.decode('utf-8'), "Matched" if bcrypt.checkpw(password, hashed) else "Not Matched", time_taken]
    sheet.append(row_data)

    # Save the spreadsheet
    wb.save(file_path)
