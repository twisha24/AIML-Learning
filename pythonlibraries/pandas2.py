import pandas as pd
data = {
    "name":["tia","tia","pia","pia"],
    "age" :[21,23,35,45],
    "salary" :[1000,4000,3500,5000],
    "text" :["hello" , "twisha" , "rastogi" , "wuhu"]
}

df = pd.DataFrame(data)
# print(df.dtypes)
# df["name"] = df["name"].astype("string")
# print(df["name"].dtype)

# df["age"]= pd.to_numeric(df["age"],errors="coerce")
# print(df["age"])
# df["gender"] = df["gender"].replace({
#     "M": "Male",
#     "F" : "Female"
# })
# print(df["gender"])

# df["gender"] = df["gender"].map({
#     "Male" : 0,
#     "Female" : 1
# })
# print(df["gender"])
# df["gender"] = df["gender"].apply({lambda x:x*2})
# print(df["gender"])
# def categorize(age):
#     if age < 18:
#         return "Teen"
#     elif age < 30:
#         return "Young"
#     else:
#         return "Adult"
    
# df["category"] = df["age"].apply(categorize)
# print(df)

# df["text"] = df["text"].str.upper()
# print(df["text"])
# df["text"] = df["text"].str.lower()
# print(df["text"])
# df["text"] = df["text"].str.strip()
# print(df["text"])
# result = df[df["text"].str.contains("hello",na = False)]
# print(result)
# df["text"] = df["text"].str.replace("hello", "hi")
# print(df["text"])
# df["text"] = df["text"].str.len()
# print(df["text"])
# df = df.groupby("name")["salary"].mean()
# print(df)
# df = df.groupby("name")["salary"].sum()
# print(df)
# df = df.groupby("name")["salary"].min()
# print(df)
# df = df.groupby("name")["salary"].max()
# print(df)
# df = df.groupby("name")["salary"].agg(["max","min","sum","count"])
# print(df)

