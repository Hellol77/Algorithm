# Algorithm


- ## 출력 형식
    
    **1. 변수 포맷(`%d`, `%s`, ...)과 `%`를 사용**
    
    ```python
    a = 5
    print("A is %d" % a)
    
    b = "apple"
    print("B is %s" % b)
    
    print("A is %d and B is %s" % (a, b))
    ```
    
    ```python
    A is 5
    B is apple
    A is 5 and B is apple
    ```
    
    ****2. format 함수를 이용****
    
    ```python
    a, b = 5, "apple"
    
    print("A is {0}".format(a))
    print("A is {new_a}".format(new_a=a))
    
    print("B is {0}".format(b))
    print("B is {new_b}".format(new_b=b))
    
    print("A is {0} and B is {1}".format(a, b))
    print("A is {new_a} and B is {new_b}".format(new_a=a, new_b=b))
    print("B is {1} and A is {0}".format(a, b))
    print("B is {new_b} and A is {new_a}".format(new_a=a, new_b=b))
    ```
    
    ```python
    A is 5
    A is 5
    B is apple
    B is apple
    A is 5 and B is apple
    A is 5 and B is apple
    B is apple and A is 5
    B is apple and A is 5
    ```
    
    ****3. f 문자열 포맷을 이용****
    
    ```python
    a, b = 5, "apple"
    
    print(f"A is {a}")
    print(f"B is {b}")
    print(f"A is {a} and B is {b}")
    ```
    
    ```python
    A is 5
    B is apple
    A is 5 and B is apple
    ```
    
    - ****소수점 맞춰 출력하기 (반올림)****
    
    ```python
    a = 33.567268
    print("%.4f" % a)
    ```
    
    ```python
    33.5673
    ```
    
    format 함수를 이용하는 것도 가능. 기존 포맷이 `{0}`이었다면 그 뒤에 `:`를 붙여 포맷을 지정해 준다.****
    
    ```python
    a = 33.567268
    print("{0:.4f}".format(a))
    ```
    
    ```python
    33.5673
    ```
    
    f 포맷을 이용하는 것 역시 가능. format 함수 이용과 비슷하게 해결이 가능
    
    ```python
    a = 33.567268
    print(f"{a:.4f}")
    ```
    
    ```python
    33.5673
    ```
    
    공백을 사이에 두고 입력
    
    ```python
    arr = input().split()
    n = int(arr[0])
    m = int(arr[1])
    
    print(n)
    print(m)
    print(n * m)
    ```
        </br>

- ## 별그리기
    
    ```python
    ***
    **
    *
    **
    ***
    ```
    
    를 그리는 것이 목적이면
    
    ```python
    // 완성 코드
    for i in range(3): 
        for j in range(3 - i):
            print("*", end="")
        print()
    
    for i in range(1, -1, -1): 
        for j in range(3 - i):
            print("*", end="")
        print()
    ```
    
    ```python
    i\j  0 1 2
    
    0    * * *
    1    * *
    2    *
    3    * *     (i = 1일때와 동일)
    4    * * *   (i = 0일때와 동일)
    ```
    
    ```python
    // 아래 3번째 4번째 출력하는 코드
    for i in range(1, -1, -1): -> i는 1부터 0까지 1씩 감소하면 됩니다.
        for j in range(3 - i): -> j는 0부터 2 - i까지 돌면 됩니다.
            print("*", end="")
        print()
    ```
    
    - **앞에 공백이 붙는 경우**
    
    ```python
    i                     공백 수    별의 개수
    0    vv*                2         1
    1    v***               1         3
    2    *****              0         5
    
    식                    2 - i      2 * i + 1
    ```
    
    ```python
    for i in range(3): 
        for j in range(2 - i):
            print(" ", end="")
        
        for j in range(2 * i + 1):
            print("*", end="")
        print()
    ```
      </br>
  
- ## 기본 정렬 함수
    
    **1. 오름차순 정렬**
    
    sort() : python3에서 리스트의 원소를 정렬하기 위해서는, `sort()`
    라는 내장된 함수를 이용할 수 있습니다. 이는 리스트를 **오름차순**
    으로 정렬해줍니다.
    
    ```python
    arr = [12, 41, 37, 81, 19, 25, 60, 20]
    arr.sort()
    print(arr) # [12, 19, 20, 25, 37, 41, 60, 81]
    ```
    
    정렬에 이용할 수 있는 함수 중에는 `sort()`와 비슷한 `sorted()`
    라는 함수도 있습니다. **단, sorted 함수는 정렬된 리스트를 반환하는 함수이기 때문에, 다음과 같이 정렬 이후의 리스트를 변수에 할당을 해줘야만 합니다.**
    
    ```bash
    arr = [12, 41, 37, 81, 19, 25, 60, 20]
    arr = sorted(arr)
    print(arr) # [12, 19, 20, 25, 37, 41, 60, 81]
    ```
    
    **2.내림차순 정렬**
    
    내림차순 정렬은 다음과 같이 sort 함수를 이용해 오름차순으로 정렬한 뒤 리스트를 뒤집는 방식으로 구현해볼 수도 있습니다.
    
    ```python
    arr = [12, 41, 37, 81, 19, 25, 60, 20]
    arr.sort()
    arr = arr[::-1] # reversed array
    print(arr) #[81, 60, 41, 37, 25, 20, 19, 12]
    ```
    
    위의 경우에서는 리스트를 뒤집기 위해 slicing을 사용했지만, 리스트를 뒤집어 주는 `reversed`
    라는 함수도 있습니다. 이 함수를 사용하면 다음과 같이 구현이 가능합니다. 다만, reversed를 사용시 다시 list로 감싸줘야 뒤집어진 list를 얻어낼 수 있음에 유의합니다.
    
    ```python
    arr = [12, 41, 37, 81, 19, 25, 60, 20]
    arr.sort()
    arr = list(reversed(arr)) # reversed array
    print(arr) #[81, 60, 41, 37, 25, 20, 19, 12]
    ```
        </br>

- ## 별 출력
    
    ```python
    * * * * *    행
    *       *    행
    * *     *    행
    * * *   *
    * * * * *
    
    열열열열열
    
    n=int(input())
    #i 가 행이고 j 가 열이다.
    for i in range(n):
        for j in range(n):
            if i==0 or j==n-1 or i>j:
                print('* ',end='')
            else:
                print('  ',end='')
        print()
    ```
        </br>

- ## 아스키 코드 (ASCII)
    
    python에서 특정 문자의 아스키 코드 값은 `ord()`라는 함수를 이용해 알 수 있습니다. 실제 문자 'A'의 아스키 코드 값은 65이기 때문에, python에서 ord('A') 코드를 실행하게 되면 65라는 값을 받게 됩니다.
    
    ```jsx
    print(ord('A'))
    
    >>65
    ```
    
    반대로 아스키 코드 값을 알고 있을 때, 대응되는 문자를 알아 낼수는 없을까요? 이 경우라면 `chr()` 함수를 이용하면 됩니다.
    
    python에서 chr(65) 코드를 실행하게 되면 'A'를 받게 됩니다.
    
    ```jsx
    print(chr(65))
    
    >> 'A'
    ```
    
    그렇다면 특정 대문자 알파벳 x 다음에 오는 문자는 어떻게 구해볼 수 있을까요?
    
    알파벳은 전부 연속한 아스키 코드로 이루어져 있다고 했으니 66번째 아스키코드와 대응되는 문자는 'B'라는 것을 알 수 있습니다.
    
    x가 'A'라 했을 때 ord('A')를 하여 65값을 얻어내고, 이 값에 1을 더한 값은 66을 다시 chr 함수로 묶어주면 'B'값을 얻을 수 있습니다.
    
    따라서 알파벳 x 다음 알파벳을 구하는 것은 `chr(ord(x) + 1)` 로 표현이 가능합니다.
        </br>

- ## List 거꾸로 탐색
    
    ### **Slicing**
    
    리스트에 대해 slice(`[]`)를 활용하면 일부 범위, 조건에 해당하는 원소들을 가져올 수 있습니다.
    
    기본적인 형태는 다음과 같습니다.
    
    ```
    arr[start:end:step]
    ```
    
    for loop과 굉장히 유사하게 동작합니다.
    
    start index에서 시작하여 end index 직전까지 step씩 뛰며 전진합니다.
    
    ```
    index  0  1  2  3  4
    =====================
    arr = [1, 2, 3, 4, 5]
    print(arr[1:3:1]) # 1번째 index부터 3번째 index 전까지 1씩 증가
    
    >> [2, 3]
    ```
    
    step이 1인 경우에는 생략이 가능합니다.
    
    ```
    index  0  1  2  3  4
    =====================
    arr = [1, 2, 3, 4, 5]
    print(arr[1:3]) # 1번째 index부터 3번째 index 전까지
    
    >> [2, 3]
    ```
    
    만약 첫 번째 index부터 slicing을 적용하고 싶다면, 첫 번째 start 값은 비워놔도 됩니다.
    
    ```
    index  0  1  2  3  4
    =====================
    arr = [1, 2, 3, 4, 5]
    print(arr[:3]) # 처음부터 3번째 index 전까지
    
    >> [1, 2, 3]
    ```
    
    만약 마지막 원소까지 slicing을 적용하고 싶다면, 두 번째 end 값은 비워놔도 됩니다.
    
    ```
    index  0  1  2  3  4
    =====================
    arr = [1, 2, 3, 4, 5]
    print(arr[2:]) # 2번째 index부터 끝까지
    
    >> [3, 4, 5]
    ```
    
    특정 구간의 원소들이 뒤집힌 형태로 리스트를 만들고 싶다면, for loop에서 처럼 step값에 -1을 넣어주면 됩니다.
    
    ```
    index  0  1  2  3  4
    =====================
    arr = [1, 2, 3, 4, 5]
    print(arr[3:0:-1]) # 3번째 index부터 0번째 index 전까지 -1씩 감소하면서
    
    >> [4, 3, 2]
    ```
    
    전체 원소를 뒤집고 싶다면, start, end를 모두 비우고 step에 -1만 적으면 됩니다.
    
    ```
    index  0  1  2  3  4
    =====================
    arr = [1, 2, 3, 4, 5]
    print(arr[::-1]) # 전체 원소 뒤집기
    
    >> [5, 4, 3, 2, 1]
    ```
    
    따라서 10개의 원소를 입력받아 뒤집는 문제는 다음과 같이 코드를 작성해볼 수도 있습니다.
    
    ### **python3 코드**
    
    ```
    arr = list(map(int, input().split()))
    reversed_arr = arr[::-1]
    
    for elem in reversed_arr:
        print(elem, end=" ")
    ```
    
    ### **출력결과**
    
    ```
    >> 1 2 4 2 5 7 8 5 8 3
    
    3 8 5 8 7 5 2 4 2 1
    ```
        </br>

- ## 2차원 리스트 입력
    
    ```python
    n = 4
    arr_2d = [
    list(map(int, input().split()))
    for _ in range(n)
    ]
    ```
        </br>

- ## **리스트에 map 사용하기**
    
    map은 리스트의 요소를 지정된 함수로 처리해주는 함수입니다(map은 원본 리스트를 변경하지 않고 새 리스트를 생성합니다).
    
    - **list(map(함수, 리스트))**
    - **tuple(map(함수, 튜플))**
    
    예를 들어 실수가 저장된 리스트가 있을 때 이 리스트의 모든 요소를 정수로 변환하려면 어떻게 해야 할까요? 먼저 for 반복문을 사용해서 변환해보겠습니다.
    
    ```python
    >>> a = [1.2, 2.5, 3.7, 4.6]
    >>> for i in range(len(a)):
    ...     a[i] = int(a[i])
    ...
    >>> a
    [1, 2, 3, 4]
    ```
    
    for에 range(len(a))를 사용해서 인덱스를 가져왔습니다. 그리고 가져온 인덱스로 요소 하나 하나에 접근한 뒤 int로 변환하여 다시 저장했습니다.
    
    매번 for 반복문으로 반복하면서 요소를 변환하려니 조금 번거롭습니다. 이때는 map을 사용하면 편리합니다.
    
    ```python
    >>> a = [1.2, 2.5, 3.7, 4.6]
    >>> a = list(map(int, a))
    >>> a
    [1, 2, 3, 4]
    ```
    
    a = list(map(int, a)) 한 줄로 변환이 끝났습니다. map에 int와 리스트를 넣으면 리스트의 모든 요소를 int를 사용해서 변환합니다. 그다음에 list를 사용해서 map의 결과를 다시 리스트로 만들어줍니다.
        </br>

- ## 문자열이 숫자인지 알파벳인지 판별하기
    
    ### string.isalpha()  → 알파벳인지 판별
    
    ```python
    # Appia Example for isalpha
     
    # It is to explain how to check whether the string consist of alphabet or not.
     
    Ex1 = 'A'
     
    Ex2 = 'ABC'
     
    Ex3 = "앱피아"
     
    Ex4 = "Hello Appia"
     
    Ex5 = "100Appia"
     
    #print the is the result for isalpha()
     
    print(Ex1.isalpha())
     
    print(Ex2.isalpha())
     
    print(Ex3.isalpha())
     
    print(Ex4.isalpha())
     
    print(Ex5.isalpha())
    
    //True
     
    //True
     
    //True
     
    //False
     
    //False
    ```
    
    ### string.isdigit()  → 숫자인지 판별
    
    ```python
    # Appia Example for isalpha
     
    # It is to explain how to check whether the string consist of digit or not.
     
    Ex1 = '010-1234-5678'
     
    Ex2 = '123456'
     
    Ex3 = "R4R3"
     
    print(Ex1.isdigit())
     
    print(Ex2.isdigit())
     
    print(Ex3.isdigit())
    
    //False
     
    //True
     
    //False
    ```
    
    ### string.**isalnum() → 알파벳인지 숫자인지 판별**
    
    ```python
    # Appia Example for isalpha
     
    # It is to explain how to check whether the string consist of digit/alphabet or not.
     
    Ex1 = '안녕'
     
    Ex2 = 'Hello3'
     
    Ex3 = "1.Where"
     
    Ex4 = "1 Where"
     
    print(Ex1.isalnum())
     
    print(Ex2.isalnum())
     
    print(Ex3.isalnum())
     
    print(Ex4.isalnum())
    
    //True
     
    //True
     
    //False
     
    //False
    ```
    
    ### string.**isdecimal() → int로 변환가능한지 판별**
    
    ```python
    a = "1"
    b = "1.2"
    c = "BlockDMask"
    d = "12ab"
    
    print(f'"1" : {a.isdecimal()}'). # int형으로 변환 할 수 있는 첫번째만 True이다.
    print(f'"1.2" : {b.isdecimal()}')
    print(f'"BlockDMask" : {c.isdecimal()}')
    print(f'"12ab" : {d.isdecimal()}')
    
    // True
    
    // False
    
    // False
    
    // False
    ```
    
    </br>
- ## **list를 Dict로 변환하기(dict.fromkeys()..등)**
1. **Dictionary Comprehension**
    
    ```python
    string_list = ['A','B','C']
    dictionary = {string : 0 for string in string_list}
    print(dictionary)
    
    # {'A': 0, 'B': 0, 'C': 0}
    ```
    
    아래 방식으로도 가능
    
    ```python
    string_list = ['A','B','C']
    dictionary = {string : i for i,string in enumerate(string_list)}
    print(dictionary)
    
    # {'A': 0, 'B': 1, 'C': 2}
    ```
    
2. **dict.fromkeys(key,value) 이용**
    
    ```python
    string_list = ['A','B','C']
    dictionary = dict.fromkeys(string_list,0)
    print(dictionary)
    
    # {'A': 0, 'B': 0, 'C': 0}
    ```
    
    Value에 아무것도 적지 않는 다면 value는 None으로 됩니다.
    
    ```python
    string_list = ['A','B','C']
    dictionary = dict.fromkeys(string_list)
    print(dictionary)
    
    # {'A': None, 'B': None, 'C': None
    ```
    
3.  **list의 값을 value로 갖는 dict 만들기 (1번 방법에서 key와 value가 반대로)**
    
    ```python
    string_list = ['A','B','C']
    dictionary = {i : string_list[i] for i in range(len(string_list))}
    print(dictionary)
    
    # {0: 'A', 1: 'B', 2: 'C'}
    ```
    
4. **두 개의 리스트 사용해서 dict 만들기**
    
    ```python
    string_list = ['A','B','C']
    int_list = [1, 2, 3]
    dictionary = dict(zip(string_list, int_list))
    print(dictionary)
    
    # {'A': 1, 'B': 2, 'C': 3}
    ```
    
5. **튜플을 dict로 바꾸는 법**
    
    ```python
    tuple_list = [('A',1), ('B',2), ('C',3)]
    dictionary = dict(tuple_list)
    print(dictionary)
    
    # {'A': 1, 'B': 2, 'C': 3}
    ```
    
   </br>
- ## **알파벳 리스트 만들기**
    
    아래와 같이 string 모듈에서 ascii_lowercase를 import 한다.
    
    ```python
    from string import ascii_lowercase
    alpha_list = list(ascii_lowercase)
     
    # ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    ```
    
    대문자 리스트가 필요하다면, ascii_uppercase를 사용한다.
