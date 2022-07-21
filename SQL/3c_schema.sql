
/*商品分類基本檔*/
CREATE TABLE category(
    category_id int primary key,  #分類id auto_increment
    category_code char(2) ,  #分類縮寫 不可重複 SP=手機 AC=配件 NB=筆電 產生規則:取縮寫(手動)
    category_name nvarchar(100), #分類名稱   手機,配件,筆電
    category_level int, #級別
    parent_id int #父類id
       
)

/*商品基本檔*/
CREATE TABLE product (
    product_id char(8) primary key,  #商品id 格式:SP000001 產生規則:category_code+該類自動增長 
    product_name nvarchar(100), #商品名稱  SAMSUNG Galaxy Note 20
    product_model nvarchar(30),
    brand_id char(5),  #品牌id FK
    -- thumbnail varchar(100), #縮圖(路徑)
    -- carousel varchar(100),  #輪播圖(路徑)
    category_id int,  #分類id(第二層分類)
    supplier_id int,  #廠商id Example:XX公司
    create_time datetime ,
    details nvarchar(500) #詳細介紹
);

/*品牌基本檔*/
CREATE TABLE brand (
    brand_id char(5) primary key ,  #品牌id 格式:B0001 產生規則:B+資料庫自動增長
    brand_code char(2), #品牌縮寫 不可重複 example:SAMSUNG=SS,APPLE=AP,XIAOMI=XM
    brand_name nvarchar(64), #品牌名稱 Example:SAMSUNG,APPLE,XIAOMI
);

/*庫存基本檔*/
CREATE TABLE sku (
    sku_id char(11) primary key,  #sku商品id 產生規則:取product_id + "-"+ 該產品count example:SP000001-01
    product_id nvarchar(100), #商品id
    sku_code varchar(50),  #sku編碼 SAMSUNG GALAXY NOTE20 8GB+256GB WHITE 產生規則:SS-N20-8G256-W 
    sell_price int,  #目前售價
    recom_price int,  #建議售價
    cost int,  #成本價
    stock_quantity int,  #庫存量
    create_time datetime,  #創建日期
    update_time datetime,  #更新日期
    memo nvarchar(300) #備註/規格
);

/*員工基本檔*/
CREATE TABLE employee (
    employee_id char(7) primary key ,  #員工id E0001 產生規則:E+資料庫自動增長
    # employee_password  #密碼
    # employee_stas, char(1), 員工在職狀態 0=離職 1=在職  
    employee_name nvarchar(20), #員工姓名
    employee_gender char(1),  #員工性別, 1-男 2-女
    employee_phone varchar(20),  #員工電話
    employee_address varchar(50), #員工地址
    join_time datetime, #加入時間
    update_time datetime, #更新資料時間
)


/*顧客基本檔*/
CREATE TABLE customer (
    customer_id char(7) primary key ,  #用戶id 格式C000001 產生規則:C+資料庫自動增長
    customer_name nvarchar(20), #用戶姓名
    customer_gender char(1),  #用戶性別, 1-男 2-女  
    customer_phone varchar(20),  #用戶電話
    customer_address varchar(50), #用戶地址
    join_time datetime, #加入會員時間
    update_time datetime #更新資料時間
)

/*廠商基本檔*/
CREATE TABLE supplier(
    supplier_id int primary key ,  #廠商id example:S0001  產生規則:S+資料庫自動增長
    supplier_name nvarchar(40), #廠商名稱
    contact_num varchar(10),
    create_time datetime, #創建時間
    last_instock_time datetime #最後一次進貨時間
)


/*盤點紀錄檔*/
CREATE TABLE chk_record(
    chkrec_id char(36) primary key,  #盤點id 產生規則:uuid
    sku_id char(11) ,  #sku商品id
    chkstaff_id char(7) ,  #盤點人員id
    chk_time datetime,  #盤點日期
    chk_amount int, #庫存盤點量
    memo varchar(300) #備註
)

/* 交易記錄表 */
CREATE TABLE trans_record(
    trans_id char(36), #訂單號 PK  產生規則:uuid
    # order_stats int(1), #訂單狀態
    employee_id char(7), #employee.employee_id FK 員工id
    customer_id char(7), #customer.customer_id FK 顧客id
    trans_date datetime, #交易時間
    total_price int #總成交金額
)

/*交易紀錄明細檔*/
CREATE TABLE trans_detail(
    trans_id char(36),  #交易記錄id 主鍵 fk 
    sku_id char(11), #sku.sku_id FK sku商品id
    serial_id char(128), # serial_product.serial_id FK 產品序列號
    sale_price int ,#單品最終銷售金額
    quantity int(4), #數量  if (serial_id is not null){quantity set 1} 
    memo varchar(300), #商品備註
)
ALTER TABLE trans_detail ADD primary key(trans_id, sku_id) #複合PK

/* 進貨記錄表 */
CREATE TABLE restock_record(
    restock_id char(36), #進貨號 PK  產生規則:uuid
    # order_stats int(1), #訂單狀態
    employee_id char(7), #employee.employee_id FK 員工id
    supplier_id char(7), #supplier.supplier_id FK 廠商id
    restock_date datetime, #進貨時間
    total_price int #總成交金額
)

/*進貨紀錄明細檔*/
CREATE TABLE restock_detail(
    restock_id char(36),  #交易記錄id 主鍵 fk 
    sku_id char(11), #sku.sku_id FK sku商品id
    serial_id char(128), # serial_product.serial_id FK 產品序列號
    sale_price int ,#單品最終銷售金額
    quantity int(4), #數量  if (serial_id is not null){quantity set 1} 
    memo varchar(300), #商品備註
)
ALTER TABLE restock_detail ADD primary key(restock_id, sku_id) #複合PK

/*序列商品基本檔*/
CREATE TABLE serial_product(
    serial_id int primary key,  #序列商品id主鍵 產生規則: 
    sku_id char(11),  #sku商品id
    SN_code varchar(128), #產品序列號
    instock_stats int(1), #庫存狀態 0=已售出 1=在庫存 2=遺失
    create_time datetime; #建立時間
    sale_time datetime; #售出時間
)

/*進貨記錄檔(restock_record)*/
CREATE TABLE restock_record(
    restock_id int primary key,  #進貨記錄表主鍵 
    order_num varchar(15), #廠商單號
    employee_id char(7), #負責進貨員工
    supplier_id char(5), #進貨廠商id
    restock_datetime datetime, #進貨時間
    total_price int #進貨總價格
)


/*進貨記錄明細表(restock_detail)*/
CREATE TABLE restock_detail(
    restock_id int primary key,  #進貨記錄明細表主鍵 
    serial_id int,   #產品序列號id
    sale_price int, #單價
    quantity int,    #進貨數量
    memo varchar(300) #商品備註
)

