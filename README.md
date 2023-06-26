# وب سرویس نورمالایز کردن متون برای عملیات Text Cleaning

## اگه توی زبون های برنامه نویسی  دیگه نیاز به یه ابزار سریع برای انجام تمیزکاری روی متون پیدا کردید و نتونستید لایبرری براش پیدا کنید Normalizer Server رو حتما امتحان کنید
Normalizer Server مخصوص متون فارسی هست

ابتدا این ریپوزیتوری رو به این شکل 


```bash
git clone  https://github.com/sapurtcomputer30/NormalizerPyServer.git
```

کلون کنید

# روش راه اندازی سرور 

ابتدا این  پکیج هارو رو نصب کنید

## نصب Dadma Tools

```bash
pip install dadmatools 
```


## نصب Fast API

```bash
pip install fastapi 
```


## نصب uvicorn

```bash
pip install uvicorn 
```


برای اجرا کردن کافیه دستور زیر رو در مسیری که فایل server.py هست اجرا کنید


```bash
python -m uvicorn server:app
```



بعد از اجرا برنامه شما روی پورت 8000 لوکال هاست ران میشه و میتونید ازش استفاده کنید 

کافیه ریکوئستتون رو به صورت جیسون و با متد POST  با شکل زیر 

{
  "text":"متن شما اینجا"

}
<br>


بفرستید تا نتیجه رو دریافت کنید



آدرس مرجع : http://localhost:8000

