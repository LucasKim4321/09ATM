# 기본 금액 : balance
# 기본 금액에 돈을 넣어주세요
# while문을 이용해서 입금, 출금, 영수증 보기, 종료라는 기능이 종료라는 버튼을 누르기전 까지 계속해서 노출되도록 만들어주세요.
# 종료를 누르면 서비스를 종료한다는 메시지를 출력하고현재 잔액을 보여주세요.

receipts = [ (2000, 3000), (-1000, 2000), (5000, 7000) ]
print("이전 영수증 리스트:",receipts)

balance = 7000


# while True:
#     service_num = input("사용하실 기능을 선택해주세요 (1:입금, 2:출금, 3:영수증 보기, 4:종료)")
#     if service_num == '4':
#         print(f"현재 잔액은 {balance}원 입니다!")
#         break
#     if service_num == '1' or '2':
#         amount = int(input('금액을 입력하세요. :b').strip())  #strip() 없어도 문제없긴 함.
#         초과_여부 = False

#         if service_num == '2':
#             if amount > balance :
#                 amount = balance
#                 초과_여부 = True
#             amount = -amount
#     balance += amount
#     거래_정보 = (amount, balance)
#     receipts.append(거래_정보)
#     print("거래 정보:",거래_정보)
#     print("영수증 리스트:",receipts)
        


# 입출금_여부 = input('입금 또는 출금을 입력하세요').strip()  #strip() 양쪽 공백 제거


# if(초과_여부 == True):
#     print(f'************************\n영수증\n****\n출금 가능한 금액을 초과하여 현재 잔액 만큼만 출금합니다!\n****\n{입출금_여부}: {abs(amount)}원. \n현재 잔액은 {balance}원입니다.\n****\n************************')

# else:
#     print(f'************************\n영수증\n****\n{입출금_여부}: {abs(amount)}원. \n현재 잔액은 {balance}원입니다.\n****\n************************')


"""


# 영수증 구조 [ (입금 or 출금 금액 , 현재잔액), (이하 동일) ... ]

receipts = [ (2000, 3000), (-1000, 2000), (5000, 7000) ]
print("이전 영수증 리스트:",receipts)

balance = 7000

입출금_여부 = input('입금 또는 출금을 입력하세요').strip()  #strip() 양쪽 공백 제거
amount = int(input('금액을 입력하세요. :b').strip())  #strip() 없어도 문제없긴 함.
초과_여부 = False

if(입출금_여부 == '출금'):
    if(amount > balance):
        amount = balance
        초과_여부 = True
    amount = -amount

balance += amount
거래_정보 = (amount, balance)
receipts.append(거래_정보)
print("거래 정보:",거래_정보)
print("영수증 리스트:",receipts)

if(초과_여부 == True):
    print(f'************************\n영수증\n****\n출금 가능한 금액을 초과하여 현재 잔액 만큼만 출금합니다!\n****\n{입출금_여부}: {abs(amount)}원. \n현재 잔액은 {balance}원입니다.\n****\n************************')

else:
    print(f'************************\n영수증\n****\n{입출금_여부}: {abs(amount)}원. \n현재 잔액은 {balance}원입니다.\n****\n************************')


"""
