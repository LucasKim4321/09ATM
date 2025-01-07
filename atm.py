# 기본 금액 : balance
# 기본 금액에 돈을 넣어주세요
# while문을 이용해서 입금, 출금, 영수증 보기, 종료라는 기능이 종료라는 버튼을 누르기전 까지 계속해서 노출되도록 만들어주세요.
# 종료를 누르면 서비스를 종료한다는 메시지를 출력하고현재 잔액을 보여주세요.

receipts = [ (2000, 3000), (-1000, 2000), (5000, 7000) ]
print("이전 영수증 리스트:",receipts)

balance = 7000

# 종료 할 때까지 무한 반복
while True:

    # 서비스 코드 입력
    service_num = input("사용하실 기능을 선택해주세요 (1:입금, 2:출금, 3:영수증 보기, 4:종료)")

    # 입출금
    if service_num == '1' or  service_num == '2':
        amount = int(input('금액을 입력하세요. :b').strip())  #strip() 없어도 문제없긴 함.

        초과_여부 = False

        if service_num == '2':
            if amount > balance :
                amount = balance
                초과_여부 = True
            amount = -amount
        
        balance += amount
        거래_정보 = (amount, balance)
        receipts.append(거래_정보)
        
        if(초과_여부 == True):
            print(f"************************\n영수증\n****\n출금 가능한 금액을 초과하여 현재 잔액 만큼만 출금합니다!\n****\n{'입금' if service_num == '1' else '출금'}: {abs(amount)}원. \n현재 잔액은 {balance}원입니다.\n****\n************************")
        else:
            print(f"************************\n영수증\n****\n{'입금' if service_num == '1' else '출금'}: {abs(amount)}원. \n현재 잔액은 {balance}원입니다.\n****\n************************")

    # 영수증 출력
    if service_num == '3':
        print('현재 잔액:', balance)
        print("모든 거래 내역")
        for i in range(len(receipts)):
            print(f"{'입금' if receipts[i][0] > 0 else '출금'} : {abs(receipts[i][0])}, 잔액 : {receipts[i][1]}")

    # 종료
    if service_num == '4':
        print(f"현재 잔액은 {balance}원 입니다!")
        break
