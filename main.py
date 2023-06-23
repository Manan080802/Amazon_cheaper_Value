
import requests
import smtplib
import lxml
from bs4 import BeautifulSoup
url="https://www.amazon.com/tamispit-Swimming-Waterproof-Touchscreen-Smartwatch/dp/B0BC3Y5LDP/ref=sr_1_1_sspa?keywords=watch+for+men&qid=1687511721&sprefix=watch%2Caps%2C449&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1"
# url="https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&language=en_US&currency=USD"
# url="https://www.amazon.com/Instant-Pot-Duo-Mini-Programmable/dp/B06Y1YD5W7/ref=pd_rhf_d_ee_s_pd_sbs_rvi_sccl_1_1/146-9256956-6809832?pd_rd_w=SQ2Fa&content-id=amzn1.sym.a089f039-4dde-401a-9041-8b534ae99e65&pf_rd_p=a089f039-4dde-401a-9041-8b534ae99e65&pf_rd_r=ECC4VNXQTYY9XZ18529F&pd_rd_wg=NZpbQ&pd_rd_r=f4d3781c-85a2-4c87-9d40-9a89aad90eed&pd_rd_i=B06Y1YD5W7&th=1"
header={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 "
                 "Safari/537.36",
    "Accept-Language":"en-US,en;q=0.9,gu;q=0.8"

}
response = requests.get(url, headers=header)

soup = BeautifulSoup(response.content, "lxml")
price = soup.find(class_="a-offscreen").get_text()
# print(price)
price_without_currency = price.split("$")[1]
price_as_float = float(price_without_currency)
# print(price_as_float)
response= requests.get("https://www.bookmyforex.com/currency-converter/usd-to-inr/")

yc_web_page=response.text
soup1 = BeautifulSoup(yc_web_page,"html.parser")
# print(soup1.title.text)
#
dollatoinr= soup1.find(class_="first_live_trade").getText()
dollatoinr = dollatoinr.split(" ")
# print(dollatoinr)
dollatoinr = dollatoinr[2]
dollatoinr =dollatoinr.split("\n")
dollatoinr = float(dollatoinr[1])
# print(dollatoinr)
finaltotalprice = round(dollatoinr*price_as_float)
print(finaltotalprice)
title = soup.find(id="productTitle").get_text().strip()
print(title)
BUY_PRICE = 3000
if price_as_float < BUY_PRICE:
    message = f"{title} is now {finaltotalprice}"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        result = connection.login("manpat@gmail.com","")
        connection.sendmail(
            from_addr="manpat@gmail.com",
            to_addrs="manvaghasiya@gmail.com,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}".encode("utf-8")
        )
