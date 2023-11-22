<template>
  <header class="bg-gradient-dark">
    <div
      class="page-header min-vh-75"
    >
      <span class="mask bg-gradient-dark opacity-6"></span>
      <div class="container">
        <div class="row justify-content-center">
          <div class="text-center mx-auto my-auto">
            <h1 class="text-white">
              <h1 class="text-white">{{ movieTitle }}</h1>
              <span class="text-white" id="typed"></span>
            </h1>
            <div id="typed-strings">
              <!-- 오펜 -->
              <h4 v-if="idx===0">"이제 나는 죽음이요, 세상의 파괴자가 되었다."</h4>
              <!-- 크리 -->
              <h4 v-if="idx===1">"너희들은 AI를 못 이겨. 이건 진화라고!!!"</h4>
              <!-- 피자가게 -->
              <h4 v-if="idx===2">"프레디의 피자가게에 오신 걸 환영합니다."</h4>
              <!-- 익스 -->
              <h4 v-if="idx===3">"장난은 끝났어"</h4>
              <!-- 미션 -->
              <h4 v-if="idx===4">"당신 목숨이 내 목숨보다 항상 중요할거야."</h4>
              <!-- 분노 -->
              <h4 v-if="idx===5">"달리거나, 죽거나"</h4>
            </div>
          </div>
        </div>
      </div>
    </div>
  </header>
</template>

<script setup>
import { onMounted } from "vue";
import Typed from "typed.js";

const props = defineProps({
  movieTitle: String,
  idx: Number,
})

onMounted(() => {
  if (document.getElementById("typed")) {
    // eslint-disable-next-line no-unused-vars
    var typed = new Typed("#typed", {
      stringsElement: "#typed-strings",
      typeSpeed: 90,
      startDelay: 500,
      showCursor: false,
      // loop: true,
      // backSpeed: 90,
      // backDelay: 200,
    });
  }
});
</script>

<style scoped>
</style>