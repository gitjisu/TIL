1. semantic Tag

```
 ## html ##

<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="semantic.css">
  <title>Layout Practice</title>
</head>
<body>
  <header class="bg-lightgrey m-4 p-4 border border-4">
    <h1 class="text-center">header</h1>
  </header>
  <nav class="bg-lightgrey m-4 p-4 border border-4">
    <h2>nav</h2>
  </nav>
  <div class="clearfix">
    <section class="bg-lightgrey p-4 section-wh border border-4">
      <h2>section</h2>
      <article class="bg-white m-4 p-4 border border-4">
        <h3>article1</h3>
      </article>
      <article class="bg-white m-4 p-4 border border-4">
        <h3>article2</h3>
      </article >
    </section>
    <aside class="bg-lightgrey p-4 aside-wh border border-4">
      <h2>aside</h2>
    </aside>
  </div>  
  <footer class="bg-lightgrey m-4 p-4 border border-4">
    <h2>footer</h2>
  </footer>
</body>
</html>

## css ##

body {
  font-family: Arial;
  width: 800px;
}

section {
  float: left;
  margin-left: 4px;
}

aside { 
  float: right;
  margin-right: 4px;
}

.clearfix::after {
  content: "";
  display: block;
  clear: both;
}

.bg-white {
  background-color: white;
}

.bg-lightgrey {
  background-color: lightgrey;
}

.m-4 {
  margin: 4px;
}

.p-4 {
  padding: 4px;
}

.text-center {
  text-align: center;
}

.section-wh {
  width: 490px;
  height: 300px;
}

.aside-wh {
  width: 280px;
  height: 300px;
}

.border {
  border: 1px solid black;
}

.border-4 {
  border: 4px
}
```

