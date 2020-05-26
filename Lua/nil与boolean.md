# nil
nil是一种只有一个nil值的类型，它的主要作用就是与其他所有值进行区分。Lua语言使用nil来表示无效值(non-value,即没有有用的值)的情况。像我们之前所学习到的，一个全局变量在第一次被赋值前的默认值就是nil,而将nil赋值给全局变量则相当于将其删除。

# boolean
boolean类型具有两个值，true和false，它们代表传统的布尔值。然而在Lua中，boolean值并非是用于条件测试的唯一方式，任何值都可以表示条件。在条件测试中，Lua会将除了false和nil以外的所有值视为true(包括数字0和空字符串)。

Lua支持常见的逻辑运算符，and、or和not（和python一样），而and、or运算符和JavaScript一样都遵循短路求值，即
1. and的左值为true时，返回右值，否则返回左值
2. or的左值为false时，返回右值，否则返回左值

not运算符会将所有的值转为boolean类型的值