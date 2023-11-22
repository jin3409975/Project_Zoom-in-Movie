<template>
    <div class="col-lg-8 text-center mx-auto my-auto">
      <h1 class="text-white">
        "<span class="text-white" id="typed"></span>"
      </h1>
      <div id="typed-strings">
        <h1>team</h1>
      </div>
    </div>
</template>

<script setup>
import Typed from "typed.js";


onMounted(() => {
  if (document.getElementById("typed")) {
    // eslint-disable-next-line no-unused-vars
    const typed = new Typed("#typed", {
      stringsElement: "#typed-strings",
      typeSpeed: 90,
      backSpeed: 90,
      backDelay: 200,
      startDelay: 500,
      loop: true,
    });
  }
});
</script>

<style scoped>

</style>