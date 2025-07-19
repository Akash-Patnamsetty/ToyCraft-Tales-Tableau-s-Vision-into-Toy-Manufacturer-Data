import pandas as pd
import random
from datetime import datetime, timedelta

# Define parameters
num_rows = 1000
start_date = datetime(2023, 1, 1)
end_date = datetime(2025, 6, 30)

# Sample data
product_ids = [f"T{i:03d}" for i in range(1, 21)]
product_names = [
    "RoboRex", "Puzzle Champ", "DinoPlay", "Super Blocks", "Magic Wand", 
    "Story Buddy", "Glow Drone", "Water Blaster", "SoccerBot", "Lego World", 
    "RaceMaster", "Fairy Princess", "Mega Craft", "Rocket Zoom", "Build-a-Car", 
    "Chess Junior", "PaintSplash", "Animal Friends", "Science Kit", "Bouncy Ball"
]
categories = [
    "Electronic", "Educational", "Outdoor", "Dolls", "Action Figures", 
    "Board Games", "Arts & Crafts"
]
regions = ["North-East", "South", "West Coast", "Midwest", "International"]
cities = {
    "North-East": ["New York", "Boston", "Philadelphia"],
    "South": ["Atlanta", "Miami", "Dallas"],
    "West Coast": ["Los Angeles", "San Francisco", "San Diego"],
    "Midwest": ["Chicago", "Cleveland", "Detroit"],
    "International": ["London", "Tokyo", "Toronto"]
}
age_groups = ["Toddlers (1–4)", "Kids (5–10)", "Pre-Teens (8–12)", "Teens (13–18)"]
genders = ["M", "F"]

# Helper functions
def random_date(start, end):
    return start + timedelta(days=random.randint(0, (end - start).days))

def season_from_date(date):
    if date.month in [12, 1, 2]: return "Winter"
    elif date.month in [3, 4, 5]: return "Spring"
    elif date.month in [6, 7, 8]: return "Summer"
    else: return "Fall"

# Generate data
data = []
for _ in range(num_rows):
    date = random_date(start_date, end_date)
    idx = random.randint(0, len(product_ids) - 1)
    category = random.choice(categories)
    region = random.choice(regions)
    city = random.choice(cities[region])
    age_group = random.choice(age_groups)
    gender = random.choice(genders)
    price = round(random.uniform(9.99, 59.99), 2)
    units_sold = random.randint(10, 300)
    total_sales = round(price * units_sold, 2)
    season = season_from_date(date)
    
    data.append([
        date.strftime("%Y-%m-%d"), product_ids[idx], product_names[idx], category, 
        price, units_sold, total_sales, region, city, age_group, gender, season
    ])

# Create and save DataFrame
df = pd.DataFrame(data, columns=[
    "Date", "Product_ID", "Product_Name", "Category", "Price", "Units_Sold", 
    "Total_Sales", "Region", "City", "Age_Group", "Gender", "Season"
])
df.to_csv("toycraft_tales_dataset.csv", index=False)
print("Dataset saved as toycraft_tales_dataset.csv")
