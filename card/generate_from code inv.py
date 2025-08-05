import qr_codes
import pandas as pd
import json
import os

# Create a folder to save QR codes
os.makedirs("qr_codes", exist_ok=True)

# Read guest data from CSV
df = pd.read_csv("guests.csv")

# Loop through each guest
for i, row in df.iterrows():
    guest_data = {
        "name": row["Name"],
        "type": row["Type"],
        "code": row["Code"]
    }
    
    # Convert to JSON and generate QR
    data_str = json.dumps(guest_data)
    qr =qr_codes.make(data_str)
    
    # Save QR image
    filename = f"qr_codes/{row['Code']}.png"
    qr.save(filename)
    print(f"Generated: {filename}")
