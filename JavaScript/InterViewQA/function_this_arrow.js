/*
这个还是this指向的问题
*/
var name = "Wscsats"; 
window.name = "Wscats----";
// 全局变量

function getName() {
   name = "Oaoafly"; //去掉var变成了全局变量
  var privateName = "Stacsw";
  return function () {
    console.log(this); //window
    return privateName;
  };
}
var getPrivate = getName("Hello"); //当然传参是局部变量，但函数里面我没有接受这个参数

console.log(name) //Oaoafly
console.log(getPrivate()) //Stacsw