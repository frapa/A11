function [dm, Pi] = kstatica([mi]) %, pos)
%KSTATICA Summary of this function goes here
%   Detailed explanation goes here

g = 9.806;
dm = 0.05/sqrt(13);
Pi = mi .* g;


end

