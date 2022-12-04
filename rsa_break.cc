#include <cmath>
#include <iostream>
#include <boost/multiprecision/cpp_int.hpp>
#include <boost/multiprecision/cpp_dec_float.hpp>
using namespace boost::multiprecision;
using namespace std;
using Float = cpp_dec_float_100;
using Int = cpp_int;



bool is_square(Int& x){

    Float temp_x = 0;
    temp_x = sqrt(static_cast<Float>(x));

    if(ceil(temp_x) == floor(temp_x)){
        return true;
    }
    return false;
}



int main(){


    cpp_int a = 0;
    cpp_int b = 0;
    cpp_int b2 = 0;

    //this uses the idea that if n = p*q
    // then -> n = (a+b)(a-b), 
    // when p = a+b
    // and q = a-b



    cpp_int p = 0; //prime 1
    cpp_int q = 0; //prime 2
    cpp_int n = 0; //priv key



    cout << "Give a private key" << endl;
    cin >> n;
    cout << "Okay your private key, 'n', is " << n << endl;


    a = (Int)ceil(sqrt((Float)n));
    

    while(true){
        b2 = pow(a,2) - n;
        
        if( is_square(b2) ){
            b = sqrt(b2);
            break;
        }
        
        a++;
    }

    cout << "A: " << a << endl;
    cout << "B: " << b << endl;

    cout << "Your p: a+b " << a+b << endl;
    cout << "Your q: a-b " << a-b << endl;


}

