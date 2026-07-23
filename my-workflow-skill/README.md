# 리드 리서치 자동화

국내 본사 기업 리드 리스트를 공개 출처로 조사해, 개인정보 라이프사이클 솔루션의 제안 가설·검토 우선순위·세일즈 매니저 의사결정 큐를 만드는 Codex Skill입니다.

## 제공 기능

- 공개 사실과 제안 가설을 분리한 리드 리서치
- 출처 URL·확인일·적합성·검토 우선순위를 포함한 워크북 설계
- 세일즈 매니저의 승인·보류·제외·수정 요청을 기록하는 의사결정 큐
- 공개 근거 부족, 개인정보·고객정보·기밀 정보 유입을 막는 안전 기준

## 설치

1. 이 폴더를 GitHub 저장소로 올리거나 저장소를 복제합니다.
2. `my-workflow-skill` 폴더 전체를 Codex의 skills 디렉터리에 둡니다.

Windows 예시:

```powershell
Copy-Item -Recurse .\my-workflow-skill "$env:USERPROFILE\.codex\skills\my-workflow-skill"
```

Codex를 새로 열거나 Skills 목록을 새로 고친 뒤 `$my-workflow-skill`을 사용합니다.

## 빠른 시작

1. `mock-data/input-example.csv`에는 국내 본사 기업 30개의 실행 가능한 예시 입력이 있습니다.
2. Python 3로 입력 형식을 확인합니다.

```powershell
python .\scripts\validate_lead_input.py .\mock-data\input-example.csv
```

3. `mock-data/expected-output.md`와 `assets/lead-research-workbook-spec.md`를 참고해 결과 워크북을 만듭니다.
4. Codex에 다음처럼 요청합니다.

```text
$my-workflow-skill을 사용해 input-example.csv를 공개 출처만으로 리서치하고,
캐치시큐 제안 가설과 세일즈 매니저 의사결정 큐가 포함된 워크북으로 정리해줘.
```

## 입력 형식

필수 열은 다음 다섯 개입니다.

| 열 | 설명 |
|---|---|
| `lead_id` | 개인 식별값이 아닌 리드 고유 ID |
| `company_name` | 조사 대상 기업명 |
| `headquarters_country` | `KR`, `KOR`, `대한민국`, `한국` 중 하나 |
| `industry` | 공개 서비스 범주를 이해하기 위한 산업명 |
| `company_website` | 공개 공식 웹사이트 |

`lead_source`는 선택 열입니다. 캠페인명 등은 더미 또는 승인된 내부 분류만 사용합니다.

## 결과물

결과 스프레드시트는 다음 시트를 만듭니다.

- **리드 리스트**: 입력 원본
- **리드 리서치**: 공개 신호, URL, 확인일, 고객 정보 접점, 제안 가설, CTA, 적합성, 우선순위
- **의사결정 큐**: 최종 판단, 다음 액션, 담당, 목표일, 검토 메모
- **검토 가이드**: 점수·표현·승인 기준

## 안전 및 사람 검토

- 개인정보, 고객정보, 비공개 정보, 회사 기밀, 로그인 뒤의 정보는 수집·기록·추론하지 않습니다.
- 실제 보안 상태, 법 위반, 예산, 도입 의향, 의사결정권자, 기존 솔루션을 공개 정보만으로 단정하지 않습니다.
- 공개 신호마다 URL과 확인일을 남기고, 사실과 가설을 별도 열에 기록합니다.
- 세일즈 매니저가 근거·제안 표현·다음 액션을 승인하기 전에는 외부 접촉이나 CRM 반영을 하지 않습니다.

## 폴더 구성

```text
my-workflow-skill/
├── SKILL.md
├── README.md
├── references/   # 리서치·점수 기준
├── scripts/      # 입력 검증 도구
├── assets/       # 워크북 명세
├── mock-data/    # 30개 입력 예시와 기대 결과
└── agents/       # Codex UI 메타데이터
```

자세한 실행 규칙은 [SKILL.md](SKILL.md)를 참고하세요.
