
 var quantity1 = 10;
 var quantity2 = 10;
 var quantity3 = 10;
 var quantity4 = 10;
 var quantity5 = 10;
 var quantity6 = 10;
 var quantity7 = 10;
 var cart = 0;
 var total = 0.00;
function updateCart(){
    cart = cart + 1;
}
function add1(){
    total + 15.00;
    cart++;
    quantity1--;
}
function add2(){
    total + 15.00;
    cart++;
    quantity2--;
}
function add3(){
    total + 15.00;
    cart++;
    quantity3--;
}
function add4(){
    total + 15.00;
    cart++;
    quantity4--;
}
function add5(){
    total + 15.00;
    cart++;
    quantity5--;
}
function add6(){
    total + 15.00;
    cart++;
    quantity6--;
}
function add7(){
    total + 15.00;
    cart++;
    quantity7--;
}
function actual_Total(){
    tax=total*0.0825
    new_total= total+tax;
}