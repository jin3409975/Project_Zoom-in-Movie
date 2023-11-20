<template>
  <div class="backSize mainBackColor">
		<div class="marginMid">
			<div class="videoDiv marginMid">
				<iframe width="560" height="315" :src="videoUrl" frameborder="0" allowfullscreen></iframe>
			</div>
			<div class="detailDiscriptions">
				<div class="leftDiscriptions">
					<h3>이두나</h3>
					<p>한국의 로맨스 웹툰. 작가는 나노리스트를 연재한 민송아. 이번에도 그림체와 인물 표현이 전작과 비슷하다. 그리고 부제는 ~두근두근 누나리스트~</p>
				</div>
				<div class="rightDiscriptions">
					<p>출연: 이유미, 김정은, 김해숙, 더 보기</p>
					<p>장르: 드라마, 코미디 시리즈, 범죄 시리즈</p>
				</div>
			</div>
			<hr class="">
			<div class="commentsPlace">
				<h3 class="commentCnt">댓글 5개</h3>
				<div>
					<CommentCreate/>
					<Comment v-for="i in 5"/>
				</div>
			</div>
			<div>
				<h1 class="listTitle">유튜브 관련 영상</h1>
				<div class="movieList">
					<YoutubeRelatedCard v-for="i in 20"/>
				</div>
			</div>
		</div>
	</div>
</template>

<script setup>
import Comment from '../components/Comment.Vue';
import CommentCreate from '@/components/CommentCreate.Vue'
import YoutubeRelatedCard from '../components/YoutubeRelatedCard.vue'
import { ref, onMounted } from 'vue'
import axios from 'axios'

// 유튜브 API 키
const apiKey = import.meta.env.VITE_YOUTUBE_KEY;

const videoId = '4ykb-ftG3Bc';
const videoUrl = ref(`https://www.youtube.com/embed/${videoId}`);
const videoTitle = ref('');
const videoDescription = ref('');
</script>
  
<style scoped>

.commentsPlace {
	margin: 20px 5% 0;
	width: 80%;
}
.commentCnt {
	font-size: 17px;
	color: white;
	margin-left: 32px;
}
.detailDiscriptions {
	margin: 5% auto 0;
	color: white;
	display: flex;
	padding: 10px;
}

.leftDiscriptions {
	width: 70%;
	margin-left: 5%;
}

.rightDiscriptions{
	color: #777777;
}

.leftAlignedTitle {
  text-align: left;
  margin-left: 15px;
}


.videoDiv {
	display: flex;
	justify-content: center;
}

.videoDiv iframe {
	border-radius: 8px;
}
</style>