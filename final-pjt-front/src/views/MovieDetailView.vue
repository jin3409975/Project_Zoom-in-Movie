<template>
  <div class="backSize mainBackColor">
		<div class="marginMid">
			<!-- <YoutubeTrailer :movieId="Number(route.params.movieId)"/> -->
			<YoutubeTrailer :movieTitle="movieStore.movie.title"/>
			<div class="detailDiscriptions">
				<div class="leftDiscriptions">
					<div class="titlePlace">
						<h3>{{ movieStore.movie.title }} </h3> 
						<LikeBtn :thisId="Number(route.params.movieId)"/>
					</div>
					<p>{{ movieStore.movie.overview }}</p>
				</div>
				<div class="rightDiscriptions">
					<p>출연: 정보 추가 중 </p>
					<p>장르: 
						<span v-for="genre in movieStore.genre">{{ genre }}&nbsp;</span>
					</p>
				</div>
				
			</div>
			<hr>
			<div class="commentsPlace">
				<h3 class="commentCnt">댓글 {{ comments.length }}개</h3>
				<div>
					<CommentCreate :movieId="Number(route.params.movieId)"/>
					<Comment
					 v-for="comment in comments"
					 :key="comment.id"
					 :comment="comment"
					 />
				</div>
			</div>
		</div>
    <Footer/>
	</div>
</template>

<script setup>
import { watch, computed } from 'vue'
import { useRoute } from 'vue-router';
import { useMovieStore } from '@/stores/movie';
import Comment from '@/components/Comment.Vue';
import CommentCreate from '@/components/CommentCreate.Vue'
import YoutubeTrailer from '@/components/YoutubeTrailer.vue'
import LikeBtn from '../components/LikeBtn.vue';
import Footer from '../components/Footer.vue';

const route = useRoute()
const movieStore = useMovieStore()
const comments = computed(() => {
	return movieStore.comments
})

// 영화
watch(() => route.params, (newParams) => {
	window.scrollTo(0, 0);
	movieStore.getMovie(newParams.movieId);
	movieStore.getComments(newParams.movieId);
}, { immediate: true });

// 댓글
watch(movieStore.comments, (newComments) => {
	movieStore.comments = newComments
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

.titlePlace{
	display: flex;
	align-items: center;
	margin-bottom: 8px;
}

.titlePlace h3{
	margin: 0;
}
</style>