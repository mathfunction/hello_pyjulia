
function forloop_sum(n::Int)
	s::Int = 0
	for i = 1:n # julia 是 1-based 語言
		s +=i
	end
	return s
end