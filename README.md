[![Deploy and Test](https://github.com/mezcalagave/devops_practice/actions/workflows/main.yml/badge.svg)](https://github.com/mezcalagave/devops_practice/actions/workflows/main.yml)
##  devops_practice

### 1. 소개

이번 프로젝트는 모두의연구소에서 진행하는 MLOps풀잎스쿨에서 DevOps 실습 프로젝트입니다.
이 프로젝트는 Flask를 이용해 사칙연산을 웹서버로 구현했습니다.
unittest내부에 있는 function_test.py에서 pytest를 이용해 test가능하며 integration내부에 있는 app_test.py를 이용해 웹 서버 상태를 test할 수 있습니다.

### 2. 사용법

1. 다운받는 방법

   ```bash
   git clone https://github.com/mezcalagave/devops_practice.git
   ```

2. 웹 서버 실행

   ```bash
   python app.py
   ```

3. 서버에 요청보내기

   덧셈

   ```bash
   curl -X GET 'http://localhost:800/plus?x=10&y=5'
   ```

   뺄셈

   ```bash
   curl -X GET 'http://localhost:800/minus?x=8&y=3'
   ```

   곱셈

   ```bash
   curl -X GET 'http://localhost:800/multiply?x=5&y=4'
   ```

   나눗셈

   ```bash
   curl -X GET 'http://localhost:800/divide?x=8&y=2'
   ```

4. 테스트

   1. 사칙연산 테스트

      ```bash
      cd devops_practice/unittest
      pytest
      ```

   2. 서버 테스트

      ```bash
      cd devops_practice/integration
      pytest
      ```

      
[원저자](https://github.com/minsulee2/devops-eng-training)
