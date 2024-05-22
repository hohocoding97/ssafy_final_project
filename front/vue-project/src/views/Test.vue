<template>
<div class="container">
  <button class="button">
    Button
  </button>
</div>
</template>

<script setup>

</script>

<style scoped>
.container {
  position: relative;
  width: 4.5em;
  height: 4em;
  background-color: #644dff;
  overflow: hidden;
  border-radius: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  scale: 2;
  box-shadow: 0 .5em #4836bb;
  transition: all .1s ease;
  filter: drop-shadow(0 6px 2px #4836bb38);
  border: 1px solid #4836bb;
}

.button {
  font-weight: 800;
  cursor: pointer;
  position: absolute;
  text-transform: uppercase;
  height: 110%;
  width: 110%;
  background-color: #644dff;
  color: white;
}

.container:has(.button:active) {
  box-shadow: none;
  margin-top: 2em;
  filter: drop-shadow(0 3px 1px #4836bbbe);
}

</style>