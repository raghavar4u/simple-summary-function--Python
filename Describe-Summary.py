def df_summary(df):
  df_U = df.nunique()
  df_M = df.isnull().sum()
  df_M_Per = (df.isnull().sum()/len(df)).sort_values()
  df_I = df.dtypes
  df_U = df_U.to_frame().reset_index()
  df_M = df_M.to_frame().reset_index()
  df_M_Per = df_M_Per.to_frame().reset_index()
  df_I = df_I.to_frame().reset_index()
  df_U = df_U.rename(columns= {0: 'Unique Data'})
  df_M = df_M.rename(columns= {0: 'Missing Data'})
  df_M_Per = df_M_Per.rename(columns= {0: 'Missing Percentage'})
  df_I = df_I.rename(columns= {0: 'Data Types'})
  output = pd.merge(pd.merge(pd.merge(df_U,df_M,on='index'),round(df_M_Per,2),on = 'index'),df_I,on='index')
  return output;
  
  
  ==================================================================================================================
  
  df_summary(data)
