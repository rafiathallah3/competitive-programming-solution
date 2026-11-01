for _ in range(int(input())):
  n = int(input())
  *b, = map(int, input().split())
  c = sorted(b[i] if i % 2 == 0 else -b[i] for i in range(n))
  print(sum(c[n // 2 :]) - sum(c[: n // 2]))