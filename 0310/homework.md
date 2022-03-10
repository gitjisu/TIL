1.  (1) python manage.py makemigrations (2) python manage.py migrate



	2. #3

​	

	3. #2



4. ```
   my_post = Post.objects.get(pk=1)
   my_post.title
   my_post.title = '안녕하세요'
   my_post.title = '반갑습니다'
   my_post.save()
   ```

5.  Post.objects.all()