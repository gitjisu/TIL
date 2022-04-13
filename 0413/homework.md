```
1. T
2. T 역참조가능
3. N
4. T
```

```
칼럼이름 : question_id
테이블이름 : answer_comment
```

```
comments
```

```
405 = 로그인하고나서 redirect=GET방식으로 갔기때문에 POST가 아니라 오류!
```

```
@require_POST
def delete(request,pk):
	if requetst.user.is_authenticated:
		article = get_object_or_404(Article, pk=pk)
		article.delete()
	return redirect('articles:index')
```



