function Foo() {
  getName = function () {
    console.log(1);
  };
  console.log(this)
  return this;
}
Foo.getName = function () {//给函数Foo定义了一个属性
  console.log(2);
};
Foo.prototype.getName = function () {
  console.log(3);
};
var getName = function () {
  console.log(4);
};
function getName() {
  console.log(5);
}

Foo.getName(); //调用函数的静态属性--一切皆对象--->所以最终调用的就是Foo对象的静态属性-》静态属性就是一个方法所以结果是2
getName(); //function关键字定义的函数存在提升，所以首先提升最前面，然后使用函数表达式定义的同名函数将其覆盖，然后就是4
Foo().getName();
/*Foo()运行后返回了一个this指向，这里的this是window对象，第一句-》》》》找到一个getName变量，然后将其赋值为一个函数表达式
因为 Foo函数内部并没有使用关键字定义，所以首先在函数内部没有找到，然后在全局找，发现getName-->function{log(4)},然后将函数内部的
function（）赋值给getName 然后Foo()返回的this->调用就是log(1) ----》》如果还没有找到的话那就函数内部的Foo 会定一个全局的getName
然后将函数赋值给getName,就是找不到的时候创建一个全局的变量。如果使用关键字进行定义的话，那样就是一个函数作用域，就会报错 找不到getName
*/
getName();//根据上面的getName现在已经被函数Foo的匿名函数进行了赋值，所以这里还是1
new Foo.getName();
/*
符号的优先级
new Foo.getName()======new(Foo.getName)()  进行构造函数进行执行
*/
new Foo().getName();//alert-1
// new new Foo().getName();//不懂
