# Battlefield Edge-Cloud Offloading Research Model
# Battlefield Edge-Cloud Offloading Research Model

## 1. 연구 목적

본 연구의 목적은 변화하는 전장환경에서 AI 기반 지휘결심 지원 임무의
처리 위치를 Edge와 Cloud 중 동적으로 결정함으로써
정보의 적시성(Information Timeliness)과 지휘결심의 적시성을 향상시키는
의사결정 방법을 개발하는 것이다.

전장환경에서는 네트워크 상태와 컴퓨팅 자원의 상태가 지속적으로 변화한다.
특히 제한된 대역폭, 가변적인 지연, 패킷 손실, 네트워크 단절 및
컴퓨팅 자원의 과부하 등으로 인해 동일한 AI 임무라도
Edge에서 처리하는 것이 유리한 경우와 Cloud에서 처리하는 것이
유리한 경우가 달라질 수 있다.

따라서 본 연구에서는 전장상황, 임무 특성, 네트워크 상태 및
컴퓨팅 상태를 고려하여 AI 임무의 예상 처리시간을 예측하고,
이를 기반으로 AI 임무의 Edge 또는 Cloud 처리 위치를
동적으로 결정하는 연구모형을 설계한다.

## 2. 연구의 기본 개념

본 연구는 다음과 같은 인과 및 의사결정 구조를 갖는다.

Battlefield Situation
↓
Data Generation
↓
Mission Requirement
↓
Network / Computing State
↓
AI Processing Time Prediction
↓
Edge-Cloud Offloading Decision
↓
Information Timeliness
↓
Command Decision Timeliness
↓
Operational Effect

## 3. 연구모형

본 연구에서는 전장환경을 다음과 같은 상태벡터로 정의한다.

S_t = {B_t, I_t, M_t, N_t, C_t}

여기서,

* B_t : Battlefield State
* I_t : Information/Data State
* M_t : Mission State
* N_t : Network State
* C_t : Computing State

### 3.1 Battlefield State

전장상황의 변화 정도를 나타내는 변수이다.

예:

* battlefield_state
* mission_intensity
* data_generation_rate

전장상황이 변화하면 센서 및 정보체계에서 생성되는 데이터의 양과
AI 임무의 발생 빈도가 변화한다고 가정한다.

### 3.2 Information/Data State

AI 임무를 수행하기 위해 생성·전달되는 데이터의 특성을 나타낸다.

주요 변수:

* data_size
* data_generation_rate
* output_data_size
* information_priority
* security_level

예를 들어 감시·정찰 영상 데이터는 상대적으로 큰 데이터 크기를
가지며, 객체탐지 또는 상황판단과 같은 AI 처리를 요구할 수 있다.

### 3.3 Mission State

AI 임무의 중요도와 처리 요구조건을 나타낸다.

주요 변수:

* mission_type
* workload
* priority
* deadline
* gpu_requirement
* cpu_requirement

AI 임무의 종류와 요구조건에 따라 필요한 컴퓨팅 자원과
허용 가능한 처리시간이 달라진다.

### 3.4 Network State

Edge와 Cloud 사이의 네트워크 상태를 나타낸다.

주요 변수:

* RTT
* bandwidth
* packet_loss
* jitter

네트워크 상태는 AI 입력데이터를 Edge 또는 Cloud로 전달하는 시간과
처리결과를 반환하는 시간에 영향을 미친다.

### 3.5 Computing State

Edge와 Cloud의 현재 컴퓨팅 자원 상태를 나타낸다.

Edge:

* edge_cpu_utilization
* edge_gpu_utilization
* edge_queue_length

Cloud:

* cloud_cpu_utilization
* cloud_gpu_utilization
* cloud_queue_length

컴퓨팅 자원의 사용률이 증가할수록 대기시간과 AI 처리시간이
증가할 수 있다고 가정한다.

## 4. AI 임무 처리시간 모델

AI 임무의 전체 응답시간은 다음과 같이 정의한다.

T_total = T_upload + T_queue + T_processing + T_return

여기서,

* T_upload : AI 입력 데이터를 처리 노드로 전달하는 시간
* T_queue : Edge 또는 Cloud에서 처리하기 위해 대기하는 시간
* T_processing : AI 모델의 실제 처리시간
* T_return : AI 처리결과가 사용자 또는 지휘체계로 전달되는 시간

따라서 Edge와 Cloud 각각에 대해 예상 응답시간을 계산한다.

T_Edge = T_upload,Edge
+ T_queue,Edge
+ T_processing,Edge
+ T_return,Edge

T_Cloud = T_upload,Cloud
+ T_queue,Cloud
+ T_processing,Cloud
+ T_return,Cloud

## 5. AI 처리시간 예측모형

본 연구에서는 전장환경, 네트워크 상태, 컴퓨팅 상태 및
AI 임무 특성을 입력변수로 사용하여 AI 처리시간을 예측한다.

입력변수 X:

X = {
RTT,
Bandwidth,
Packet Loss,
Jitter,
Edge CPU Utilization,
Edge GPU Utilization,
Cloud CPU Utilization,
Cloud GPU Utilization,
Queue Length,
Data Size,
Workload,
Mission Type
}

출력변수 Y:

Y = AI Processing / Response Time

예측모형의 후보는 다음과 같다.

* Linear Regression
* Random Forest
* XGBoost
* Neural Network

각 모형의 예측성능을 비교하여 적절한 AI 처리시간 예측모형을
선정한다.

## 6. Edge-Cloud Offloading Decision

AI 임무의 처리 위치는 Edge와 Cloud 중 하나를 선택한다.

기본적인 의사결정 기준은 다음과 같다.

D* = argmin(T_Edge, T_Cloud)

즉, 예상 응답시간이 더 짧은 처리 위치를 선택한다.

그러나 실제 전장환경에서는 단순히 평균 응답시간만 최소화하는 것이
아니라 임무의 중요도와 시간제한을 함께 고려할 필요가 있다.

따라서 최종적으로는 다음과 같은 목적함수를 고려한다.

D* = argmin Cost(D)

Cost(D) =
α × T_response

* β × Deadline_Violation
* γ × Resource_Usage

여기서,

* T_response : AI 임무의 전체 응답시간
* Deadline_Violation : 요구시간 초과 여부 또는 초과 정도
* Resource_Usage : Edge 또는 Cloud 자원 사용량
* α, β, γ : 각 요소의 중요도를 나타내는 가중치

## 7. 정보 적시성(Information Timeliness)

본 연구에서는 단순한 네트워크 지연시간이나 AI 처리시간만을
최종적인 성과지표로 사용하지 않는다.

AI 임무가 요구된 시간 안에 완료되는지를 판단하기 위해
다음과 같은 지표를 사용한다.

P(T_response <= T_required)

여기서,

* T_response : 실제 AI 임무의 전체 응답시간
* T_required : 해당 임무가 요구하는 최대 허용시간

이를 통해 특정 전장상황에서 AI 기반 정보가
요구시간 내 제공될 확률을 평가한다.

## 8. 연구의 독립변수와 종속변수

### 독립변수

#### Battlefield Variables

* Battlefield State
* Mission Intensity
* Data Generation Rate

#### Network Variables

* RTT
* Bandwidth
* Packet Loss
* Jitter

#### Computing Variables

* Edge CPU Utilization
* Edge GPU Utilization
* Cloud CPU Utilization
* Cloud GPU Utilization
* Queue Length

#### Mission Variables

* Data Size
* Workload
* Priority
* Deadline
* Mission Type

### 종속변수

#### Technical Performance

* AI Processing Time
* End-to-End Response Time
* Throughput

#### Operational Performance

* Deadline Satisfaction Probability
* Information Timeliness
* Command Decision Timeliness

## 9. 비교대상

제안하는 동적 Offloading 방법의 효과를 검증하기 위해
다음 방법과 비교한다.

### Method 1. Always Edge

모든 AI 임무를 Edge에서 처리한다.

### Method 2. Always Cloud

모든 AI 임무를 Cloud에서 처리한다.

### Method 3. Nearest Node

물리적으로 가까운 처리 노드를 선택한다.

### Method 4. Proposed Dynamic Offloading

전장상황, 네트워크 상태, 컴퓨팅 상태 및 임무 특성을 고려하여
Edge 또는 Cloud를 동적으로 선택한다.

## 10. 연구가설

### H1

네트워크 상태는 AI 기반 지휘결심 지원 임무의
End-to-End Response Time에 유의한 영향을 미칠 것이다.

### H2

컴퓨팅 자원의 이용률은 AI 임무의 처리시간에
유의한 영향을 미칠 것이다.

### H3

AI 임무의 데이터 크기와 연산량은 AI 임무의
End-to-End Response Time에 유의한 영향을 미칠 것이다.

### H4

Edge와 Cloud의 상대적인 성능은 전장상황과
네트워크 및 컴퓨팅 상태에 따라 달라질 것이다.

### H5

전장상황과 네트워크·컴퓨팅 상태를 고려한 동적 Offloading 방법은
고정적인 처리방식보다 AI 정보의 적시성을 향상시킬 것이다.

### H6

동적 Offloading 방법은 다양한 전장상황에서
Deadline Satisfaction Probability를 향상시킬 것이다.

## 11. 연구 수행 방법

본 연구는 다음의 단계로 수행한다.

### Step 1. Battlefield Scenario Modeling

추상화된 전장상황을 정의한다.

* Normal
* High Information Demand
* Network Congestion
* Edge Overload
* Cloud Connectivity Restriction

각 상황에 따라 데이터 생성량과 네트워크 및 컴퓨팅 상태를 변화시킨다.

### Step 2. Simulation

Python과 SimPy를 이용하여

* Battlefield
* AI Task
* Network
* Edge
* Cloud

를 모델링한다.

이를 통해 다양한 전장상황에서 AI 임무 처리 데이터를 생성한다.

### Step 3. AI Processing Time Prediction

시뮬레이션을 통해 생성한 데이터를 이용하여
AI 처리시간 예측모형을 구축한다.

Regression 및 Machine Learning 방법을 비교한다.

### Step 4. Dynamic Offloading

AI 처리시간 예측결과와 현재의 네트워크·컴퓨팅 상태를 이용하여
AI 임무의 처리 위치를 Edge 또는 Cloud로 결정한다.

### Step 5. SDN-based Control

SDN Controller를 이용하여 네트워크 상태와 컴퓨팅 상태를
수집하고 동적인 Offloading 의사결정을 지원한다.

### Step 6. Performance Evaluation

다음 방법을 비교한다.

* Always Edge
* Always Cloud
* Nearest Node
* Proposed Dynamic Offloading

평가지표:

* Response Time
* 95th Percentile Latency
* Deadline Satisfaction Probability
* Information Timeliness
* Resource Utilization

### Step 7. Testbed Validation

가상화 환경에서 Edge와 Cloud를 구축하고
실제 AI 처리 및 네트워크 조건을 적용하여
시뮬레이션 결과와 실제 측정결과를 비교한다.

## 12. 최종 연구모형

본 연구의 전체 연구모형은 다음과 같이 구성한다.

Battlefield Situation
↓
Data Generation
↓
AI Mission Requirement
↓
┌───────────────────────────────┐
│ Network State                 │
│ - RTT                         │
│ - Bandwidth                   │
│ - Packet Loss                 │
│ - Jitter                      │
└───────────────────────────────┘
+
┌───────────────────────────────┐
│ Computing State               │
│ - CPU Utilization             │
│ - GPU Utilization             │
│ - Queue Length                │
└───────────────────────────────┘
+
┌───────────────────────────────┐
│ Mission State                 │
│ - Data Size                   │
│ - Workload                    │
│ - Priority                    │
│ - Deadline                    │
│ - Mission Type                │
└───────────────────────────────┘
↓
AI Processing Time
Prediction
↓
Edge-Cloud Offloading
Decision
↓
End-to-End Response
Time
↓
Deadline Satisfaction
↓
Information Timeliness
↓
Command Decision Timeliness
↓
Operational Effect

## 13. 연구의 핵심 연구질문

본 연구는 다음 연구질문에 답하는 것을 목표로 한다.

RQ1. 전장상황의 변화는 AI 기반 지휘결심 지원 임무의
데이터 생성과 처리시간에 어떠한 영향을 미치는가?

RQ2. 네트워크 및 컴퓨팅 상태는 AI 임무의
Edge 및 Cloud 처리시간에 어떠한 영향을 미치는가?

RQ3. 어떠한 전장 및 네트워크·컴퓨팅 조건에서
Edge 처리가 Cloud 처리보다 유리한가?

RQ4. AI 처리시간 예측을 이용한 동적 Offloading 방법은
고정적인 Edge 또는 Cloud 처리방식보다 우수한가?

RQ5. 동적 Offloading을 통해 AI 기반 정보의 적시성과
지휘결심의 적시성을 향상시킬 수 있는가?
