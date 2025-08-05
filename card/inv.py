import csv
import json
import qrcode  # <--- correct library

with open("guests.csv", newline="") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        guest_data = {
            "name": row["Name"],
            "type": row["Type"],
            "code": row["Code"]
        }

        data_str = json.dumps(guest_data)
        qr = qrcode.make(data_str)  # <--- fixed line

        filename = f"qr_codes/{row['Code']}.png"
        qr.save(filename)
        print(f"Generated: {filename}")
