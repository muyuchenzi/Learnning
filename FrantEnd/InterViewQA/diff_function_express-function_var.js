/*
两种定义函数的方式一个是使用函数声明的定义方式一种是函数表达式，他们有两个区别
1、使用函数声明定义的函数会被提升到最前面，所以函数声明的会放到上下文的最前
2、函数表达式是进行运行时，才进行赋值，而且是赋值结束后才能调用
所以第一个getName 首先是oaoafly，对函数声明的进行提升，然后放到最前面
第二个是先将匿名函数赋值给getName,这样getName就是指向了匿名函数，所以刚刚在最前面的函数声明的
函数被覆盖，
第三个就是还是直接调用覆盖后函数表达式

总结：这两个其实还是有区别的。一个是函数的提升，一个就是函数表达式的运行机制
 */

getName(); //oaoafly
var getName = function () {
  console.log("wscat");
};
getName(); //wscat
function getName() {
  console.log("oaoafly");
}
getName(); //wscat
