%% Homework 2

clear,clc, close all
load('regress1.mat') % Load in the data, X and Y independent and dependent variables
xregressionLine =  x;

% For Linear Regression, the polynomial takes the form of 
% y = B0 + B1*x + B2*x^2 ... BN*x^n
% Each additional term being added to the polynomial helps create a better
% fit for the data. However, at some point, adding too many terms leads to
% a line that perfectly fits the data fails to describe the pattern of the
% data

%% Creating the Polynomial Regression Equation through SVD
% M = 0,1
% M = 0 is a constant term and M = 1 both give a single line for the
% regression fit

% Creates a matrix with a constant vector and the x data
design_matrix1 = [x ones(length(x),1)];
% Beta terms is a function that calculates beta from using the SVD method

%[U,S,V] = svd(XX); 
% Y_star = U'*y;
% b_ss = [Y_star(1:length(diag(S)));0];
% b_star = b_ss(1:length(diag(S)))./diag(S);
% b = V*b_star;

beta1 = beta_terms(design_matrix1,y);

% y0 is simply a constant
y0 = beta1(2)*ones(length(x),1);

% y1 is a linear line of the form y = B0 + B1*x
y1 = beta1(1)*x + beta1(2)*ones(length(x),1);

% M = 2
% This is a quadratic fit for the data
% This design matrix adds on a x^2 term to the matrix
design_matrix2 = [x.^2 x ones(length(x),1)];
beta2 = beta_terms(design_matrix2,y);

% y = b0 + b1*x + b2*x^2
y2 = beta2(1)*xregressionLine.^2 + beta2(2)*xregressionLine + beta2(3);


% M = 3
% This is a third order polynomial that adds on a x^3 term
design_matrix3 = [x.^3 x.^2 x ones(length(x),1)];
beta3 = beta_terms(design_matrix3,y);

% Takes the form of y3 = b0 + b1*x + b2*x^2 + b3*x^3
y3 = beta3(1).*xregressionLine.^3 + beta3(2).*xregressionLine.^2 + beta3(3).*xregressionLine + beta3(4);


% M = 4
% This is a forth order polynomial that adds on a x^4 term
design_matrix4 = [x.^4 x.^3 x.^2 x ones(length(x),1)];
beta4 = beta_terms(design_matrix4,y);

% Takes the form of y3 = b0 + b1*x + b2*x^2 + b3*x^3 + b4*x^4
y4 = beta4(1).*xregressionLine.^4 + beta4(2).*xregressionLine.^3 + beta4(3).*xregressionLine.^2 + beta4(4).*xregressionLine + beta4(5);


% M = 5
% This is a forth order polynomial that adds on a x^5 term
design_matrix5 = [x.^5 x.^4 x.^3 x.^2 x ones(length(x),1)];
beta5 = beta_terms(design_matrix5,y);

% Takes the form of y3 = b0 + b1*x + b2*x^2 + b3*x^3 + b4*x^4 + b5*x^5
y5 = beta5(1)*xregressionLine.^5 + beta5(2)*xregressionLine.^4 + beta5(3)*xregressionLine.^3 + beta5(4)*xregressionLine.^2 + beta5(5)*xregressionLine + beta5(6);


%% Plotting everything
% Plots the regression fit for each polynomial order 0:5
figure(1)
plot(x,y,'o')
hold on
plot(xregressionLine,y0,xregressionLine, y1)
hold on
plot(xregressionLine, y2)
hold on
plot(xregressionLine,y3)
hold on
plot(xregressionLine,y4)
hold on
plot(xregressionLine,y5)

title('Polynomial Regression Best Fit')
xlabel('Independent Variable Data (Arbitrary Units)')
ylabel('Dependent Variable Data (Arbitrary Units)')
grid on

legend('Original data','M = 0','M = 1','M = 2','M = 3','M = 4','M = 5')

%% Determine the Error

% Calculates and plots the sum of error 
M(1) = sum((y-y0).^2);
M(2) = sum((y-y1).^2);
M(3) = sum((y-y2).^2);
M(4) = sum((y-y3).^2);
M(5) = sum((y-y4).^2);
M(6) = sum((y-y5).^2);

Order = [0,1,2,3,4,5];

figure(2)
plot(Order,M,'--o')
title('Error as a function of polynomial order')
xlabel('Polynomial Order')
ylabel('Error')
xticks([0,1,2,3,4,5,6])

% From the plots, it seems like the best fit is the x^3 polynomial.
% Additional terms only decrease the error by a minute amount. M=0, M = 1,
% and M = 2 have a large degree of error associated with them making these
% fits not as good as M = 3. 