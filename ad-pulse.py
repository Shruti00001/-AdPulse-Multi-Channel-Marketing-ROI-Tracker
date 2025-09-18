import csv
import random

channels = ['Social Media', 'Email', 'Search', 'Display', 'Influencer']
regions = ['North', 'South', 'East', 'West']
quarters = ['Q1', 'Q2', 'Q3', 'Q4']
segments = ['Fashionistas', 'Foodies', 'Techies', 'Parents', 'Students', 'Fitness Buffs', 'Travelers', 'Homeowners']
categories = ['Apparel', 'Electronics', 'Grocery', 'Furniture', 'Wellness', 'Education', 'Travel', 'Finance']

with open('adpulse_campaign_data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow([
        "Campaign_ID", "Channel", "Region", "Quarter", "Spend_INR", "Revenue_INR",
        "Impressions", "Clicks", "Conversions", "CPC_INR", "CTR_Percent",
        "Conversion_Rate_Percent", "Audience_Segment", "Product_Category"
    ])

    for i in range(1000):
        spend = random.randint(50000, 200000)
        revenue = random.randint(spend, spend * 2)
        impressions = random.randint(100000, 1000000)
        clicks = random.randint(2000, 20000)
        conversions = random.randint(100, clicks)
        cpc = round(spend / clicks, 2)
        ctr = round((clicks / impressions) * 100, 2)
        conv_rate = round((conversions / clicks) * 100, 2)

        writer.writerow([
            f"C{i+1:04}",
            random.choice(channels),
            random.choice(regions),
            random.choice(quarters),
            spend,
            revenue,
            impressions,
            clicks,
            conversions,
            cpc,
            ctr,
            conv_rate,
            random.choice(segments),
            random.choice(categories)
        ])
