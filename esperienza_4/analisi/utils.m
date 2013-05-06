function s = sigma (dati, medie)
	N = length(dati(:,1));
	
	d = sum( (dati .- medie).^2 ) / (N - 1);
	s = sqrt(d / N);
endfunction

function chi = chi2(y, x, dy, A, B)
	chi = sum((y - A - B*x).^2 ./ (dy .^ 2));
endfunction

function A, B, sA, sB = fit(y, x, w) % w = dy^(-2)
	N = length(x);
	
	m1 = sum(w);
	m2 = sum(w .* x);
	m4 = sum(w .* x.^2);
	
	M = [m1, m2; m2, m4];
	
	n1 = sum(w .* y);
	n2 = sum(w .* x .* y);
	
	Noto = [n1; n2];
	
	R = inv(M) * Noto;
	
	A = R(1);
	B = R(2);
	
	sA = sqrt(sum((x.^2) .* w) / det(M));
	sB = sqrt(sum(w) / det(M));
endfunction