<template>
  <tr>
    <td :colspan="columns" class="px-6 py-4">
      <div class="animate-pulse flex space-x-4">
        <div class="flex-1 space-y-4 py-1">
          <div
            v-for="i in 5"
            :key="i"
            class="h-4 bg-gray-200 rounded"
          ></div>
        </div>
      </div>
    </td>
  </tr>
</template>

<script setup lang="ts">
import { defineProps } from 'vue';

defineProps<{ columns: number }>();
</script>