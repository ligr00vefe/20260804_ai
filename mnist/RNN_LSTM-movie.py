# pip install keras
# pip install torchsummaryX
# pip install --upgrade keras tensorflow
import os
os.environ["KERAS_BACKEND"] = "torch"  # PyTorch가 설치되어 있다면 PyTorch 백엔드 사용

from keras.datasets import imdb
from keras.utils import pad_sequences  # Keras 3에서는 utils 아래에 위치합니다.

from sklearn.metrics import f1_score, confusion_matrix
from time import time

import torch
from torch import nn
from torchsummaryX import summary  # 각종 층에 사용되는 가중치와 데이터 shape출력

MY_NUM = 10000  # 사전에서 사용할 단어의 수
MY_LEN = 80     # 각 영화평의 최대 단어 수
MY_EMBED = 30   # 단어 임베딩의 출력 차원 수
MY_HIDDEN = 100 # LSTM 은닉층의 출력 수
MY_EPOCH = 50   # 학습 반복 수

torch.manual_seed(111)

# 데이터 준비
(X_train, Y_train), (X_test, Y_test) = imdb.load_data(num_words=MY_NUM)

print('학습용 입력 데이터 모양: ', X_train.shape) # (25000, ) 문장
print('학습용 출력 데이터 모양: ', Y_train.shape) # (25000, ) 라벨
print('평가용 입력 데이터 모양: ', X_test.shape) 
print('평가용 출력 데이터 모양: ', Y_test.shape)

print('첫번째 영화평 (숫자 데이터)')
print(X_train[0])
print('총 단어 수: ', len(X_train[0]))
print('감성 (0=부정, 1=긍정): ', Y_train[0])
print(type(X_train[0]))
print(type(Y_train[0]))

def show_length():
  print('첫 10개 영화평의 길이')
  for i in range(10):
    print('영화평', i, ":", len(X_train[i]))

print("===============================")
show_length()

word_to_id = imdb.get_word_index()
print('사전 정보')
print('총 단어 수:', len((word_to_id)))
print('단어 virus는', word_to_id['virus'], '번째 수')
print('단어 korea는', word_to_id['korea'], '번째 수')
print('단어 the는', word_to_id['the'], '번째 수')

# 먼저 사전과 반대 역할
id_to_word = {} # {}에 데이터가 없는 경우 dict 타입 선언
for key, val in word_to_id.items():
  id_to_word[val] = key

print('3310번째 단어는 ', id_to_word[3310])
print('88583번째 단어는 ', id_to_word[88583])
print('1번째 단어는 ', id_to_word[1])

#  각 영화평의 길이를 일정하게 맞춤(통일 시킴)
X_train = pad_sequences(X_train, truncating='post',
                        padding='post',
                        maxlen=MY_LEN)
X_test = pad_sequences(X_test, truncating='post',
                        padding='post',
                        maxlen=MY_LEN)

print('길이 정리 후')
show_length()

def decoding(id):
  decoded = []
  for i in X_train[id]:
    word = id_to_word.get(i - 3, "???")
    decoded.append(str(i))
    decoded.append("(" + word + ")")
  print('=== 첫번째 영화평(단어 변환) ===')
  print(" ".join(decoded))

decoding(0)
print()
print('학습용 입력 데이터 모양:', X_train.shape)
print('학습용 출력 데이터 모양:', Y_train.shape)
print('평가용 입력 데이터 모양:', X_test.shape)
print('평가용 출력 데이터 모양:', Y_test.shape)

print("{0:=^20}".format('인공 신경망 구현'))
# 일반적인 RNN / LSTM / GRU: Sequential 사용 가능
# Seq2Seq, Attention, 다중 입출력 RNN: Sequential 사용 불가능 (Functional API 사용 필요)
class my_LSTM(nn.Module):
  def __init__(self):
    super(my_LSTM, self).__init__()
    self.embeddings = nn.Embedding(MY_NUM, MY_EMBED) #10000, 30
    # LSTM(입력값의 차원, 은닉층 출력 차원, batch_first::배치정보가 처음인경우)
    self.lstm = nn.LSTM(MY_EMBED, MY_HIDDEN, batch_first=True) #30,100,처음부터
    self.linear = nn.Linear(MY_HIDDEN, 1)
    self.sigmoid = nn.Sigmoid()

  def forward(self, inputs):
    x = self.embeddings(inputs)
    lstm_out, _ = self.lstm(x)  # 그단의 아웃풋, 다음단으로 전달하는 값 Sequential을 사용하지 않는 이유

    # LSTM의 최종 은닉층 3차원 출력값
    x = lstm_out[:, -1, :]  # : 모든 위치의 값, -1은 마지막의 위치, 80개 단에서 마지막 단을 취한다.맨 오른쪽의 값을 받겠다.
    x = self.linear(x)
    x = self.sigmoid(x)
    return x

# 모델 생성
model = my_LSTM()

print('\nLSTM 요약')
inputs = torch.zeros((MY_LEN, 1), dtype=torch.long)
# summary(model, inputs)

optimizer = torch.optim.Adam(model.parameters(), lr=0.01)
criterion = nn.BCELoss()

X_train = torch.from_numpy(X_train).long()
Y_train = torch.from_numpy(Y_train).float()

begin = time()
print('\nLSTM 학습 시작')

for epoch in range(3):
    output = model(X_train)

    # 출력값을 (25000, 1)에서 (25000)로 전환
    output = torch.squeeze(output)
    loss = criterion(output, Y_train)

    print('에포크: {},'.format(epoch),
          '손실: {:.3f}'.format(loss.item()))

    # 역전파 알고리즘으로 가중치 보정
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

end = time()
print('최종 학습 시간: {:.1f}초'.format(end - begin))

Test = torch.from_numpy(X_test).long()

with torch.no_grad():
  pred = model(Test)
  pred = torch.squeeze(pred)

print('\n전환 전:', type(pred))
pred = pred.numpy()

print('전환 후:', type(pred))
pred = (pred > 0.5)

print('\n혼동 행렬:')
print(confusion_matrix(Y_test, pred))

f1 = f1_score(Y_test, pred, average='micro')
print('\n최종 정확도: {:.2f}%'.format(f1 * 100))

sample = 5
decoded = []

for i in X_test[sample]:
    word = id_to_word.get(i - 3, "???")
    decoded.append(word)

print('\n샘플 영화평')
print(" ".join(decoded))

print('\n총 단어 수:', len(X_test[sample]))
print('감성 정답 (0=부정, 1=긍정):', Y_test[sample])
print('LSTM 예측:', pred[sample])
