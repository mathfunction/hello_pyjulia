import timeit # 量時間
import julia 
julia.install() #第一次用 pyjulia 才要這行, 抓 PyCall 位置 !!

# 可啟動類似 julia REPL 的用法!!
julia_cmd = julia.Julia()
julia_cmd.include("forloop.jl")

#-----------------------------------------------
# python 函式
def forloop_sum(n):
  s = 0
  for i in range(1,n+1):
    s+=i
  return s
#-------------------------------------------------  
if __name__ == "__main__":
  n = 1000000
  # julia
  for t in range(5): # 註：第一次 call forloop 函式會比較慢 , 因為要先編譯！！
    t1 = timeit.default_timer()
    j = julia_cmd.eval('forloop_sum({})'.format(n))
    t2 = timeit.default_timer()
    print("julia:{},{} ms".format(j,(t2-t1)*1000))
  
  # python 
  for t in range(5):
    t3 = timeit.default_timer()
    p = forloop_sum(n)
    t4 = timeit.default_timer()
    print("python:{},{} ms".format(p,(t4-t3)*1000))