import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix

df = pd.read_csv("customer_churn.csv")
print("-"*40)
print("Customer Dataset :")
print(df)
print("-"*40)

X = df.drop(columns=["churn"])
Y = df["churn"]

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

model = LogisticRegression(max_iter=1000)
model.fit(X_train,Y_train)

Y_pred = model.predict(X_test)

accurancy = accuracy_score(Y_test,Y_pred)
print("Accuracy is:",accurancy)

age = int(input("Enter the Age:"))
tenure = int(input("\nEnter your tenure"))
charges = int(input("\nEnter your charges"))
calls = int(input("\nEnter calls:"))

new_customer = pd.DataFrame({
    "Age" : [age],
    "Tenure" : [tenure],
    "Charges" : [charges],
    "SupportCalls" : [calls]
})

new_customer["Churn"] = model.predict(new_customer)

if new_customer["Churn"].iloc[0] == 1:
    print("Customer is likely to churn")
else:
    print("Customer is not likely to churn")

joblib.dump(model)
print("model saved successfully...")