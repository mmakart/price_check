# price\_check

## Description

It's a simple price extractor and logger to see goods prices history.

## Usage

Put the urls with the interested items into the file `goods.txt`, each in one line. To do this you can just open the page in any browser and copy the text from the address line. At the moment the program can only read the prices from online stores `nix.ru` and `citilink.ru`, the others won't give you the result.

### Sample content of `goods.txt`:

```
https://www.citilink.ru/product/smartfon-apple-iphone-11-mhdh3ru-a-chernyi-1429419/
https://www.citilink.ru/product/smartfon-apple-iphone-se-mhgp3ru-a-chernyi-1429464/
https://www.nix.ru/autocatalog/hp/hp_compaq_notebook/HP-17-ca2036ur-22V23EA-ACB-Ryzen-3-3250U-8-512SSD-WiFi-BT-noOS-173-219-kg_481369.html
https://www.nix.ru/autocatalog/lcd_lg/_433809.html
```

Prices will be written to the text file `prices.log` every time the program is executed. You would like to automate the logging process. Then you should add the program to a task scheduler of your operating system (cron in UNIX-like systems and the Task Scheduler in MS Windows).
