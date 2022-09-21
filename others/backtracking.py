def permute(a, l, r): 
            if l==r:
                list_.add(''.join(a))
            else: 
                for i in range(l,): 
                    a[l], a[i] = a[i], a[l]
                    if open<n:
                        permute(['('], l+1, r) 
                    if close<open:
                        permute([')'], l+1, r,open)
                    a[l], a[i] = a[i], a[l]