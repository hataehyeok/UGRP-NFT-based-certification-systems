# NFT를 활용한 확장된 PAMS 시스템 제작
NFT-based certification systems for eﬀicient recruitment processes
NFT와 블록체인을 이용한 PAMS 시스템 개선과 NFT 소유자들의 커뮤니티 구현을 위한 학부생 연구 프로그램

팀장: 하태혁 hth021002@postech.ac.kr<br>
팀원: 김형수 hyeongsoo@postech.ac.kr<br>
팀원: 최대현 daehyeonchoi@postech.ac.kr<br>
팀원: 차은성 ender3553@postech.ac.kr<br>
팀원: 신상현 ohsong656565@gmail.com<br>
github Changing

서론
  
본 연구는 NFT의  ‘정보의 고유성 증명'이라는 기술적 가치에 주목하여 NFT의 새로운 활용성과 방안을 탐구하고 개발한 연구이다. 먼저, NFT를 이력서에 적용하여 별도의 증빙자료가 필요하지 않은 NFT 포트폴리오를 연구했다. NFT 포트폴리오의 기술적 가능성을 점검하고, 베타 버전의 모바일 애플리케이션을 만들어 교내 구성원을 대상으로 테스트하였다. 또한, NFT가 가진 심리적 특성을 활용하여 새로운 가치를 창출하고자 했고, 이를 ‘포스테키안 활동 통합관리시스템(PAMS)’이라는 플랫폼에 적용하였다. 우리는 NFT를 PAMS에 적용하여 학생들의 비교과 활동 참여율을 증진하고자 하였다.
본 연구팀은 최종적으로 PAMS에 블록체인 NETWORK를 접목한 모바일 애플리케이션 ‘팜플렛(PAM+NET)’을 제작하여 새로운 NFT 포트폴리오 플랫폼으로 활용하는 동시에, 비교과 활동 참여를 증진하는 SNS 형식의 건전한 커뮤니티 플랫폼을 제안한다.


1. 연구 목적
 - 현재 이력 증빙 과정의 비효율성 분석
이력서에서 일부 활동은 위조되거나 과장되기도 한다. 이를 방지하기 위해 기업 및 기관에서는 추가적인 증빙자료를 요청하여 활동의 진위를 확인한다. 그러나 이 과정에서 비효율적인 많은 부가 비용이 발생한다. 개인은 분산된 증빙 자료로 모아 제출해야 하는 번거로운 과정을 거친다. 기업 및 기관에서는 증빙 자료의 진위도 확인하기 위해 다시 검수하는 번거로운 과정을 거친다.
<img width="494" alt="image" src="https://github.com/hataehyeok/UGRP-NFT-based-certification-systems/assets/105369662/29128f57-a860-4ad1-a7c7-bd9125835860">

 - PAMS의 문제점 및 개선점 분석
PAMS는 포스텍의 여러 비교과 활동을 신청할 수 있으며, 개인의 핵심 역량을 관리할 수 있는 우수한 플랫폼이다. 그러나 접근성이 좋지 않다는 치명적인 결점이 존재하기에 극히 일부 학생만 관심을 두고 이를 활용해왔다. 포스텍 학부생의 PAM 점수 분포를 살펴보면 대부분이 최하위 구간에 속해있다. 
<img width="621" alt="image" src="https://github.com/hataehyeok/UGRP-NFT-based-certification-systems/assets/105369662/991339fb-c554-4848-92a2-a84c93bef6e6">

 - 문제 해결 계획
효율적으로 이력 증빙이 가능한 NFT 포트폴리오를 제작하고 편의성 높은 PAMS의 모바일 애플리케이션 제작한다. 그리고 이 둘을 연동한다.
<img width="328" alt="image" src="https://github.com/hataehyeok/UGRP-NFT-based-certification-systems/assets/105369662/66856da5-33ff-4c89-831a-5b50c26134ee">


2. 연구 내용 및 진행
애플리케이션 이름인 ‘팜플렛(PAM+NET)’은 PAMS에 블록체인을 활용하고 비교과 활동을 하는 사용자 사이의 관계를 형성한다는 의미로 ‘Network’라는 단어를 합성하고 ‘+’ 문자를 더한 것이 유래이다. 한글 이름은 팜플렛으로, 영문 이름인 ‘PAM+NET’을 읽으면 비슷하게 발음할 수 있다.
<img width="147" alt="image" src="https://github.com/hataehyeok/UGRP-NFT-based-certification-systems/assets/105369662/ca3800f9-6cea-4418-8ff7-815b9846af53">

   - 애플리케이션 구상
Front-end 코딩에는 Figma로 먼저 디자인한 페이지를 구현하는 방식으로 진행했으며, 특히 UI와 UX에 신경을 써 사용자 친화적인 디자인으로 탭 바(tap-bar)와 리스트 뷰(list-view) 등을 배치했다. 앱 기능 구현은 홈 화면, 검색 화면, 프로필 화면, NFT 요청 화면으로 나누어 각 핵심 기능을 구현했다.

<img width="694" alt="image" src="https://github.com/hataehyeok/UGRP-NFT-based-certification-systems/assets/105369662/a9a9b192-2a39-442f-b212-f1af7b10598b">

 - 애플리케이션 구현
Front-end 구현은 Flutter를 사용했다. Back-end 코딩은 두 가지 영역으로 나누어져 있으며, 일반 Web2.0 구조에서는 Python과 Firebase를 사용하고 Web3.0 구조에는 Solidity로 Smart Contract를 작성하였다.
<img width="619" alt="image" src="https://github.com/hataehyeok/UGRP-NFT-based-certification-systems/assets/105369662/e839e598-2f34-46f6-ae60-0435e7bf404f">

애플리케이션의 화면은 다음과 같이 구현하였다. 각각 홈, 활동 정보(홈 화면 세부 항목), 검색, NFT 신청, 프로필 화면이다.

<img width="698" alt="image" src="https://github.com/hataehyeok/UGRP-NFT-based-certification-systems/assets/105369662/e0d06141-fc4c-4fa3-9ff3-930d896d7109">


3. 연구 결과
총 39명의 베타테스터 중 23명이 앱을 설치하고 접속하였다. Firebase에서 사용자의 활동량을 분석한 결과, 앱 배포 직후 13일에 데이터 읽기 및 쓰기가 발생한 횟수는 각각 2.6만 회, 2.2천 회로 나타났다. 이후 14일에는 1.1만 회의 읽기와 348회의 쓰기가 발생했으며, 15일에는 1.3만 회의 읽기와 1.3천 회의 쓰기와 발생했다. 3일간 진행된 베타테스트 기간 동안 발급된 NFT는 총 119개이다. 
<img width="623" alt="image" src="https://github.com/hataehyeok/UGRP-NFT-based-certification-systems/assets/105369662/af8fc669-6e1c-4934-83b7-cff814d2233d">

4. 결론 및 전망
본 연구팀은 Dapp ‘팜플렛(PAM+NET)’을 제작하고 배포에 성공하였다. PAMS 사용자 접근성을 높이고 NFT 포트폴리오의 가능성을 확인할 수 있었다. 앱의 프로필 기능과 검색 기능은 사용자끼리 활동을 자유롭게 공유하는 ‘주체적 활동 관리 체계’ 가 하나의 문화가 될 수 있음을 입증했다.
또한, 본 연구팀이 최종적으로 이루고자 하는 목표는 NFT 포트폴리오를 하나의 문화로 자리 잡을 수 있도록 하여 이력 증빙 과정을 최소화하는 시스템을 구축하는 것이다. 연구 기간에는 본 연구팀이 NFT 증빙을 심의했기 때문에, NFT에 신뢰성이 있다고 보기 어렵다. 그러나 교육기관이나 활동 주체 기관 등의 전문 증빙 기관과 협업해 해당 NFT 요청 심의를 할 수 있다면, NFT를 증빙 자료 및 포트폴리오로 신뢰할 수 있게 된다.
연구팀은 앞으로 애플리케이션을 더욱 안정성 있고 편리하게 발전시킨 뒤, 대학의 협력을 주선하여 대학에서 직접 학생들의 이력을 NFT로 보증해 줄 수 있도록, 그리고 블록체인을 활용하여 이력 인증 체계의 비효율을 해결할 수 있는 시스템을 구축할 수 있는지에 대한 연구를 이어 나갈 것이다.





관련 링크
https://cse.postech.ac.kr/%ed%95%98%ed%83%9c%ed%98%81%c2%b7%ec%b0%a8%ec%9d%80%ec%84%b1%c2%b7%ec%b5%9c%eb%8c%80%ed%98%84-%ed%8c%80-ugrp-%ec%b5%9c%ec%9a%b0%ec%88%98%ec%83%81-%ec%88%98%ec%83%81/?pageds=1&p_id=109&e=&k=&c=&cat=5

https://www.youtube.com/watch?v=4UjtIF1WRzg&t=115s
