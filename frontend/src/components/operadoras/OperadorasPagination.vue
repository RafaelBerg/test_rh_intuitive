<template>
  <div class="mt-4 flex justify-between items-center">
    <div class="text-sm text-gray-500">
      Mostrando {{ Math.min((currentPage * itemsPerPage), totalItems) }} de {{ totalItems }} registros
    </div>
    <div class="flex space-x-2">
      <button
        @click="$emit('prev')"
        :disabled="currentPage === 1"
        :class="{
          'bg-blue-600 text-white': currentPage > 1,
          'bg-gray-200 cursor-not-allowed': currentPage === 1
        }"
        class="px-3 py-1 rounded-md"
      >
        Anterior
      </button>
      <button
        @click="$emit('next')"
        :disabled="currentPage * itemsPerPage >= totalItems"
        :class="{
          'bg-blue-600 text-white': currentPage * itemsPerPage < totalItems,
          'bg-gray-200 cursor-not-allowed': currentPage * itemsPerPage >= totalItems
        }"
        class="px-3 py-1 rounded-md"
      >
        Próxima
      </button>
    </div>
  </div>
</template>

<script setup lang="ts">
import { defineProps, defineEmits } from 'vue';

defineProps<{ 
  currentPage: number;
  itemsPerPage: number;
  totalItems: number;
}>();

defineEmits<{ 
  (event: 'prev'): void;
  (event: 'next'): void;
}>();
</script>