```
{% extends 'base.html' %}

{% block content %}
  <h1>Articles</h1>
  {% if request.user.is_authenticated %}
    <a href="{% url 'articles:create' %}">[CREATE]</a>
  {% else %}
    <a href="{% url 'accounts:login' %}">[새 글을 작성하려면 로그인하세요.]</a>
  {% endif %}
  <hr>
  {% for article in articles %}
    <p>
      <b>작성자 : <a href="{% url 'accounts:profile' article.user.username %}">{{ article.user }}</a></b>
    </p>
    <p>글 번호 : {{ article.pk }}</p>
    <p>글 제목 : {{ article.title }}</p>
    <p>글 내용 : {{ article.content }}</p>
    <div>
      <form class="like-form" data-id="{{ article.pk }}">
        {% csrf_token %}
        {% if request.user in article.like_users.all %}
          <button id="like-{{ article.pk }}">좋아요 취소</button>
        {% else %}
          <button id="like-{{ article.pk }}">좋아요</button>
        {% endif %}
      </form>
    </div>
    <p>
      <span id="like-count-{{ article.pk }}">
        {{ article.like_users.all|length }}명이 이 글을 좋아합니다.
      </span>
    </p>
    <a href="{% url 'articles:detail' article.pk %}">[DETAIL]</a>
    <hr>
  {% endfor %}
  <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
  <script>
    // 1. form 태그 전부다 가져오기 (좋아요버튼)
    const forms = document.querySelectorAll('.like-form')
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value

    forms.forEach(function (form) {
      
      form.addEventListener('submit', function (event) {
        event.preventDefault()
        const articleId = event.target.dataset.id
        axios.post(`http://127.0.0.1:8000/articles/${articleId}/likes/`, {}, {headers: {'X-CSRFToken': csrftoken},})
        .then(function (response){
          const { count, liked } = response.data

          const likeButton = document.querySelector(`#like-${articleId}`)
          if (liked) {
            likeButton.innerText = '좋아요취소'
          } else {
            likeButton.innerText = '좋아요'
          }
          
          const likeCount = document.querySelector(`#like-count-${articleId}`)
          likeCount.innerText = `${count} 명이 이 글을 좋아합니다`
        })
        .catch(err => {
          if (err.response.status === 401) {
            window.location.href = '/accounts/login/'
          }
        })
      })
    })



  </script>
{% endblock %}

```

