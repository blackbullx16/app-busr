<template>
  <div>
    {{ store.doubleCount }}
    <button @click="store.increment">add</button>
  </div>
</template>

<script setup lang="ts">
import { useCounterStore } from "@/stores/counter";
import { watch } from "vue";
const store = useCounterStore();

store.$subscribe((mutation, state) => {
 console.log( mutation.events);
 
  localStorage.setItem("count", JSON.stringify(state));
});
</script>

<style scoped></style>
