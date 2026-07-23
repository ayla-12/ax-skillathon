---
name: my-workflow-skill
description: Use when a sales team needs to turn a Korean-headquartered company lead list into public-source research, privacy-lifecycle solution hypotheses, a transparent review priority, and a sales-manager review queue.
---

# 리드 리서치 자동화

공개 근거와 제안 가설을 분리해, 세일즈 매니저가 다음 영업 액션을 결정할 수 있는 리드 리서치 워크북을 만든다.

## Quick start (처음 사용할 때)

1. `mock-data/input-example.csv`를 열어 최소 입력 열과 30개 국내 본사 기업 예시를 확인한다.
2. 아래처럼 입력을 검증한다. `python` 경로는 사용하는 환경의 Python 실행 파일로 바꾼다.
   `python scripts/validate_lead_input.py mock-data/input-example.csv`
3. `mock-data/expected-output.md`와 `assets/lead-research-workbook-spec.md`를 열어 만들 워크북의 열과 표현 수준을 확인한다.
4. 실제 리드 파일로 같은 검증을 실행한 뒤, 공개 출처 조사와 워크북 작성을 진행한다.
5. 세일즈 매니저 승인 전에는 외부 접촉이나 CRM 반영을 하지 않는다.

## When to use (사용 시점)

- 신규 리드 리스트를 검토·너처링·아웃바운드 준비에 사용할 때
- 개인정보 라이프사이클 솔루션의 적합성 가설과 우선 검토 대상을 정리할 때
- 근거 링크와 사람 검토 이력이 남는 스프레드시트가 필요할 때

다른 목적의 시장 조사, 실명 연락처 수집, 실제 고객 데이터 분석에는 사용하지 않는다.

## Required inputs (필요한 입력)

1. 리드 CSV 또는 스프레드시트: `lead_id`, `company_name`, `headquarters_country`, `industry`, `company_website`.
2. 솔루션 프로필: 제공 가치, 우선 라이프사이클 범위, 제외할 산업 또는 계정.
3. 리드 운영 기준: 조사 기간, 우선순위 기준, 결과물 파일 위치.

입력이 불완전하면 `scripts/validate_lead_input.py`로 확인하고, 회사명 또는 본사 국가가 없으면 리서치를 진행하지 않는다. 예시 형식은 `mock-data/sample-leads.csv`를 따른다.

| 입력 열 | 필수 | 설명 |
|---|---:|---|
| `lead_id` | 예 | 리드별 고유 식별자. 개인 식별값을 사용하지 않는다. |
| `company_name` | 예 | 조사 대상 기업명 |
| `headquarters_country` | 예 | `KR`, `KOR`, `대한민국`, `한국` 중 하나 |
| `industry` | 예 | 공개 서비스 범주를 이해하기 위한 산업명 |
| `company_website` | 예 | 공개 공식 웹사이트 |
| `lead_source` | 아니오 | 마케팅 유입 경로. 캠페인명 등은 더미 또는 승인된 내부 분류만 사용 |

## Workflow (실행 단계)

1. 입력을 검증하고, 본사가 대한민국인 기업만 대상에 남긴다.
2. 공식 웹사이트·뉴스룸·IR·공시·공개 채용 공고 등 신뢰 가능한 공개 출처를 조사한다. 최근 신호는 확인일과 URL을 함께 기록한다. 최근 공개 신호가 없으면 없다고 표기한다.
3. 공개 사실, 고객 정보 접점, 캐치시큐 제안 가설, 제안 CTA를 분리해 기록한다. 가설에는 단정 대신 조건부 표현을 쓴다.
4. `references/research-rubric.md`에 따라 적합성과 검토 우선순위를 산정한다. 이 점수는 매출 가능성이나 실제 개인정보 관리 수준을 뜻하지 않는다.
5. `assets/lead-research-workbook-spec.md`의 열 구조로 리드 리스트, 리드 리서치, 의사결정 큐, 검토 가이드를 만든다.
6. 세일즈 매니저가 최종 판단·다음 액션·담당·목표일·검토 메모를 입력할 수 있게 한다.

### 검토 게이트

| 시점 | 확인자 | 통과 조건 |
|---|---|---|
| 조사 전 | 작업자 | 입력에 개인·고객·기밀 정보가 없고, 본사 국가와 기업명이 채워짐 |
| 리서치 완료 전 | 작업자 | 모든 공개 신호에 URL·확인일이 있고, 사실과 가설이 분리됨 |
| 외부 행동 전 | 세일즈 매니저 | 우선순위·제안 표현·다음 액션을 승인함 |

## Deliverable (결과물 형식)

스프레드시트에는 다음을 포함한다.

- 리드별 공개 신호, 출처 URL, 확인일, 고객 정보 접점
- 개인정보 라이프사이클 제안 가설, 우선 범위, CTA, 반증 또는 추가 확인 질문
- 적합성 점수와 점수 사유, 검토 우선순위
- 의사결정 큐: 최종 판단, 다음 액션, 담당, 목표일, 검토 메모
- 전체·우선 검토·승인·미검토 현황을 보여주는 의사결정 요약

## Prohibitions (금지사항)

- 개인정보, 고객정보, 비공개 정보, 회사 기밀, 로그인 뒤의 정보, 유료벽 우회 정보는 수집·기록·추론하지 않는다.
- 공개 정보만으로 보안 사고, 법 위반, 도입 의향, 예산, 의사결정권자, 현재 사용 솔루션을 단정하지 않는다.
- 사실·추론·권고를 같은 문장에 섞지 않는다. 근거 없는 최근 동향이나 수치를 만들지 않는다.
- 세일즈 매니저 승인 전에는 외부 접촉, CRM 반영, 자동 발송을 실행하지 않는다.

## Human review (사람 검토)

세일즈 매니저가 우선 검토 리드의 근거, 제안 가설, 표현의 적절성, 영업 전략 적합성을 검토한다. 검토 결과는 `승인`, `보류`, `제외`, `수정 요청` 중 하나로 기록하고, 승인된 리드만 다음 세일즈 단계로 전달한다.

## Resources

- `references/research-rubric.md`: 신호·가설·점수 판단 기준
- `assets/lead-research-workbook-spec.md`: 워크북 열과 입력 규칙
- `scripts/validate_lead_input.py`: 최소 입력 검증
- `mock-data/sample-leads.csv`: 익명·더미 입력 예시
- `mock-data/input-example.csv`: 검증 스크립트로 바로 실행하는 국내 본사 30개 기업 입력
- `mock-data/input-example.md`: 국내 본사 30개 기업을 사용한 리드 입력 설명
- `mock-data/expected-output.md`: 공개 사실·가설·사람 검토를 분리한 기대 결과 예시
