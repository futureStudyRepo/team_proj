# DES05 데이터베이스 설계서 예시

문서명: 데이터베이스 설계서  
대상 시스템: HIS 연계 CDSS

## 1. 문서 목적

본 문서는 CDSS 운영에 필요한 데이터 저장 구조를 정의하기 위한 것이다.

## 2. 주요 테이블

| 테이블명 | 설명 | 주요 컬럼 |
|---|---|---|
| ALERT_LOG | 알림 발생 및 처리 로그 | log_id, patient_id, visit_id, alert_type, created_at, user_id, action_result, ignore_reason |
| ALERT_RULE_VERSION | 규칙 버전 관리 | rule_id, version_no, threshold_value, message_text, active_yn, applied_at |
| ALERT_TARGET_PATIENT | 관리대상 환자 상태 | patient_id, visit_id, dm_target_yn, sepsis_watch_yn, updated_at |
| ALERT_ACTION_HISTORY | 후속조치 이력 | action_id, log_id, order_type, ordered_yn, ordered_at |

## 3. 대표 컬럼 정의

| 테이블 | 컬럼 | 타입 | 설명 |
|---|---|---|---|
| ALERT_LOG | log_id | VARCHAR(30) | 로그 식별자 |
| ALERT_LOG | alert_type | VARCHAR(30) | HBA1C_MISSING, SEPSIS_HIGH 등 |
| ALERT_LOG | created_at | DATETIME | 알림 발생 시각 |
| ALERT_LOG | action_result | VARCHAR(30) | VIEWED, IGNORED, ORDERED_TEST |
| ALERT_RULE_VERSION | threshold_value | VARCHAR(100) | 규칙 기준값 |
| ALERT_TARGET_PATIENT | dm_target_yn | CHAR(1) | 당뇨 관리대상 여부 |

## 4. 인덱스 고려사항

- patient_id + created_at
- alert_type + created_at
- visit_id

## 5. 한 줄 정리

DB 설계서의 핵심은  
`알림 자체뿐 아니라 규칙 버전, 대상 환자 상태, 후속조치 이력까지 추적 가능하게 저장하는 것`이다.
