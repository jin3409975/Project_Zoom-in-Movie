import os
import django
import random
from django_seed import Seed

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "final_pjt_back.settings")
django.setup()

from movies.models import Movie, Comment  # 여기서 your_app을 앱의 이름으로 교체
from accounts.models import User  # 여기서 your_app을 앱의 이름으로 교체

def seed_comments(num):
    if not User.objects.exists() or not Movie.objects.exists():
        print("User 또는 Movie 인스턴스가 필요합니다.")
        return

    seeder = Seed.seeder()

    # 실제 User 및 Movie 인스턴스를 가져옵니다
    all_users = list(User.objects.all())
    all_movies = list(Movie.objects.all())

    # Comment 모델을 위한 데이터 생성 규칙을 정의합니다
    seeder.add_entity(Comment, num, {
        'user': lambda x: random.choice(all_users),
        'movie': lambda x: random.choice(all_movies),
    })

    # 더미 데이터 생성
    seeder.execute()

# 실행
seed_comments(100)
