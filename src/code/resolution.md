# 屏幕分辨率适配

本组做的一些项目其实不是很需要太复杂的屏幕适配，其实在这种环境下，让用户去适配设计稿明显是最优解。在用户打开网页的时候使用javascript对用户的屏幕和设计稿的尺寸做计算得出用户需要缩放的倍数可能会比编码适配要更好一些。在这种状态下，编码只需要用绝对布局按照设计稿的位置布局即可，

关于这方面，只需要复制如下的代码即可。

index.html

```html
<!DOCTYPE html>
<html lang="zh_CN">
  <head>
    <meta charset="UTF-8">
    <link rel="icon" href="/favicon.ico">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>放课后的下午茶时间</title>
  </head>
  <body>
    <div id="app"></div>
    <script type="module" src="/src/main.ts"></script>
  </body>
  <script>
      function resizeWindow() {
          // 设计稿：1920 * 1080
          // 1.设计稿尺寸
          let targetWidth = 1920;
          let targetHeight = 1080;

          let targetRatio = targetWidth / targetHeight; // 宽高比率 （宽 / 高）

          // 2.拿到当前设备（浏览器）的宽度和高度
          let currentWidth =
              document.documentElement.clientWidth || document.body.clientWidth;

          let currentHeight =
              document.documentElement.clientHeight || document.body.clientHeight;

          // console.log(`${currentWidth}, ${currentHeight}`)

          // 3.计算缩放比率(屏幕过宽，根据高度计算缩放比例)
          // 若currentWidth是4k屏宽度 3840 除于 我们设计稿的宽度 1920  3840/1920 = 2
          // 这样页面就行进行2倍缩放
          let scaleRatio = currentWidth / targetWidth; // 参照宽度进行缩放（默认情况下）

          // 当前页面宽高比例，当页面越宽currentRatio值就越大
          let currentRatio = currentWidth / currentHeight;

          // 判断是根据宽度进行缩放，还是根据高度进行缩放
          if (currentRatio > targetRatio) {
              // 根据高度进行网页的缩放
              scaleRatio = currentHeight / targetHeight; // 参照高度进行缩放（屏幕很宽的情况下）
              document.querySelector("#app").style = `transform: scale(${scaleRatio}) translateX(-50%)`;
          } else {
              // 根据宽度进行网页的缩放
              document.querySelector("#app").style = `transform: scale(${scaleRatio}) translateX(-50%)`;
          }
      }

      resizeWindow();

      window.addEventListener("resize", resizeWindow);
  </script>
</html>
```

可能使用该代码之后还需要对标签的位置做出一定的调整，但说实话我并不记得适配的具体方式了，故将所有相关的css粘贴出来，供大家参考选用。

```css
/* base.css */

*,
*::before,
*::after {
    box-sizing: border-box;
    margin: 0;
    font-weight: normal;
}

* {
    margin: 0;
    padding: 0;
}

body {
    overflow: hidden;
    width: 100vw;
    min-height: 100vh;
}

/* main.css */

@import './base.css';

#app {
    position: relative;
    width: 1920px;
    min-height: 1080px;
    transform-origin: left top;
    overflow: auto;
    left: 50%;
}

/* Main.vue */

.container {
  width: 100%;
  height: 1080px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.title {
  position: absolute;
  left: 50%;
  top: 50%;
  transform-origin: center center;
  transform: translateX(-50%);

  opacity: 0;

  color: var(--color-text);
  font-size: 42px;
}

```
