What's the difference between Python type and object?
=====================================================

- [知乎](https://www.zhihu.com/question/38791962?sort=created)


要搞懂这个问题，首先要先把类、类型、对象这些概念全部舍掉，重构世界观。
首先，python里面一切皆是对象，包括type、object、所有class，全部都是对象，那对象之间靠什么联系在一起呢？
没错，靠的就是关系：Python的世界里，对象之间一共有两种关系：

1. 继承关系：
比如有class A和class B(A)，再强调一下，A和B都是对象，
则对象B继承了对象A，或者说A是B的超类，
继承关系可以通过__base__属性得知，
```
>>>B.__base__
<class 'A'>
```
在python里，所有对象（包括type）均继承自object，而object则是继承体系的根，上面再无对象：
```
>>> object.__base__
>>> type.__base__
<class 'object'>
```

2. 实例关系
比如有class A， a = A()，不嫌烦的再强调一下，a和A都是对象，则对象a是对象A的实例，或者说对象A是对象a的类型.
实例关系可通过__class__属性获知：如：
```
>>> a.__class__
<class 'A'>
```

在python里，对象又可以分为三种：type object、class object和non-class object。
type object指type对象及其子类，如：class TypeA(type): pass
则TypeA和type均属于type object
class object指obect对象及其子类，如：class A(object)：pass
则object和A均属于class object
non-class object指通过实例化class object得来的对象，如a = A()
则a就是一个non-class object
三者的区别和联系在于：
type object都是type的实例，
class object是type object的实例，
non-class object是class object的实例，
type object和class object都可以进行实例化，而non-class object不能进行实例化
在python的世界里，type object和class object这两种类型的对象都是type对象的实例而type属于type object，object属于class object，则显然：>>> object.__class__
<class 'type'>
```
>>> type.__class__
<class 'type'>
```