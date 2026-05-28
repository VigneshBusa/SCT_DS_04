# ==========================================
# SPAM MESSAGE DATA ANALYSIS
# ==========================================

# Import Libraries
import pandas as pd
import matplotlib.pyplot as plt

# ==========================================
# LOAD DATASET
# ==========================================

data = pd.read_csv('spam.csv', encoding='latin-1')

print("DATASET LOADED SUCCESSFULLY\n")

# ==========================================
# DISPLAY FIRST 5 ROWS
# ==========================================

print("FIRST 5 RECORDS OF DATASET")
print(data.head())

# ==========================================
# DATASET INFORMATION
# ==========================================

print("\nDATASET SHAPE")
print("Rows :", data.shape[0])
print("Columns :", data.shape[1])

# ==========================================
# MISSING VALUES TABLE
# ==========================================

missing_values = data.isnull().sum()

missing_table = pd.DataFrame({
    'Column Name': missing_values.index,
    'Missing Values': missing_values.values
})

print("\nMISSING VALUES TABLE")
print(missing_table)

# ==========================================
# SPAM VS HAM ANALYSIS
# ==========================================

message_counts = data['v1'].value_counts()

analysis_table = pd.DataFrame({
    'Message Type': message_counts.index,
    'Count': message_counts.values
})

print("\nMESSAGE TYPE ANALYSIS")
print(analysis_table)

# ==========================================
# VISUALIZATION
# ==========================================

plt.figure(figsize=(6,4))

message_counts.plot(kind='bar')

plt.title('Spam vs Ham Message Distribution')
plt.xlabel('Message Type')
plt.ylabel('Count')

plt.show()
