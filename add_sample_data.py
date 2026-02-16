import sqlite3

conn = sqlite3.connect("database/app.db")
cursor = conn.cursor()

colleges = [
    ("Aditya Engineering College", "Andhra Pradesh", "India", "State"),   
    ("Pragati Engineering College", "Andhra Pradesh", "India", "State"),  
    ("KL University", "Andhra Pradesh", "India", "State"),                
    ("VIT AP", "Andhra Pradesh", "India", "State"),                       
    ("LPU", "Punjab", "India", "National"),                               
    ("Tokyo Tech University", "Tokyo", "Japan", "International"),         
    ("SRM University", "Tamil Nadu", "India", "National"),                
    ("Amrita University", "Kerala", "India", "National"),                
    ("IIT Bombay", "Maharashtra", "India", "National"),                   
    ("IIT Delhi", "Delhi", "India", "National"),                          
    ("NIT Warangal", "Telangana", "India", "National"),                   
    ("BITS Pilani", "Rajasthan", "India", "National"),                    
    ("MIT", "Massachusetts", "USA", "International"),                     
]

cursor.executemany(
    "INSERT INTO colleges (name, place, country, type) VALUES (?, ?, ?, ?)",
    colleges
)


placements = [

    (1, 2024, 420, 520),
    (1, 2023, 400, 500),
    (1, 2022, 370, 480),

    (2, 2024, 340, 470),
    (2, 2023, 320, 450),
    (2, 2022, 300, 430),

 
    (3, 2024, 620, 720),
    (3, 2023, 590, 700),
    (3, 2022, 560, 680),


    (4, 2024, 310, 390),
    (4, 2023, 290, 370),
    (4, 2022, 260, 350),

  
    (5, 2024, 760, 1034),
    (5, 2023, 720, 1000),
    (5, 2022, 690, 980),

  
    (6, 2024, 310, 340),
    (6, 2023, 300, 330),
    (6, 2022, 290, 320),

 
    (7, 2024, 810, 950),
    (7, 2023, 770, 920),
    (7, 2022, 730, 890),

 
    (8, 2024, 680, 780),
    (8, 2023, 650, 760),
    (8, 2022, 610, 730),


    (9, 2024, 950, 1020),
    (9, 2023, 920, 1000),
    (9, 2022, 880, 980),

    (10, 2024, 900, 980),
    (10, 2023, 870, 960),
    (10, 2022, 830, 940),

    (11, 2024, 720, 860),
    (11, 2023, 690, 840),
    (11, 2022, 650, 820),

    (12, 2024, 880, 950),
    (12, 2023, 850, 930),
    (12, 2022, 820, 910),

    
    (13, 2024, 1200, 1300),
    (13, 2023, 1170, 1280),
    (13, 2022, 1140, 1260),
]

cursor.executemany(
    "INSERT INTO placements (college_id, year, placed_students, total_students) VALUES (?, ?, ?, ?)",
    placements
)


college_details = [
    (1, 85000, 3.4, 4000, 90000, 82, 3.3, "CSE"),
    (2, 65000, 4.4, 7000, 100000, 76, 4.3, "CSE"),
    (3, 120000, 4.5, 1000, 9000, 90, 4.3, "CSE"),
    (4, 140000, 2.2, 3000, 80000, 72, 2.3, "ECE"),
    (5, 40000, 3.4, 400, 5000, 70, 4.3, "MECH"),
    (6, 90000, 4.4, 1, 900, 91, 4.4, "AIML"),
    (7, 180000, 4.0, 500, 8000, 85, 4.1, "CSE"),
    (8, 160000, 4.3, 700, 10000, 83, 4.2, "CSE"),
    (9, 25000, 4.7, 1, 500, 95, 4.6, "CSE"),
    (10, 26000, 4.6, 1, 600, 94, 4.5, "CSE"),
    (11, 90000, 4.2, 2000, 25000, 86, 4.0, "CSE"),
    (12, 220000, 4.8, 1, 2000, 92, 4.7, "CSE"),
    (13, 450000, 4.9, 1, 200, 97, 4.8, "CSE"),
]

cursor.executemany(
    """
    INSERT INTO college_details
    (college_id, fee, hostel_rating, cutoff_l, cutoff_h, placements_all, hostel_food_rating, top_branch)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """,
    college_details
)

companies = [
    (1, 2024, "TCS"), (1, 2024, "Infosys"), (1, 2024, "Wipro"),
    (2, 2024, "Capgemini"), (2, 2024, "Cognizant"),
    (3, 2024, "Amazon"), (3, 2024, "Microsoft"), (3, 2024, "Google"),
    (4, 2024, "Accenture"), (4, 2024, "Deloitte"),
    (5, 2024, "HCL"), (5, 2024, "Tech Mahindra"),
    (6, 2024, "Sony"), (6, 2024, "Rakuten"), (6, 2024, "Toyota"),
    (7, 2024, "Zoho"), (7, 2024, "Samsung"),
    (8, 2024, "Oracle"), (8, 2024, "IBM"),
    (9, 2024, "Google"), (9, 2024, "Goldman Sachs"),
    (10, 2024, "Amazon"), (10, 2024, "Adobe"),
    (11, 2024, "Infosys"), (11, 2024, "Wipro"),
    (12, 2024, "Microsoft"), (12, 2024, "Apple"),
    (13, 2024, "Meta"), (13, 2024, "Netflix"),
]

cursor.executemany(
    "INSERT INTO companies (college_id, year, company_name) VALUES (?, ?, ?)",
    companies
)


branch_names = [
    ("CSE", 240, 15000, 4.6, 4.4),
    ("IT", 180, 20000, 4.4, 4.2),
    ("AIML", 120, 17000, 4.5, 4.3),
    ("DS", 60, 22000, 4.3, 4.1),
    ("CSBS", 60, 25000, 4.2, 4.0),
    ("ECE", 180, 28000, 4.2, 4.0),
    ("EEE", 120, 42000, 3.9, 3.8),
    ("MECH", 120, 55000, 3.8, 3.6),
    ("CIVIL", 120, 75000, 3.5, 3.4),
]

branches = []
for college_id in range(1, 14):
    for b in branch_names:
        branches.append((college_id, b[0], b[1], b[2], b[3], b[4]))

cursor.executemany(
    """
    INSERT INTO branches (college_id, branch_name, intake, cutoff_rank, branch_rating, faculty_rating)
    VALUES (?, ?, ?, ?, ?, ?)
    """,
    branches
)


def branch_id(college_id, index_1_to_9):
    return ((college_id - 1) * 9) + index_1_to_9

branch_placements = []


branch_multiplier = {
    "CSE": 0.92,
    "IT": 0.88,
    "AIML": 0.90,
    "DS": 0.89,
    "CSBS": 0.86,
    "ECE": 0.75,
    "EEE": 0.68,
    "MECH": 0.60,
    "CIVIL": 0.52
}


college_avg_base = {
    1: 6.5, 2: 6.0, 3: 8.5, 4: 5.5, 5: 4.8,
    6: 7.5, 7: 7.0, 8: 6.8, 9: 12.0, 10: 11.5,
    11: 8.0, 12: 10.5, 13: 13.5
}

branches_order = ["CSE", "IT", "AIML", "DS", "CSBS", "ECE", "EEE", "MECH", "CIVIL"]
intake_map = {"CSE":240, "IT":180, "AIML":120, "DS":60, "CSBS":60, "ECE":180, "EEE":120, "MECH":120, "CIVIL":120}

for college_id in range(1, 14):
    base = college_avg_base[college_id]

    for idx, bname in enumerate(branches_order, start=1):
        total = intake_map[bname]

        # placed %
        placed_2024 = int(total * branch_multiplier[bname])
        placed_2023 = int(total * (branch_multiplier[bname] - 0.05))
        placed_2022 = int(total * (branch_multiplier[bname] - 0.10))

        # avg packages
        avg2024 = round(base * (1 if bname in ["CSE","IT","AIML","DS","CSBS"] else 0.75), 1)
        avg2023 = round(avg2024 - 0.5, 1)
        avg2022 = round(avg2023 - 0.4, 1)

        # highest packages
        high2024 = int(avg2024 * 3)
        high2023 = int(avg2023 * 3)
        high2022 = int(avg2022 * 3)

        bid = branch_id(college_id, idx)

        branch_placements.extend([
            (college_id, bid, 2024, total, placed_2024, avg2024, high2024),
            (college_id, bid, 2023, total, placed_2023, avg2023, high2023),
            (college_id, bid, 2022, total, placed_2022, avg2022, high2022),
        ])

cursor.executemany(
    """
    INSERT INTO branch_placements
    (college_id, branch_id, year, total_students, placed_students, avg_package, highest_package)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """,
    branch_placements
)

conn.commit()
conn.close()

print(" FULL dummy data inserted successfully (clean + no duplicates)!")
