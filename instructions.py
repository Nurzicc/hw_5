#  в приложение urls прописываем ссылки на страницу, а то что находится в core это для отображение чтобы в самом сайте все виделось

# В urls через path задаем ссылку на ту или иную страницу вот таким образом:

# urlpatterns = [
#     path ('', index, name='index'),
#     path('about/', about, name='about')
# ]

# а дальше в index прописываем эти ссылки 

# makemigrations - собирает наши ихменнение 
# migrate - добавляет эти поля в сайт

# upload_to = logo - для того чтобы фотки сохранялись в опр папке (logo - эта та папка где будет храниттся фотки)

# class Meta - пишем перевод для админ панельки, для легкой ориантации

css - мы прописываем стили 

static - это css