# 푸시/알림 아키텍쳐

서비스 리텐션 상승을 위해 푸시/알림 기능 설계 및 개발

## 1. 기술스택

- Python3.8
- AWS
    - Lambda (Serverless)
    - RDS (DB)
    - SQS (Message Queue)
- FCM (Firebase Cloud Messaging)

## 2. 시스템 아키텍쳐

![스크린샷 2023-09-11 오전 3 26 3](https://github.com/2023-team-judy-coding-test-study/coding-test/assets/70069253/7706a308-a120-44c9-a517-ac3dd0794ffc)

## 3. 동작 방식

### producer

1. 정책에 따른 ‘푸시 메세지 타입’과 ‘발송자에 대한 정보’를 SQS에 전달합니다.

### consumer(push system)

1. 푸시 메세지 타입과 발송자의 유효성을 검증합니다.
2. 푸시 대상이 되는 사용자들을 식별하고 유저의 fcm token 정보와 함께 조회합니다.
3. FCM에 보낼 메세지를 세팅하여 전달합니다.
4. FCM에서 대상 유저들에게 푸시/알림을 전송합니다.