<template>
    <div class="background backSize">
        <Login class="loginComponent"/>
    </div>
</template>

<script setup>
import Login from '../components/Login.vue';
</script>

<style scoped>
.backSize {
  margin: 7vh 0 0 0;
  height: 93vh;
}
.background {
    position: relative;
    background-image: url(https://an2-img.amz.wtchn.net/image/v2/v_rtGmsGmmSGuScg0hC76g.webp?jwt=ZXlKaGJHY2lPaUpJVXpJMU5pSjkuZXlKdmNIUnpJanBiSW1KbklsMHNJbkFpT2lJdmRqSXZjM1J2Y21VdmFXMWhaMlV2TVRZNE5Ea3hOVGN4T1RJM05UQTVOVGs0TXlKOS5mRjlhcmYwZWNJd2cyNUl4YnBfZkZyV0E5UmpkMnhLdmVEUnhUUU1jUXN3);
    background-size: cover;
    background-position: center;
    display: flex;
    align-items: center;
    flex-direction: column;
    justify-content: center;
}

.background::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: rgba(0, 0, 0, 0.8); /* 검정색으로 50% 투명도 */
    pointer-events: none;
}

.loginComponent {
    z-index: 0;
}
</style>