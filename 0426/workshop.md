asantaatnasa

asantaatnasa



google

elgoog



1.

```
    function isPalindrome(str) {
      let a = str.replace(/(\s*)/g, "").split('').reverse().join('')
      let origin = str.replace(/(\s*)/g, "").split('').join('')
      if (a === origin) return true
      return false
    }

    // 출력
    console.log(
      isPalindrome('a santa at nasa'),  // true
      isPalindrome('google')  // false
    )
```

