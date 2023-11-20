<template>
  <div class="backSize mainBackColor">
		<div class="marginMid">
			<div class="videoDiv marginMid">
				<iframe width="560" height="315" :src="videoUrl" frameborder="0" allowfullscreen></iframe>
			</div>
			<div class="detailDiscriptions">
				<div class="leftDiscriptions">
					<h3>{{ movieStore.movie.title }}</h3>
					<p>{{ movieStore.movie.overview }}</p>
				</div>
				<div class="rightDiscriptions">
					<p>출연: 정보 추가 중</p>
					<p>장르: 
						<span v-for="genre in movieStore.genre">{{ genre }}&nbsp;</span>
					</p>
				</div>
			</div>
			<hr class="">
			<div class="commentsPlace">
				<h3 class="commentCnt">댓글 {{ commentCnt }}개</h3>
				<div>
					<CommentCreate/>
					<Comment
					 v-for="comment in movieStore.comments"
					 :key="comment.id"
					 :comment="comment"
					 />
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
import { ref, onMounted, watch } from 'vue'
import { useRoute } from 'vue-router';
import axios from 'axios'
import { useMovieStore } from '../stores/movie';
import { useCounterStore } from '../stores/account';
import Comment from '../components/Comment.Vue';
import CommentCreate from '@/components/CommentCreate.Vue'
import YoutubeRelatedCard from '../components/YoutubeRelatedCard.vue'

const route = useRoute()
const accountStore = useCounterStore()
const movieStore = useMovieStore()
const apiKey = import.meta.env.VITE_YOUTUBE_KEY
const videoId =  ref(null)
const videoUrl = ref(null)

// 예고편
onMounted(() => {
	movieStore.getMovie(route.params.movieId);
	axios({
		method: 'get',
		url: `https://www.googleapis.com/youtube/v3/search`,
		params: {
			part: 'snippet',
			q: `${movieStore.movie.title} 공식 예고편`,
			type: 'video',
			key: apiKey
		}
	})
		.then((res) => {
			videoId.value = res.data.items[0].id.videoId
			videoUrl.value = `https://www.youtube.com/embed/${videoId.value}`;
		})
		.catch((err) => {
			console.log(err)
		})

})

// 댓글
const commentCnt = ref(null)
onMounted(() => {
	movieStore.getComments(route.params.movieId)
	commentCnt.value = movieStore.comments.length
})
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