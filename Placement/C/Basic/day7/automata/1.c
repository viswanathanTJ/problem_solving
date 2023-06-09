// You are using GCC
if (conu < 200)
    chg = 1.20;
else if (conu >= 200 && conu < 400)
    chg = 1.50;
else if (conu >= 400 && conu < 600)
    chg = 1.80;
else
    chg = 2.00;
gramt = conu * chg;
if (gramt > 300)
    surchg = gramt * 15 / 100.0;
netamt = gramt + surchg;
if (netamt < 100)
    netamt = 100;