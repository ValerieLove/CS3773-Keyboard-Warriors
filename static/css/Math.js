
 var quantity1 = 10;
 var quantity2 = 10;
 var quantity3 = 10;
 var quantity4 = 10;
 var quantity5 = 10;
 var quantity6 = 10;
 var quantity7 = 10;
 var cart = 0;
 var total = 0.00;
 var tax = total*0.0825;
 var new_total= total+tax;
 var slap = 0.00;

 var new_total= total+tax+slap;


 document.getElementById('price').innerHTML = total + " + " + tax + " + " + slap + " =  $" + new_total;
 document.getElementById('cartNum').innerHTML = cart;

function discount(){
    slap = total * 0.20;
}


function updateCart(){
    cart = cart + 1;
}
function add1(){
    total = total + 15.00;
    cart++;
    quantity1--;
    string = "Black shirt"
}
function add2(){
    total = total + 15.00;
    cart++;
    quantity2--;
}
function add3(){
    total = total + 40.00;
    cart++;
    quantity3--;
}
function add4(){
    total = total + 15.00;
    cart++;
    quantity4--;
}
function add5(){
    total = total + 15.00;
    cart++;
    quantity5--;
}
function add6(){
    total = total + 15.00;
    cart++;
    quantity6--;
}
function add7(){
    total = total + 15.00;
    cart++;
    quantity7--;
}

    
