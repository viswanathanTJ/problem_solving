from numpy import sort


def h_index(n, citations):
  ans = []
  # ans = []
  r = 0
  citations.sort()
  # 1 2 2 3 3 15
  for i in range(n):
    # sorted_c = sorted(citations[2:n])
    # if sorted_c[-1] >= i:
    print(citations[i], i)
    if citations[i] > i:
        r = r + 1
        ans.append(r)
    else:
        ans.append(r)
  return ans

if __name__ == '__main__':
  t = int(input())                           
  # t = 1                                           
  for test_case in range(1, t + 1):
    n = int(input())
    # n = 6
    # citations = [1, 2, 2, 3, 3, 15]
    citations = list(map(int, input().split()))
    print(citations)
    h_index_scores = h_index(n, citations)
    print("Case #" + str(test_case) + ": " +
          ' '.join(map(str, h_index_scores)))
