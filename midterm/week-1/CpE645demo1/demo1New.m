f=fopen('lenna.512', 'r');
x=fread(f,[512,512], 'uchar');
figure, imshow(x, [0,256]);
xx = x(225:288, 225:288);
y=x;
y(225:288,225:288)=zeros(64,64);
imshow(y,[0,255]);
figure(3);
meshz(xx);