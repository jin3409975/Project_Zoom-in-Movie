<template>
  <div class="backSize mainBackColor">
		<div class="marginMid">
			<YoutubeTrailer :movieId="Number(route.params.movieId)"/>
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
				<h3 class="commentCnt">댓글 {{ movieStore.comments.length }}개</h3>
				<div>
					<CommentCreate/>
					<Comment
					 v-for="comment in movieStore.comments"
					 :key="comment.id"
					 :comment="comment"
					 />
				</div>
			</div>
			<div v-if="false">
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
import { useMovieStore } from '../stores/movie';
import Comment from '../components/Comment.Vue';
import CommentCreate from '@/components/CommentCreate.Vue'
import YoutubeRelatedCard from '../components/YoutubeRelatedCard.vue'
import YoutubeTrailer from '@/components/YoutubeTrailer.vue'

const route = useRoute()
const movieStore = useMovieStore()


// 영화 및 댓글
watch(() => route.params.movieId, (newMovieId) => {
	window.scrollTo(0, 0);
  movieStore.getMovie(newMovieId);
  movieStore.getComments(newMovieId);
}, { immediate: true });
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
</style>