### 함수 ###


### 전역 ###
SIZE = 5
queue =[None for _ in range(SIZE)]
front = rear = -1

### 메인 ###

# enQueue()
print('---- enQueue ----' )
rear += 1
queue[rear] = '화사'

rear += 1
queue[rear] = '쏠라'

rear += 1
queue[rear] = '문별'

print("출구 <--", queue, "<-- 입구")

# deQueue
print('---- deQueue ----' )
front += 1
data = queue[front]
queue[front] = None # 비워주는게 좋아
print("식사 손님: ", data)

front += 1
data = queue[front]
queue[front] = None # 비워주는게 좋아
print("식사 손님: ", data)

front += 1
data = queue[front]
queue[front] = None # 비워주는게 좋아
print("식사 손님: ", data)

print(queue)