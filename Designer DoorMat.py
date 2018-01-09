n, m = raw_input().split()
pattern = [('.|.'*(2*i + 1)).center(int(m), '-') for i in range(int(n)//2)]
print('\n'.join(pattern + ['WELCOME'.center(int(m), '-')] + pattern[::-1]))