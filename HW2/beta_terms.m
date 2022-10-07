function b = beta_terms(XX,y)
[U,S,V] = svd(XX);

Y_star = U'*y;
b_ss = [Y_star(1:length(diag(S)));0];
b_star = b_ss(1:length(diag(S)))./diag(S);
b = V*b_star;
end

