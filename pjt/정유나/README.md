# 아이디어 구체화 / 기획 방향 설정

1. 노래방 키 맞추는 기능을 제공(자동으로)
2. 사용자 목소리 데이터를 가지고
3. 노래를 부르는것과 말을 하는것은 다름, → 말로는 분석이 어렵고 노래가 분석이 좀 더 나을듯(대중적인 노래를 이용하여)
4. 사용자 관점의 재미를 추구하고 싶으면 → 모창점수,
5. 집에서 혼자 이어폰끼고 연습할 때는 모바일(연습을 도와주는 느낌)
6. 노래방 가서는 진검승부 느낌으로 노래방 기계로 연결 →

---

노래에 내 목소리를 맞추는것보다 목소리에 맞는 노래를 찾는게 더 빠름

이런 수요층만 고려 해도 개연성 확보할 수 있을 듯?

노래 녹음본을 활용하는것은 어렵지 않을듯합니다…

모바일은 ⇒ 연습

노래방 ⇒ 가수모드 → 좀 더 정밀한 분석 가능(정말로 음정 박자 등 잘 맞췄는지) → 우리끼리 정해봅시다……………….. 옛날의 나와 대결(비교)

---

### 변조 활용방안

음성변조(실시간으로 한다면) ⇒ 듀엣모드에서 활용해보는건 어떨까?

ㄴ 변조된 목소리는 듣는사람이 있어야 재미있는 모드이니까….

목소리를 완전히 입히는 구조이면 → 재미없삼

ㄴ 이 노래를 이 가수가 부르면 어떨까 → 이게 더 재밌을듯

솔직히 한번은 해봐도 두번이상은 안할듯?

차라리 내 목소리에 대한 변조(예를들어 허스키한 목소리로 변조시켜주기)

ㄴ 내 목소리에 임재범 창법이라면? 태연 창법이라면?

ㄴ 뭐 두껍게 얇게

ㄴ 근데 이것도 한두번 쓰고 안쓰게 될듯………………………….

API 콜이면 오히려 더 잘 될듯? → 연속적인 변환은 어렵지만……..

---

차라리 원곡 가수와 나와의 유사도 측정

학습된 내 목소리로 노래 부르기(내가 실제로 부르는게 아님!)

→ 괜찮으면 모바일 연습모드로 연습

→ 노래방 가서 분석 모드 사용

⇒ 이런 플로우 어떤지 생각해보기

페르소나 → 코노 가고싶은데 집에서 가볍게 즐기고 노인코래방

목표에 오락성 들어가도 상관없음

기획의도 → 아무데서나 재밌게 즐길 수 있는 서비스!!!! ← 이런것도 상관없음.

좀 더 연습의 개념으로 가보기

# 전문가 리뷰

- ai 서버 → ai 처리하고 받아주는, 백, 프론트 세가지로

- 데이터는 어떤식으로 확보할 생각인지?

- ai 라는 요소가 들어가지만, 어플리케이션이 완성 된 상태에서 ai 를 첨가해서 어플리케이션을 풍성하게 만들어야함
- ai 를 어떤 기능을 넣을것인지..?
- 음정 수동으로 맞추는 부분만 ai
- 사람이 수동으로 음정을 조정해서 그 기능

- 그 기능을 구현하기 위한 시스템 구성을 빠르게 해보아야할듯
- 백에서 ai 맡은 사람들은 수동으로 조정하는 부분을 ai 로 조정할 수 있게

- ai 혹은 수동으로라도 작동할 수 있게 만든 후 ai 로
- 2-3주 안에는 수동 음성 조정 버전 완성하고
- 2-3주 안에 ai자동 조정 버전 완성 시키기
- ai 음성은 자연스럽게 이야기가 되는,, 실시간 처리가 중욧함

- 음정 조절 기능 구현 후 리버브?? 등 나머지 기능을 구현을 해보자

- 음성 데이터
- 정밀 조정이 힘들기 때문에 처음엔 폭을 크게 가져가기

디자인 시 그런 부분 고려하기…

연결을 할 때 사용자가 이야기 하는 음성을 어떤 수단으로

어플리케이션이 앱으로 갈건지 어플리케이션으로(웹?앱?) os 앱 기반으로 갈건지

ai 의 안드로이드 앱 기반으로 할거고 마이크

그런부분을 신경쓰기

라이브러리 구분만 ..

콜드스타트→ 자료ㅕ없이 시작하는 경우. 데이터가 많지 않은 경우,,

데이터는 얼마나

공인된 데이터인지?

이러한 부분도 고려해야함

데이터 이슈가 작더라도…

엔드포인트에 대한 협의 필요

→ 우리조가 기간안에 끝내기 어려워 보이는 정도를 엔드포인트로 잡

→ 2주 단위 1주단위도 가능하긴 함

검색 시 영어로 검색 하자

fake voice generator ⇒ 검색해보삼

기능 자체가 완성되어야하므로 실시간 빼고 후보정 이쪽 방향으로도 생각해보기

본인이 노래를 부르는것을 ai 동영상으로 만들어질 수 있도록,

1. → 회사같은 입장에서는 리소스를 빡빡하게 주고 기간을 짧게 잡음
1. 수익성이 좋다? 이건 좀 판단하기 어려운쪽임…
1. 기본기가 좋은 프로젝트!!(기본적으로 해야하는 기능은 다 구현되어있는)

어플리케이션을 두단계로 나눠랏

→ 실시간으로 되려면 백 없이 프론트에서 어느정도 처리가 되어야함

→ 어떤식의 서비스가 될 지 명확하지 않은 상태에서 실시간으로 구현이 된대도 최종 아웃풋은 스피커를 통해 나가기 때문에 하드웨어적인 붑분 때문에

# 코치세션 - 서비스 고도화 방법

- 고도화의 목적
  - 사용자 경험 향상
  - 시스템 안정화

### chapter 02. 사용자 경험 향상을 위한 고도화 방안

- Google Analytics
  - 구글에서 제공하는 무료 웹 로그 분석 툴
  - 구글의 고유한 통계 및 머신러닝 기술
  - ga 장점
    1. gamail 사용 시 무료
    2. 다양한 데이터 시각화 제공
    3. 실시간 데이터 수집
    4. 시장에 대한 인사이트
    5. 웹사이트 및 페이지 분석
- Heatmap
  - 색상으로 표현할 수 있는 다양한 정보를 일정한 이미지 위에 열 분포 형태의 그래픽으로 출력하는것
  - 웹 사이트의 방문자를 분석하는 웹로그 분석에 많이 이용되는 기법
  - movemap
    사용자가 페이지를 탐색할 떄 마우스를 움직이는 위치를 추적
  - clickmap
    데스크톱 장치에서 마우스를 클릭하고 모바일 장치에서 터치하는 위치를 잡아 냄
  - scrollmap
    페이지의 특정 지점까지 아래로 스크롤 한 사람들의 비율 파악 가능
  서비스 → hotjar, clarity

### chapter 03. 시스템 안정화를 위한 고도화 방안

- 시스템 모니터링
  - 모니터링이 필요한 이유
    - 사용자 증가 및 서버 사용량 실시간 파악
    - 시스템 장애 발생 시 즉각 반응
  - 시스템 모니터링
    - 시스템 상태와 성능을 지속적 관찰
    - 서버 운영체제, 애플리케이션 상태 및 성능 지표 체크
    ⇒ 서버 문제 조기 감지 및 시스템 다운 방지
  - 네트워크 모니터링
    - 네트워크 성능과 문제점 관찰
    ⇒ 네트워크 장애 조기 감지 및 통신 문제 최소화
  - 데이터베이스 모니터링
    - 데이터 베이스 성능 관찰
    - 데이터베이스 응답 시간 및 처리량 최적화, 데이터 무결성 유지
    ⇒ 데이터 베이스 성능 저하 방지 및 데이터 베이스 안정
  - 애플리케이션 성능 모니터링
    - 애플리케이션 성능과 사용자 경험 관찰
    ⇒ 원활한 서비스 제공을 위한
  prometheus ⇒ 오픈소스 시스템 모니터링 및 경고 툴킷
  grafana ⇒ 오픈소스 시각화 및 분석 도구 툴킷, 다양한 유형의 차트와 그래프 제공

# Vite 시작시 환경설정

- React-vite-eslint(airbnb)-prettier-typescript 설정
  참고링크: [https://velog.io/@kmh060020/React-vite-eslintairbnb-prettier-typescript-설정](https://velog.io/@kmh060020/React-vite-eslintairbnb-prettier-typescript-%EC%84%A4%EC%A0%95)
- vite에서 절대경로 사용하기
  참고링크: [https://velog.io/@navyjeongs/vite로-리액트-프로젝트-초기-세팅하기-1-with.-typescript-eslint-prettier-husky-절대경로](https://velog.io/@navyjeongs/vite%EB%A1%9C-%EB%A6%AC%EC%95%A1%ED%8A%B8-%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8-%EC%B4%88%EA%B8%B0-%EC%84%B8%ED%8C%85%ED%95%98%EA%B8%B0-1-with.-typescript-eslint-prettier-husky-%EC%A0%88%EB%8C%80%EA%B2%BD%EB%A1%9C)
  tsconfig.json 파일을 열어 complierOptions에 baseUrl과 paths를 추가
  tsconfig에서 작성한 path를 vite.config.ts에 작성해야 사용할 수 있는데 vite-tsconfig-paths 플러그인을 사용하여 간단하게 등록
- vite pwa 설정
  pwa 최소 요구사항(공식문서) https://vite-pwa-org.netlify.app/guide/pwa-minimal-requirements.html
  pwa란 무엇인가 https://velog.io/@gsh723/0715-pwa
  vite pwa 적용해보기 [https://jonghoonpark.com/2023/08/27/pwa-만들어보기](https://jonghoonpark.com/2023/08/27/pwa-%EB%A7%8C%EB%93%A4%EC%96%B4%EB%B3%B4%EA%B8%B0)
  pwa setting [https://velog.io/@strong-minsu/PWA-세팅](https://velog.io/@strong-minsu/PWA-%EC%84%B8%ED%8C%85)
- linebreak-style(lf, crlf)
  https://ddeck.tistory.com/48

# 와이어 프레임

<img src="../정유나/안쏭맞춤와이어프레임.png" />
와이어 프레임 설계 완료

# UI / UX 설계

<img src='//pjt/정유나/안쏭맞춤 UI _ UX.png' />

## TypeScript + Vite 환경에서 절대경로 설정하기

1. `vite-tsconfig-paths` install
2. plugin 에 `tsconfigPaths()` 추가

   ```tsx
   // vite.config.ts

   import { defineConfig } from "vite";
   import react from "@vitejs/plugin-react-swc";
   //...//
   import tsconfigPaths from "vite-tsconfig-paths";

   // https://vitejs.dev/config/
   export default defineConfig({
     plugins: [
       react(),
       //... //
       tsconfigPaths(),
     ],
   });
   ```

3. tsconfig.json compilerOptions에 경로 설정

   ```json
   {
     "compilerOptions": {
       /* ... */
       /* 절대경로 설정 */
       "baseUrl": ".",
       "paths": {
         "@/*": ["src/*"],
         "@pages/*": ["src/pages/*"],
         "@styles/*": ["src/styles/*"],
         "@components/*": ["src/components/*"]
       }
     },
     "include": ["src"],
     "references": [{ "path": "./tsconfig.node.json" }]
   }
   ```

## Vite 환경에서 PWA 환경설정

1. vite-plugin-pwa 라이브러리 설치
2. vite-plugin-pwa 구성
    `vite.config.ts` 에서 
    `registerType: "autoUpdate"`
    추가
3. `vite-plugin-pwainjectRegister` 플러그인은 구성 옵션을 사용하여 서비스 워커를 자동으로 등록

   ```ts
   import { defineConfig } from "vite";
   import react from "@vitejs/plugin-react-swc";
   import { VitePWA } from "vite-plugin-pwa";
   import tsconfigPaths from "vite-tsconfig-paths";

   // https://vitejs.dev/config/
   export default defineConfig({
     plugins: [
       react(),
       VitePWA({
         registerType: "autoUpdate",
         injectRegister: "auto",
       }),
       tsconfigPaths(),
     ],
   });
   ```
4. manifest.json 설정