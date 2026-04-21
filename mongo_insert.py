from pymongo import MongoClient
from datetime import datetime

def main():
    # Connect to local MongoDB
    client = MongoClient("mongodb://localhost:27017/")

    # Use the database vehicle_db
    db = client["vehicle_db"]

    # Collections
    auth_server = db["auth_server"]
    service = db["service"]

    # ------------------------------------------
    # INSERT INTO auth_server (4 total records)
    # ------------------------------------------
    auth_data = [
        # Existing sample users
        {
            "username": "vijay123",
            "email": "vijay@example.com",
            "role": "customer",
            "created_at": datetime.now()
        },
        {
            "username": "shree456",
            "email": "shree@example.com",
            "role": "admin",
            "created_at": datetime.now()
        },

        # New 2 additional records
        {
            "username": "vijay_user",
            "email": "vijay_new@example.com",
            "role": "customer",
            "created_at": datetime.now()
        },
        {
            "username": "prathaap_user",
            "email": "prathaap@example.com",
            "role": "customer",
            "created_at": datetime.now()
        },

        # Admin Shree Shanth
        {
            "username": "shree_shanth_admin",
            "email": "shree_shanth@example.com",
            "role": "admin",
            "created_at": datetime.now()
        }
    ]

    # ------------------------------------------
    # INSERT INTO service (4 total records)
    # ------------------------------------------
    service_data = [
        # Existing sample records
        {
            "customer_name": "Vijay",
            "vehicle_number": "KA01AB1234",
            "service_type": "Full Service",
            "status": "Completed",
            "amount": 2500,
            "created_at": datetime.now()
        },
        {
            "customer_name": "Shree",
            "vehicle_number": "KA09HG2211",
            "service_type": "Oil Change",
            "status": "Pending",
            "amount": 900,
            "created_at": datetime.now()
        },

        # New 2 additional service records
        {
            "customer_name": "Vijay",
            "vehicle_number": "KA05MQ9090",
            "service_type": "Tyre Rotation",
            "status": "In Progress",
            "amount": 700,
            "created_at": datetime.now()
        },
        {
            "customer_name": "Prathaap",
            "vehicle_number": "KA11TT5567",
            "service_type": "Engine Check",
            "status": "Pending",
            "amount": 1800,
            "created_at": datetime.now()
        },

        # Admin Shree Shanth (as service manager entry)
        {
            "customer_name": "Shree Shanth",
            "vehicle_number": "KA03SS3333",
            "service_type": "Inspection (Admin Verification)",
            "status": "Verified",
            "amount": 0,
            "created_at": datetime.now()
        }
    ]

    # Insert documents
    auth_insert = auth_server.insert_many(auth_data)
    service_insert = service.insert_many(service_data)

    # Print confirmation
    print("Inserted into auth_server:", auth_insert.inserted_ids)
    print("Inserted into service:", service_insert.inserted_ids)

    print("\nFetching all auth_server documents:")
    for doc in auth_server.find():
        print(doc)

    print("\nFetching all service documents:")
    for doc in service.find():
        print(doc)


if __name__ == "__main__":
    main()
