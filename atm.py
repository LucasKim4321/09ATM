# 기본 금액 : balance
# 기본 금액에 돈을 넣어주세요
# while문을 이용해서 입금, 출금, 영수증 보기, 종료라는 기능이 종료라는 버튼을 누르기전 까지 계속해서 노출되도록 만들어주세요.
# 종료를 누르면 서비스를 종료한다는 메시지를 출력하고현재 잔액을 보여주세요.

receipts = [ (2000, 3000), (-1000, 2000), (5000, 7000) ]
# receipts = []
print("이전 영수증 리스트:",receipts)

balance = 7000

# 종료 할 때까지 무한 반복
while True:

    # 서비스 코드 입력
    service_num = input("사용하실 기능을 선택해주세요 (1:입금, 2:출금, 3:영수증 보기, 4:종료)").strip()
    # 숫자 입력만 가능
    if not(service_num.isdigit()):
        print("숫자만 입력해주세요!")
        continue

    # 입출금
    if service_num == '1' or  service_num == '2':
        while True:
            amount = input(f"{'입금' if service_num == '1' else '출금'}하실 금액을 입력하세요. :b  ").strip()  #strip() 없어도 문제없긴 함.
            # 숫자 입력시에만 형변환, 덤으로 -도 입력 안됨 :b
            if amount.isdigit(): #문자형 숫자일 경우만.
                amount = int(amount)
            else:
                print("숫자만 입력해주세요!")
                continue

            초과_여부 = False

            if service_num == '2':
                # amount = min(balance, amount)  # 두 값을 비교해서 작은 값을 반환
                if amount > balance :
                    amount = balance
                    초과_여부 = True
                amount = -amount
            
            balance += amount
            거래_정보 = (amount, balance)
            receipts.append(거래_정보)
            # receipts.insert(len(receipts), 거래_정보)
            
            if(초과_여부 == True):
                print(f"************************\n영수증\n****\n출금 가능한 금액을 초과하여 현재 잔액 만큼만 출금합니다!\n****\n출금: {abs(amount)}원. \n현재 잔액은 {balance}원입니다.\n****\n************************")
            else:
                print(f"************************\n영수증\n****\n{'입금' if service_num == '1' else '출금'}: {abs(amount)}원. \n현재 잔액은 {balance}원입니다.\n****\n************************")
            break

    # 영수증 출력
    if service_num == '3':
        print('현재 잔액:', balance)
        if receipts:
            print("모든 거래 내역 (최근 거래순)")
            # for i in reversed(range(len(receipts))):  # reversed() 역순으로 리턴
                # print(f"{'입금' if receipts[i][0] > 0 else '출금'} : {abs(receipts[i][0])}, 잔액 : {receipts[i][1]}")  # abs(숫자) 절대값 리턴
            for i in reversed(receipts):
                print(f"{'입금' if i[0] > 0 else '출금'} : {abs(i[0])}, 잔액 : {i[1]}")
            print("***************************")
        else:
            print("출력할 거래 내역이 없습니다. :b")

    # 종료
    if service_num == '4':
        print("서비스를 종료하겠습니다.")
        print(f"현재 잔액은 {balance}원 입니다!")
        print("안녕히가십시오!")
        break
