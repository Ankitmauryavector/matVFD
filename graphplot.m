path='D:\ankit\videos\4th_sem\PDF\Video_Forgery\EightXEight35';
files=dir(strcat(path,'\*.jpg'));
L=length(files);
x=1:421;
z=[];
for i=1:L
    if i==L
        %y=1;
        %plot(x,y,'linewidth',2)
    else
        name='Ayush';
        d=int2str(i);
        e=int2str(i+1);
        df=strcat(name,d);
        ef=strcat(name,e);
        ex='.jpg';
        dg=strcat(df,ex);
        eg=strcat(ef,ex);
        a=rgb2gray(imread(strcat(path,'\',dg)));
        b=rgb2gray(imread(strcat(path,'\',eg)));
        y=corr2(a,b);
        z=[z,y];
    end
end

plot(x,z)