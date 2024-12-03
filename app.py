# import os
import pandas as pd
from sqlalchemy import create_engine, Column, Integer, String 
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import sessionmaker

# อ่านไฟล์ CSV
df = pd.read_csv("Product-List.csv")
df.rename(
    columns={
        "ลำดับ": "index",
        "รายการสินค้า (Product List)": "product_List",
        "ชื่อสินค้า (Product Name)": "product_Name",
        "จำนวน Quantity": "quantity",
        "ราคา Price": "price",
    },
    inplace=True,
)

# ตั้งค่า SQLAlchemy
class Base(DeclarativeBase):
    pass

class Products(Base):
    __tablename__ = "tutorial"
    index = Column(Integer, primary_key=True)
    product_List = Column(String(255))
    product_Name = Column(String(255))
    quantity = Column(String(255))
    price = Column(String(255))

# สร้าง URL การเชื่อมต่อฐานข้อมูล
DATABASE_URL = "mysql+mysqlconnector://root:root@db:3306/tutorial"

# สร้าง engine และเซสชัน
engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# เพิ่มข้อมูลลงในฐานข้อมูล
try:
    df.to_sql(
        "tutorial",
        con=engine,
        if_exists="replace",
        index=False,
        method="multi",
    )
    print("Data successfully imported into the database!")
except Exception as e:
    print(f"Error importing data: {e}")
