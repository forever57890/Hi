class elec:
    def __init__(self,winter,summer) :
        self.winter=winter
        self.summer=summer
            
    def elecWinterNT(Kwh):
        Do=Kwh
        winter = 0
        summer = 0
        while Do>1000:
            winter+=(Do-1000)*5.48
            summer+=(Do-1000)*6.99
            Do-=(Do-1000)
            break
        while Do>700:
            winter+=(Do-700)*4.6
            summer+=(Do-700)*5.66
            Do-=(Do-700)
            break
        while Do>500:
            winter+=(Do-500)*3.94
            summer+=(Do-500)*4.8
            Do-=(Do-500)
            break
        while Do>330:
            winter+=(Do-330)*2.89
            summer+=(Do-330)*3.52
            Do-=(Do-330)
            break           
        while Do>120:
            winter+=(Do-120)*2.1
            summer+=(Do-120)*2.38
            Do-=(Do-120)
            break
        while Do>=0:
            winter+=Kwh*1.63
            summer+=Kwh*1.63
            Do-=Do
            break
        return winter, summer



while True:
        try:
            print("請輸入單月總用電度數 , 或輸入 cls 關閉....")
            print("      ")
            Kwh=input("月用電度數: ")
            if Kwh=="cls":
                break
            Kwh=int(Kwh)
            a,b=elec.elecWinterNT(Kwh)
            print("     ")     
            print("非夏月電費 :", int(a),  " 元 ,", "平均每度 :", round(a/Kwh, 2) ,"元")
            print("夏月電費 :", int(b), " 元 ,", "平均每度 :", round(b/Kwh , 2) ,"元")
            print("------------------------------------------------------------------------------")
        except ValueError:
            print("請輸入數字")

        except KeyboardInterrupt:
            print("結束.....")
            break
            
# def test(winter,summer,Kwh):
#     print("非夏月電費 :", int(winter),  " 元 ,", "平均每度 :", round(winter/Kwh, 2) ,"元")
#     print("夏月電費 :", int(summer), " 元 ,", "平均每度 :", round(summer/Kwh , 2) ,"元")
    

