import pandas as pd
zoho_df=pd.read_csv('rate and mark up info from zoho.csv')
#print(zoho_df.head())
print(zoho_df.describe())
acct_df=pd.read_csv('accounting_rate_info.csv')
#print(acct_df.head())
print(zoho_df.describe())
#is_expert=zoho_df['Expert']==acct_df['Expert']
#print(is_expert)
#is_matter=zoho_df['Matter Name']==acct_df['Matter Name']
#print(is_matter)
#is_markup=zoho_df['Markup']==acct_df['Mark-up']
#confirmed_match=is_expert & is_matter & is_markup
#print(confirmed_match)


#change column on accounting spreadsheet to match zoho spreadsheet
acct_df = acct_df.rename(columns={'Mark-up': 'Markup'})
print(zoho_df.columns)
print(acct_df.columns)

#merge both spreadsheets for rows that expert, markup and matter name colums are equal
merged_df = pd.merge(zoho_df, acct_df, on=['Expert', 'Markup', 'Matter Name'])
print(merged_df.head())
print(merged_df.describe())
#print(merged_df['Rate'])
merged_df.to_csv('merged_data.csv', index=False)

#merge both spreadsheets for rows that expert and matter name colums are equal
merged_df = pd.merge(zoho_df, acct_df, on=['Expert', 'Matter Name'])
print(merged_df.head())
print(merged_df.describe())
#print(merged_df['Rate'])
merged_df.to_csv('merged_data_wo_markup_match.csv', index=False)
