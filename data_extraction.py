import pandas as pd

input_file = 'sales_train_evaluation.csv'
output_file = 'm5_sales_last_365_days.csv'

print("1. Đang đọc và lọc dữ liệu gốc...")
id_vars = ['id', 'item_id', 'dept_id', 'cat_id', 'store_id', 'state_id']
day_cols = [f'd_{i}' for i in range(1577, 1942)]
cols_to_use = id_vars + day_cols

df = pd.read_csv(input_file, usecols=cols_to_use)

print("2. Đang chuyển đổi cấu trúc dữ liệu (Unpivot/Melt)...")
df_melted = pd.melt(df, 
                    id_vars=id_vars, 
                    value_vars=day_cols, 
                    var_name='day', 
                    value_name='sales')

print("3. Đang xuất ra file CSV mới...")
df_melted.to_csv(output_file, index=False)

print(f"Hoàn tất! File {output_file} đã được tạo với {len(df_melted):,} dòng.")