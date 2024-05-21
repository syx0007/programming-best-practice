# 拦截

Java中实现AOP（面向切面编程）的一种常见方式是使用动态代理。以下是一个简单的例子，展示了如何使用动态代理来实现方法的拦截和增强。
```
import java.lang.reflect.InvocationHandler;
import java.lang.reflect.Method;
import java.lang.reflect.Proxy;
 
public class AopExample {
 
    public static void main(String[] args) {
        TargetInterface target = new TargetImpl();
        TargetInterface proxy = (TargetInterface) createProxy(target);
        proxy.businessMethod();
    }
 
    public static Object createProxy(final TargetInterface target) {
        // 使用InvocationHandler来实现拦截逻辑
        InvocationHandler handler = new InvocationHandler() {
            @Override
            public Object invoke(Object proxy, Method method, Object[] args) throws Throwable {
                System.out.println("Before method execution");
                Object result = method.invoke(target, args);
                System.out.println("After method execution");
                return result;
            }
        };
 
        // 创建代理对象
        return Proxy.newProxyInstance(
                target.getClass().getClassLoader(),
                target.getClass().getInterfaces(),
                handler
        );
    }
 
    // 目标对象接口
    public interface TargetInterface {
        void businessMethod();
    }
 
    // 目标对象实现
    public static class TargetImpl implements TargetInterface {
        @Override
        public void businessMethod() {
            System.out.println("Business method executed");
        }
    }
}
```
在这个例子中，我们定义了一个TargetInterface接口和一个实现了该接口的TargetImpl类。createProxy方法负责创建代理对象，它使用了InvocationHandler来拦截所有的方法调用。当代理对象的方法被调用时，invoke方法会被执行，在方法执行前后打印出相应的消息。

运行main方法会输出：

```
Before method execution
Business method executed
After method execution
```
