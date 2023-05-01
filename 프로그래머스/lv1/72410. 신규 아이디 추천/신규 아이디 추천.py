def solution(new_id):
    # 대문자 -> 소문자로
    new_id=new_id.lower()
    answer=''
    # new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
    for word in new_id:
        if word.isalnum() or word in '-_.':
            answer += word
    new_id=answer
    # .. 연속된 부분
    while '..' in new_id:
        new_id=new_id.replace('..','.')
    # 처음이나 끝에 . 삭제
    if new_id[0] =='.' and len(new_id)>1:
        new_id=new_id[1:]
    else:
        new_id=new_id
    if new_id[-1]=='.':
        new_id=new_id[:len(new_id)-1]
    # 빈 문자열일때 a 대입
    if new_id=='':
        new_id='a'
    # 16자리 이상이면 첫 15개 문자만 살린다
    if len(new_id)>15:
        new_id=new_id[:15]
        if new_id[-1]=='.':
            new_id=new_id[:-1]
    # 2자 이하라면, 끝문자를 길이 3이 될 때가지 반복해서 끝에 붙입니다.
    if len(new_id)<=2:
        temp=new_id[-1]
        while len(new_id)!=3:
            new_id+=temp
        

    return new_id