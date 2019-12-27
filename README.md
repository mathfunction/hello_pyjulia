## PyJulia = 在 Python 上 call Julia 程序 , 提升效能!!

### 如何安裝 ?

1. 安裝 julia , 確定在 cmd / terminal 上可呼叫 julia

2. 安裝 pyjulia

   ```shell
   pip install julia  # conda or python2
   pip3 install julia # python3
   ```

3. 安裝 PyCall (這是讓 julia 可以 call python 的模組)

   ```shell
   Pkg.add("PyCall") # 或在 cmd 上執行 julia REPL 執行按下 ] 後,輸入 add PyCall
   ```

   

### 測試程式 :  for loop 1+2+3+......+n !!

先寫一個 julia 函式

```julia
# forloop.jl
function forloop_sum(n::Int)
	s::Int = 0
	for i = 1:n # julia 是 1-based 語言
		s +=i
	end
	return s
end
```

寫 python 主程式 main.py 

```python
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
  for t in range(5): 
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
		
	
	 
```

執行方式:

```shell
python main.py  # conda ,python2
python3 main.py # python3
```



輸出結果:     

```shell
julia:500000500000,7.609202999999454 ms
julia:500000500000,0.2684160000008262 ms
julia:500000500000,0.21388000000044372 ms
julia:500000500000,0.18532600000042976 ms
julia:500000500000,0.19419300000045325 ms
python:500000500000,59.81285100000022 ms
python:500000500000,62.50343199999975 ms
python:500000500000,61.26390899999912 ms
python:500000500000,64.62924199999875 ms
python:500000500000,59.933210000000514 ms
```

註：第一次 call  julia 函式 forloop_sum 會略慢 , 因為要先編譯!! 



### 相關連結:

	- github: https://github.com/JuliaPy/pyjulia
	- documentation: https://readthedocs.org/projects/pyjulia/downloads/pdf/stable/
	- pip: https://pypi.org/project/julia/



