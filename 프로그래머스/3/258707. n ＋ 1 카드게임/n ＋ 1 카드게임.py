from collections import deque
def check(hand,deck,target):
    deckSet=set(deck)
    for h in hand:
        if (target-h in deckSet):
            deck.remove(target-h)
            hand.remove(h)
            return True
    return False

def solution(coin, cards):
    answer=1
    target = len(cards)+1
    hand = cards[:len(cards)//3]
    deck = deque(cards[len(cards)//3 :])
    arr=[]
    while deck and coin>=0:
        arr.append(deck.popleft())
        arr.append(deck.popleft())
        
        if check(hand,hand,target):
            pass
        elif coin>=1 and check(hand,arr,target):
            coin-=1
        elif coin>=2 and check(arr,arr,target):
            coin-=2
        else:
            break
        
        answer+=1
    return answer