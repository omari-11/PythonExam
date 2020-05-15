def mcd(n1, n2):
      mxcd = 0
  for i in range(1,n1):
    f = n1 % i
    print('i is {}, f is {}'.format(i, f))
    for j in range(1,n2):
      g = n2 % j
      print('\n  j is {}, g is {}'.format(j, g))
      if (f == 0 and g == 0 and f == g): 
        mxcd = f  
      else: 
        mxcd = "No hay comun divisor"
  return mxcd 
