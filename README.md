C번 - 발머의 피크 이론 성공
시간 제한 메모리 제한
1 초 (추가 시간 없음) 1024 MB
문제
발머의 피크 이론이란 혈중 알코올 농도
$C$가
$(0.129 \leq C\leq0.138)$일때 초인적인 프로그래밍 능력을 가지게 된다는 이론이다. 기령이는 발머의 피크 이론 신봉자이기 때문에 지금부터 코딩테스트를 볼 때까지 혈중 알코올 농도를 최대한 지키려고 한다. 기령이는 매 시간마다 정해진 술을 섭취하며, 섭취한 알코올은 일정 시간이 지나면 분해된다. 기령이가 지금부터 코딩테스트를 볼 때까지 얼마나 혈중 알코올 농도를 0.129와 0.138 사이로 지킬 수 있는지 알아내보자. 단, 혈중 알코올 농도 증가량은 술에 포함된 알코올의 양
$A * 0.001$로 계산하며 최초의 혈중 알코올 농도는 0이다.

입력
첫째 줄에 코딩테스트를 볼 때까지 남은 시간
$N(1 \leq N \leq 1\ 000\ 000)$, 섭취한 알코올의 지속시간
$L(1 \leq L \leq 10\ 000)$이 공백으로 구분되어 주어진다.

둘째 줄에 술에 포함된 알코올의 양 정수
$a_i(0 \leq a_i \leq 200)$가 공백으로 구분되어 주어진다.

출력
혈중 알코올 농도
$C$를
$(0.129 \leq C \leq 0.138)$로 유지한 시간을 출력한다.
