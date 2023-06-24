import sqlite3
from scripts import webscrapers as wb


conn = sqlite3.connect("db.sqlite3")
conn.row_factory = lambda c, row: row
c = conn.cursor()
c.execute("""SELECT url_morrisons, url_sainsburys, url_tesco
             FROM products_product""")
database_urls = c.fetchall()


for rows in database_urls:
    for url in rows:
        if "bigbasket.com" in url:
            bigbasket_price = wb.bigbasket_scrape(url)
            # print(morrisons_price)
            c.execute("""UPDATE products_product
                         SET price_morrisons=?
                         WHERE url_morrisons=?""", (bigbasket_price, url))

        elif "dmart.in" in url:
            dmart_price = wb.dmart_scrape(url)
            # print(sainsburys_price)
            c.execute("""UPDATE products_product
                         SET price_sainsburys = ?
                         WHERE url_sainsburys=?""", (dmart_price, url))

        elif "amazon.in" in url:
            amazon_price = wb.amazon_scrape(url)
            # print(tesco_price)
            c.execute("""UPDATE products_product
                         SET price_tesco=?
                         WHERE url_tesco=?""", (amazon_price, url))

        else:
            print("FLAG: Is the following url correct? {}".format(url))

conn.commit()
c.close()
conn.close()
